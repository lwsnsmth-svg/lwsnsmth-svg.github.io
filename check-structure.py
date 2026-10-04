#!/usr/bin/env python3
"""
check-structure.py — verify SITE-COPY.md is still shaped the way the copy editor
reads it.

`check-copy.py` compares *strings*: does every quoted line in the doc appear in the
HTML, and vice versa. That is the right check for wording, and it is blind to the
layer the copy editor actually renders — pages, sections, IDs and the fields under
them. A section heading left standing over nothing contains no copy, so it passes
check-copy cleanly while showing the owner an empty section in the editor. This
script checks that layer.

The parser below is a port of `app/doc.js` in the Website builder folder, regex for
regex. That is deliberate: the point is to fail here, in a script Claude runs, on
anything that would render wrongly there. If doc.js changes, change this too.

Seven checks:

  1. DUPLICATE IDS    doc.js keeps the first block for a repeated ID; the second is
                      unaddressable, and edits made to it are dropped on write.
  2. EMPTY SECTIONS   a `## ` heading with no blocks under it. This is what a
                      half-finished deletion leaves behind.
  3. EMPTY BLOCKS     an `**ID:**` with no `>` copy lines — a block with no fields.
  4. SECTION NUMBERS  `## A4.` prefixes must carry the page's own letter and run
                      1..n with no gaps. The editor prints them verbatim, so a
                      deletion that leaves A3, A5, A6 is visible to the owner.
  5. PAGE LETTERS     `# A.` … must likewise run from A with no gaps.
  6. FILE MAPPING     a page whose intro names an HTML file must name one that
                      exists, and every page on disk must be claimed by exactly one
                      doc page. A doc page naming no file is fine — A. Global and
                      I–K describe text spread across the site — because an
                      undocumented page shows up as an unclaimed file either way.
  7. COVERS COUNT     the header's "Covers: N pages" must match check 6's tally.

Exit code 0 = sound, 1 = problems found.

  python3 check-structure.py            # report
  python3 check-structure.py --verbose  # also print the structure it parsed
  python3 check-structure.py --hook     # enforcement mode: silent when sound,
                                        # exit 2 with the problems on stderr otherwise

--hook needs no timestamp heuristic of the kind check-copy.py uses. Every problem here
is wrong whoever caused it: a duplicate ID or a heading over nothing is not a legitimate
half-finished state the owner might be sitting in, so there is nothing to disambiguate.

Blocks marked `[DELETE]` are reported but never fail the run: that marker is the
owner asking for a removal, so it is a legitimate inbox state, exactly like the
doc-is-newer case in check-copy.py --hook.
"""
import glob, os, re, sys

DOC = 'SITE-COPY.md'

# --- mirrored from app/doc.js, deliberately identical -----------------------
PAGE_RE = re.compile(r'^# ([A-Z])\. (.+?)\s*$')
SECTION_RE = re.compile(r'^## (.+?)\s*$')
ID_RE = re.compile(r'^\*\*ID:\s*`([^`]+)`\*\*\s*$')
COPY_RE = re.compile(r'^>( ?)(.*)$')
NOTE_RE = re.compile(r'^»( ?)(.*)$')
FENCE_RE = re.compile(r'^\s*```')
RULE_RE = re.compile(r'^-{3,}\s*$')
FILE_RE = re.compile(r'`([\w-]+\.html)`')
VERSION_RE = re.compile(r'\*\*Version:\*\*\s*([^\s·]+)')
COVERS_RE = re.compile(r'\*\*Covers:\*\*\s*(\d+)\s*pages')

# "## A4. Footer — link columns" → letter A, number 4.
SECTION_NUM_RE = re.compile(r'^([A-Z])(\d+)\.\s')

DELETE_MARKER = '[DELETE]'


