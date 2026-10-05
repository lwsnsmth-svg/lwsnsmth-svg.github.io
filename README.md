# Ascent — Nonprofit Website Template

A complete, dependency-free static website template for a nonprofit organisation.
Plain HTML, one CSS file, one JS file. No build step, no framework, no CDN calls —
open `index.html` in a browser and it works.

The content is realistic placeholder copy for **The Ascent Collaborative**, a fictional
nonprofit program evaluation practice in New York City. It deliberately makes no claim
about track record, client count, staff size or years in operation — everything asserted
describes the model and its published standards. Everything is meant to be replaced —
see `SITE-COPY.md`.

---

## Files

```
.
├── index.html          Homepage — hero, stats, problem, pipeline, standards, CTA
├── about.html          Mission and method, evidence timeline
├── programs.html       Two ways in + four phase detail sections + engagement structures
├── get-involved.html   "Our Model" — delivery stack, evidence base, model benefits, roles
├── demo.html           Live demo of the Logic Model Mapper, embedded from Netlify — the
│                       one page that loads something from another host
├── 404.html            Not-found page
├── css/styles.css      All styling, organised into 23 numbered sections
├── js/main.js          Nav, counters, accordion
├── js/theme-init.js    Tiny head script that adds the `js` class
└── assets/
    ├── Logo.png        Your logo — line art, used as the header/footer mark
    ├── Logo_simple.png Previous mark (unused since 1 October 2026)
    ├── Logo_full.png   Filled variant of the previous mark (unused)
    ├── favicon.png     Browser-tab icon (apple-touch-icon.png is its home-screen twin)
    ├── phase-*.png     Tool screenshots on the four Programs & Services phase cards
    └── fonts/          Caladea Regular + Italic (Cambria stand-in) and its OFL licence
```

## Running it

Just open `index.html`. For a local server (needed if you later add `fetch` calls):

```bash
python3 -m http.server 8000
```

Then visit <http://localhost:8000>.

---

## What's built in

- **Responsive** from 320px up, with a slide-down mobile nav at ≤900px.
- **Dark only.** There is no theme toggle; the dark palette is the `:root` token set.
- **Accessible foundations** — skip link, visible focus rings, landmark elements,
  `aria-current` on the active nav item, ARIA-wired accordion
  and toggle buttons, `prefers-reduced-motion` respected throughout.
- **Animated stat counters** and scroll-reveal, both of which degrade gracefully
  without `IntersectionObserver` and switch off under reduced-motion.
- **SEO basics** — per-page titles and descriptions, Open Graph and Twitter card tags,
  and `NGO` schema.org JSON-LD on the homepage.
- **Print stylesheet** that strips navigation and CTAs.

---

## Making it yours

### 1. Names and details

Search and replace across all `.html` files:

| Find | Replace with |
| --- | --- |
| `Ascent` | Your organisation's name |
| `For Research & Evaluation` | Your tagline |
| `example.org` | Your domain |
| `New York, NY` | Your city |
| `(555) 014-2000` | Your phone numbers |

```bash
# macOS/BSD sed — adjust the strings first, and keep the backup files until you've checked
sed -i '' 's/Ascent/Your Org/g' *.html
```

### 2. Colours

Everything derives from the tokens at the top of `css/styles.css`. Change the brand
ramps and the whole site follows — including the dark theme, which is defined in the
two blocks immediately after.

```css
:root {
  --pine-600: #1d6355;   /* primary brand */
  --amber-500: #e07b22;  /* accent / call-to-action */
}
```

Check contrast after changing these. Body text should hit at least 4.5:1 against its
background, large headings 3:1.

### 3. Fonts

The type system, set by tokens at the top of `css/styles.css`:

