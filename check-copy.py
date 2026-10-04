#!/usr/bin/env python3
"""
check-copy.py — verify SITE-COPY.md and the site's HTML still agree.

Two checks, run in both directions:

  A. ACCURACY  Every quoted copy fragment in SITE-COPY.md appears in the HTML/JS.
               Catches: doc edited but the site never updated.

  B. COVERAGE  Every visible string in the HTML appears somewhere in SITE-COPY.md.
               Catches: site edited but the doc left stale, or new copy added
               that was never documented.

Exit code 0 = in sync, 1 = drift found.

  python3 check-copy.py            # summary
  python3 check-copy.py --verbose  # also list what was checked
  python3 check-copy.py --hook     # enforcement mode, see below

Exit codes: 0 = in sync, 1 = accuracy drift, 2 = coverage drift, 3 = both.

Note that content alone cannot tell you WHO caused drift: rewriting a line in the
doc also orphans the old string in the site, so a legitimate human edit trips both
directions, exactly as a forgotten doc update would.

--hook therefore uses file times to tell the two apart:

  doc is newer than every page  → the human edited SITE-COPY.md and the change has
                                  not landed yet. Legitimate inbox state; passes
                                  with a note so the session is never wedged.
  otherwise, with drift         → HTML moved without the doc following. Blocks.

That is a heuristic, not a proof. Plain `check-copy.py` always reports the raw
truth in both directions; only --hook applies the timestamp interpretation.
"""
from html.parser import HTMLParser
import glob, os, re, sys, unicodedata

DOC = 'SITE-COPY.md'
JS_FILES = ['js/main.js']

# Text nodes shorter than this are ignored — initials, "©", stat placeholders.
MIN_LEN = 5

# Placeholders the doc uses where the site fills a value in at runtime.
PLACEHOLDERS = re.compile(r'\[[a-z_]+\]')

# "Heading:", "Body:", "Date:", "Q:" … labels the doc uses to structure an entry.
LABEL = re.compile(r'^[A-Z][A-Za-z0-9 \-()\',]{0,34}:\s*')
# Inline labels that appear mid-line after an em dash, e.g. "Email — hint: …".
INLINE_LABEL = re.compile(r'^(?:hint|note|tagged)\s*:\s*', re.I)

SKIP_TAGS = {'script', 'style', 'path', 'circle', 'rect', 'line',
             'defs', 'g', 'polygon', 'text'}
COPY_ATTRS = {'placeholder', 'aria-label', 'alt', 'data-demo-form', 'title'}


def norm(s):
    """Comparable form: entities decoded, quotes straightened, spacing collapsed."""
    s = unicodedata.normalize('NFKC', s)
    s = (s.replace('&amp;', '&').replace('&lt;', '<')
          .replace('&gt;', '>').replace('&nbsp;', ' '))
    s = re.sub(r'[‘’]', "'", s)
    s = re.sub(r'[“”]', '"', s)
    s = ' '.join(s.split())
    s = re.sub(r'\s+([.,;:!?])', r'\1', s)   # no space before punctuation
    s = s.replace('(', '').replace(')', '')  # hint spans add/remove parens
    return s.lower().strip('"\'')


class TextNodes(HTMLParser):
    """Visible text nodes plus copy-bearing attributes."""
    def __init__(self):
        super().__init__()
        self.out, self.skip = [], 0

    def handle_starttag(self, tag, attrs):
        if tag in SKIP_TAGS:
            self.skip += 1
        for k, v in attrs:
            if k in COPY_ATTRS and v and v.strip():
                self.out.append(v)

    def handle_endtag(self, tag):
        if tag in SKIP_TAGS and self.skip:
            self.skip -= 1

    def handle_data(self, data):
        if self.skip:
            return
        data = ' '.join(data.split())
        if data:
            self.out.append(data)


def build_corpus(pages):
    """One flat searchable blob. Tags become spaces so text split across
    inline elements (<strong>, <a>) rejoins as the reader sees it."""
    parts = []
    for f in pages:
        html = open(f, encoding='utf-8').read()
        # Read attributes first — <svg> carries aria-label and is stripped below.
        parts += re.findall(
            r'(?:placeholder|aria-label|alt|title|data-demo-form|data-count-to'
            r'|data-suffix|content)="([^"]*)"', html)
        html = re.sub(r'<(script|style|svg)\b.*?</\1>', ' ', html, flags=re.S)
        parts.append(re.sub(r'<[^>]+>', ' ', html))
    for j in JS_FILES:
        if os.path.exists(j):
            parts.append(open(j, encoding='utf-8').read())
    return norm(' | '.join(parts))


