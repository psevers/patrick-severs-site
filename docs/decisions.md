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
