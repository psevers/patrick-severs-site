# Design, positioning, and content decisions (grilling session, 2026-07-17)

- **Fresh build.** Three prior artifacts (`patrick-gtm-record/`, `patrick-builder-record/`, `patrick-agent-profile/` under `~/Personal/`) are source material only, not a base to extend.
- **Structure:** single-page home covering three pillars (GTM Leadership, Agentic Systems, Products Built), each linking to a full deep-dive page. Career timeline is a compact section on the home page, not a fourth deep-dive.
- **Positioning:** hero leads with the hybrid claim itself ("GTM leader who operates like a technical founder"), not GTM-first or builder-first.
- **Design:** terminal/markdown-native aesthetic — monospace accents (JetBrains Mono), IBM Plex Sans body, custom workflow/pipeline diagrams, technical-green accent. Light mode primary, dark mode toggle (persisted via localStorage).
- **No longer employed at G2i** — fully public, search-indexed, no visibility gating needed. Standard confidentiality obligations to a former employer still apply.
- **Contact:** email (pvsevers@gmail.com) + LinkedIn (linkedin.com/in/pvsevers) + booking link for "book time" (Google Calendar at v1; Calendly since 2026-09-08, see below).
- **Domain:** patricksevers.com — registered via Cloudflare (2026-07-17). **Hosting:** Cloudflare Pages (same account). **Analytics:** Cloudflare Web Analytics (privacy-friendly, no cookie banner).
- **Downloadable PDF resume** alongside the site (one-page, ATS-friendly).
- **Personal content:** softball-recruiting-tool story stays in, kept specific (not anonymized) — Patrick's explicit call.
- **Headshot:** in contact/footer section only, not the hero.
- **Timeline:** ship v1 fast; career-progression content keeps being refined after launch.

## Content sources
- Career history (companies/titles/dates back to 1999): `~/Downloads/Profile.pdf` (LinkedIn export).
- Headshot: `src/assets/images/headshot.png`.
- Redaction-sensitive source: `patrick-gtm-record/patrick-severs-gtm-record.html` — see the confidentiality rail in `AGENTS.md`.

## Redesign, 2026-09-08 UTC (interview session; full spec in `docs/redesign-2026-09.md`)

