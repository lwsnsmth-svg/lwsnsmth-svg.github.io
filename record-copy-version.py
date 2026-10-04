#!/usr/bin/env python3
"""
record-copy-version.py — file the current SITE-COPY.md into the copy editor's
version history, so the owner can see what Claude changed and why.

The copy editor (../Website builder) already notices edits made outside it: when it
next opens and finds a document history has never seen, it snapshots it as "SITE-COPY.md
changed outside the editor". That keeps history complete, but it is anonymous. It
records that something moved, not what or why, and only when the owner happens to
open the app next — by which time several of Claude's changes may have collapsed
into one unexplained jump.

This script files the same snapshot at the moment of the change, with a label and a
note. The owner opens History and reads "Removed the footer newsletter" instead of
guessing from a diff.

  python3 record-copy-version.py --label "Removed the footer newsletter" \
                                 --note "No newsletter exists; the signup came off all 7 pages."

It is idempotent on content: one entry per distinct document, never a duplicate. That
is what makes it safe to run from a Stop hook with no arguments — a turn that touched no
copy records nothing. So: label it yourself when you know what you did; the hook is the
backstop for when you forget.

When the editor is *running* it usually gets there first: the server polls the file every
few seconds and files its own anonymous "SITE-COPY.md changed outside the editor". So a
matching sha does not mean the work is done — it usually means the snapshot exists but is
unlabelled. This script therefore adopts that entry: same content, same position in
history, now carrying the label and note. An entry the owner made (saved, written, backup)
or one already labelled is never touched.

The record it writes is byte-compatible with the one `server.py:add_version` writes —
same fields, same id format, same `changed_lines` count — and uses kind `claude`, which
the app labels "Changed by Claude". Because the editor's own `snapshot_disk_if_new`
skips any sha already in history, filing the version here also stops the app adding
its anonymous duplicate later.

Exits 0 whatever happens, including when the editor app is not installed. Keeping the
doc and the site in sync is enforced elsewhere (check-copy.py, check-structure.py);
failing to write a history entry is not a reason to block a turn.
"""
import argparse, difflib, hashlib, json, os, re, secrets, sys
from datetime import datetime

DOC = 'SITE-COPY.md'
# The editor lives beside the website folder; --history or $COPY_EDITOR_HISTORY wins.
DEFAULT_HISTORY = os.path.join('..', 'Website builder', 'history')


def sha(text):
    return hashlib.sha256(text.encode('utf-8')).hexdigest()


def copy_lines(text):
    """The editable payload only — '>' copy and '»' note lines. Mirrors server.py."""
    return [l for l in text.split('\n') if l.startswith('>') or l.startswith('»')]


def versions(history):
    """Every record in history, newest first, exactly as server.py orders them."""
    if not os.path.isdir(history):
        return []
    out = []
    for name in sorted((f for f in os.listdir(history) if f.endswith('.json')),
                       reverse=True):
        try:
            with open(os.path.join(history, name), encoding='utf-8') as f:
                out.append(json.load(f))
        except (OSError, ValueError):
            continue  # a half-written or hand-edited file is not worth failing over
    return out


def main():
    ap = argparse.ArgumentParser(description='File SITE-COPY.md into the copy editor history.')
    ap.add_argument('--label', default='', help='short name shown in History')
    ap.add_argument('--note', default='', help='longer explanation, shown under the label')
    ap.add_argument('--history', default=os.environ.get('COPY_EDITOR_HISTORY', DEFAULT_HISTORY))
    ap.add_argument('--quiet', action='store_true', help='say nothing when there is nothing to do')
    args = ap.parse_args()

    root = os.path.dirname(os.path.abspath(__file__))
    os.chdir(root)
    say = (lambda *a: None) if args.quiet else print

    doc_path = os.path.join(root, DOC)
    if not os.path.exists(doc_path):
        say(f'record-copy-version: {DOC} not found — nothing to record.')
        return 0

    history = os.path.abspath(os.path.expanduser(args.history))
    parent = os.path.dirname(history)
    if not os.path.isdir(parent):
        say(f'record-copy-version: no copy editor at {parent} — skipping.')
        return 0

    content = open(doc_path, encoding='utf-8').read()
    digest = sha(content)

    prev = versions(history)

    # The running editor may already have snapshotted this exact content, anonymously.
    # Adopt that entry rather than skipping: the content is right, the label is missing.
    AUTO = ('SITE-COPY.md changed outside the editor', 'SITE-COPY.md when history began')
    for v in prev:
        if v.get('sha') != digest:
            continue
        if v.get('kind') != 'disk' or (v.get('label') or '') not in AUTO:
            say('record-copy-version: this version of SITE-COPY.md is already in '
                f'history as "{v.get("label") or v.get("kind")}" — left alone.')
            return 0
        if not args.label and not args.note:
            say('record-copy-version: already in history (unlabelled). '
                'Re-run with --label to name it.')
            return 0
        v['kind'] = 'claude'
        v['label'] = args.label.strip()[:120] or 'SITE-COPY.md after a change by Claude'
        v['note'] = args.note.strip()[:2000]
        try:
            with open(os.path.join(history, v['id'] + '.json'), 'w', encoding='utf-8') as f:
                json.dump(v, f, ensure_ascii=False, indent=1)
        except OSError as e:
            say(f'record-copy-version: could not update history ({e}) — not blocking.')
            return 0
        print(f'record-copy-version: named the editor\'s own snapshot '
              f'"{v["label"]}" in the copy editor history.')
        return 0

    changed = None
    if prev:
        before = copy_lines(prev[0].get('content', ''))
        diff = difflib.ndiff(before, copy_lines(content))
        changed = sum(1 for d in diff if d[:1] in '+-')

    now = datetime.now().astimezone()
    vid = now.strftime('%Y%m%d-%H%M%S') + '-' + secrets.token_hex(2)
    m = re.search(r'\*\*Version:\*\*\s*([^\s·]+)', content)
    record = {
        'id': vid,
        'created': now.isoformat(timespec='seconds'),
        'kind': 'claude',
        'label': (args.label or 'SITE-COPY.md after a change by Claude').strip()[:120],
        'note': args.note.strip()[:2000],
        'sha': digest,
        'size': len(content.encode('utf-8')),
        'doc_version': m.group(1) if m else None,
        'changed_lines': changed,
        'content': content,
    }

    try:
        os.makedirs(history, exist_ok=True)
        with open(os.path.join(history, vid + '.json'), 'w', encoding='utf-8') as f:
            json.dump(record, f, ensure_ascii=False, indent=1)
    except OSError as e:
        say(f'record-copy-version: could not write history ({e}) — not blocking.')
        return 0

    n = '' if changed is None else f', {changed} copy line(s) changed'
    print(f'record-copy-version: filed "{record["label"]}" in the copy editor history{n}.')
    return 0


if __name__ == '__main__':
    sys.exit(main())