| Text | Face | Token |
| --- | --- | --- |
| Site title | Helvetica Neue Condensed Bold, **small caps** | `--font-bold` + `font-variant-caps: small-caps` |
| Site subtitle | Helvetica Neue Light | `--font-light` |
| All headings and bold text — page and section titles, card headings, buttons, nav, eyebrows, tags, inline `<strong>` | Helvetica Neue Condensed Bold | `--font-bold` |
| Table cells and captions | Helvetica Neue Thin | `--font-thin` |
| Table column and row headings (`th`) | Helvetica Neue Condensed Bold | `--font-bold` |
| Form fields — typed text, placeholders, dropdowns | Helvetica Neue Thin | `--font-thin` |
| Body text and pull quotes | Cambria | `--font-body` |
| Form field labels | Helvetica Neue | `--font-heading` |

**Where the fonts come from.** Helvetica Neue, including Condensed Bold, Light and Thin, ships
with macOS and iOS and is read from the visitor's machine through `local()` `@font-face`
rules; it is licensed with the operating system, so no file is hosted. Cambria ships with
Windows and with Microsoft Office. Where Cambria is missing — most Macs — body text uses
**Caladea**, hosted in `assets/fonts/`: an open-licence face (SIL OFL 1.1, licence in
`assets/fonts/OFL.txt`, which must stay with the files) drawn to Cambria's letter widths, so
line breaks match. Browsers download Caladea only when Cambria isn't installed.

**What non-Apple visitors see.** Windows and Android have no Helvetica Neue. Bold text falls
to Arial Narrow or Roboto Condensed where installed, then ordinary Helvetica/Arial Bold;
table text falls to regular Arial rather than Thin. To make those identical everywhere,
license webfont versions (or choose close free ones such as Roboto Condensed and Roboto
Thin), self-host them and put them first in `--font-bold` and `--font-thin`.

**Rules that keep it working.** Anything on `--font-bold` stays at weight 700 and anything on
`--font-thin` at weight 100, and `--font-light` at 300 — each family has a single face.
Helvetica Neue has no true small-caps cut, so the browser draws the site title's small caps
from scaled capitals. Thin loses legibility quickly at small sizes and in pale colours, which
is why table text is set in the full text colour rather than muted grey.

### 4. Images

Every photo is currently an inline SVG placeholder marked with a comment. Replace each
one with a real `<img>`:

```html
<!-- was: <svg viewBox="0 0 800 640" …>…</svg> -->
<img src="assets/hero.jpg" alt="Two researchers reviewing a study design at a table"
     width="800" height="640" loading="lazy" decoding="async">
```

Write real alt text describing what's in the photo — and update `ALT.*` in
`SITE-COPY.md` to match. Use `loading="lazy"` on everything
below the fold, but *not* on the hero image.

Team portraits: square, at least 600×600px, replacing the initials block inside
`.person__photo`.

### 5. Forms, contact and donations

**There are no forms on the site, and no way to contact Ascent.** The Contact page, every
link and button to it, the email addresses and phone numbers, and the demo form handler in
`js/main.js` were removed on 1 October 2026; the site as it stood before is in
`~/Desktop/Ascent Website archive/2026-10-01 before contact removed/`. If a form comes
back, point it at a real service (Formspree, Netlify Forms, Basin, or your CRM's hosted
endpoint) rather than a front-end-only stub.

**Donations are off the site for now.** The Fund page, the nav and footer links to it,
and the donation widget in `js/main.js` were removed on 1 October 2026; the full site as
it stood before is in `~/Desktop/Ascent Website archive/`. If they come back, they need a
payment processor — never collect card details yourself; use an embed or hosted checkout
from Stripe, Donorbox, Classy, Givebutter, or similar.

### 6. Numbers and copy

Every statistic, financial figure, quote, and staff name in this template is invented.
Replace them with your audited figures before publishing anything, and remove the
placeholder notes (search for "Template note" and "Template notice").

---

## Deploying

Any static host works — there is no build step:

- **Netlify / Vercel / Cloudflare Pages** — drag the folder in, or connect a repo.
- **GitHub Pages** — push to a repo, enable Pages on the root of the branch.
- **Traditional hosting** — upload the folder over SFTP.

Before launch:

