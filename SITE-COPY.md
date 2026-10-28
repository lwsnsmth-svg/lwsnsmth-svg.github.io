# Ascent — Site Copy Document

Every piece of text on the site, in the order a visitor meets it, with the context
you need to judge whether the wording is right.

**Version:** 81 · **Updated:** 28 October 2026 · **Covers:** 8 pages

> **What changed in v81.** Your edits to the home page, applied word for word. The card on the
> hero image (`HOME.HERO.badge`) is now one sentence, "Unrestricted implementation support and
> intuitive software make MEL accessible to **every** program", with "every" in orange; it
> was a big "1.5%" over "of program budget for two years of hands-on evaluation support". The
> "Evaluation that Goes Further" heading now reads "An evaluation process accountable to
> outcomes and a platform to monitor it all" (was "…accountable to program outcomes"), and its
> lead drops its opening sentence ("Static evaluations describe a snapshot of a program.").
> The line above the "Try the demo" and "Download the app" buttons ("A single app shows the
> power of our evaluation model.") is gone, since you emptied it; the buttons now follow the
> tool-view cards directly. The empty `Tagline:` field stays in this document as you left it.
> **No ID changed.**
>
> Worth a look: the new heading runs to three lines on a laptop and four on a phone, past the
> one or two it was sized for. The 1.5% fee now appears nowhere on the site; the badge was the
> last place it showed. And "MEL" is the only acronym in the hero and is spelled out nowhere on the site, so
> a first-time visitor meets it undefined above the fold.

> **What changed in v80.** The Download page's eyebrow no longer says "pre-release build",
> at your request: v1.0.0 is out. It reads "Version 1.0.0" (`DOWNLOAD.CHOOSE.intro`, was
> "Version 0.0.3 · pre-release build"). The three buttons' fallback links in the page's markup
> moved to the v1.0.0 installers with it. **No ID changed.**
>
> Worth knowing: while the page can reach GitHub, the version still comes from the newest
> release, so it follows every future release with no edit here. Nothing in the eyebrow is
> now left to change when a build is signed.

> **What changed in v79.** Our Model is now unlisted, at your request: nothing on the site
> links to it, so a visitor reaches it only from a link you give them. Removed: "Our Model"
> from the main navigation on every page (`GLOBAL.NAV.items`, now five items), the
> "How the model works" link under the home page's "Ascent, in brief" (`HOME.BRIEF.links`,
> now just the "Our program" button), and the Our Model shortcut card on the 404 page
> (`NOTFOUND.cards`, now one card). The page itself is unchanged except that it carries a
> `noindex, nofollow` tag, so search engines don't list it either, the way the editor demo
> (§K) is kept out. **No ID changed.**
>
> Worth a look: the page's own nav has no "Our Model" item, so a visitor who lands there
> sees no highlighted tab; they get back through the "Home" breadcrumb or the nav. The
> page's closing button, "Explore the pipeline", still goes to Evaluation Process.

> **What changed in v78.** Our Model, at your request: "Impact logic" now comes before "The
> structure". The page runs banner, Impact logic, The structure, closing band. The two
> sections swapped places whole, so no wording changed; the alternating background tint
> swapped with them (the first section is plain, the second tinted). Headings renumbered:
> Impact logic is §E2 (it was the odd "E2b"), The structure §E3, the closing band §E4.
> **No ID changed.**
>
> Worth a look: the structure section's heading ("Finding affordability in better
> coordination.") used to follow straight on from the banner's promise of an explanation;
> it now follows the impact cascade instead.

> **What changed in v77.** Evaluation Process, at your request: more space between the end of
> the "How the program runs" text and the Evaluation Pipeline app: 96px, the same as the space
> at the top of the section. No wording changed. **No ID changed.** The
> app itself now shows the program journey (Intake through Onward support, Graduation
> included), so "until graduation" in the paragraph above it is explained again. I updated the
> notes in §D3 that said otherwise.

> **What changed in v76.** About, at your request: the opening of "The evidence base" is now
> stacked and centred, like "How the program runs" on Evaluation Process. The eyebrow and "An
> outcomes-oriented synthesis." used to sit on the left with the paragraph beside them; now
> the paragraph sits under the heading. No wording changed. **No ID changed.**
>
> Worth a look: the paragraph is five sentences, about 430 characters, so centred it runs to
> six or seven lines on a laptop. Long centred text is harder to read than text set left.