def parse(text):
    """Port of doc.js parse(). Returns the page/section/block tree it builds."""
    lines = text.split('\n')
    pages, blocks = [], []
    page = section = block = None
    fence = False

    def close_block(end):
        nonlocal block
        if block:
            block['end'] = end
            finish_block(block, lines)
            block = None

    def ensure_section():
        nonlocal section
        if section is None:
            section = {'title': None, 'line': None, 'intro': [], 'blocks': []}
            page['sections'].append(section)
        return section

    for i, line in enumerate(lines):
        if FENCE_RE.match(line):
            fence = not fence
            if block is None and section is not None:
                section['intro'].append(line)
            continue
        if fence:
            if block is None and section is not None:
                section['intro'].append(line)
            continue

        if line.startswith('# '):
            close_block(i)
            m = PAGE_RE.match(line)
            page = ({'letter': m.group(1), 'title': m.group(2), 'line': i,
                     'intro': [], 'sections': []} if m else None)
            if page:
                pages.append(page)
            section = None
            continue

        if page is None:
            continue  # preamble: title, changelog, how-to, contents

        if line.startswith('## '):
            close_block(i)
            m = SECTION_RE.match(line)
            section = {'title': m.group(1) if m else line[3:], 'line': i,
                       'intro': [], 'blocks': []}
            page['sections'].append(section)
            continue

        if RULE_RE.match(line):
            close_block(i)
            continue

        m = ID_RE.match(line)
        if m:
            close_block(i)
            block = {'id': m.group(1), 'start': i, 'page': page['letter'],
                     'section': section}
            ensure_section()['blocks'].append(block)
            blocks.append(block)
            continue

        if block is not None:
            continue
        (section['intro'] if section is not None else page['intro']).append(line)

    close_block(len(lines))

    for p in pages:
        m = FILE_RE.search(' '.join(p['intro']))
        p['file'] = m.group(1) if m else None
        p['blockCount'] = sum(len(s['blocks']) for s in p['sections'])

    return {'pages': pages, 'blocks': blocks,
            'version': (VERSION_RE.search(text) or [None, None])[1] if VERSION_RE.search(text) else None}


def finish_block(b, lines):
    copy, notes = [], []
    for i in range(b['start'] + 1, b['end']):
        line = lines[i]
        m = COPY_RE.match(line)
        if m:
            copy.append(m.group(2))
            continue
        m = NOTE_RE.match(line)
        if m:
            notes.append(m.group(2))
    b['copy'] = copy
    b['notes'] = notes
    b['deleted'] = '\n'.join(copy).strip() == DELETE_MARKER


