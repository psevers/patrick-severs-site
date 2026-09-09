# Redesign spec: "working whiteboard" (interview session, 2026-09-08 UTC)

**Status:** draft. Decisions below were made by Patrick in the interview; judgment calls by Claude are marked *(judgment)*.

## Positioning (Patrick's rulings)
- **Primary bet:** Head of GTM / VP Revenue. **Wedge:** Human Data. **Claim:** the builder/GM who stands up an AI-native service line (human data for frontier labs) inside a company, walks it into the labs, and builds the team that delivers.
- Evidence that drove it: 3 of 4 live conversations are human-data or AI-ops specific (GLG final round, Kabota Health, Lean Layer). The GLG loss was a GM-breadth objection, not a GTM one. The site must argue the GM claim explicitly.
- **Hero:** "I build the AI training-data business inside your company, walk it into the frontier labs, and build the team that delivers." Proof line: G2i, one staffing line to human data for frontier labs, $10-15M to ~$80M target in three years, margin held.
- **Point of view (recurs three times in the record):** AI-era GTM wins on presence and proof; agents do the operating work so a small team can afford to be present. G2i events = 59% of Q2 2026 leads; GLG blueprint "cold outbound is weak, go where researchers are"; Agent Company local-first beat outbound email.
- **Founding Strategic AE:** cut from the site. **Rev Ops consulting:** shown as current work (proof of being in-market), not offered as a service. **Head of Human Data:** the wedge inside the GTM story, not a separate track.

## New content (Patrick's rulings)
- **Human Data Operating Layer** page: the GLG blueprint, genericized. No GLG name, no interviewer names or quotes, no "2M experts", the $10M/$50M/$100M rows abstracted to "market-norm ~30% gross margin". Six sections, same structure as the deck.
- **The Agent Company** case study: named, linked, 45 days in. Day one: no CRM, no lead source, stitched outreach tooling, no decision on what to sell. Shipped: CRM stood up agentically, local-first lead motion, agent-run outbound (10-15 campaigns/day), demos and solution landing pages. Result: 5 demos, 4 pilots; local/in-person beat email on response rate. *Needs founder OK before publish:* the pilot count and the "no direction on product" framing. Pricing framed as "priced for pilots to learn fast" *(judgment)*.
- **How I operate** section (5 rules, each with a receipt): direct don't do; interview before you task (credit: Geoff Woods, *The AI-Driven Leader*, CRIT); cost is policy; a human approves every send; presence beats outbound. The book gets one line of credit, not a page.

## Structure
- Home: hero → POV → three proofs (G2i record, Operating Layer blueprint, Agent Company) → How I operate → testimonials → contact.
- Pages: `index.html`, `gtm-leadership.html` (reframed as the GM record), `human-data-operating-layer.html` (new), `agent-company.html` (new), `how-i-operate.html` (new; absorbs Agentic Systems + Products, with the 2026 repos as receipts), `career.html`.
- `agentic-systems.html` and `products.html` become redirects to `how-i-operate.html` so inbound links survive *(judgment)*.
- CTA hierarchy unchanged: resume primary, book time secondary.

## Design (Patrick's ruling: editorial/executive, whiteboard visual system)
- Off-white paper ground with faint grid. Serif display (Fraunces), humanist sans body (Source Sans 3), a handwriting face (Caveat) for whiteboard annotations only, monospace (IBM Plex Mono) reserved for receipts and data.
- One accent: blue marker. Sticky-note yellow for working notes. Diagrams are clean, slightly hand-drawn line work (architectural, not cartoon). Every page carries at least one whiteboard.
- Dark mode retained as a dark whiteboard.
- Guardrail: if it reads as a 2022 startup landing page, it failed. Type stays executive.

## Confidentiality
- `AGENTS.md` rail still governs. GLG is never named on the site. The blueprint is Patrick's own framework; the inputs (network size, interviewer quotes, their economics) are abstracted.

## Out of scope this pass
- Resume PDF regeneration (headline should follow the new positioning; `scripts/build_resume.py` still says the old one).
- OG image redraw in the new visual language.