- **Primary bet:** Head of GTM / VP Revenue. **Wedge:** Human Data. The site argues the builder/GM claim explicitly (the GLG-style final-round loss was a GM-breadth objection, not a GTM one).
- **Hero:** "I build the AI training-data business inside your company, walk it into the frontier labs, and build the team that delivers."
- **Point of view:** presence and proof win the deal; agents do the operating work so a small team can afford to be present.
- **New pages:** `human-data-operating-layer.html` (Patrick's own final-round blueprint, genericized: no company, no interviewer names, no network size, their economics abstracted) and `agent-company.html` (named, live, dated case study). `how-i-operate.html` absorbs the old Agentic Systems and Products pages; those two files are now meta-refresh redirects.
- **Cut:** Founding Strategic AE. Consulting is shown as current work, not offered as a service. *The AI-Driven Leader* (Woods) gets one line of credit inside the rules, not a page.
- **Design:** "working whiteboard". Editorial/executive type (Fraunces, Source Sans 3), Caveat for whiteboard annotations only, IBM Plex Mono for receipts. Blue marker accent replaces technical green. Paper ground with faint grid. Dark mode kept as a dark whiteboard.
- **Pending Patrick / founder OK before deploy:** Agent Company pilot count and the "no decision on what to sell" framing; whether to link their site.

## 2026-09-08: copy pass and objections block
- Booking link is now https://calendly.com/pvsevers/30min; button copy "Book 30 min" on every page (30 minutes stated as a risk reducer).
- Home page gains a mid-page CTA after the three receipts and an objections section (four objections, each linked to its receipt page) between testimonials and contact. Adapted from a 14-section sales-page framework; the salesy sections (consequences, urgency, false solutions) were rejected as off-brand.
- Word-level deslop across all six pages: intensifier "real", "on purpose/deliberate", "stood up", "AI leverage" cut or varied. Hero headline, figures, and open rulings untouched.

## 2026-09-09: objection 5 and Agent Company hold
- Home objections block gains a fifth card, "Why did you leave G2i?": the company pivoted to a technology focus built on agentic orchestration and brought in new leadership to drive it; Patrick left July 2026. Patrick's own framing, no further detail.
- Objections lede ("I've lost a final round on one of these") stays. Objection 1's "hired into each" (incl. finance) confirmed accurate.
- **Agent Company storyline is on hold.** Patrick is not convinced by the case-study framing as written. Needs its own grill session before the page, the home receipt, and objection 3 are treated as final. Founder OK items (pilot count, link, "no decision on what to sell") remain open under this.
- `scripts/site-gen/` is committed; `AGENTS.md` now says edit the generator, never `src/`.
- Career page, Braintrust: "on intentionally thin margins" (Patrick: the thin margins were the point, not a hazard).
- How I operate keeps six rules; spec updated from five. "Priced to learn" deferred into the Agent Company hold.

## 2026-09-09: Agent Company storyline rulings (grill session; hold lifted)
- **Frame:** the Agent Company page is **working notes**, not a case study. A dated day-45 snapshot that proves GM breadth in the present tense. Decisions first, numbers last.
- Eyebrow: "Live engagement · working notes · day 45". Headline: "Diagnose, decide what to sell, build the layer, get in the room." Stat row removed; one mono receipt line under the headline.
- Section 02 lede is the thesis: the product decision came out of the sales motion, not ahead of it.
- Day one, offer: "The platform could do many things; nobody had picked which one to sell first."
- CRM is "set up," never "built": set up in week one, agents did the wiring and the migration off the stitched stack. *Assumption, not confirmed by Patrick: the CRM is Attio configured by agents.*
- Numbers kept: 5 demos, 4 paid pilots. "10 to 15 campaigns per day" dropped everywhere. Pricing is one sentence: paid pilots, priced so the constraint is projects built, not deals closed. "Priced to learn fast" retired.
- "What's not proven yet" stays without the "next 45 days" tail. The update pledge is gone; the date stays.
- Home objection 3 reworded around the three decisions made in 45 days. *Assumption: title keeps "consulting."*
- Presence receipt stays qualitative, no number. How I operate CRM card: speed and method, not the artifact.
- Founder OK: three yes/no asks (name and link; the 5/4 numbers; the "nobody had picked" sentence), sent by Patrick as three lines. Fallback on any no: unnamed ("an agent startup for small-business operations"), numbers kept. Deploy does not wait on the answer.

## 2026-09-09: home page design pass (critic loop)
- Home rebuilt as an editorial dossier: Fraunces for display and text, Plex Mono for datelines and labels only; Source Sans and the hand face dropped from the home page; blue accent removed; one 12-column grid at 1060px.
- Structure: hero with bleed portrait, essay, operating-layer table plus a numbers ledger, three receipts index, one pull quote, six rules, objections, unruled close with colophon. Card grids, banded backgrounds, stat tiles, and the mid-page CTA are gone. Two testimonials moved to the G2i record page.
- A fresh Fable 5.1 design critic scored each round; scores plateaued at 5.5 to 6 of 10 across twelve rounds with contradictory advice between rounds. Loop paused pending Patrick's direction.


## 2026-09-09: imagery and shader pass (critic loop resumed)
- Patrick's call: keep the critic loop running; add personality with generated imagery plus shader/3D effects; verify frame-by-frame in the browser.
- Images come from Codex CLI with gpt-6-astra on high. One visual language for the set: two-colour risograph, near-black plus burnt orange (#c2410c) on warm paper, no text. The spot colour is back with three jobs: nav CTA, footer mail, the orange in the plates.
- Hero portrait is a generated riso plate drawn from the headshot (faithful likeness), bleeding to the nav rule and the right edge. `riso.js` (WebGL, no library) adds pointer-driven misregistration and grain; reduced motion gets one frame; no WebGL gets the plain image. Dark mode shows the print untransformed (an inverted portrait reads as a negative).
- Four plates: river-into-four (G2i), building with a floor craned in (Operating Layer), desk from above with an orange paper boat (Agent Company), round table with one orange chair (The read). Plates tilt toward the pointer with a sheen.
- Critic scores: 5.5 (baseline), then 5.5, 6.0, 5.5 with imagery. Round 3 repeated: plate b's engraving style breaks the set, mono eyebrow on every section, stats numerals need one baseline, hero disc clipped, and hero tracking too tight (loosened to -0.035em / 0.96). Applied only the signals that repeated: hero bleed, one measure, one label system, stats at display scale, pull quote down and hung, quieter receipts. Table tint and numbered eyebrows were asked for in one round and penalised in the next; treat single-round advice as noise.
- Round 4 changes (applied the three signals that repeated): plate b regenerated flat (five plain floors, an orange slab lowered by a crane; the engraved cross-section broke the set). Running heads are now a display-scale numeral (Fraunces, opsz 144) with the mono label as its caption; above 1300px the numeral hangs in the left margin so the caption stays flush with the text column. The pull quote section no longer counts, so the numerals run 01 to 04 without a gap. Ledger rows align on the baseline and the percent sign no longer grows the line box, so 4 and 7 sit on the same line as 59% and 122%.

## 2026-09-09: subpage plates (Operating layer, Agent Company, How I operate, Career)
- Home page frozen by Patrick's ruling; the subpages got the same system: page hero with a plate beside the lede, chapters as `section.numbered-head` with the margin numeral and mono running head, a display-scale deck, one measure, one label style. The legacy whiteboard SVGs are gone from these four pages; `gtm-leadership` keeps its two by Patrick's call, and its hub idea (one role, many functions) became the fleet plate on How I operate.
- Diagram content was kept as type, not deleted: the operating-layer table (`.ftable`), the owners-and-KPIs table, six-step motions and four-gate lists (`.steps`), the scoreboard (`.score`). Plates are metaphors; the tables carry the facts.
- New plates, all gpt-6-astra via Codex CLI, same style block as the home set, one orange element each: e six chairs on one orange cable (the team), f lecture hall with one orange figure in the aisle (the motion), g conveyor through four gates with one orange tile (quality), h orange tent on a black roof (startup inside a mature business), i three shop doors and one orange awning (Agent Company, the product decision), j conductor with an orange baton (How I operate hero), k orange hub with seven black squares (the fleet), m staircase with an orange flag (Career). Rejected: a row of black blocks, an open door with an orange chair, a magnifying glass over a grid, a warehouse with one lit window, a demo table with a price tag, a boss pointing at a row of workers, a winding road with milestones that read as headstones.
- Plate ground fix. The critic's "pasted rectangle" had two causes. (1) `perspective` on the `.plate` wrapper isolated the image so `mix-blend-mode: multiply` never reached the page; perspective now lives in the image transform. (2) Plate paper was warmer and darker than the page. `retone.py` (scratchpad) white-balances each plate's paper mean to just above `#f6f4ee`, so multiply plus `brightness(1.05)` clamps paper to the page colour exactly (measured 246/244/238 both sides). Plates a to d were retoned from the installed JPEGs; the originals did not survive the old scratchpad.
- Dark mode: plates blend with `lighten` after invert and `contrast(1.25)`, so inverted paper falls below the page and disappears (measured 21/23/26 both sides). The brownish box from hue-rotating warm paper is gone.
- `gen.py` now stamps `body.home` or `body.sub`; the subpage deck rule is scoped to `body.sub` so the home page renders exactly as it did.
- Video loops not started. Pipeline plan unchanged from the design handoff: fal.ai image-to-video from each still, ffmpeg loop and encode, `<video>` with the JPEG as poster and reduced-motion fallback. Waiting on Patrick's go before any paid generation.

## 2026-09-09: plate loops (video)
- Every plate becomes a short muted loop; the JPEG stays the source of truth as poster, in-video fallback, and the whole experience under reduced motion (main.js swaps the video for its inner img so the still renders exactly).
- Generator: gen.py wraps a plate img in a video wherever `src/assets/video/plate-<x>.mp4` exists, so pages keep referencing the still. CSS plate rules cover img and video; the light multiply and dark lighten chains measure identical paper both sides (246/244/238 and 21/23/26).
- Model: Kling v3 pro on fal, chosen by Patrick without a bake-off. LTX and Wan also support end frames; Seedance was ruled out on price and 720p.
- Recipe (scripts/loops/fal-loop.py): no end frame, one explicit motion line per plate, cfg 0.75, 5 s, then trim to 4 s and ping-pong to 8 s. Sending the still as both start and end froze the clip twice; letting Kling run free and mirroring the swing was the fix and costs nothing extra.
- Accepted first pass: b crane block swings, c boat drifts, d chair scoots, e cable sways, h tent flaps, i awning billows, m flag waves. Rejected: a (contour lines vanished), f (a hatted figure appeared in the crowd), g (the gate row vanished), k (whole wheel rotated and jumped on frame one). j never ran (balance exhausted). Their prompts now pin the black ink explicitly.
- Cost: $0.112 per second, about 56 cents a clip; 13 runs so far.

## 2026-09-09: new direction, the first-load type moment (dither reveal)
- Patrick's ruling on the plates: "these aren't good enough and don't really make the page stand out." The home hero (plate d) and the building (plate b) stay; the other ten are throwaways, no further generation. The gridboard (32px hairline grid from `1b64079`) is back on the body, light and dark tokens.
- References he named (onepagelove reviews of Aaron Sananes, Refined, David Bastian) share one thing: textured minimal ground, type as the star, one memorable moment on first load, no illustration system. Rulings: no sound; memorable on first load, scroll only enhances; the home hero image stays as is.
- Direction chosen from four options: a site-wide type moment every page inherits (over type-only pages, one bespoke interactive object per page, or a thinner plate system). Three reveals were prototyped on the real pages behind `?variant=`: A unscramble (glyphs churn and settle), B dither (a hard-thresholded noise mask thickens into solid type, edges displaced by grit), C misregister (orange plate slides into register under the black, a hair stays). Patrick picked B. The variant file is not in the repo; the winner lives in `main.js`.
- Mechanics: one SVG filter per element (feTurbulence, luminanceToAlpha, a linear then discrete alpha transfer as the mask, feDisplacementMap for grit, feComposite in). Eyebrow and h1 on load after `document.fonts.ready`, lede and hero-sub fade up, every h2 outside the hero gets a shorter pass on entering the viewport. Safety nets: every element unhides after 4 s regardless, and each filter tears itself down after its run. Under reduced motion nothing runs, so the frozen home render is untouched.
- Open, not ruled: whether the subpage hero and chapter plates (e to m) come out now that the direction is type-first; the five throwaway loop files are still on disk pending an explicit delete.


## 2026-09-09 20:48 UTC: whiteboards return alongside selected loops
- Patrick asked to keep the home hero and building, simplify the other heroes, retain some loops, and revisit the useful whiteboard diagrams, including possible Kling animation.
- Implementation judgment for this pass: Agent Company, How I Operate, and Career get type-only heroes. The home stays as it was; Operating Layer keeps the building loop. Existing chair, boat, team cable, awning, and rooftop tent loops remain in context. The flag stays available in the gallery. No media files were deleted.
- Restored the relationship motion and quality-flow whiteboards to Operating Layer, and the strategy/fleet/human-gate loop to How I Operate. Existing text lists remain as a readable alternative. Fleet package count omitted because the current page only establishes that each service has tests.
- All original diagrams are available in a local review gallery. The archived Agent Company timeline contains superseded CRM and campaign-volume copy; it is reference only, not restored to the site.
- Loop selection and diagram animation remain open for visual review. No new Kling generation was run. This supersedes the earlier direction to remove the illustration system entirely and the blanket throwaway designation for the remaining loops.


## 2026-09-09 21:00 UTC: GTM leadership leads the site
- Patrick: the site focuses too heavily on Human Data. Lead with GTM expertise, leadership, and thought leadership; keep the homepage visual direction, shorten the hero and sub-hero.
- Six-page grouping for review *(implementation judgment)*: Home, Previous Performance, How I Operate, Human Data, Now, Career. This consolidates the overlapping employment/client/engagement ideas without adding thin pages. Existing URLs remain stable.
- Draft hero: "I turn strategy into revenue." Sub-hero: "I lead go-to-market teams and build the systems that help them win." Alternative copy directions for later review: "Build the team. Grow the business." emphasizes leadership; "I build the team behind the growth." emphasizes people. These are proposals, not Patrick's approved wording.
- Home now leads with buyer trust, team ownership, and AI operations. Its table covers those capabilities. Full Human Data content and all five original whiteboards live on the dedicated page. G2i anchors Previous Performance; earlier work uses claims already present in Career. Agent Company stays a separate dated current-work page.
- Page titles, descriptions, navigation, footer invitation, redesign spec, and product-marketing context updated to the new positioning. Resume PDF and social preview image have not been refreshed. No new claims, paid generation, commit, or deployment.
- Verification: all six pages fit a 390px iframe viewport with no document overflow. Desktop home/nav and restored diagrams checked in Chrome. Local links and fragments resolve. Mobile portrait bleed and table overflow corrected; wide evidence tables scroll within their own region.


## 2026-09-09 21:09 UTC: AI as a thought partner, clearer projects, portrait repair
- Patrick asked for the six rules to emphasize the AI-driven leader approach, context, interviewing, better questions, and AI enhancing his judgment. Replaced the engineering-policy emphasis on Home and How I Operate with six practices: question, context, interview, challenge, action, ownership. Example prompts are proposals, not claimed quotations from past sessions.
- Split projects into business and personal/family groups. The Forge sits in personal learning *(judgment)*, based on the existing "to learn in public" description.
- Rebuilt the fleet whiteboard with wider boxes, shorter labels, and space around the human-approval gate. Kept the feedback pulse.
- Portrait crop cause: the tall source image covered a wide, shallow area after the hero copy shrank. The portrait now has an independent 2:3 desktop aspect ratio, without the horizontal bleed, and top-aligned crop on mobile and in the shader.
- Previous Work gains the existing round-table loop beside the headline *(image selection judgment)*. No new generation.


## 2026-09-09 21:20 UTC: whiteboard lettering for the home hero
- Patrick rejected the Fraunces hero type in a preview annotation and asked for a whiteboard/collaboration feel. The home headline now uses the already-loaded Caveat handwriting face, weight 600, natural spacing, and an orange underline on revenue. This overrides the editorial-serif direction for this headline.


## 2026-09-09 21:22 UTC: whiteboard typography across the site
- Patrick extended the hero-font rejection to the ledger numbers and the remaining fonts. Replaced Fraunces and Plex Mono with Caveat for headings and numbers, and Nunito Sans for prose, navigation, labels, and diagram detail. Code samples retain a system monospace. Removed Fraunces optical-axis settings and tight tracking.
- Font selection is an implementation judgment for preview. This supersedes the earlier editorial-serif typography direction across all pages.


## 2026-09-09 21:23 UTC: Previous Work hero uses the reversed fork
- Patrick selected the fork illustration for the Previous Work hero, horizontally reversed, replacing the reused round-table loop. The reversal is scoped to this placement; the source asset remains unchanged.


## 2026-09-09 21:57 UTC: visible visitor theme toggle
- Patrick requested an optional light/dark toggle for visitors. It is visible in the shared navigation on desktop and mobile, labels the destination mode, and saves each visitor’s selection. System preference applies until they choose.
- Verified both directions, keyboard activation, reload persistence, and mobile fit across six pages. Fresh standards and spec reviews found no blockers.
