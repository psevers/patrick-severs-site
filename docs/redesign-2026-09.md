# Redesign spec: "working whiteboard" (interview session, 2026-09-08 UTC)

**Status:** draft. Decisions below were made by Patrick in the interview; judgment calls by Claude are marked *(judgment)*.

## Positioning (updated 2026-09-09 21:00 UTC)
- Patrick's ruling: lead with go-to-market expertise, leadership, and point of view. Human Data is one area of expertise and gets a dedicated page; it does not define the whole site.
- Keep the homepage's editorial design, portrait, grid, and type reveal. Shorten the headline and supporting copy substantially.
- Current draft hero *(judgment)*: "I turn strategy into revenue." Supporting line: "I lead go-to-market teams and build the systems that help them win."
- The homepage point of view covers buyer trust, team ownership, and AI doing operating work under human judgment. Its evidence table covers GTM, leadership, and AI operations. Human-data delivery detail belongs on the Human Data page.
- Earlier Human Data-first positioning and hero are superseded by this ruling. Historical interview context remains in `docs/decisions.md`.

## New content (Patrick's rulings)
- **Human Data Operating Layer** page: the GLG blueprint, genericized. No GLG name, no interviewer names or quotes, no "2M experts", the $10M/$50M/$100M rows abstracted to "market-norm ~30% gross margin". Six sections, same structure as the deck.
- **The Agent Company** working notes (ruled 2026-09-09, replacing the case-study framing): named, linked, a dated day-45 snapshot. Decisions first, numbers last. Day one: no CRM, no lead source, stitched outreach tooling, and a platform that could do many things with nobody having picked which one to sell first. Shipped: a CRM set up in week one with agents doing the wiring, a local-first lead motion, agent-run outbound, demos and solution landing pages. Result: 5 demos, 4 paid pilots; local and in-person beat email on response rate. Paid pilots priced so the constraint is projects built, not deals closed. Founder OK (name and link, the 5/4 numbers, the "nobody had picked" sentence) is asked as three yes/no lines; deploy does not wait on it.
- **How I operate**: six practices for AI as a thought partner: start with the right question; give it the context; ask it to interview me; challenge my thinking; turn insight into action; own the decision. Credit Geoff Woods and *The AI-Driven Leader* as an influence. Example prompts are labelled as examples, not past events. Business projects and personal/family projects have distinct groups.

## Structure
The home links directly to each primary page. Existing URLs remain stable; the page names and emphasis change. The overlapping previous clients, employment, and engagements ideas are grouped by purpose *(judgment)*.

| Page | Existing URL | Purpose |
|---|---|---|
| Home | `/` | GTM leadership, point of view, and routes into the evidence |
| Previous performance | `/gtm-leadership.html` | Detailed G2i record, earlier engagements, clients in context, team testimonials |
| How I operate | `/how-i-operate.html` | Leadership rules, AI operations, fleet diagram, projects |
| Human Data | `/human-data-operating-layer.html` | Complete blueprint, original whiteboards, tables, and selected loops |
| What I’m working on now | `/agent-company.html` | Agent Company, dated day-45 working notes |
| Career overview | `/career.html` | Employment chronology and transitions |

- Header order: Previous work, How I operate, Human Data, Now, Career, Book 30 minutes. The name links home.
- Home order: compact hero, point of view and evidence, work index, testimonial, operating rules, hiring questions, contact.
- Performance links to career for dates and current work for the ongoing engagement. Human Data is linked as a specialization. Home links to the team's perspective and the operating fleet.
- Resume remains the primary low-friction action; book time is the direct conversation path. Existing legacy redirects remain intact.

## Design (Patrick's ruling: editorial/executive, whiteboard visual system)
- Off-white paper ground with faint grid. Serif display (Fraunces), humanist sans body (Source Sans 3), a handwriting face (Caveat) for whiteboard annotations only, monospace (IBM Plex Mono) reserved for receipts and data.
- One accent: blue marker. Sticky-note yellow for working notes. Diagrams are clean, slightly hand-drawn line work (architectural, not cartoon). Every page carries at least one whiteboard.
- Dark mode retained as a dark whiteboard.
- Guardrail: if it reads as a 2022 startup landing page, it failed. Type stays executive.
- Superseded 2026-09-09 (see `docs/decisions.md`, the 2026-09-09 design blocks): the whiteboard system gave way to an editorial dossier. Fraunces for display and text, Plex Mono for labels and datelines; Source Sans and Caveat dropped. One spot colour, burnt orange, with three jobs: nav CTA, footer mail, the orange element in each plate. Imagery is a set of two-colour risograph plates (near-black plus orange on the page paper), one per chapter, generated with gpt-6-astra and retoned to the page. Every page opens with a plate beside the lede and runs chapters under a margin numeral. `gtm-leadership` still carries two whiteboard SVGs by Patrick's call. Diagram facts live in tables and step lists, never only in a picture.

## Confidentiality
- `AGENTS.md` rail still governs. GLG is never named on the site. The blueprint is Patrick's own framework; the inputs (network size, interviewer quotes, their economics) are abstracted.

## Out of scope this pass
- Resume PDF regeneration (headline should follow the new positioning; `scripts/build_resume.py` still says the old one).
- OG image redraw in the new visual language.

## Visual integration, 2026-09-09 21:00 UTC
- All five original Human Data whiteboards are back on that page. The restored motion and quality diagrams have expandable text alternatives. Layer/team tables and the scoreboard remain available. Building, cable, and tent loops remain alongside the relevant chapters.
- How I Operate keeps the fleet diagram and its existing feedback pulse. Previous Performance keeps both G2i whiteboards. The home and Now pages retain their existing loops. No new generated animation in this pass.
- Current design is the editorial system with selected illustrations and useful whiteboards, superseding the earlier every-page-plate requirement.

## Current typography, 2026-09-09 21:22 UTC
Patrick rejected the remaining editorial fonts after the home hero changed. The current preview uses Caveat for headings and numbers and Nunito Sans for body text and labels. Diagram detail stays sans serif for legibility; code samples use system monospace. This supersedes the Fraunces/Plex typography described in earlier design history above.