def main():
    verbose = '--verbose' in sys.argv
    hook = '--hook' in sys.argv
    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)

    if not os.path.exists(DOC):
        print(f'FAIL  {DOC} not found in {root}')
        return 1

    text = open(DOC, encoding='utf-8').read()
    doc = parse(text)
    pages, blocks = doc['pages'], doc['blocks']
    problems = []

    # 1. Duplicate IDs.
    seen = {}
    for b in blocks:
        if b['id'] in seen:
            problems.append(f'duplicate ID `{b["id"]}` — '
                            f'{DOC}:{seen[b["id"]] + 1} and {DOC}:{b["start"] + 1}. '
                            f'The editor can only reach the first; edits to the second '
                            f'are dropped on write.')
        else:
            seen[b['id']] = b['start']

    # 2. Empty sections and 3. empty blocks.
    for p in pages:
        for s in p['sections']:
            if not s['blocks']:
                where = f'{DOC}:{s["line"] + 1}' if s['line'] is not None else DOC
                problems.append(f'section "{s["title"]}" has no blocks ({where}) — '
                                f'it shows in the editor as an empty heading. '
                                f'Remove the heading, or add the blocks it promises.')
    for b in blocks:
        if not b['copy']:
            problems.append(f'block `{b["id"]}` has no `>` copy lines '
                            f'({DOC}:{b["start"] + 1}) — nothing to edit.')

    # 4. Section numbering, per page.
    for p in pages:
        numbered = []
        for s in p['sections']:
            m = SECTION_NUM_RE.match(s['title'] or '')
            if m:
                numbered.append((m.group(1), int(m.group(2)), s))
        for letter, num, s in numbered:
            if letter != p['letter']:
                problems.append(f'section "{s["title"]}" sits on page '
                                f'{p["letter"]}. {p["title"]} but is numbered {letter}{num} '
                                f'({DOC}:{s["line"] + 1}).')
        run = [n for l, n, _ in numbered if l == p['letter']]
        if run and run != list(range(1, len(run) + 1)):
            got = ', '.join(f'{p["letter"]}{n}' for n in run)
            want = ', '.join(f'{p["letter"]}{n}' for n in range(1, len(run) + 1))
            problems.append(f'page {p["letter"]}. {p["title"]} numbers its sections '
                            f'{got} — expected {want}. A removed section leaves a gap; '
                            f'renumber the headings (IDs never change).')

    # 5. Page letters.
    letters = [p['letter'] for p in pages]
    want = [chr(ord('A') + i) for i in range(len(letters))]
    if letters != want:
        problems.append(f'page letters run {", ".join(letters)} — '
                        f'expected {", ".join(want)}.')

    # 6. Page ↔ file mapping.
    on_disk = set(glob.glob('*.html'))
    claimed = {}
    for p in pages:
        if p['file'] is None:
            continue  # cross-cutting page; check 6b catches anything left undocumented
        if p['file'] not in on_disk:
            problems.append(f'page {p["letter"]}. {p["title"]} names `{p["file"]}`, '
                            f'which is not in {root}.')
        claimed.setdefault(p['file'], []).append(p['letter'])
    for f, ls in sorted(claimed.items()):
        if len(ls) > 1:
            problems.append(f'`{f}` is claimed by more than one page: '
                            f'{", ".join(ls)}.')
    for f in sorted(on_disk - set(claimed)):
        problems.append(f'`{f}` is on disk but no page in {DOC} documents it — '
                        f'add a page section for it.')

    # 7. Header page count.
    m = COVERS_RE.search(text)
    if m and int(m.group(1)) != len(claimed):
        problems.append(f'the header says "Covers: {m.group(1)} pages" but '
                        f'{len(claimed)} pages map to a file — update the header.')

    pending = [b for b in blocks if b['deleted']]

    say = (lambda *a, **k: None) if (hook and not problems) else print

    say(f'check-structure · {len(pages)} pages · '
        f'{sum(len(p["sections"]) for p in pages)} sections · {len(blocks)} blocks')
    say()

    if verbose:
        for p in pages:
            say(f'  {p["letter"]}. {p["title"]}  [{p["file"] or "—"}]  '
                f'{p["blockCount"]} blocks')
            for s in p['sections']:
                say(f'      {s["title"] or "(no heading)"}  ({len(s["blocks"])})')
        say()

    if problems:
        print(f'STRUCTURE   FAIL — {len(problems)} problem(s):')
        for p in problems:
            print(f'     {p}')
        print(f'\n     → {DOC} still parses, but the copy editor will not show the '
              f'owner\n       what the site actually is. Fix these before finishing.')
    else:
        say('STRUCTURE   PASS — the copy editor reads this document cleanly')

    if pending:
        say(f'\nNOTE  {len(pending)} block(s) marked {DELETE_MARKER}, waiting to be '
            f'applied to the site:')
        for b in pending:
            say(f'     {DOC}:{b["start"] + 1}  `{b["id"]}`')

    say()
    say('SOUND' if not problems else 'STRUCTURE DRIFT')

    if not problems:
        return 0
    if hook:
        # Same contract as check-copy.py --hook: exit 2 with the fix on stderr.
        sys.stderr.write(
            f'{DOC} is out of shape for the copy editor. The owner would see this in '
            f'the app.\nFix before finishing:\n'
            f'  1. run  python3 check-structure.py  for the list above\n'
            f'  2. correct {DOC}\n'
            f'  3. re-run until it reports SOUND\n')
        return 2
    return 1


if __name__ == '__main__':
    sys.exit(main())