def doc_fragments(doc_text):
    """Copy fragments from the '>' quote lines, split into checkable pieces."""
    frags, fence, in_entry = [], False, False
    for lineno, line in enumerate(doc_text.split('\n'), 1):
        if line.lstrip().startswith('```'):
            fence = not fence
            continue
        if fence:
            continue
        if line.startswith('**ID:'):
            in_entry = True
            continue
        if line.startswith('#'):
            in_entry = False
            continue
        if not in_entry or not line.startswith('> '):
            continue
        raw = line[2:].strip()
        if not raw:
            continue
        # Composite rows: "Programs · $3,723,600 · 87%" and "a / b".
        pieces = re.split(r'\s+·\s+|\s+/\s+', raw) if ('·' in raw or ' / ' in raw) else [raw]
        for piece in pieces:
            piece = LABEL.sub('', LABEL.sub('', piece.strip()))
            piece = (piece.replace('**', '').replace('{{', '')
                          .replace('}}', '').replace('`', ''))
            piece = re.sub(r'\((?:none)\)', '', piece)
            piece = re.sub(r'\(tagged "[^"]*"\)', '', piece)
            # "Name — Role" pairs are two separate strings in the markup.
            subs = ([p for p in piece.split(' — ')]
                    if ' — ' in piece and not re.search(r'[.?!]', piece)
                    else [piece])
            for sub in subs:
                sub = INLINE_LABEL.sub('', sub.strip())
                # A runtime placeholder splits one line into several literals.
                for lit in PLACEHOLDERS.split(sub):
                    lit = lit.strip(' .·—/"\'')
                    if len(lit) >= MIN_LEN:
                        frags.append((lineno, lit))
    return frags


def resolves(frag, corpus):
    """True if the fragment exists in the site, whole or as em-dash-joined parts."""
    if norm(frag) in corpus:
        return True
    if ' — ' in frag:
        parts = [INLINE_LABEL.sub('', p).strip(' .·—/"\'')
                 for p in frag.split(' — ')]
        if all(len(p) < MIN_LEN or norm(p) in corpus for p in parts):
            return True
    return False


def main():
    verbose = '--verbose' in sys.argv
    hook = '--hook' in sys.argv
    say = (lambda *a, **k: None) if hook else print
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    if not os.path.exists(DOC):
        print(f'FAIL  {DOC} not found in {root}')
        return 1

    pages = sorted(glob.glob('*.html'))
    if not pages:
        print('FAIL  no HTML pages found')
        return 1

    doc_text = open(DOC, encoding='utf-8').read()
    corpus = build_corpus(pages)

    # --- A. every documented string still exists in the site ---
    frags = doc_fragments(doc_text)
    missing_from_site = [(n, f) for n, f in frags if not resolves(f, corpus)]

    # --- B. every string in the site is documented ---
    # Strip only the leading blockquote marker, so '>' inside code survives.
    doc_flat = norm(re.sub(r'^\s*>\s?', ' ', doc_text, flags=re.M)
                      .replace('**', ' ').replace('`', ' ')
                      .replace('{{', ' ').replace('}}', ' '))
    missing_from_doc = {}
    for f in pages:
        p = TextNodes()
        p.feed(open(f, encoding='utf-8').read())
        for node in p.out:
            n = norm(node)
            if len(n) < MIN_LEN:
                continue
            if n not in doc_flat:
                missing_from_doc.setdefault(n, set()).add(f)

    say(f'check-copy · {len(pages)} pages · {len(frags)} documented fragments')
    print()

    ok = True
    if missing_from_site:
        ok = False
        say(f'A. ACCURACY   FAIL — {len(missing_from_site)} documented string(s) '
              f'not found in the site:')
        for n, f in missing_from_site:
            say(f'     {DOC}:{n}  "{f[:88]}"')
        say('\n     → the doc was edited but the HTML was not. Apply these changes.')
    else:
        say(f'A. ACCURACY   PASS — all {len(frags)} documented fragments match the source')

    if missing_from_doc:
        ok = False
        say(f'\nB. COVERAGE   FAIL — {len(missing_from_doc)} site string(s) '
              f'missing from {DOC}:')
        for n, fs in sorted(missing_from_doc.items()):
            say(f'     [{", ".join(sorted(fs))}]  "{n[:88]}"')
        say(f'\n     → the site was edited but the doc was not. Update {DOC}.')
    else:
        say(f'B. COVERAGE   PASS — every visible string on every page is documented')

    print()
    say('IN SYNC' if ok else 'DRIFT DETECTED')
    if verbose and ok:
        print(f'\nchecked {len(frags)} fragments against '
              f'{len(pages)} pages + {len(JS_FILES)} script(s)')

    code = (1 if missing_from_site else 0) | (2 if missing_from_doc else 0)

    if hook:
        if ok:
            return 0
        doc_mtime = os.path.getmtime(DOC)
        newest_page = max(os.path.getmtime(f) for f in pages)
        if doc_mtime > newest_page:
            print('check-copy: SITE-COPY.md has edits not yet applied to the site '
                  '(doc is newer than every page). Not blocking.')
            return 0
        sys.stderr.write(
            'SITE-COPY.md and the site have drifted, and the HTML is the newer side '
            '— copy\nwas changed without the doc following. Reconcile them before '
            'finishing:\n'
            '  1. run  python3 check-copy.py  to see both directions\n'
            '  2. update SITE-COPY.md so it describes what the site now says\n'
            '  3. re-run until it reports IN SYNC\n')
        return 2

    return code


if __name__ == '__main__':
    sys.exit(main())
