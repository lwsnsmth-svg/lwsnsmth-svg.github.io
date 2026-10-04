# Ascent Website

Static marketing site for a nonprofit. Plain HTML, one stylesheet, two scripts.
**No build step and no framework** — the `.html` files are what ship.

```
index · about · programs · get-involved · demo · 404   (6 pages)
css/styles.css     all styling; design tokens at the top drive everything
js/main.js         nav, theme, counters, accordion
js/theme-init.js   sets theme before first paint; also adds html.js
SITE-COPY.md       ← source of truth for all user-facing text
check-copy.py      verifies SITE-COPY.md and the HTML still agree (wording)
check-structure.py verifies the copy editor can still read SITE-COPY.md (shape)
record-copy-version.py  files the doc in the copy editor's history, with a label
```

The owner edits `SITE-COPY.md` through a local app in `../Website builder`
("Copy Editor"). It is a pure view over the doc — pages, sections and fields are
parsed out of it live — so **the doc is the only thing to keep aligned.** See
"Keeping the copy editor aligned" below.

Preview with `python3 -m http.server 8000`. There is nothing to compile.

---

## SITE-COPY.md is the source of truth for copy

Every user-facing string on this site is documented in `SITE-COPY.md`: 180+ blocks,
each with a stable `ID:`, the context around it, and the copy itself in `>` lines.
The owner edits that file and hands it back as the way of requesting copy changes.

**Read `SITE-COPY.md` before changing any user-facing text.** It carries intent and
length constraints that are not recoverable from the HTML — which strings are
placeholders, which numbers are invented, what a block is trying to achieve, and
what breaks if it gets longer.

### The three rules

1. **Never change copy in the HTML without updating `SITE-COPY.md` in the same pass.**
   A stale doc is worse than no doc, because it is still trusted.
2. **Run `python3 check-copy.py` before finishing any turn that touched copy.**
   It must report `IN SYNC`. This is enforced by a Stop hook, but run it yourself
   rather than waiting to be told.
3. **Run `python3 check-structure.py` too.** It must report `SOUND`. Copy can be in
   sync while the document is mis-shaped for the editor — see below.

### Applying the owner's edits

When asked to apply the copy doc, diff `SITE-COPY.md` against what the HTML
currently says and change **only** what moved. `check-copy.py` prints both
directions and is the fastest way to see the delta.

Conventions inside the doc:

| Marker | Meaning |
| --- | --- |
| `> text` | the live copy — the editable payload |
| `ID: SECTION.block` | stable address; **never renumber or remove** |
| `{{text}}` | renders in the orange accent colour |
| `**text**` | bold within a sentence |
| `» note` | an instruction to you, not copy — act on it, don't paste it |
| `[DELETE]` | remove this block from the site |

A `»` note may ask for judgement rather than a specific string ("make this
punchier"). Answer it in your reply; don't silently invent a rewrite and ship it.

### When copy is added or removed

Adding a section to the site means adding a matching block to `SITE-COPY.md` with a
new ID, context line, and length guidance. Removing one means removing its block.
`check-copy.py` fails on both directions, so neither can be forgotten.

A removal is not finished when the blocks are gone. Also:

- **Delete the `##` section heading** if it now stands over nothing.
- **Renumber the remaining headings** on that page so they run `X1, X2, X3…` with no
  gap. Headings carry a number; **IDs never change** — renumber `## A5.` → `## A4.`,
  never `GLOBAL.FOOTER.col2`.
- **Follow the string into the other blocks.** A deleted form leaves its confirmation
  behind in §H, its alt text in §J, its description in a neighbour's `Context:` line.
  Grep the doc for the subject word, not just the ID stem.
- **Update the changelog** at the top of the doc and bump `**Version:**`. That block is
  how the owner learns what moved and why.

---

## Keeping the copy editor aligned

The owner reads the doc through the Copy Editor app in `../Website builder`. It parses
`SITE-COPY.md` on a few seconds' poll and renders whatever it finds, so content
alignment is automatic — but only if the document is *shaped* the way it expects.

`check-copy.py` cannot see that layer. It compares strings, and the residue of a
half-finished deletion contains no strings: a heading over nothing, a gap in the
section numbers, a duplicated ID. All of that passes `IN SYNC` and still shows the
owner a document that does not describe the site.

**`check-structure.py`** closes that gap. It is a port of the app's own parser
(`app/doc.js`, regex for regex) plus seven checks — duplicate IDs, empty sections,
blocks with no fields, section numbering, page letters, page↔file mapping, and the
header's page count. Run it after any structural change; it must say `SOUND`. If you
change `doc.js`, change this script with it.

**`record-copy-version.py`** puts the change in the app's History with a name:

```bash
python3 record-copy-version.py --label "Removed the footer newsletter" \
                               --note "Why, and what else came off with it."
```

Do this on any turn that edits the doc. Without it the owner gets an unlabelled
"SITE-COPY.md changed outside the editor" and has to reconstruct the reason from a
diff. If the app happens to be running it will have filed that anonymous snapshot
already — the script then adopts and renames it rather than adding a duplicate.

All three run as Stop hooks (`.claude/settings.json`): the two checks block on drift,
and the recorder is a silent backstop that labels nothing you have not labelled
yourself. Run them by hand anyway — a hook that fires after you have stopped is a
worse place to learn this than the middle of the turn.

---

## Images: the owner can change them without you

The copy editor's **Images** tab lists every picture the site shows and replaces any of
them from an upload. That half writes to the site directly — `assets/` and the `<img>`
tags — because there is no document in between. Three consequences for you:

- **A placeholder may already be a photograph.** Replacing an inline
  `<svg role="img" aria-label="…">` swaps the whole block for an `<img>` carrying the same
  text as its `alt`. Never put the drawing back because a `<svg>` "should" be there, and
  never rewrite that alt text to describe the old drawing.
- **The image slots are found by shape, not by a list.** An `<img>`, a `<link rel="icon">`,
  an `og:image`, and any `<svg role="img" aria-label="…">` are offered to the owner;
  `aria-hidden` icons are not. New artwork you add is replaceable only if it follows that
  shape, so give every real image an `alt` or `aria-label` — which §J of the doc documents
  anyway.
- **Image history is not doc history.** It lives in `../Website builder/history/images`,
  with the file that was replaced and the previous text of every page touched. Nothing
  there needs `record-copy-version.py`, and nothing about an image belongs in
  `SITE-COPY.md` except its description.

The owner's replacement keeps the alt text, so `check-copy.py` stays in sync by
construction. If they tell you the picture now shows something else, change the §J wording
and the HTML `alt` in the same pass, as with any other copy.

---

## Content status

The copy is realistic placeholder text for a fictional organisation. Not yet real:
staff and board names, all statistics, and most images (inline SVG placeholders stand in;
the four phase cards on Programs & Services use real tool screenshots from `assets/`).
The Demo page embeds that same tool (the Logic Model Mapper) live, in an iframe from
Netlify; nothing inside the frame is site copy. The site
describes a hypothetical service set; it carries no quality assurance or governance detail.

There are no forms, and no way to contact Ascent: the Contact page went in v9 of the
doc, donations in v6. Snapshots of the site before each removal are in
`~/Desktop/Ascent Website archive/`.

## Things that look wrong but are deliberate

Documented in `README.md` under "Things that are deliberate" — `html.js` gating the
scroll reveal, `minmax(min(280px, 100%), 1fr)` in the grids, `.nav-toggle` using flex
rather than grid, the `.section--brand` colour overrides, and buttons being allowed
to wrap. Each fixes a real bug; read that section before simplifying any of them.