> **What changed in v75.** Evaluation Process, at your request: the eight-step timeline in "How
> the program runs" (Intake through Onward support, `PROGRAMS.SEQUENCE.steps`) is gone, and all
> of that section's text (eyebrow, heading, lead and both paragraphs) now sits directly above
> the Evaluation Pipeline app, in one section with it. So §D3 (the app) and §D4 (the text) are
> one section, §D3 "How the program runs"; the `#pilot-sequence` anchor the home page links to
> moved with the text. The text is now centred. Its lead ("Reports and communication support
> are deliverables…", `PROGRAMS.SEQUENCE.lead`) is gone, also at your request; the rest of the
> wording is unchanged. The removed timeline and lead are in the snapshot
> `~/Desktop/Ascent Website archive/2026-10-20 before program timeline removed/`, and in git.
> **No remaining ID changed.**
>
> Worth a look: the last paragraph ends "until graduation", but nothing on the page says what
> graduation is any more — it was step 07 of the timeline. The app's text doesn't use the word.

> **What changed in v74.** The four phase detail sections on Evaluation Process (Evaluative
> Foundation; Data Architecture; Analytics & Inference; Monitoring, Learning & Reporting) are
> gone, at your request: the Evaluation Pipeline app above them now explains each phase. That
> removed §D5–§D8 (`PROGRAMS.PHASE1.*` to `PROGRAMS.PHASE4.*`) and their four illustrations
> (the "Phase N detail" lines of `ALT.programs`). The four overview cards lost their "Learn
> more" buttons (`PROGRAMS.CARDS.1`–`4`, the `Link:` line), which only scrolled down to those
> sections. The page now ends on "How the program runs". The removed copy is in the snapshot
> `~/Desktop/Ascent Website archive/2026-10-20 before phase details removed/`, and in git.
> **No remaining ID changed.**

> **What changed in v73.** The Evaluation Pipeline app (`evaluationguide.netlify.app`) is now
> embedded on Evaluation Process, at your request, straight after "Opening the black box" and
> its four cards, full width. At your request it has no border, and it is as tall as the app,
> so it blends into the page with no scrollbar of its own; the app's background is the
> site's. It is a new §D3 with one block, `PROGRAMS.PIPELINE.frame`: the name a screen reader
> gives the frame. The sections after it are renumbered D4–D8. **No ID changed.**

> **What changed in v72.** Your edit to the home page headline (`HOME.HERO.h1`): the full
> stop after "context" is now inside the orange accent, so it turns orange with the word. The
> wording is unchanged. **No ID changed.**

> **What changed in v71.** Your edits across the doc, applied to the site word for word.
> Home: the hero lead now opens "The Ascent Collaborative's goal is to champion and implement
> an integrated evaluation model…", the badge says "hands-on" rather than "embedded" support,
> and the "Evaluation that Goes Further" lead, two of the phase and tool descriptions, the
> "Why it matters" lead and the "in brief" body are tightened. About: the banner heading reads
> "Built for the benefit of organizations…", the opening paragraph drops its last sentence
> ("Ascent is structured to make that relationship affordable."), the two field definitions
> are reworded, and every timeline entry has lost its author citation in brackets. Evaluation
> Process: the lead, the Phase 2 and 3 card summaries, the "how it works" paragraphs (the
> "Deeper involvement in the technical work…" sentence is gone), the Intake and Embed steps,
> and four Phase 1–3 outputs. Get Involved: three role descriptions and the last pipeline
> step. Demo: the intro starts "Try the app…", the lead under "Six views of one program" was
> left empty, so it is gone from the page, and three view cards are rewritten. Download: "and
> project change" in the banner lead. I updated the Context notes that described the old
> wording (§B1 hero lead, §C timeline citations, §F3). **No ID changed.**
>
> Worth a look: the hero lead is now about 230 characters, past the ~180 it was sized for,
> so the hero runs longer. On the Demo page the Logic model card is now two sentences and
> about three times the length of its neighbours, so its row is taller than the others.

> **What changed in v70.** Two "Download the app" buttons to the Download page, at your
> request. On the home page, an outlined one sits beside "Try the demo" at the end of
> "Evaluation that Goes Further" (`HOME.METHODS.demo`, now with a second button). On the Demo
> page, an orange one closes the "Using the app" band, under the six view cards
> (`DEMO.VIEWS.download`, new). The label repeats the Download page's own heading. **No
> existing ID changed.**

> **What changed in v69.** The Download page's eyebrow reads "Version 0.0.3 · pre-release
> build" (`DOWNLOAD.CHOOSE.intro`, was 0.0.2), at your request, for the build you are
> publishing now. The three buttons' fallback links in the page's markup moved to the v0.0.3
> installers with it. **No ID changed.**
>
> Worth knowing: while the page can reach GitHub, the eyebrow and buttons show whatever the
> newest published release is. Until v0.0.3 is up with all three installers, visitors still
> see 0.0.2 and download it; once it is, they see 0.0.3 with no further edit. The 0.0.3
> written here shows only if GitHub can't be reached, and its links work once the release exists.

> **What changed in v68.** The Download page's buttons start a download again, and now always
> of the newest release. v67 sent all three to the app's releases list on GitHub, which was not
> what you meant. Each button now downloads its installer directly. As the page loads, it asks
> GitHub for the newest release that has all three installers, pre-releases included, and
> points each button at that release's file. The version number in the eyebrow follows the same
> lookup, so it reads 0.0.2 today and will read 0.0.3 when you publish that, with no edit here.
> I updated the Context notes in §L2 to say so. **No ID changed.**
>
> Worth knowing: if GitHub can't be reached (or a visitor has JavaScript off), the buttons fall
> back to the v0.0.2 files and the eyebrow to "0.0.2", as written in this document. GitHub
> allows each visitor 60 lookups an hour, far more than anyone will use. A release still
> uploading its installers is passed over until all three are up. "Pre-release build" in the
> eyebrow does not change by itself: edit it when a build is signed.

> **What changed in v67.** The Download page, at your request. The eyebrow over the
> installers reads "Version 0.0.2 · pre-release build" (`DOWNLOAD.CHOOSE.intro`, was 0.0.1),
> for the release you published today. The three buttons no longer name one file of one
> release: each now opens the app's releases list on GitHub, which puts the newest release
> first, pre-releases included, so they follow every new release without an edit. I updated
> the Context notes in §L2 to say so. **No ID changed.**
>
> Worth knowing, not changed: the buttons now open a GitHub page rather than starting a
> download, and all three open the same one, where the visitor finds their file under the
> newest release's Assets. Their labels still say "Download for Apple silicon" and so on
> (`DOWNLOAD.CHOOSE.cards`). The version in the eyebrow still has to change by hand with
> each release; dropping the number from it would make the page need no edit at all.

> **What changed in v66.** Your edit to the Download banner's line under the heading
> (`DOWNLOAD.HERO.lead`), applied word for word: "The desktop app that supports our evaluation
> process: build program logic models, aggregate evidence and map it to each link, monitor the
> effects of external policy developments, project change across all metrics." It runs to
> three lines on desktop, up from two, and I updated the Context and Fits notes to say so.
> **No ID changed.**
>
> Not changed: the Download page's search-engine description (`SEO.download`) still says "the
> desktop app for building and reading program logic models", the banner's first wording.
> Say if you want it to follow.

> **What changed in v65.** Your edits to the Download page (§L), applied word for word. The
> banner heading is "Download the app" (`DOWNLOAD.HERO.h1`, was "Download Ascent Mapper").
> Installers: the eyebrow reads "Version 0.0.1 · pre-release build" and the heading "Choose
> your operating system"; the lead under it is empty, so it is gone from the page
> (`DOWNLOAD.CHOOSE.intro`); the cards are headed "Apple silicon Macs", "Intel Macs" and
> "Windows", and the first says only "Requires macOS 12 Monterey or later."
> (`DOWNLOAD.CHOOSE.cards`). The "Not sure which Mac you have?" note and the "See every
> release on GitHub" link are deleted (`DOWNLOAD.CHOOSE.note`, `DOWNLOAD.CHOOSE.link`), and
> with them the whole "Opening it the first time" band: the first-launch heading, the Mac and
> Windows steps and the IT-team notice (`DOWNLOAD.OPEN.*`, four blocks). I removed those
> blocks and the empty §L3 heading, and updated the Context notes that described them. The
> page now ends after the three installer cards. **No ID changed or renumbered; six retired:
> `DOWNLOAD.CHOOSE.note`, `DOWNLOAD.CHOOSE.link`, `DOWNLOAD.OPEN.intro`, `.mac`, `.windows`,
> `.managed`.**
>
> Worth knowing, not changed: with the walkthrough gone, the page no longer says that the
> builds are unsigned, so a visitor meets the macOS and Windows warnings unprepared (the
> app's README on GitHub still explains them), and nothing says how to tell an Apple-silicon
> Mac from an Intel one. The name "Ascent Mapper" now appears only in the browser-tab title
> and description (`SEO.download`).

> **What changed in v64.** Your two edits to this document, applied to the site word for word.
> Evaluation Process: the first word of the heading over the four phase cards,
> "{{Opening}} the black box" (`PROGRAMS.CARDS.h2`), is now in the orange accent colour. That
> needed a new style rule, since only the home page's hero title coloured accent words; the rule
> covers any section heading, so `{{…}}` works in the others too. About: the closing entry of
> the evidence timeline, "Where the two fields meet" (`ABOUT.TIMELINE.synthesis`), now stops
> after "…explicitly and measurably." — the sentence about what Ascent is designed to do is
> gone. I updated the Context notes on both blocks, and the "Fits" line on the second, which
> still said two sentences. **No ID changed.**

> **What changed in v63.** A new page, §L: **Download** (`download.html`), at your request. It
> links to the installers for Ascent Mapper in the app's GitHub releases: one button each for
> Macs with Apple silicon, Macs with an Intel processor, and Windows. They are three links
> because a web page cannot reliably tell which kind of Mac someone has. Below the buttons is
> the first-launch walkthrough from the app's README, since the early builds are not yet
> signed and both systems warn before opening them. "Download" is the sixth item in the nav,
> after Demo, on every page (`GLOBAL.NAV.items`). **New IDs: `DOWNLOAD.*` and
> `SEO.download`; none renumbered.** The page is §L, after the unlisted editor demo, so that no
> existing page letter moved.
>
> All the wording is mine, taken from the app's README and the v0.0.1 release notes, so please
> change any of it. Two things to decide. The page calls the app **Ascent Mapper**, as its
> installer, README and release do, while the Demo and the editor demo still call it **Program
> Mapper**; I left those alone. And the version in `DOWNLOAD.CHOOSE.intro` ("Version 0.0.1"),
> with the three download links in the page's markup, are what change with each release.

> **What changed in v62.** Evaluation Process. At your request, the heading over the four phase
> cards, "Opening the black box", gained a subhead: "A platform built for program teams that
> gets to outcomes by driving clarity in practice." (`PROGRAMS.CARDS.lead`, new). It is centred
> under the heading in the page's grey lead style, and I updated the Context note on
> `PROGRAMS.CARDS.h2`, which said there was no lead. Applied word for word. **New ID:
> `PROGRAMS.CARDS.lead`; none renumbered.**

> **What changed in v61.** Evaluation Process. At your request, the four phase cards under the
> page banner now sit under a centred heading, "Opening the black box" (`PROGRAMS.CARDS.h2`,
> new), styled like the section headings on the home page. I also applied the edits you made
> to the phase output lists, which the doc had but the site did not, word for word. Phase 1:
> theory of change and evaluability assessment. Phase 2: instrument suite ("community
> members", was "community representatives"). Phase 3: both findings memos and the
> contribution and attribution analysis. Phase 4: all five entries. Your Phase 3 edit dropped
> "Required for every non-experimental evaluation", so I corrected the `Context:` note on
> `PROGRAMS.PHASE3.list`, which still pointed to it. One thing to decide: the Phase 4 learning
> agenda now says "out of MEL scope", and "MEL" is spelled out nowhere on the site (the phase
> is named "Monitoring, Learning & Reporting"). I left it as you wrote it. **New ID:
> `PROGRAMS.CARDS.h2`; none renumbered.**

> **What changed in v60.** At your request, the tagline under the name in the brand lockup
> (`GLOBAL.BRAND.tagline`) now reads "For Comprehensive Evaluation" (was "For Research &
> Evaluation"). It changes on every page, header and footer, and on the unlisted editor demo.
> It is three characters longer, but it still sits on one line on desktop and tablet at the
> same type size; on a phone it wraps to two lines, as before. It no longer matches the
> Program Description's cover, so I dropped that from the block's Context note. The README's
> find-and-replace table now names the new tagline too. **No ID changed.**

> **What changed in v59.** At your request, one paragraph moved from About to Home. "When
> evidence quality determines funding, capital consolidates toward whoever can afford to prove
> their outcomes…" no longer opens "The evidence base" on About. It is now the lead line under
> "The organizations that need it most can least afford it" on the home page (§B4), above the
> three statistics. Its wording is unchanged. It has a new ID, `HOME.STATS.lead`, because IDs
> name their page; the old one, `ABOUT.STORY.para1`, is retired, not reused. On About, the
> heading now stands beside a single paragraph (`ABOUT.STORY.para2`), and I updated the
> Context notes on both blocks. **No ID renumbered.**

> **What changed in v58.** A typo fixed at your request: step 06 of the program sequence on
> Evaluation Process (`PROGRAMS.SEQUENCE.steps`) now reads "Traces the underlying links…" (was
> "underlaying"). **No ID changed.**

> **What changed in v57.** Your edit from the editor, applied: on Evaluation Process, step 06 of
> the program sequence (`PROGRAMS.SEQUENCE.steps`, "Recursion and integration") now begins
> "Traces the underlaying links that turn inputs to outcomes:" and says "the next round of
> evaluation" (was "the next evaluation cycle"). Applied word for word. **No ID changed.**

> **What changed in v56.** About: the evidence timeline is redrawn to show the model as a
> synthesis of two fields. Implementation science and evaluation capacity building now run as
> two separate rails, teal and orange, each headed by its name and a one-line description
> (`ABOUT.TIMELINE.field_is`, `ABOUT.TIMELINE.field_ecb`). They meet only at the bottom, in a
> new closing entry, "Where the two fields meet" (`ABOUT.TIMELINE.synthesis`). Six new entries
> on the ECB rail come from Table 2 of the Evidence & Peer Context brief: Patton 1997,
> Stockdill, Baizerman & Compton 2002, Preskill & Boyle 2008, Labin et al. 2012, Cousins et al.
> 2014 and Buckley et al. 2015 (`ABOUT.TIMELINE.11`–`16`). Every entry gained a `Field:` line,
> which says which rail it sits on. The two Getting To Outcomes trials (`.1`, `.4`) are tagged
> "Cited by both fields" and drawn as one stop across both rails, because the brief counts them
> in both. The Innovation Network figure (`.3`) is tagged "The sector" and boxed, since it
> belongs to neither field. The §C3 blocks are re-ordered to match the page. The text above the
> timeline no longer sticks beside it; it sits above, heading on the left. No existing entry's
> wording changed. The new wording is mine — the field descriptions, the six entries, the tags
> and the closing entry — so please change any of it. **No ID renumbered.**

> **What changed in v55.** Your edits from the editor, applied to the site, with the three that
> had been waiting since v53. Home: the Stakeholder Mapping and Policy and Practice Context card
> descriptions; the "Why it matters" card is now for "nonprofit leaders, programs teams and
> evaluators", with three new points (Map and monitor efficacy, Build and document a
> knowledge-base, Track exogenous effects) and a longer "Hear from the people served"; the
> "in brief" heading ends "…into program teams", and its lead begins "An implementation support
> professional embeds…" with **full and recursive** in bold. About: the 2018–19 timeline entry
> "A profession emerges" (`ABOUT.TIMELINE.9`) is gone, so the timeline has eight entries.
> Evaluation Process: steps 04–08 of the program sequence; the Phase 1 body now ends "…the
> evaluation would lack clarity."; Phase 2 is one sentence and Phase 3 two (the heaviest-phase
> warning and both "an organization that enters here…" sentences are gone); Phase 4 is shorter.
> Our Model: the structure heading is "Finding affordability in better coordination.", plus the
> Partner Programs card, a comma in the orange notice, the impact-logic lead and the "Why
> recursion and integration exists" notice. Demo: the views lead loses its second sentence.
> Editor demo: the line under the heading (`EDITOR.HERO.lead`) is gone, so the banner is the
> heading alone. I also brought the Context notes on those blocks up to date where they
> described the old wording. **No ID renumbered.**
>
> Two typos fixed at your request: the Demo banner `DEMO.HERO.lead` now reads "…the demo
> depicts the data penetration of multiple rounds…" (was "depicts data the data penetration"),
> and the Partner Programs card says "Implementation staff listen… and shepherd" (was
> "shepherds").

> **What changed in v54.** The demo app's address is now `ascentmapper.netlify.app`. The Demo
> page and the unlisted editor demo (§K) frame it and link to it there, and the note under
> §F names it. **No copy changed and no ID changed** — the address is in the pages' markup,
> not in anything you edit here.

> **What changed in v53.** A new page, §K: an unlisted editor demo at `editor_demo.html`, the
> Demo page's app with editing switched on (`EDITOR.*`, `SEO.editor_demo`, `ALT.editor_demo`).
> Nothing on the site links to it, its tags keep it out of search results, and it is reached
> only by typing `/editor_demo` after the site's address — which is why it sits at the end,
> after the pages a visitor meets. It has the Demo page's header, footer and frame; the new
> wording is a heading, a line saying nothing is kept, and the link under the frame. I wrote
> all of it — please change it if you want other wording. The Demo page itself is unchanged
> and still shows the view-only app. **No existing ID changed.**
>
> Not touched: your two unapplied edits in this document — the Our Model heading
> `INVOLVED.STACK.intro` ("Finding affordability in better coordination.") and the Demo
> banner `DEMO.HERO.lead`, which now reads "…depicts data the data penetration of multiple
> rounds…" and looks like it was left mid-edit. Say the word and I'll apply them.

> **What changed in v52.** Our Model: the whole "Model benefits" section ("What the structure
> produces" — `INVOLVED.BENEFITS.*`, the six cards) is gone, so the page runs structure,
> impact logic, closing band; the closing band is now §E3. Also applied, from edits you had
> already made to this document and not yet sent to the site: the footer blurb on every page
> now says "The Ascent Collaborative is dedicated…" (was "Ascent Research Collaborative",
> which settles the two-names note on `GLOBAL.FOOTER.blurb`); on Evaluation Process the
> "What Phase N produces" subheads read "Phase N outputs", the Phase 1 lead loses its last
> sentence, the Phase 2 question ends "…how do we ensure its quality?", the program
> description bullet reads "…for whom, and at what scale…", the indicator dashboard bullet
> ends after "Phase 2", and the graduation step no longer mentions the network and literature
> briefs. **No ID renumbered.**

> **What changed in v51.** Evaluation Process: the "How we measure it" button under the program
> sequence is gone (`PROGRAMS.SEQUENCE.buttons` removed; nothing on the site links to the
> impact logic section on Our Model from there any more). Your edits applied: the banner lead
> now ends "…the ethics of the work and its success.", and the About timeline entry
> `ABOUT.TIMELINE.4` is headed "Repetition and duration drive results" (was "Year two is where
> it lands"). **No ID renumbered.**

> **What changed in v50.** The "Why it matters" section on the home page ends with a button,
> "See the evaluation process", linking to Evaluation Process (`HOME.WHY.button`, new). You did
> not give the label, so it is mine — please change it if you want other wording. **No
> existing ID changed.**

> **What changed in v49.** All six cards in "Evaluation that Goes Further" now expand on click
> into a short description, and none of them links anywhere. The three phase cards (Logic
> Models & Metric Integration, Data Architecture, Analytics & Forward Planning,
> `HOME.METHODS.phases`) used to link to their sections on Evaluation Process; they gained
> `Description` lines like the tool-view cards got in v48. I wrote all six descriptions from the
> screenshots — please correct them. **No ID changed.**

> **What changed in v48.** The three tool-view cards on the home page (`HOME.METHODS.tools`)
> no longer link to the Demo page. Each now expands on click into a short description of that
> view (new `Description` lines, which I wrote from the screenshots — please correct them),
> and closes on a second click. **No ID changed.**

> **What changed in v47.** The home page's phase cards (`HOME.METHODS.phases`): the first is
> now "Logic Models & Metric Integration" (was "Evaluative Foundation"), the third "Analytics &
> Forward Planning" (was "Analytics & Inference"), and the "Monitoring, Learning & Reporting"
> card is gone, so the section has three phase cards and three tool-view cards, in two rows of
> three. The Evaluation Process page keeps the original phase names. `ALT.home_phases` loses its
> fourth line. **No ID changed.**

> **What changed in v46.** Three more cards under the home page's phase cards:
> **Stakeholder Mapping**, **Policy and Practice Context** and **Evidence & Theories of
> Change**, each a screenshot of that view of the Program Mapper (`HOME.METHODS.tools`, alt
> text in `ALT.home_tools`), linking to the Demo page. Also applied: your edit to the lead
> under "Why it matters" — "Evaluation should not be a static exercise." (was "compliance").
> **No existing ID changed.**

> **What changed in v45.** Your edits, applied to the site. Our Model: the orange notice under the
> structure cards loses its bold lead-in ("Why the implementation layer is the innovation.") and
> is reworded ("…the holistic appraisal of the organization's and community's needs…", "…with
> attention to its resources and practice context."); the "Why recursion and integration
> exists" notice now says it uses qualitative analysis to trace each evaluation and program
> input through to downstream outcomes, and that results change how "our work is delivered".
> The page's browser-tab and search title (`SEO.involved`) is just "Our Model". **No ID
> changed.**

> **What changed in v44.** Your edits, applied to the site. Home: the demo tagline reads "A
> single app shows the power of our evaluation model." (with its full stop). Our Model: the
> four structure cards lost their bold role lines ("Engaged on retainer or contract" and the
> rest), the fourth card is "Partner Programs" (was "Clients"), "What the structure produces"
> has no heading under its "Model benefits" eyebrow, and the orange notice below the six cards
> (`INVOLVED.BENEFITS.note`, "Ascent aims to be a development partner…") is gone. The empty
> `Commitment:` and `Heading:` fields stay in this document as you left them. **No ID
> renumbered.**

> **What changed in v43.** Your edits, applied to the site. Home: the "Evaluation that Goes
> Further" lead is now "Static evaluations describe a snapshot of a program. Ascent's
> recursive process maps the links from program inputs to final outcomes…", and the four
> phase lines in the "in brief" band are the longer versions you wrote. Evaluation Process:
> the "Phase 4 is the last phase, not the end" paragraph (`PROGRAMS.PHASE4.gate`) is gone.
> Our Model: the lead under "What the structure produces" and the line under "See the model
> in action." are gone. **No ID renumbered.**

> **What changed in v42.** Your edits to the home page, applied to the site. The hero lead is
> now "Ascent is an evaluation practice designed to lower the cost, improve the quality, and
> broaden the impact of evaluative services for mission-oriented organizations." The heading
> of "Evaluation that Goes Further" is "An evaluation process accountable to program
> outcomes", and the "Ascent Evaluation, in brief" band is headed "Evaluation and capacity
> building that integrates into your program", with a new lead and a new body ("The process is
> the program…"). The body no longer mentions the $500,000 ceiling or the 1.5% fee; the hero
> badge still shows the 1.5%.
>
> Applied as written, but worth a look: the band's heading says "your program", which the
> third-person copy (v23) otherwise avoids, and its lead reads "embed within programs teams
> and carries the them through" — probably "embed within program teams and carry them
> through". **No ID changed.**

> **What changed in v41.** "Evaluation that Goes Further" now ends with a tagline, "A single
> app shows what makes our evaluation process unique", and a "Try the demo" button to the Demo
> page (`HOME.METHODS.demo`, new). **No existing ID changed.**

> **What changed in v40.** Your edits, applied to the site. Home: the two paragraphs under the
> phase cards (`HOME.METHODS.body`) and the "The research behind it" link
> (`HOME.METHODS.link`) are gone, so "Evaluation that Goes Further" ends on the four cards.
> That link had been repointed to the About timeline in v38; with it gone nothing links to
> `about.html#timeline` any more, though the anchor stays. About: the banner heading reads
> "Built for organizations priced out of comprehensive evaluation" (was "effective").
> **No ID renumbered.**
>
> Left alone: the About search description (`SEO.about`) still says "effective evaluation".

> **What changed in v39.** Your edits and your note, applied to the site. About: the banner
> heading drops "the" ("Built for organizations priced out of effective evaluation") and gets
> the subhead you asked for, "And designed to translate evaluation to outcomes." — the block
> `ABOUT.HERO.lead`, which had been removed in v12 and now returns under the same ID. Our
> Model: the banner line under "The Model" is "Everything special about the Ascent model, and
> how it can deliver real change in the mission-oriented sector.", and the four Impact logic
> cards lost their bold "Measured" lines; card 4's description now reads "Traces the
> processes that translate metrics to outcomes and builds cross-cutting improvement strategies
> that feed into the next cycle." **No ID renumbered.**
>
> Left alone: the About search description (`SEO.about`) and the Our Model shortcut on the
> 404 page (`NOTFOUND.cards`) still use the older wording of the two banners above.

> **What changed in v38.** Your deletions on Our Model, applied to the site. Gone: the
> three-interventions table in Impact logic (`INVOLVED.IMPACT.table`); the whole Evidence
> section (`INVOLVED.EVIDENCE.*` — heading and lead, the four cited studies, the synthesis
> paragraph); and the whole "Who does this work" section (`INVOLVED.NETWORK.*` — the four
> roles, the plain definitions and the pull quote). The closing band's heading is "See the
> model in action." Headings renumbered: What the structure produces is §E3 and the closing
> band §E4. **Also changed, for you to confirm:** the home page's "The research behind it"
> link pointed at the Evidence section that no longer exists, so it now goes to the
> timeline on About (`about.html#timeline`). "What the structure produces" also moved from
> a grey to a plain background so it does not sit flush against the grey Impact logic band
> above it. **No ID renumbered.**

> **What changed in v37.** Your three deletions on Our Model, applied to the site. The
> structure section's lead (the "two lines that turn out to be connected" paragraph), its
> body paragraph (`INVOLVED.STACK.body`, "Solving the second relieves the first…") and the
> subhead above the four cards (`INVOLVED.STACK.subhead`, "How the work is staffed") are
> gone, so the heading now leads straight into the four cards. The line
> about efficiency buying time rather than margin went with the body. **No other ID
> changed.**

> **What changed in v36.** The 2005 entry ("Implementation becomes a field of study",
> `ABOUT.TIMELINE.6`) is off the About timeline, which now has nine entries. The remaining
> IDs keep their numbers. **No other ID changed.**

> **What changed in v35.** Em dashes no longer have spaces around them anywhere in the site
> copy (33 places on the pages, 29 lines in this document). Also applied: your three
> headline edits on the About timeline ("Implementation support becomes a field of research",
> "A profession emerges", "Competencies, described"). In the 404 page's two shortcut-card
> notes the dash is a separator between a card's title and its text, not part of the copy,
> so those keep their spaces. **No ID changed.**

> **What changed in v34.** The About timeline now covers how implementation science developed
> and how implementation support became a profession: five new entries
> (`ABOUT.TIMELINE.6`–`10`) — 2005 a synthesis of the implementation research literature,
> 2009 the Consolidated Framework for Implementation Research, 2017 the NIRN / Centre for
> Effective Services project on the role of implementation support, 2018–19 the validation
> survey and systematic review, and 2020 the Implementation Support Practitioner Profile and
> Practice Guide, with both PDFs linked. They sit in date order among the five existing
> entries, which are unchanged. The 2005 entry comes from general knowledge, not from the
> two PDFs. Also applied: your edit to the Evaluation Process banner lead
> (`PROGRAMS.HERO.lead`), now "…Our process is recursive, building upon past findings and
> expanding a model's explanatory leverage." **No existing ID changed.**

> **What changed in v33.** Your two edits to the affordability figures, applied to the site.
> Both numbers now describe organizations that *lack* dedicated evaluation staff: the home
> stat label reads "Organizations above $5M lacking the same" (98% of small nonprofits, 80%
> of those above $5M), and the About timeline entry says 98% of small nonprofits and 80% of
> organizations with budgets above five million dollars have no dedicated staff. This
> reverses v32, which had read the 80% as organizations that *have* staff. **No ID
> changed.**

> **What changed in v32.** The About timeline entry on affordability (`ABOUT.TIMELINE.3`) now
> uses the same figures as the home stats: 98% of small nonprofits have no dedicated
> evaluation staff, while 80% of organizations above $5M do. It said 2% and 20% before,
> which disagreed with v31's home stats (that "worth a look" note is resolved and removed
> from v31). The home stats were already as you specified. **No ID changed.**

> **What changed in v31.** Your edits to the doc, applied to the site. Home: the "Why it
> matters" heading is now "Catalyze a continual improvement process" with a new lead;
> its first card is "For nonprofit leaders and programs teams"; the stats read 98% of small
> nonprofits *without* dedicated evaluation staff and 80% of organizations above $5M with
> them; the brief is headed "Ascent Evaluation, in brief" / "An evaluation process
> accountable to program outcomes", loses "in New York City" and the consulting sentence, and
> now says "full and recursive evaluations". About: the story heading is "An
> outcomes-oriented synthesis." and its first paragraph starts at "When evidence quality…".
> Demo: the banner sentence gains a second one about the app. Em dashes lost their spaces
> throughout. **No ID changed.**


> **What changed in v30.** The home page's phase cards (`HOME.METHODS.phases`) are 1.5x larger
> — two across instead of four — so the screenshots are legible. **No ID or wording changed.**

> **What changed in v29.** The phase screenshots left the home hero and now live in the
> "Evaluation that Goes Further" section, between its lead and body: larger, with each
> phase's name underneath and no overlaid "Phase 0N" tag (`HOME.METHODS.phases`; the block was
> `HOME.HERO.phases` in v27–28, and its tags are gone). The section's eyebrow is now
> "Evaluation that Goes Further" (was "How evaluation goes further"), and §B2 is renamed to
> match. The page's stylesheet and script version strings were also bumped, so browsers that
> cached the old CSS (Safari especially) fetch the new one. **No other ID changed.**

> **What changed in v28.** The home hero thumbnails (`HOME.HERO.phases`) are much smaller and
> pared down to a screenshot with its phase tag, like the Evaluation Process cards without
> their captions or "Learn more" buttons. The four phase names that labelled them are gone
> from the block. **No ID changed.**

> **What changed in v27.** The home hero gained a row of four small thumbnails of the
> Evaluation Process phase screenshots (`HOME.HERO.phases`, alt text `ALT.home_phases`),
> placed under the headline and illustration rather than inside the hero image. Each links to
> its phase section. **No existing ID changed.**

> **What changed in v26.** Programs & Services is now **Evaluation Process**. The page
> heading (`PROGRAMS.HERO.h1`, which this document had as "The Process" while the site said
> "Programs & Services" — now both say the new name), the nav label on every page, the
> breadcrumb, the 404 shortcut card, and the search title (`SEO.programs`) all follow. The
> file is still `programs.html` and no ID changed. Older entries below keep the old name.

> **What changed in v25.** The four footer social icons are gone from every page
> (`ALT.social`, the Instagram / LinkedIn / Facebook / YouTube names a screen reader read
> out, came out with them). None linked anywhere. The footer is now the brand lockup and
> blurb over the copyright line. **No other ID changed.**

> **What changed in v24.** The footer lost its last link and its two legal links, and
> shrank. Removed: "Collaborate with us" (`GLOBAL.FOOTER.col2`) and "A.I. statement" /
> "Annual report" (`GLOBAL.FOOTER.legal_links`, both of which went nowhere). With the link
> column gone, §A4 (link columns) went too and the legal line is now §A4. The footer is a
> single row — brand, blurb and social icons — over a thin copyright line, with tighter
> padding throughout. **No other ID changed.**

> **What changed in v23.** The copy no longer addresses the reader. Every "you", "your" and
> "yourselves" in the site text now speaks about the organization, the program team or the
> community in the third person ("Counting tells an organization how many people it served";
> "The implementation support professional joins the program team"). Touched: Home, Programs &
> Services, Get Involved, the 404 page and the Demo search description. Two sentences were
> restructured rather than swapped: the "If you enter here with…" entry points in Phases 2 and 3
> now read "An organization that enters here with…", and the Get Involved CTA headline is "The
> model only matters if organizations can buy it." Older entries below still quote the earlier
> wording. **No ID changed.**

> **What changed in v22.** Three blocks marked `[DELETE]` are gone. On About, the whole
> Mission / Method card pair (`ABOUT.MVV.mission`, `ABOUT.MVV.vision`) came off, so §C2 went
> with it and the remaining About sections are renumbered C2 and C3. The closing "We are
> deliberate about what this site does not claim" paragraph (`ABOUT.STORY.para3`) also came
> off, leaving the story as two paragraphs. **No other ID changed.** Left alone, worth a
> look: the search title `SEO.about` still says "the mission and the evidence".

> **What changed in v21.** `SEO.demo` only. The name takes "the" after all — *Demo — try the
> Program Mapper* — and the description is yours: "map every facet of your program, measure
> outcomes and test the effects of different changes." That reverses the wording decision
> noted in v20. The frame's screen-reader name (`ALT.demo`) and the page heading are
> unchanged, so both still read "Program Mapper" with no article. At 116 characters the
> description is a little under the 120 Google likes to show; it will display in full either
> way, with a few characters of the snippet unused.

> **What changed in v20.** The tool is called **Program Mapper** everywhere now, settling
> the first open question from v19. The page title and search description (`SEO.demo`) and
> the name a screen reader gives the frame (`ALT.demo`) were the last places still saying
> "Logic Model Mapper"; the title now reads *Demo — try Program Mapper*, and both
> descriptions drop "the" before the name, which the old name needed and this one doesn't.
> The em dash in the stakeholder-map card stays exactly as you left it. **No ID changed.**

> **What changed in v19.** Your edits to the Demo page, applied to the site. The tool is
> called **Program Mapper** in the page heading (`DEMO.HERO.h1`); the hero lead is now its
> first sentence alone; the small print under the frame is shorter and no longer names the
> fictional program; the band below is headed "Using the app" rather than "Inside the tool".
> `DEMO.VIEWS.link` — the "Where it fits in the pipeline" arrow link under the six cards —
> was marked `[DELETE]` and is gone from the page and from this document. **No other ID
> changed.**
>
> Two things left alone, both worth a decision: the page title, the search description and
> the frame's screen-reader name still say *Logic Model Mapper* (`SEO.demo`, `ALT.demo`), so
> the tool now has two names on one page; and the first em dash in the stakeholder-map card
> lost the spaces around it while the second kept them.

> **What changed in v18.** The four buttons at the foot of the phase sections on Programs &
> Services are gone: "What Phase 2 / 3 / 4 adds" and Phase 4's "Back to Phase 1".
> `PROGRAMS.PHASE1.buttons` through `PROGRAMS.PHASE4.buttons` were removed. The cycle idea
> still lives in the Phase 4 paragraph. **No other ID changed.**

> **What changed in v17.** The site is dark-only. The sun/moon theme button is gone from the
> header on every page, so `SYSTEM.ui` loses its "Theme button" line. **No ID changed.**

> **What changed in v16.** A new page, **Demo** (`demo.html`), with a working copy of the
> Logic Model Mapper embedded in it — the tool whose screenshots are on the four phase
> cards on Programs & Services. It is the new §F; the pages after it moved down one letter
> (404 is now §G, System text §H, Search-engine text §I, Image descriptions §J).
>
> - `GLOBAL.NAV.items` — "Demo" is the fifth nav item, after Our Model, on every page.
> - New blocks: `DEMO.HERO.*`, `DEMO.EMBED.*` and `DEMO.VIEWS.*` on the page itself, plus
>   `SEO.demo` and `ALT.demo` (the name a screen reader gives the embedded app).
> - The app inside the frame is **not** covered by this document. It is hosted separately,
>   so its own wording changes there, not here.
>
> **No existing ID changed.** Everything on the new page is a first draft — edit it like
> any other block.

> **What changed in v15.** Programs & Services now ends with Phase 4. Two sections came off
> the bottom of the page:
>
> - **"How engagements are structured"** (old §D8, eyebrow "Scoping",
>   `PROGRAMS.STRUCTURES.*`): the four-row structures table (full-pipeline, phase-entry,
>   phase-only, hybrid integration), its Integration Memo caption, and the orange "Not
>   sure which phase you need?" box.
> - **The closing card** (old §D9, `PROGRAMS.CTA`): "Rigor costs money. Rigor you can act
>   on costs patience." with its "See how the model works" button.
>
> **No other ID changed.** The intake assessment is still the first step of "How the
> program runs" (`PROGRAMS.SEQUENCE.steps`).

> **What changed in v14.** The "Who we work with / Two ways in" section is gone from
> Programs & Services (old §D3, `PROGRAMS.WAYSIN.*` — the evaluation consulting and "Our
> program" panels). "How the program runs" is now §D3; the later sections keep their
> numbers. **No other ID changed.** Three things followed from it:
>
> - Both "Our program" buttons on the home page (`HOME.HERO.buttons`, `HOME.BRIEF.links`)
>   linked to that section's `#flagship` anchor. They now go to "How the program runs".
> - The 404 shortcut card (`NOTFOUND.cards`) no longer promises "the two ways in".
> - The phase cards above it moved to a grey background, so the page still alternates grey
>   and plain sections now that the grey "Two ways in" band is gone.
>
> The 1.5% fee and the $500,000 ceiling no longer appear on Programs & Services — only on
> the home page (`HOME.HERO.badge`, `HOME.BRIEF.body`). The consulting option is now
> mentioned only in the last sentence of `HOME.BRIEF.body`.

> **What changed in v13.** The four phase cards at the top of Programs & Services now show
> your screenshots instead of placeholder illustrations, in the order you sent them:
> Phase 1 the logic model, Phase 2 the data-lineage view, Phase 3 the single-indicator
> analysis, Phase 4 the scenario dashboard. Their alt text (`ALT.programs`, cards 1–4) now
> describes each screenshot. The illustrations beside the four phase *detail* sections
> further down are unchanged. **No ID changed.**

> **What changed in v12.** The About page banner. The heading (`ABOUT.HERO.h1`) is now
> "Built for the organizations priced out of effective evaluation" (was "Built for the
> organizations evaluation was priced away from"), and the subhead under it
> (`ABOUT.HERO.lead`) is gone. The page's search description (`SEO.about`) repeated the old
> heading's wording, so it now uses the new one. **No other ID changed.**

> **What changed in v11.** The last quality assurance mentions are gone, and so is the
> About page's Governance section.
>
> - **Home:** the line under the hero button, "Every engagement runs under a published
>   quality assurance plan" (`HOME.HERO.trust_note`), with its tick icon.
> - **Programs & Services:** the "Quality gate" paragraphs at the end of Phases 1, 2 and 3
>   (`PROGRAMS.PHASE1.gate`, `.PHASE2.gate`, `.PHASE3.gate`). Phase 4's slot was never a
>   gate — it is the "last phase, not the end" cycle note — and stays.
> - **Our Model:** the project lead is no longer "personally accountable for compliance
>   with the quality assurance plan"; the line now reads "Signs off on every phase
>   deliverable before it is released" (`INVOLVED.NETWORK.commit_list`).
> - **About:** the whole Governance section (old §C5, `ABOUT.BOARD.*` — the board
>   paragraph and the list of board and committees). The page now ends on "Why this
>   exists", and its title drops "the governance" (`SEO.about`).
>
> **No other ID changed.** Phase 2 still produces a *data quality plan* for the client, and
> describes itself as "assuring the quality of evidence" — that is a deliverable of the
> service, not Ascent's own quality assurance, so it stays.

> **What changed in v10.** The About page no longer covers quality assurance — the site
> describes a hypothetical service set, and doesn't need to go that deep.
>
> - **Removed:** the Commitments card (`ABOUT.MVV.values`); the whole standards band (old
>   §C5, `ABOUT.STANDARDS.*` — the four threshold statistics and the "Download the quality
>   assurance plan" button); the whole four-domains section (old §C6, `ABOUT.DOMAINS.*` —
>   analytical rigor, data quality, constituent privacy, social justice, the five-tier
>   evidence-strength table and the template note under it); the enforcement paragraph in
>   `ABOUT.BOARD.body`; the violations note (`ABOUT.BOARD.contact_note`); and the quality and
>   ethics committee from `ABOUT.BOARD.members`.
> - **Trimmed:** `ABOUT.HERO.lead` loses "This page is what we are, what we will not do,
>   and who enforces it"; `ABOUT.STORY.para3` now says it describes "the model" rather than
>   "the model and the standards".
> - **Reworded because their subject went:** the Governance heading (`ABOUT.BOARD.h2`) is
>   now "How Ascent is governed" (was "Who enforces this"), and both lines of `SEO.about`.
> - **Off another page because its target went:** "Read our standards" on Our Model
>   (`INVOLVED.NETWORK.buttons`) linked to the standards band.
> - Governance (now §C5) moved from a grey to a plain background so it doesn't sit flush
>   against the grey "Why this exists" band.
>
> **No other ID changed.** Quality assurance is still mentioned elsewhere: the home hero's
> "Every engagement runs under a published quality assurance plan"
> (`HOME.HERO.trust_note`), the four "Quality gate" paragraphs on Programs & Services, and
> the project lead's "compliance with the quality assurance plan" on Our Model.
>
> **Logo, corrected.** `assets/Logo.png` is now the fully opaque version; the 42% opacity
> in v9's file was a mistake. The favicon matches it.

> **What changed in v9.** Every way of contacting Ascent is off the site, and there is a
> new logo.
>
> - **The Contact page (`contact.html`) is gone**, and with it all of the old `# F. Contact`
>   and every `CONTACT.*` block: the intake form, the email addresses and phone number, the
>   filler street address, the service-area map, the four inquiry cards, the quick-answers
>   FAQ and the participant data-withdrawal notice. The pages after it moved up one
>   letter — 404 is now §F, System text §G, Search-engine text §H, Image descriptions §I.
> - `GLOBAL.NAV.items` — "Contact" is out of the nav on every page.
> - `GLOBAL.FOOTER.col2` — "Contact us" is out of the footer. "Collaborate with us" stays:
>   it links to Our Model, not to a way of getting in touch.
> - Home: the hero's "Contact us" button (`HOME.HERO.buttons`) and the whole closing band
>   (`HOME.CTA.*`, old §B6 — "Tell us what you're trying to understand" / "Get in touch").
> - About: the closing band (`ABOUT.CTA`, old §C8 — "Want the full picture?" / "Ask a
>   question"), and the committee@example.org address at the end of
>   `ABOUT.BOARD.contact_note`.
> - Programs & Services: the "Start a conversation" / "Ask about the program" buttons on
>   both "ways in" cards, the program sequence and all four phases; the phone number and
>   "send a message" in `PROGRAMS.STRUCTURES.note`; and the body and contact button of
>   `PROGRAMS.CTA`.
> - Our Model: "Work with us as a specialist" (`INVOLVED.NETWORK.buttons`) and the "tell us
>   what you are trying to understand" half of `INVOLVED.CTA`, with its button.
> - 404: "Tell us what broke".
> - System text: the form confirmations (`SYSTEM.forms.confirmations`) — there are no forms
>   left — plus `SEO.contact` and `ALT.contact`. The email, phone and street address also
>   came out of the structured data in the head of `index.html`.
>
> **No other ID changed.** Wording that *describes* the program rather than inviting contact
> stays: the implementation support professional as "your continuous point of contact",
> and the scoping conversation that opens the program sequence.
>
> **New logo.** `assets/Logo.png` is now the mark in the header and footer of every page
> and in the structured data. The favicon was redrawn to match it. The old mark,
> `assets/Logo_simple.png`, is still in the folder but nothing uses it.
>
> A full copy of the site as it stood before this change is in
> `~/Desktop/Ascent Website archive/2026-10-01 before contact removed/`.

> **What changed in v8.** Two changes to the home page.
>
> - **"How evaluation goes further" (§B2) is much shorter and in plain prose.** The six
>   method cards (`HOME.METHODS.card1`–`card6`) are gone. Their ideas are now one sentence
>   in the lead, followed by two paragraphs (`HOME.METHODS.body`, new) on how Ascent
>   combines evaluation capacity building with implementation science, drawn from the
>   Evidence & Peer Context section of the Pitch Doc. A new arrow link
>   (`HOME.METHODS.link`) goes to the cited studies on Our Model. The heading is now
>   "Evaluation that becomes part of how an organization works". About 900 characters, down from about
>   3,000.
> - **The hypothetical example is gone** — old §B3, all four `HOME.EXAMPLE.*` blocks: the
>   82% / 64% / 18-point chart, the four tool cards and the "What it adds up to" box.
>   The home sections after it moved up one number (Why it matters is now §B3, and so on
>   to the closing call to action at §B6). **No other ID changed.**
>
> The section's background is now plain rather than grey, so it doesn't run straight into
> the grey "Why it matters" band now that the example no longer sits between them.

> **What changed in v7.** The "For funders" card is gone from the home page's "Why it
> matters" section (`HOME.WHY.funders` — four benefits: what a grant caused, comparing
> grantees fairly, funding learning, trusting a finding). The "For nonprofit leaders" card
> now stands alone, in a narrower column so its lines don't run the full page width.
> **No other ID changed.** The section lead still mentions "the people paying for" programs;
> it was left as it was and flagged in §B3 (formerly §B4).

> **What changed in v6.** Donations are off the site, for now. Nothing on any page asks
> for money, links to a way to give, or describes Ascent's own fundraising:
>
> - **The Fund page (`donate.html`) is gone**, and with it all of the old `# F. Fund` and
>   every `DONATE.*` block. The pages after it moved up one letter — Contact is now §F,
>   404 §G, System text §H, Search-engine text §I, Image descriptions §J. **No ID changed.**
> - `GLOBAL.NAV.cta` — the orange "Donate" button at the end of the nav, removed from every
>   page.
> - `GLOBAL.FOOTER.col2` — the "Donate" footer link.
> - `HOME.CTA.buttons` — the "For funders" button, which went to the funder case on the
>   Fund page.
> - About §C8 *Allocations* (`ABOUT.FINANCE.*`) — the whole "Where the money goes" section.
>   Both of its tables were about fundraising and individual giving, and with those rows
>   gone the remaining percentages would no longer add up, so the section went rather than
>   leaving a set of numbers nobody chose. The closing call to action is now §C8.
> - `ABOUT.CTA` — the "Fund the model" button. "Ask a question" is now the orange one.
> - `CONTACT.LOCATIONS.inquiries` — the funders card no longer points to the Fund page.
> - `CONTACT.FAQ.4` — "subsidized by charitable contributions" is gone from the fee answer.
> - `NOTFOUND.cards` — the Fund shortcut card.
> - System text — the donate button label, the impact sentence, the donation-form
>   confirmation and the donate widget's screen-reader labels (`SYSTEM.donate.*`), all of
>   which lived in `js/main.js` and came out of it.
> - `SEO.donate`.
>
> Funders are still on the site **as an audience for evaluation** — "For funders" on the
> home page, the funders-and-partners contact card, funder reporting in the pipeline —
> because that is about what Ascent does for them, not about money given to Ascent.
> "Directly subsidized engagement" in `PROGRAMS.WAYSIN.panel2` also stays: it is the
> Program Description's own wording for how the program is priced.
>
> A full copy of the site as it stood before this change, Fund page included, is in
> `~/Desktop/Ascent Website archive/2026-10-01 before donations removed/`.

> **What changed in v5.** The site no longer states a legal or tax status. Every mention of
> 501(c)(3), registered status, tax-deductibility or tax filings is gone, so the site
> describes the program and nothing about the entity behind it:
>
> - `GLOBAL.FOOTER.blurb` — "is a registered 501(c)(3) nonprofit dedicated to…" is now
>   "is dedicated to…", on all seven pages.
> - `GLOBAL.FOOTER.copyright` — the status sentence after the name came off.
> - `HOME.HERO.trust_note` — the registered-status clause came off; the quality assurance
>   plan stands alone.
> - `DONATE.FORM.tax_note` — removed. It was the line under the donate button asserting
>   registered status and deductibility.
> - `DONATE.FAQ.1` ("Is my donation tax-deductible?") — removed. The FAQ is four questions;
>   `DONATE.FAQ.2` is now the one open by default. **No other ID changed.**
> - `DONATE.FORM.details` — the email hint says "receipt", not "tax receipt".
> - `DONATE.OTHER.cards` — the stock and donor-advised-fund card no longer claims those gifts
>   are more tax-efficient; it says they are accepted.
> - `ABOUT.FINANCE.lead` — "audited statements and a Form 990" is now "audited statements".
>
> This supersedes the v3 decision that every page assert registered status, and the
> outstanding EIN question below is moot while the site makes no status claim. The word
> "nonprofit" still appears where it describes the model or the sector (for example
> `ABOUT.HERO.lead`, `HOME.BRIEF.lead`, `DONATE.CASE.intro`) — it is a description rather than a
> specific legal designation, and it was left alone.

> **What changed in v4.** The newsletter is gone. There was never anything to send, and
> a signup that collects addresses for a mailing that does not exist is a promise the
> organisation cannot keep on day one — so the footer form came off all seven pages
> along with everything that pointed at it:
>
> - `## A4. Footer — newsletter signup` and its four blocks
>   (`GLOBAL.FOOTER.newsletter.label`, `.placeholder`, `.button`, `.confirmation`).
>   The remaining footer sections renumbered A5→A4 and A6→A5; **no ID changed.**
> - The newsletter line in `SYSTEM.forms.confirmations` — no form left to confirm.
> - The third tickbox on the donate form ("Send me the monthly note on what the model is
>   learning"), in `DONATE.FORM.checkboxes`. It was the same offer in another place, so it
>   went with the rest; say the word if you want a donor-only update kept as an intention.
>
> The footer's brand column is now blurb and social icons under the lockup. It is shorter
> than it was, which suits a two-column footer better than the form did.
>
> **What changed in v3.** Two things happened in one pass. First, your edits to v2 were
> applied: the brand name, the tagline, the nav labels, the footer (two columns and two
> legal links deleted), the newsletter strings, and the whole home-page hero.
>
> Second, everything you had *not* edited was replaced from the **Website Copy Deck
> v1.0**, so the site now describes the organisation that document describes: a nonprofit
> **program evaluation practice** in New York City, serving small and mid-sized
> organisations that funders have started asking outcome evidence from. The previous
> placeholder subject — an economic-mobility research collaborative — is gone entirely.
>
> The deck's deliberate constraint is now the site's constraint: **no claim anywhere about
> track record, client count, staff size, years in operation, or a past result.** That
> removed every invented statistic, every invented person, the seven-year origin story,
> the funder logo wall, and the two testimonials. What replaced them describes the model,
> the standards and the published evidence base — all true on day one.
>
> Page mapping, following your nav edit:
>
> | File | Was | Now | Deck source |
> | --- | --- | --- | --- |
> | `index.html` | Home | Home | Page 1 |
> | `about.html` | About | About | Page 4 (standards) + 5.6 (governance) |
> | `programs.html` | Research | Programs & Services | Page 3 + 1.5 |
> | `get-involved.html` | Collaborate | Our Model | Page 2 |
> | `donate.html` | Fund | Fund | Page 5 |
> | `contact.html` | Contact | Contact | Page 6 |
>
> ID stems renamed to match the new content, on the same precedent as v2:
> `PROGRAMS.FIELD.*` → `PROGRAMS.PHASE1.*`, `PROGRAMS.COMMONS.*` → `PROGRAMS.PHASE2.*`,
> `PROGRAMS.PRACTICE.*` → `PROGRAMS.PHASE3.*`, plus a new `PROGRAMS.PHASE4.*` and
> `PROGRAMS.WAYSIN.*`. `PROGRAMS.ELIGIBILITY.*` → `PROGRAMS.STRUCTURES.*`.
> On the Our Model page, `INVOLVED.ROLES.*` → `INVOLVED.STACK.*`,
> `INVOLVED.PARTNER.*` → `INVOLVED.NETWORK.*`, and `INVOLVED.ADVOCATE.*` →
> `INVOLVED.BENEFITS.*`. On About, `ABOUT.IMPACT.*` → `ABOUT.STANDARDS.*` and
> `ABOUT.TEAM.*` → `ABOUT.DOMAINS.*`.
>
> **Blocks removed** (their content had no honest equivalent pre-launch): the home-page
> testimonials, the funder logo wall's named funders, `INVOLVED.EVENTS.*` (four invented
> events), `INVOLVED.FORM.*` (a second enquiry form — the richer intake form from the deck
> now lives on Contact, which is where the deck puts it), `ABOUT.TIMELINE` as an org
> history, and `ABOUT.BOARD.members` as named people.
>
> **Four decisions you settled on 4 September**, now applied throughout:
>
> - **Nonprofit status is not pending.** The hero no longer says it is. Every page now
>   makes the same claim: Ascent is a registered 501(c)(3). See `HOME.HERO.trust_note`.
> - **A mailing address is published** — filler for now, at `CONTACT.INFO.office`, and
>   repeated in the structured data in the head of `index.html`. Swap in the real one
>   before launch; New York State charitable-solicitation rules make it necessary once the
>   site takes donations, and it does.
> - **No response-time promises on the contact page.** The three-business-day promise came
>   out of the form confirmation and of `CONTACT.FAQ.1`, and the five-working-day
>   confirmation came out of the participant data-withdrawal notice. Two similar promises
>   survive elsewhere and are noted where they sit: the same-working-day promise in
>   `DONATE.FAQ.2`, and "a person, not a form, will answer" in `DONATE.FAQ.5`.
> - **The pilot fee is published as a number.** 1.5% of program budget, in
>   `PROGRAMS.WAYSIN.panel2` and `CONTACT.FAQ.4`.
>
> **One thing still outstanding.** The EIN came off the footer and the donor FAQ with your
> v2 edits. Now that the site asserts registered status and asks for money, donors will
> look for it — say the word and I'll put it back in both places.
>
> **13 September — the Program Description (Version 2, September 2026) is incorporated.**
> Where it and the copy deck disagree, the Program Description wins: it is newer and it is
> specifically about the pilot program. What changed:
>
> - **Two corrections.** The pilot is for program budgets *at or below* $500,000 (the site
>   said "under"), and in the pilot, **Phase 4 comes after graduation** — by discounted
>   retainer or a written guide — rather than being part of the core engagement. The site
>   had implied the pilot included the full four-phase suite.
> - **The fee** is now described as the brief describes it: a fixed *annual* fee of 1.5% of
>   program budget, paid on flexible terms.
> - **New: how the pilot runs** (`PROGRAMS.SEQUENCE.*`) — the eight-step sequence from
>   intake to onward support, including the two-year duration and graduation.
> - **New: impact logic** (`INVOLVED.IMPACT.*`) on Our Model — the four-step impact stream,
>   the three interventions with what each is measured by, and why recursion and
>   integration exists.
> - **New: `CONTACT.FAQ.5`**, on how long the pilot lasts and what happens after.
> - **The mission statement** on About is now the brief's own wording, and the About story's
>   middle paragraph uses its diagnosis of the problem.
> - Smaller additions to the Phase 1–4 bodies (Phase 2 as the heaviest lift, Phase 3's
>   analysis running offsite), and the implementation support role now cites the
>   Collaborative for Implementation Practice guidance it is built on.
>
> **13 September, later — the home page was rebuilt** as a plain-language pitch for what
> evaluation is, aimed at funders and nonprofit leaders who think of it as counting. The
> hero is untouched; see the note at the top of §B for what was added and removed.
>
> **13 September, last — tagline and logo.** The tagline is now *"For Research &
> Evaluation"*, matching the Program Description's cover, and the lockup is back at its
> original type size. The logo was being cropped because browsers held on to an old copy
> of the stylesheet; every page now loads its stylesheet, main script and favicon with a
> version number, so a changed file is always refetched. See `README.md` → "Things that are
> deliberate".
>
> **Later still — "pilot" dropped, standards band removed.** The program is no longer called
> a pilot anywhere on the site: "our pilot program" is now "our program", and every other
> reference follows (headings, buttons, the Contact FAQ, the Fund page, the About revenue
> table). "Pilots" and "pilot tested" in the Phase 2 and sequence copy mean trial runs, not
> the program, and stay. The home page's "What we will not do" band (`HOME.STANDARDS.*`) is
> gone; the standards themselves still live on About.
>
> **And — the worked example is a toolkit, not a sequence.** Its five timeline steps became four
> unordered tool cards plus a separate "What it adds up to" box (`HOME.EXAMPLE.tools`,
> `HOME.EXAMPLE.synthesis`; was `HOME.EXAMPLE.steps`).

---

## How to use this

1. **Edit the text inside the `>` quote blocks.** That's the live copy. Change it,
   rewrite it, delete it — whatever you like.
2. **Leave the `ID:` lines alone.** They're how I find the exact spot in the HTML.
   If an ID is gone I can't place your change reliably.
3. **Hand the whole file back to me** and say "apply these." I'll diff it against
   this version and make only the changes you made.

You don't need to re-upload it — the file lives in the project folder and I can read
it from disk. Just say you've updated it.

### Conventions

| You'll see | It means |
| --- | --- |
| `> text` | The actual copy on the site. **This is what you edit.** |
| `{{text}}` | Renders in the orange accent colour |
| `**text**` | Renders bold within a sentence |
| `ID: HOME.HERO.h1` | Stable address — don't edit |
| `Context:` | Where it sits and what job it does |
| `Fits:` | Length the design expects; over this it wraps or looks cramped |

### Talking back to me

Add a line starting with `»` anywhere. I read those as instructions, not copy:

```
ID: HOME.HERO.h1
Fits: 3 lines max
> Analytics based in {{trust,}} application in {{context}}.
» Too abstract for a first-time visitor. Try something that names the service.
```

To **delete** a block, replace the copy with `[DELETE]`. To flag something for
discussion rather than a specific edit, use `» ?` and I'll come back with options.

### Checking it stays true

`check-copy.py` verifies this document and the HTML still agree, in both directions:

```bash
python3 check-copy.py
```

It fails if the doc describes copy the site doesn't have, or the site contains copy
the doc doesn't document. A Stop hook runs it automatically.

---

## Contents

- [A. Global](#a-global-every-page) — header, footer, appears on all 8 pages
- [B. Home](#b-home) — `index.html`
- [C. About](#c-about) — `about.html`
- [D. Evaluation Process](#d-evaluation-process) — `programs.html`
- [E. Our Model](#e-our-model) — `get-involved.html`
- [F. Demo](#f-demo) — `demo.html`
- [G. 404](#g-404-page) — `404.html`
- [H. System text](#h-system-text) — interface labels
- [I. Search-engine & social text](#i-search-engine--social-text) — titles and descriptions
- [J. Image descriptions](#j-image-descriptions) — screen-reader alt text
- [K. Editor demo](#k-editor-demo-unlisted) — `editor_demo.html`, unlisted
- [L. Download](#l-download) — `download.html`

---

# A. Global (every page)

Edit these once; they change on all eight pages, the unlisted editor demo (§K) included.

## A1. Brand lockup

**ID: `GLOBAL.BRAND.name`**
Context: Top-left of every page and in the footer, next to the logo. Three words is
longer than the lockup was drawn for, so the name sits a size smaller than it did. It fits
on one line on desktop and wraps to two beside the mark on a phone.
Fits: Up to ~24 characters before it starts crowding the nav on a tablet.
> The Ascent Collaborative

**ID: `GLOBAL.BRAND.tagline`**
Context: Tiny uppercase line directly under the name. A category descriptor, not a
slogan — it tells a first-time visitor what kind of organisation this is. Since v60 it
reads "For Comprehensive Evaluation" and no longer matches the cover of the Program
Description. At this length it keeps the lockup's original type size and sits on one line
under the name on desktop and tablet, with very little room to spare; it wraps to two on a phone.
Fits: ~28 characters, the current length. Longer wraps on desktop too, and the type would need
shrinking again.
> For Comprehensive Evaluation

## A2. Main navigation

**ID: `GLOBAL.NAV.items`**
Context: Horizontal on desktop, a drop-down panel on mobile. Order is left to right.
The page file is still named `programs.html` internally — only the visible label changed,
so no links break. "Demo" (v16) goes to `demo.html` and
"Download" (v63) to `download.html`.
Fits: 1–2 words each. Six items is about the ceiling before it crowds the logo, and
the nav now has five. Our Model is deliberately not in it (v79): that page is unlisted.
> Home
> About
> Evaluation Process
> Demo
> Download

## A3. Footer — organisation blurb

**ID: `GLOBAL.FOOTER.blurb`**
Context: Beside the logo in the footer's single row (stacks under it on narrow screens). Since
v52 it uses the same name as the brand lockup above it, "The Ascent Collaborative".
Fits: 2–3 lines, ~180 characters. Makes no claim about legal or tax status (v5).
> The Ascent Collaborative is dedicated to making program evaluation more accessible, sustainable and effective.

## A4. Footer — legal line

**ID: `GLOBAL.FOOTER.copyright`**
Context: Bottom bar. The year updates itself — leave `[year]` as a placeholder. The
status line after the name came off in v5; the site states no legal or tax status.
> © [year] The Ascent Collaborative.

---

# B. Home

`index.html` — the page most first-time visitors land on.

**Rebuilt on 13 September around one job:** convincing a nonprofit leader who thinks of
evaluation as counting — people served, percentages, averages — that it is much more than
that, in plain terms. **Simplified on 1 October (v8):** the six method cards became three
short paragraphs of plain prose (§B2), which also say how Ascent combines evaluation
capacity building with implementation science, and the hypothetical job-training example
that followed them was removed. Ascent itself comes second, in a single "in brief" section
near the bottom.

The hero is yours; its first button now says "Our program". The "What evaluation is" section that followed it — the
"Measurement tells you what happened. Evaluation tells you what your program caused."
heading and its two-column comparison table (`HOME.MORE.*`) — was removed at your request,
so the page now goes straight from the hero to "How evaluation goes further". The "What we will not
do" standards band (`HOME.STANDARDS.*`) was removed the same way. The closing call to action
(`HOME.CTA.*`, "Tell us what you're trying to understand") came off in v9 with the Contact
page, so the page now ends on "Ascent, in brief".

Removed in the rebuild to make room: the problem split
(`HOME.PROBLEM.*`), the four pipeline cards (`HOME.PIPELINE.*` — the pipeline now appears
as four one-line bullets in `HOME.BRIEF.list`), the four "ways in" cards (`HOME.HELP.*`),
and the row of study citations (`HOME.EVIDENCE.*`). All of that content still lives on
Evaluation Process, Our Model and About.

## B1. Hero

The dark banner at the top. Text on the left, illustration on the right.

**ID: `HOME.HERO.h1`**
Context: The biggest text on the site. It does not say what Ascent sells; the lead
below has to carry all of that.
Fits: 3 lines at desktop, 4 on mobile. Currently ~57 characters.
> Analytics based in {{trust,}} application in {{context.}}

**ID: `HOME.HERO.lead`**
Context: The one paragraph that has to explain what you actually do. Sits directly
under the headline and does the work the headline deliberately doesn't. Since v71 it opens
with the organization's name and runs to about 230 characters, past the ~180 it was sized for.
Fits: 3–4 lines, ~180 characters; the v71 wording runs longer.
> The Ascent Collaborative's goal is to champion and implement an integrated evaluation model that is designed to lower the cost, improve the quality, and broaden the impact of evaluative services for mission-oriented organizations.

**ID: `HOME.HERO.buttons`**
Context: One orange button, to "How the program runs" on Evaluation Process. The outlined
"Contact us" beside it came off in v9 with the Contact page.
Fits: 2–4 words.
> Our program

**ID: `HOME.HERO.badge`**
Context: Card overlapping the bottom of the hero image. Since v81 one sentence, with no full
stop, and an orange accent word; until then a big number ("1.5%") and a phrase about the fee.
It is the hero's one claim about what Ascent gives a program. "MEL" (monitoring, evaluation
and learning) is not spelled out anywhere on the site.
Fits: ~100 characters, about two lines on desktop; it covers more of the image on a phone.
> Unrestricted implementation support and intuitive software make MEL accessible to {{every}} program

## B2. Evaluation that goes further

A heading, a lead, a row of three phase cards, since v46 a second row of three tool-view
cards, and, since v41, a "Try the demo"
button (and, since v70, a "Download the app" button beside it). The tagline above the
buttons came off in v81. **Rewritten on 1 October (v8)** to replace six
method cards (`HOME.METHODS.card1`–`card6`); since v40 the two paragraphs that followed the
cards (`HOME.METHODS.body`) and the "The research behind it" link (`HOME.METHODS.link`) are
gone too, so the section ended on the cards until v41.

**ID: `HOME.METHODS.intro`**
Context: The lead is the whole old six-card argument in one sentence: whether it made the
difference (causal inference, attribution), for whom (impact), why (qualitative analysis),
and how much to trust it (evidence strength). Keep it one sentence.
Fits: Heading 1–2 lines; lead ~200 characters. The v81 heading runs to three lines on desktop.
> Eyebrow: Evaluation that Goes Further
> Heading: An evaluation process accountable to outcomes and a platform to monitor it all
> Lead: Ascent's recursive process links program inputs to final outcomes and incorporates practice context to build a dynamic outcomes model.

**ID: `HOME.METHODS.phases`**
Context: New in v29 (it began in v27 as `HOME.HERO.phases`, a thumbnail row inside the hero,
and moved here). Three cards between the lead and the tool-view cards: Evaluation Process
phase screenshots with a home-page name underneath (not the phase names on that page). Since
v49 they no longer link to Evaluation Process: like the tool-view cards, a click opens a short
description and a second click closes it. Without JavaScript the descriptions are shown. They
reuse the screenshots of `PROGRAMS.CARDS.*` (alt text in `ALT.home_phases`). The descriptions
are mine, written from the screenshots and the phase sections; correct them freely.
Fits: Name ≤ ~35 characters; description 1–2 sentences, ~200 characters. Three across on
desktop, one column on narrow screens.
> Name 1: Logic Models & Metric Integration
> Description 1: Map how a program's inputs and activities lead to its outputs and its short-, medium- and long-term outcomes, and tie each part of the model to the metrics that will track it.
> Name 2: Data Architecture
> Description 2: Trace every number in the model back to the data series it comes from so its sources are clear and the quality of the evidence can be checked.
> Name 3: Analytics & Forward Planning
> Description 3: Analyze how a program's results move over time and what drives them, test how sensitive they are to changes in inputs and assumptions, and use that to plan ahead.

**ID: `HOME.METHODS.tools`**
Context: New in v46; expanding since v48. A second row of three cards under the phase cards,
each a screenshot of another view in the Program Mapper with its name underneath. They no
longer link anywhere (they went to the Demo page in v46): clicking a card opens a short
description of that view, and clicking again closes it. Without JavaScript the descriptions
are simply shown. The screenshots are `assets/tool-*.png`; their alt text is in
`ALT.home_tools`. The sample data in them (a job-readiness program) is example data, not a
client result. The descriptions began as mine, written from what the screenshots show; you
rewrote the first two in v55. Correct them freely.
Fits: Name ≤ ~35 characters; description 1–2 sentences, ~200 characters. Three across, one
column on narrow screens.
> Name 1: Stakeholder Mapping
> Description 1: Lay out everyone with a stake in the program, from funders and governance to the delivery team, partners and the people served, and see how their connections affect your practice.
> Name 2: Policy and Practice Context
> Description 2: Keep track of the rules, regulations, funding formulas and incentives that shape the program: what is in force today, what is proposed, and how changes can affect the program's projections.
> Name 3: Evidence & Theories of Change
> Description 3: Build the logic model from inputs to long-term outcomes, attach the evidence and assumptions behind each link, and see at a glance which links are evidenced, mixed, untested or refuted.

**ID: `HOME.METHODS.demo`**
Context: New in v41. Closes the section: a button to the Demo page. The phase cards above
show screenshots of the tool; this is where a visitor gets to use it. Since v70 a second,
outlined button beside the orange one goes to the Download page; the two wrap onto two lines
on a phone. The tagline above them (last "A single app shows the power of our evaluation
model.") came off in v81: the field is empty, and the site shows no line.
Fits: Tagline ≤ ~70 characters; each button 2–4 words.
> Tagline: 
> Button: Try the demo
> Button 2: Download the app

## B3. Why it matters

One card, for nonprofit leaders, programs teams and evaluators, in a narrowed column. There
were two, one per audience; the funders card (`HOME.WHY.funders`) came off in v7.

**ID: `HOME.WHY.intro`**
> Eyebrow: Why it matters
> Heading: Catalyze a continual improvement process
> Lead: Evaluation should not be a static exercise. For beneficiaries, program services can be a lifeline. They should always be improving.

**ID: `HOME.WHY.leaders`**
Context: Four benefits with bold lead-ins, rewritten in v55 around what the process and the
tool do: track what works, build an evidence base, watch the policy context, and hear from
participants.
> Heading: For nonprofit leaders, programs teams and evaluators
> **Map and monitor efficacy.** Evaluation shows which parts of a program are most effective, so limited resources can go where they count the most.
> **Build and document a knowledge-base.** Map evidence to internal assumptions about a program's theory of change. Approach programs with clarity and integrate them into global fields of research.
> **Track exogenous effects.** Monitor policy and other contextual developments and project their impacts on program functions.
> **Hear from the people served.** Qualitative methods put participants' own accounts of what helped into the evidence, tracing the path from program inputs to the effects reported by participants.

**ID: `HOME.WHY.button`**
Context: New in v50. One orange button under the benefits card, to Evaluation Process, so a
reader who has just been told why evaluation matters can see what the process is. The label
is mine; change it freely.
Fits: 2–5 words.
> See the evaluation process

## B4. Statistics strip

Now a bridge rather than an opener: having argued that evaluation is valuable, the page
shows who can't get it. A heading and a one-sentence lead, then three numbers that count up
as they scroll into view. The fourth stat
(phases in the pipeline) came out; it was about Ascent, and this strip is about the sector.

**ID: `HOME.STATS.h2`**
Context: New heading. It turns three numbers into an argument and hands the reader to the
next section, where Ascent appears.
> The organizations that need it most can least afford it

**ID: `HOME.STATS.lead`**
Context: Grey lead line centred under the heading, before the numbers. Moved here from the
About page in v59 at your request; it was `ABOUT.STORY.para1`, the paragraph that opened
"The evidence base", and that ID is retired. The founding argument, stated as arithmetic
rather than anecdote: the numbers below are the evidence for it. The
four-hundred-thousand-dollar organisation with a program director doing evaluation at night
is the reader this whole site is addressed to.
Fits: 2–3 lines at this width; one sentence.
> When evidence quality determines funding, capital consolidates toward whoever can afford to prove their outcomes—whether or not they are the organizations doing the most consequential work.

**ID: `HOME.STATS.1`**
> Value: 98 · Suffix: % · Label: Small nonprofits without dedicated evaluation staff

**ID: `HOME.STATS.2`**
> Value: 80 · Suffix: % · Label: Organizations above $5M lacking the same

**ID: `HOME.STATS.3`**
> Value: 16 · Suffix: % · Label: Surveyed organizations spend nothing on evaluation

**ID: `HOME.STATS.disclaimer`**
Context: The source citation. Keep it visible — precision is part of the pitch.
> Source: Innovation Network, State of Evaluation 2016.

## B5. Ascent, in brief

Illustration left, text right, light grey background. The program summary you asked for,
kept to one section so the page stays about evaluation.

**ID: `HOME.BRIEF.eyebrow`**
> Ascent Evaluation, in brief

**ID: `HOME.BRIEF.h2`**
Context: Names the differentiator — the work integrates into the program team — rather than
the service, because the page above has already explained the service.
Fits: 2 lines.
> Evaluation and capacity building that integrates into program teams

**ID: `HOME.BRIEF.lead`**
> An implementation support professional embeds within programs teams and carries them through **full and recursive** evaluations, turning evaluation findings into holistic changes the organization can actually make.

**ID: `HOME.BRIEF.body`**
Context: Since v42 a statement of principle rather than the program in facts: the two years,
the $500,000 ceiling and the 1.5% fee are no longer here (since v81 the fee is nowhere on the site).
> The process is the program. Participants’ active collaboration in pursuing inquiry, scoping analysis, and employing new methods is central to both the ethics of Ascent’s practice and the achievement of its mission.

**ID: `HOME.BRIEF.list`**
Context: The four phases, one line each, replacing the four pipeline cards that used to
sit mid-page. Plain names first; the full detail is on Evaluation Process.
> **Evaluative foundation.** What is this program trying to do, for whom, and why we believe it will work.
> **Data architecture.** What data is needed, from whom, through what means, and how to ensure quality.
> **Analytics and inference.** What the data tell us, and with what degree of confidence, about how the program works and what of its characteristics are effective.
> **Monitoring, learning and reporting.** Ensuring the program continues to work while communicating impact to stakeholders and incorporating policy and other contextual factors.

**ID: `HOME.BRIEF.links`**
Context: A solid button. A text link after it, "How the model works", went to Our Model
and came off in v79 when that page became unlisted.
> Our program

---
# C. About

`about.html` — what Ascent is and why it exists: a banner and the evidence base. The deck has no About page; this one was built from its standards
chapter and its governance section, and both are now gone — the quality assurance
material in v10, the Governance section in v11 — because the site describes a
hypothetical service set and doesn't need that depth.

## C1. Page banner

**ID: `ABOUT.HERO.h1`**
Context: Dark banner at the top of the page. Every interior page has one. Since v12 the
heading stands alone — the subhead under it (`ABOUT.HERO.lead`, "Ascent is a nonprofit
program evaluation practice in New York City.") came off. Was "Built for the
organizations evaluation was priced away from".
Fits: 1–2 lines.
> Built for the benefit of organizations priced out of comprehensive evaluation

**ID: `ABOUT.HERO.lead`**
Context: Subhead under the banner heading. Back in v13 after being off since v12 (it used to be
"Ascent is a nonprofit program evaluation practice in New York City."). Completes the sentence
the heading starts: who the work is for, then what it is designed to do.
Fits: One line.
> And designed to translate evaluation to outcomes.

## C2. Why this exists

Eyebrow, heading and one paragraph of argument, stacked and centred (since v76; until then the
heading sat on the left with the paragraph beside it); the two-field timeline (§C3) runs below.
The same treatment as "How the program runs" on Evaluation Process. Until v56 this text stuck
beside the timeline as it scrolled; the timeline now needs the full width.

**ID: `ABOUT.STORY.eyebrow`**
> The evidence base

**ID: `ABOUT.STORY.h2`**
Fits: 2 lines.
> An outcomes-oriented synthesis.

**ID: `ABOUT.STORY.para2`**
Context: The only paragraph under the heading since v59, when the founding argument that
used to open it (`ABOUT.STORY.para1`) moved to the home page as `HOME.STATS.lead`. It says
why the answer is a different structure rather than a discount. The
diagnosis in the first three sentences comes from the Program Description's mission
section, lightly edited for a web reader ("methodologies" → "methods", "self-implement" →
"take on alone").
> Program evaluation is inaccessible and underleveraged. As a service, its practitioners are disparate or overpriced. As a practice, its methods are too niche, its implementation too resource-intensive, and its benefits too obscure for program teams to incorporate alone. The evidence says evaluation works best through long-term collaboration that builds trust, deepens context and shepherds adoption. In the current market, those carry impossible costs for small and mid-sized organizations. 

## C3. Evidence timeline

Two fields, one synthesis. Since v56 the timeline shows the model as a combination of
implementation science and evaluation capacity building (ECB): each field has a rail of its
own, teal and orange, and the rails never touch until they join at the bottom in the Ascent
entry (`ABOUT.TIMELINE.synthesis`). Entries run in date order down both rails, so the
picture also shows the timing — ECB maturing from the late 1990s, implementation support
professionalizing in the late 2010s, both arriving in 2020. On a phone the two rails run
side by side down the left edge.

The six ECB landmarks in Table 2 of the Evidence & Peer Context brief are `ABOUT.TIMELINE.11`
to `16`; the four studies in its Table 3 were already here. Add or remove entries freely —
the rails redraw themselves. IDs 6 and 9 came off in v36 and v55 and are not reused.

Each entry's `Field:` is the rail it sits on; change it to move the entry to the other field.
On a wide screen the lane already says which field an entry belongs to, so the label is kept
for screen readers only; on a phone it is printed after the year. A `Tag:` prints after the
year everywhere.

Context: Until v71 each entry ended with a short-form author citation in brackets; you took
them all out. The sources are still named in each entry's Context note below. If you want
them back as full references, say so and I'll build a references page and link each entry.

**ID: `ABOUT.TIMELINE.field_is`**
Context: Heading over the implementation science rail (on a phone, the first key above
both rails). New in v56; my wording.
Fits: Name one line; Line two lines in half the page width (about 20 words).
> Name: Implementation science
> Line: The study of how new practices take hold in real programs, and how to shepherd adoption while ensuring that they are aligned with target needs and capabilities.

**ID: `ABOUT.TIMELINE.field_ecb`**
Context: Heading over the ECB rail. New in v56; my wording, after the definition in
Stockdill, Baizerman & Compton (2002).
Fits: As `ABOUT.TIMELINE.field_is`.
> Name: Evaluation capacity building
> Line: The practice of making evaluation, and the use of its findings, an ordinary part of a program's operations.

**ID: `ABOUT.TIMELINE.11`**
Context: New in v56, from Table 2 of the brief (process use, Patton 1997). The mechanism the model leans on: taking part in evaluation teaches more than the report does.
> Year: 1997
> Field: Evaluation capacity building
> Headline: Learning from the process
> Detail: Process use names the learning that comes from taking part in an evaluation, beyond anything in its findings.

**ID: `ABOUT.TIMELINE.12`**
Context: New in v56, from Table 2 (Stockdill, Baizerman & Compton 2002) — the point the brief dates ECB from as a field of its own.
> Year: 2002
> Field: Evaluation capacity building
> Headline: Capacity by design
> Detail: Evaluation capacity building is defined as a field: designed practice rather than a by-product, with the use of evaluation built into what capacity means.

**ID: `ABOUT.TIMELINE.13`**
Context: New in v56, from Table 2 (Preskill & Boyle 2008).
> Year: 2008
> Field: Evaluation capacity building
> Headline: Capacity lives in culture
> Detail: A multidisciplinary model ties evaluation capacity to organizational learning and culture, and sets out the conditions for practice that lasts.

**ID: `ABOUT.TIMELINE.7`**
Context: New in v34, with entries 8–10 (9 came off in v55): these bring in how implementation science developed and
how implementation support became a profession. 2009 is cited in the two PDFs linked from
entry 10. `ABOUT.TIMELINE.6` (2005) was removed in v36; IDs are not renumbered.
> Year: 2009
> Field: Implementation science
> Headline: A framework for what shapes implementation
> Detail: The Consolidated Framework for Implementation Research organizes the factors that help or hinder putting evidence into practice.

**ID: `ABOUT.TIMELINE.14`**
Context: New in v56, from Table 2 (Labin, Duffy, Meyers, Wandersman & Lesesne 2012). "Weaknesses in its designs" follows the brief's "identifies design weakness".
> Year: 2012
> Field: Evaluation capacity building
> Headline: The field takes stock
> Detail: A research synthesis consolidates the literature, codes its outcomes at the individual and organizational levels, and identifies weaknesses in its designs.

**ID: `ABOUT.TIMELINE.1`**
Context: A Getting To Outcomes trial, published in *Implementation Science*. The brief's executive summary counts these trials as implementation science and its Table 3 as ECB evidence, so this sits on the implementation science rail and is drawn as one stop across both.
> Year: 2013
> Field: Implementation science
> Tag: Cited by both fields
> Headline: Dose matters
> Detail: A two-year cluster-randomized trial finds dose-dependent gains across four capacity scales, greatest where technical assistance hours were highest.

**ID: `ABOUT.TIMELINE.2`**
> Year: 2013
> Field: Evaluation capacity building
> Headline: Organizations, not individuals
> Detail: Instrument validation establishes that leadership, resources and learning climate decide whether individual knowledge ever becomes mainstreamed practice.

**ID: `ABOUT.TIMELINE.15`**
Context: New in v56, from Table 2 (Cousins, Goh, Elliott & Bourgeois 2014).
> Year: 2014
> Field: Evaluation capacity building
> Headline: Doing is not using
> Detail: The capacity to do evaluation is separated from the capacity to use it: methodological skill on one side, the organizational conditions that let findings have influence on the other.

**ID: `ABOUT.TIMELINE.16`**
Context: New in v56, from Table 2 (Buckley, Archibald, Hargraves & Trochim 2015).
> Year: 2015
> Field: Evaluation capacity building
> Headline: A habit of mind
> Detail: Evaluative thinking is named as the lasting disposition that evaluation capacity building aims to instill.

**ID: `ABOUT.TIMELINE.3`**
Context: Belongs to neither field: it measures the sector the synthesis is for. Boxed across both rails, with no stop on either, and has no `Field:` line.
> Year: 2016
> Tag: The sector
> Headline: The affordability gap, measured
> Detail: Roughly ninety-eight percent of small nonprofits and eighty percent of organizations with budgets above five million dollars have no dedicated evaluation staff.

**ID: `ABOUT.TIMELINE.8`**
Context: From the Practice Guide's "How we developed this guide": the work began in 2017 as an
internal R&D project between NIRN (USA) and the Centre for Effective Services (Ireland and
Northern Ireland).
> Year: 2017
> Field: Implementation science
> Headline: Implementation support becomes a field of research
> Detail: Two intermediary organizations, one in the USA and one in Ireland and Northern Ireland, begin studying the role and competencies of the people who support implementation.

**ID: `ABOUT.TIMELINE.4`**
Context: The second Getting To Outcomes trial; drawn across both rails for the same reason as `ABOUT.TIMELINE.1`.
> Year: 2018
> Field: Implementation science
> Tag: Cited by both fields
> Headline: Repetition and duration drive results
> Detail: A replication trial finds no significant effect in year one and small significant improvement after a second-year quality improvement cycle.

**ID: `ABOUT.TIMELINE.10`**
Context: Two of the words are links, opening in a new tab: "Implementation Support Practitioner
Profile" → https://cippro.wpengine.com/wp-content/uploads/2022/10/IS-Practice-Profile-single-page-printing-v10-October-2022.pdf
and "Practice Guide" → https://cippro.wpengine.com/wp-content/uploads/2022/10/ISP-Practice-Guide-v1-10.27.22.pdf
The PDFs are dated November and December 2020 (Profile v4.0; Guide), re-hosted in October 2022.
> Year: 2020
> Field: Implementation science
> Headline: Competencies, described
> Detail: The Implementation Support Practitioner Profile and Practice Guide set out fifteen core competencies in three domains: co-creation and engagement, ongoing improvement, and sustaining change.

**ID: `ABOUT.TIMELINE.5`**
Context: The finding the whole model is built on. If you cut one entry, don't cut this.
> Year: 2020
> Field: Evaluation capacity building
> Headline: Relationship, not training
> Detail: Evaluation practice persists years after an intervention, and the persistence tracks ongoing evaluator contact rather than the initial training.

**ID: `ABOUT.TIMELINE.synthesis`**
Context: Where the two rails join, centred under the timeline (on a phone, a stop across both
rails). New in v56; my wording. It states the gap the brief's executive summary names — no
model applies implementation science's evidence within ECB, explicitly and measurably — and
stops there. Until v64 a second sentence said what the model is designed to do about it;
your edit removed it, so the entry now makes the claim about the field and none about Ascent.
Fits: Label one word; Headline one line; Detail one sentence, about 20 words.
> Label: Ascent
> Headline: Where the two fields meet
> Detail: No existing model delivers evaluation capacity building on the evidence of implementation science, explicitly and measurably.

---

# D. Evaluation Process

`programs.html` — the detail page. Someone deciding whether to hire you reads this.
(File name is still `programs.html`; the visible label is "Evaluation Process".)

## D1. Page banner

**ID: `PROGRAMS.HERO.h1`**
> Evaluation Process

**ID: `PROGRAMS.HERO.lead`**
Context: "A link in a chain and a standalone engagement" is the commercial proposition
in nine words — it says you can buy one piece without buying the programme.
> A four-phase evaluation pipeline. Our process is recursive, building upon past findings and expanding a model's explanatory leverage.

## D2. Overview cards

Four cards, two by two. Since v74 they have no "Learn more" buttons: the phase detail
sections they linked down to are gone (the app in §D3 covers the phases). These summaries are
**shorter than the home page versions** on purpose. Since v13 each card shows a
screenshot of a working tool in place of its placeholder illustration: Phase 1 a logic
model, Phase 2 a data-lineage view, Phase 3 a single-indicator analysis, Phase 4 a
scenario dashboard (`assets/phase-1-logic-model.png` … `phase-4-scenarios.png`). The cards
crop to 16:9; Phases 2–4 are anchored to the top of the screenshot so their headers stay
in view. Alt text is in `ALT.programs`.

**ID: `PROGRAMS.CARDS.h2`**
Context: New in v61, at your request. A centred heading over the four cards, with no eyebrow
(the subhead below it is `PROGRAMS.CARDS.lead`). It is the first `h2` on the page; until now
the cards' own headings came straight after the page title. "Black box" is evaluation's term
for a program judged only on what goes in and what comes out; the four cards below each open
one phase of what happens between. Since v64 the first word is in the orange accent colour,
as the words picked out in the home page's hero title are.
Fits: 3–5 words, one line at every width.
> {{Opening}} the black box

**ID: `PROGRAMS.CARDS.lead`**
Context: New in v62, at your request. The subhead under "Opening the black box", centred, in
the same grey lead style as the home page's section leads. It is a statement about the
platform, not the process: the heading is about what the phases open up, this line says who
the platform is for and what it gets them.
Fits: One sentence, ~90 characters; two lines on desktop, up to three on a phone.
> A platform built for program teams that gets to outcomes by providing clarity in practice.

**ID: `PROGRAMS.CARDS.1`**
> Tag: Phase 01
> Name: Evaluative Foundation
> Summary: The conceptual infrastructure that makes rigorous evaluation possible: stakeholder map, logic model, theory of change.

**ID: `PROGRAMS.CARDS.2`**
> Tag: Phase 02
> Name: Data Architecture
> Summary: A practical system for collecting and managing data while preserving the needs of stakeholder communities.

**ID: `PROGRAMS.CARDS.3`**
> Tag: Phase 03
> Name: Analytics & Inference
> Summary: Collected data turned into defensible evidence; outcomes here inform change recommendations and help scope further inquiry.

**ID: `PROGRAMS.CARDS.4`**
> Tag: Phase 04
> Name: Monitoring, Learning & Reporting
> Summary: Findings converted into systems that sustain learning and accountability over time.

## D3. How the program runs

New on 13 September, from the Program Description's sequencing diagram. Since v75 one section,
text above the Evaluation Pipeline app: the eight-step timeline that stood beside the text is
gone, and the app below now shows the sequence. The text is centred over the app, as "Opening
the black box" is over the cards; the long paragraphs read more slowly centred than set left.
Anchored at `#pilot-sequence` — since v14 both "Our program" buttons on the home page land
here (they went to `#flagship`, on the removed "Two ways in" section).

The app, **new in v73**, is live from `evaluationguide.netlify.app`, the full width of the
page and as tall as the app itself. The app tells the page its height, so the frame grows and
shrinks with it (over 3,000px on a laptop, more on a phone and while a step's card is open)
and never scrolls inside itself; with JavaScript off it falls back to 720px. Unlike the
Demo page (§F2) it has no border, shadow or rounded corners: the app's background is the
page's own, so it reads as part of the page rather than a framed window. Nothing inside it is
site copy, and there is no small print or "open in a new tab" link under it. Since v77 the
text above the app leaves 96px before the app's content, the same as the space at the top of
the section.

**ID: `PROGRAMS.SEQUENCE.eyebrow`**
> Our program

**ID: `PROGRAMS.SEQUENCE.h2`**
Context: "The process is the program" is the Program Description's own headline claim and
the most compressed statement of what makes the program different. Keep it verbatim.
> The process is the program.

**ID: `PROGRAMS.SEQUENCE.body`**
Context: Two paragraphs. The first says what the implementation support professional does
and what your staff co-create. The second explains the loop: written for the timeline that
stood beside it until v75, it now introduces the app straight below, whose own title
follows it. "Recursion and integration" and "graduation" were the names of steps 06 and 07
of that timeline; since 20 October the app shows that program journey itself, Graduation
included, in a column beside the pipeline.
> The implementation support professional coordinates the evaluation, shepherds findings into program changes, and helps build a culture of inquiry within the team. The organization's staff co-create the frameworks, collection methods, pilots and data architecture alongside them.
> The sequence runs in one direction until it reaches recursion and integration, and then it loops: findings become program changes, outcomes feed the next round of evaluation, and the cycle repeats until graduation.

**ID: `PROGRAMS.PIPELINE.frame`**
Context: Not visible: the name a screen reader announces for the embedded app before reading
the app itself, as `ALT.demo` does on the Demo page. It is the app's own page title.
> Embedded app: Evaluation Pipeline

---
# E. Our Model

`get-involved.html` — the page that explains why the price is possible. Deck Page 2.
(File name is still `get-involved.html`; the visible label is "Our Model".)
**Unlisted since v79:** nothing on the site links here and it carries `noindex, nofollow`.
Reached only from a link you give out.

## E1. Page banner

**ID: `INVOLVED.HERO.h1`**
> The Model

**ID: `INVOLVED.HERO.lead`**
Context: Six words of problem, four of claim. It promises an explanation rather than a
pitch, which is the right promise for the reader who has just been told the price.
> Everything special about the Ascent model, and how it can deliver real change in the mission-oriented sector.

## E2. Impact logic

New on 13 September, from the Program Description's impact-stream diagram and its
interventions table. Four cards, then an orange box (the table came off in v38). Anchored at
`#impact-logic`; nothing links here now that the program sequence button is gone (v51).

**ID: `INVOLVED.IMPACT.intro`**
Context: The heading is the brief's positioning claim, shortened. It only works because
the lead immediately says *how* the program differs from each: deeper than consulting,
more participatory than capacity building.
> Eyebrow: Impact logic
> Heading: More than evaluation consulting. Beyond capacity building.
> Lead: The program reaches deeper into an organization than traditional evaluation consulting, and it is far more participatory, on both sides, than typical capacity-building models. While building capacity, our model is designed to incorporate outcomes sensitivity through the following impact cascade:

**ID: `INVOLVED.IMPACT.stream`**
Context: Four cards in the order of the brief's impact stream. Each = number tag, name,
what happens, then a bold line saying who leads it and what gets measured there. The bold
lines are the accountability claim: they say which parts Ascent answers for directly and
which belong to the client. Card three is orange, marking the step Ascent does not touch.
Fits: ~130 characters per description; bold line one short sentence.
> Tag: 01
> Name: Evaluation
> Description: Establishes the systems and standards for recursive improvement, and the baseline measurements that change is rated against.
> Measured: 
>
> Tag: 02
> Name: Programs
> Description: Evaluation results inform program changes, and drive improvements in implementation fidelity and measurability.
> Measured: 
>
> Tag: 03
> Name: Outcomes
> Description: The program team defines implementation strategies from the recommendations, and reports results, roadblocks and community concerns.
> Measured: 
>
> Tag: 04
> Name: Recursion and integration
> Description: Traces the processes that translate metrics to outcomes and builds cross-cutting improvement strategies that feed into the next evaluative cycle.
> Measured: 

**ID: `INVOLVED.IMPACT.note`**
Context: Orange box. Recursion and integration is the concept a first-time reader has
never met, so this explains why it exists before asking anyone to care about its three
mechanisms (causal chain identification, metric integration, evaluation recursion — here
in plain words rather than by name). The second sentence says why existing models lose the
connection to outcomes; the last is what makes it matter to a funder.
> **Why recursion and integration exists.** Studies of existing models find a weak connection between evaluation-based services and final program outcomes. Existing models, due to their reliance on time-determined fees and/or discrete deliverables, essentially absolve themselves of accountability for their clients' outcomes by dissolving their connection to the work on the ground. Recursion and integration explicitly does the opposite: qualitative analysis traces each evaluation and program input through to its effect on downstream outcomes. This keeps our practice accountable to outcomes rather than to deliverables.

## E3. The structure

*(Was `INVOLVED.ROLES.*` — six collaboration roles.)*

**ID: `INVOLVED.STACK.intro`**
Context: The heading's claim is the reason the model works: better coordination is what
makes the service affordable.
> Eyebrow: The structure
> Heading: Finding affordability in better coordination.

**ID: `INVOLVED.STACK.layer1`**
Context: Four cards, two by two, in the order the deck's delivery stack runs — outside
in, ending with you. Each is a heading and a description; the bold role line came off in v44.
> Heading: Outsourced expertise
> Commitment: 
> Description: Specialists with deep methodological or domain knowledge, available when a project needs them and not carried as overhead when it doesn't.

**ID: `INVOLVED.STACK.layer2`**
> Heading: In-house analytics
> Commitment: 
> Description: The most common technical work, sourced in-house: data analysis, instrument design, program design and measurement.

**ID: `INVOLVED.STACK.layer3`**
Context: Orange icon — this is the layer the whole model turns on, and the one the
sector doesn't currently staff.
> Heading: Implementation support
> Commitment: 
> Description: The primary liaison between analysts and the program team. Implementation support professionals translate findings into actionable changes and shepherd them through the organization, ensuring that changes redound to the benefit of participants.

**ID: `INVOLVED.STACK.layer4`**
> Heading: Partner Programs
> Commitment: 
> Description: Implementation staff listen to an organization's needs and shepherd feasible change within it. Program teams co-create the evaluation design and inform its application. Here, the relationship is as important as the analysis.

**ID: `INVOLVED.STACK.note`**
Context: Orange box under the cards. The last sentence is a claim about the field, not
about Ascent, and it is checkable — which is why it can be made this bluntly. The
second-to-last names the published guidance the role is built on, as the Program
Description does; if you want it linked, send me the URLs you use for the two documents.
> An implementation support professional's expertise is the holistic appraisal of the organization's and community's needs and the methods most likely to make new knowledge and practice stick. They translate findings into feasible program changes and shepherd those changes through the organization, with attention to its resources and practice context. The role is grounded in the Collaborative for Implementation Practice's Implementation Support Practitioner Profile and Practice Guide. No existing model applies that evidence, explicitly and measurably, to evaluation capacity building.

## E4. Closing call to action

**ID: `INVOLVED.CTA`**
Context: A model page has to end by admitting that the model is not the product.
> Heading: See the model in action.
> Button: Explore the pipeline

---

# F. Demo

`demo.html` — a working demo of Program Mapper, the tool shown on the four phase
cards on Evaluation Process. **New in v16.** The app is not part of this site: it is hosted
separately (ascentmapper.netlify.app) and shown in a frame, so nothing inside the
frame is covered here — its wording changes in the app. Its sample program is a fictional
job-readiness program.

## F1. Page banner

**ID: `DEMO.HERO.h1`**
Context: The tool's own name, as the app titles itself.
> Program Mapper

**ID: `DEMO.HERO.lead`**
Context: What the tool is, then three things a visitor can do in it. "Behind our evaluation
pipeline" ties it to the phase cards on Evaluation Process, which show its screenshots.
Fits: 2–3 lines, ~180 characters.
> Try the app behind our evaluation pipeline. The application **describes** the evaluation process, and the demo depicts the data penetration of multiple rounds of recursive evaluation.

## F2. The demo

The app in a bordered frame, the full width of the page and 720px tall. Under it, a line of
small print on the left and a link on the right.

**ID: `DEMO.EMBED.note`**
Context: The first sentence is the one that matters. The site claims no past result, and the
demo is full of realistic numbers that would otherwise read like one. The second is there
because the tool has three panels side by side and gets cramped on a phone.
Fits: 1–2 lines.
> The program and figures in the demo are fictional. The application works best on a large screen.

**ID: `DEMO.EMBED.link`**
Context: Arrow link. Opens the app on its own in a new tab, at full window size — the better
way to use it on a small screen.
> Open the demo in a new tab

## F3. Inside the tool

Grey band. A heading, then six cards, three by two, one per view in the app's left-hand rail
and in the rail's order. They are not numbered: the views are different angles on one model,
not steps. Since v70 the band ends on a button to the Download page.

**ID: `DEMO.VIEWS.intro`**
Context: The lead ("Move between them from the rail down the left side of the demo.") came
off in v71 and the field is left empty; type one there and hand the file back to bring it back.
> Eyebrow: Using the app
> Heading: Six views of one program
> Lead: 

**ID: `DEMO.VIEWS.cards`**
Context: One sentence each (the Logic model card two, since v71), describing what the view shows, in the app's own terms. The rail
labels them Map, Logic, Theory, Policy, Change and Data; the headings use the fuller names
the app gives them. Keep them roughly this length or the grid goes ragged.
> Heading: Stakeholder map
> Body: Who is affected by the program and how they are tied to one another.
>
> Heading: Logic model
> Body: Map the connections that take program inputs through activities and outputs to short-, medium- and long-term outcomes. Place each logical pathway on its own layer and aggregate them to visualize the logical trusses of your program.
>
> Heading: Theory of change
> Body: The assumptions each causal link depends on, and the evidence filed under each one, with every link marked evidenced, mixed, untested or refuted.
>
> Heading: Policy
> Body: The rules regulating the program today, the changes in development, and which of the program's measures each one affects.
>
> Heading: Change
> Body: Outputs and outcomes modeled dynamically and projected under changes to inputs and policy, with every scenario read against a baseline.
>
> Heading: Data
> Body: Every number in the model, held once as a series and traced to each place it is used.

**ID: `DEMO.VIEWS.download`**
Context: New in v70. One orange button under the six cards, left-aligned with the heading,
to the Download page: having seen the views in the browser, this is where a visitor gets the
app for their own program. Same label as the Download page's heading and the home page's
second button (`HOME.METHODS.demo`).
Fits: 2–4 words.
> Download the app

---

# G. 404 page

`404.html` — shown when someone hits a URL that doesn't exist.

**ID: `NOTFOUND.h1`**
> Eyebrow: Error 404
> Heading: This path doesn't go anywhere
> Lead: This page has moved, been renamed, or never existed. Here's the way back.

**ID: `NOTFOUND.buttons`**
Context: One button since v9; "Tell us what broke" went to Contact.
> Back to home

**ID: `NOTFOUND.cards`**
Context: One shortcut card so the page is useful rather than just apologetic. The
third, to the Fund page, came off in v6; the second, to Our Model ("Why evaluation costs
what it costs, and what we changed."), came off in v79 when that page became unlisted.
> Heading: Evaluation Process — The four-phase evaluation pipeline.

---

# H. System text

Text that appears in response to something the visitor does. It lives in `js/main.js`
rather than in the pages, but it's still copy.

## H1. Interface labels

**ID: `SYSTEM.ui`**
Context: Small functional strings. The skip link is only visible to keyboard users.
> Skip link: Skip to main content
> Menu button: Toggle navigation menu

---

# I. Search-engine & social text

The title is what shows in a browser tab, a Google result, and a shared link. The
description is the grey summary line beneath it in search results.

**Fits:** Titles under ~60 characters or Google truncates them. Descriptions 120–158
characters.

**ID: `SEO.home`**
> Title: The Ascent Collaborative—nonprofit program evaluation
> Description: Program evaluation is more than measurement. Ascent helps nonprofits learn what their programs cause, for whom, and why—at a price they can meet.

**ID: `SEO.about`**
Context: Rewritten in v10, when both lines described the quality assurance commitments,
and the title shortened in v11 when Governance came off. The description combines the
old banner subhead with the current heading, so it changed with the heading in v12.
> Title: About Ascent—the mission and the evidence
> Description: Ascent is a nonprofit program evaluation practice in New York City, built for the organizations priced out of effective evaluation.

**ID: `SEO.programs`**
> Title: Evaluation Process—the four-phase evaluation pipeline
> Description: A four-phase program evaluation pipeline: evaluative foundation, data architecture, analytics and inference, monitoring and reporting. Enter at any phase.

**ID: `SEO.involved`**
> Title: Our Model
> Description: How Ascent restructures evaluation delivery to make sustained, evidence-based capacity building affordable for organizations priced out of the consulting market.

**ID: `SEO.demo`**
Context: New in v16. The description lists four of the six views in the order the
page does.
> Title: Demo—try the Program Mapper
> Description: Try the Program Mapper: map every facet of a program, measure outcomes and test the effects of different changes.

**ID: `SEO.download`**
Context: New in v63. Names both systems the page covers, since that is what someone searching
for an installer types. The description is 132 characters.
> Title: Download—Ascent Mapper for Mac and Windows
> Description: Download Ascent Mapper, the desktop app for building and reading program logic models, for Mac (Apple silicon or Intel) and Windows.

**ID: `SEO.404`**
> Title: Page not found | Ascent
> Description: The requested page could not be found.

**ID: `SEO.editor_demo`**
Context: New in v53. A title and nothing else, on purpose: the page is kept out of search
results, so there is no summary line to write, and it has no social-card tags because it is
not meant to be shared.
> Title: Program Mapper editor demo

---

# J. Image descriptions

Read aloud by screen readers in place of each image. Nobody sees these, but they're the
difference between a usable page and an unusable one for blind visitors. They'll all
need rewriting once real photographs replace the placeholder illustrations — describe
what's actually in the photo. The deck's note on the hero stands: a graphic mark, not a
stock photo of people at a whiteboard.

**ID: `ALT.home`**
> Hero: Stylised mountain ridge with a rising line of plotted data points
> In-brief block: Illustration of an evaluation team and program staff working at one table

**ID: `ALT.programs`**
Context: Cards 1–4 describe real screenshots since v13, so they say what the image shows
rather than naming an illustration. The sample data in the screenshots (a mentoring and
employment program) is not described — it is example data, not a client result. The four
"detail" illustrations went with the phase detail sections in v74.
> Card 1: Logic model linking a program's inputs and activities through its outputs to short-, medium- and long-term outcomes
> Card 2: Data lineage view tracing each number in the model back to the data series it comes from
> Card 3: Analysis of one program activity: its trend over time, what moves it, its sensitivity to inputs and the assumptions it rests on
> Card 4: Scenario dashboard showing every indicator in the model under a chosen funding scenario

**ID: `ALT.home_phases`**
Context: New in v27. The three phase-card screenshots on the home page, which are the same
screenshots as `ALT.programs` cards 1–3, so the wording matches it.
> Thumbnail 1: Logic model linking a program's inputs and activities through its outputs to short-, medium- and long-term outcomes
> Thumbnail 2: Data lineage view tracing each number in the model back to the data series it comes from
> Thumbnail 3: Analysis of one program activity: its trend over time, what moves it, its sensitivity to inputs and the assumptions it rests on

**ID: `ALT.home_tools`**
Context: New in v46. The three tool-view cards under the phase cards on the home page.
> Card 1: Stakeholder map showing ten stakeholders as shapes, grouped by type, with labelled links such as funds, governs and delivers to
> Card 2: Policy and practice timeline for three topics, showing the rule in force today beside proposed changes that can be included in a projection
> Card 3: Logic model from inputs to long-term outcomes with each link colored by strength of evidence, above a library of sources and a list of assumptions

**ID: `ALT.demo`**
Context: New in v16. Not an image: the name a screen reader announces for the embedded
app on the Demo page, before reading the app itself.
> Embedded app: Program Mapper demo

**ID: `ALT.editor_demo`**
Context: New in v53. Not an image: the name a screen reader announces for the embedded
editor on the unlisted Editor demo page (§K), before reading the app itself.
> Embedded app: Program Mapper editor demo

---

# K. Editor demo (unlisted)

`editor_demo.html` — the Demo page's app with editing switched on. **New in v53.** Nothing
on the site links here, it is kept out of search results, and it is reached only by typing
`/editor_demo` after the site's address. It has the same header and footer as every other
page, so §A applies to it. As on the Demo page, the app is hosted separately and shown in a
frame, so nothing inside the frame is covered here. The editor is a second build of the
app, served beside the view-only one rather than switched on in it; the Demo page still
shows the view-only app.

## K1. Page banner

**ID: `EDITOR.HERO.h1`**
Context: The Demo page's heading with "editor" added, so the two can be told apart in a tab
or a screenshot.
> Program Mapper editor

## K2. The editor

The app in the same bordered frame as the Demo page, the full width of the page and 720px
tall, with the same small print on the left and a link on the right.

**ID: `EDITOR.EMBED.note`**
Context: The same two sentences as `DEMO.EMBED.note`, and for the same reason: the sample
program is fictional, and the tool gets cramped on a phone. Its own block so either page can
be reworded without the other following.
Fits: 1–2 lines.
> The program and figures in the demo are fictional. The application works best on a large screen.

**ID: `EDITOR.EMBED.link`**
Context: Arrow link. Opens the editor on its own in a new tab, at full window size.
> Open the editor in a new tab

---

# L. Download

`download.html` — the installers for Ascent Mapper, the desktop app. **New in v63.** The
files are not on this site: each button goes straight to a file in a release in the app's
GitHub repository (Ascent-Evaluation/ascent-mapper), so nothing about the installers is
covered here, only the page that points at them. It is last in this document so that no
existing page letter moved; on the site it is the sixth nav item, after Demo. It was drafted
from the app's README and release notes and reworded by you in v65.

## L1. Page banner

**ID: `DOWNLOAD.HERO.h1`**
Context: Since v65 the heading does not name the app, so no visible text on the page does:
the name appears only in the browser-tab title and description (`SEO.download`) and in the
downloaded file. That sidesteps the "Ascent Mapper" / "Program Mapper" question for now.
Fits: 3–4 words, one line.
> Download the app

**ID: `DOWNLOAD.HERO.lead`**
Context: What the app is and does, in your v66 wording: it supports "our evaluation process"
and names four things it does (build logic models, aggregate evidence against each link,
monitor external policy developments, project change across all metrics), which makes it a
list in one line rather than a description. The first draft, from the app's README, said
"building and reading program logic models, with the evidence behind each link and the
people around the program".
Fits: 2–3 lines, ~215 characters, the current length: three lines on desktop.
> The desktop app that supports our evaluation process: build program logic models, aggregate evidence and map it to each link, monitor the effects of external policy developments and project change across all metrics.

## L2. The installers

Three cards in a row, one per installer, each with one button; the last section on the page.
Anchored at `#installers`. Nothing picks for the visitor: a web page cannot reliably tell an
Apple-silicon Mac from an Intel one, so they choose. Since v68 each button downloads its
installer from the newest release on GitHub, pre-releases included: the page looks the
release up as it loads, so the buttons follow each new release with no edit.

**ID: `DOWNLOAD.CHOOSE.intro`**
Context: The eyebrow names the release the buttons download. Since v68 the page fills in the version number from GitHub as it loads, so it
follows each release on its own. The number written here is the fallback, shown (with
that release's files behind the buttons) only if GitHub can't be reached; there is no need
to change it for each release. The lead ("Each button downloads the installer
from our GitHub releases.") came off in v65 and the field is left empty; type one there and
hand the file back to bring it back.
> Eyebrow: Version 1.0.0
> Heading: Choose your operating system
> Lead: 

**ID: `DOWNLOAD.CHOOSE.cards`**
Context: One card per installer, in this order. Each has the kind of computer, one line on
what it needs, and the button. The requirements are the README's. The buttons name the
computer rather than saying "Download", so the three can be told apart by a screen reader
that lists the links alone. The buttons sit level however long the line above them is.
Each button starts the download of its installer from the newest release.
The Apple silicon line says "Requires" where the other two say "Needs"; kept as you wrote it.
Fits: Headings up to ~28 characters, button labels up to ~28, or they wrap in a narrow card.
> Heading: Apple silicon Macs
> Body: Requires macOS 12 Monterey or later.
> Button: Download for Apple silicon
>
> Heading: Intel Macs
> Body: Needs macOS 12 Monterey or later.
> Button: Download for Intel Macs
>
> Heading: Windows
> Body: Needs 64-bit Windows 10 or later.
> Button: Download for Windows

---

*End of document — 8 pages, 12 sections. Edit and send back.*