- [ ] Replace all placeholder copy, figures, and names
- [ ] Replace the SVG placeholders with real photos and real alt text
- [ ] Add a real `assets/og-image.jpg` (1200×630) and update the `og:url` on each page
- [ ] Write real privacy, terms, and accessibility pages (footer links are `#` stubs)
- [ ] Update the JSON-LD block in `index.html`
- [ ] Run the pages through Lighthouse and a contrast checker
- [ ] Test the whole site once with a keyboard only, and once with a screen reader

---

## Copy is documented in SITE-COPY.md

Every user-facing string is catalogued in `SITE-COPY.md` with a stable ID, the
context around it, and length guidance. That file is the source of truth for copy:
edit it and the changes get applied to the HTML, rather than editing markup directly.

`check-copy.py` verifies the two still agree, in both directions:

```bash
python3 check-copy.py
```

It fails if the doc describes copy the site doesn't have, or the site contains copy
the doc doesn't document.

The owner edits that file through the Copy Editor app in `../Website builder`, which
reads `SITE-COPY.md` live and renders whatever it finds. Its Images tab also replaces the
pictures on the site: it writes into `assets/` and updates the `<img>` tags itself, so a
placeholder `<svg role="img">` may already have become a photograph — see `CLAUDE.md`.
Two more scripts keep the app honest about the site:

```bash
python3 check-structure.py       # is the doc still shaped the way the editor reads it?
python3 record-copy-version.py --label "what changed"   # file it in the app's History
```

`check-structure.py` catches what `check-copy.py` structurally cannot see, because it
involves no copy: a section heading left standing over nothing, a gap in the section
numbering, a duplicated ID, a page on disk that no part of the doc documents. It is a
port of the editor's own parser, so what fails here is what would render wrongly there.

All three run as Stop hooks in `.claude/settings.json`. See `CLAUDE.md` for the full
workflow.

## Things that are deliberate

A few choices look like they could be simplified but shouldn't be:

- **`html.js` gates the scroll reveal.** `.reveal` elements start at `opacity: 0` only
  when `js/theme-init.js` has added the `js` class. If you remove that class, a JS
  error or a blocked script will leave large parts of the page permanently invisible.
- **The reveal has a 3-second failsafe.** If `IntersectionObserver` never reports an
  intersection — a zero-height viewport, a hidden container, an embedded frame — the
  timer in `js/main.js` reveals everything. Without it the page renders blank in those
  cases. It never fires in a normal viewport, where the first element resolves at once.
- **`.hero__title em` must not be `nowrap`.** The accent phrase is copy and can be any
  length; pinning it to one line drives the text column to min-content and collapses
  the hero image track to `0px`. The `minmax(0, …)` on `.hero__inner` guards the same
  failure.
- **`minmax(min(280px, 100%), 1fr)`** in the grid definitions — the inner `min()` lets
  a track collapse below its ideal width. Plain `minmax(280px, 1fr)` overflows any
  viewport narrower than 280px.
- **`.nav-toggle` is `display: flex`, not `grid`.** Grid rows stretch to fill the
  button, which spreads the three bars too far apart for the close-icon transform to
  form a clean ×.
- **Light-surfaced components override their colours inside `.section--brand`.**
  Without that block, a `.card` or `.quote` on a dark band inherits white text onto a
  white background.
- **Buttons wrap.** `.btn` deliberately has no `white-space: nowrap`, so long labels
  reflow instead of overflowing small screens.
- **Asset URLs carry a version: `css/styles.css?v=…`, `js/main.js?v=…`,
  `assets/favicon.svg?v=…`.** Browsers keep static files for a while without asking the
  server whether they changed, so an edited stylesheet can go unseen — which is how the
  logo swap once showed the new image inside the old, square-cropping CSS. **Whenever you
  change one of those files, change its `?v=` value on all five pages** (a date works).
  Deleting the query string brings the stale-file problem back.

## Browser support

Current versions of Chrome, Edge, Firefox, and Safari. The layout uses CSS grid,
custom properties, `clamp()`, and `color-mix()`; older browsers will get an unstyled
but readable document rather than a broken one.

## Licence

Template code is yours to use and modify freely. The placeholder copy is fictional —
"Ascent", its staff, statistics, and partner names are invented for demonstration.
