# patrick-severs-site

Personal marketing/portfolio site for Patrick Severs — job-search-facing, replaces a traditional resume.

## Decisions (from grilling session, 2026-07-17)

- **Fresh build.** Three prior artifacts (`patrick-gtm-record/`, `patrick-builder-record/`, `patrick-agent-profile/` under `~/Personal/`) are source material only, not a base to extend.
- **Structure:** single-page home covering three pillars (GTM Leadership, Agentic Systems, Products Built), each linking to a full deep-dive page. Career timeline is a compact section on the home page, not a fourth deep-dive.
- **Positioning:** hero leads with the hybrid claim itself ("GTM leader who operates like a technical founder"), not GTM-first or builder-first.
- **Design:** terminal/markdown-native aesthetic — monospace accents (JetBrains Mono), IBM Plex Sans body, custom workflow/pipeline diagrams, technical-green accent. Light mode primary, dark mode toggle (persisted via localStorage).
- **Confidentiality policy:** name G2i explicitly. Keep real ratios/percentages (122% growth, 2.7×, 21.7× EBITDA). Strip exact dollar figures from the *private* GTM record, all named prospects (Cohere, Mistral, DeepMind, Amazon AGI) and vendors cut. Exception: figures/clients Patrick already made public himself on LinkedIn (the "$10-15M → targeting $80M" framing, and Microsoft/Meta/Coinbase/Discover as enterprise clients) are fair game since they're already disclosed under his own name.
- **No longer employed at G2i** — fully public, search-indexed, no visibility gating needed. Standard confidentiality obligations to a former employer still apply regardless of employment status.
- **Contact:** email (pvsevers@gmail.com) + LinkedIn (linkedin.com/in/pvsevers) + Google Calendar booking link (https://calendar.app.google/DJfJDwJz4SbvFGMg6) for "book time."
- **Domain:** patricksevers.com — registered via Cloudflare (2026-07-17).
- **Hosting:** Cloudflare Pages (same account as domain).
- **Analytics:** Cloudflare Web Analytics (privacy-friendly, no cookie banner).
- **Downloadable PDF resume** alongside the web site (one-page, ATS-friendly).
- **Personal content:** softball-recruiting-tool story stays in, kept specific (not anonymized) — Patrick's explicit call.
- **Headshot:** in contact/footer section only, not the hero.
- **Timeline:** ship v1 fast; career-progression content can keep being refined after launch.

## Content sources

- Career history (companies/titles/dates back to 1999): `~/Downloads/Profile.pdf` (LinkedIn export).
- Headshot: `src/assets/images/headshot.png`.
- Redaction-sensitive source: `patrick-gtm-record/patrick-severs-gtm-record.html` — do not copy exact dollar tables, named prospects, or vendor names from this file.

## Stack

Static HTML/CSS/JS, no build step. Deploy target: Cloudflare Pages.
