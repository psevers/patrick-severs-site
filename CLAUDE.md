# patrick-severs-site

Personal marketing/portfolio site for Patrick Severs — job-search-facing, replaces a resume. Live at patricksevers.com (Cloudflare Pages, account pvsevers@gmail.com) + patrick-severs-site.pages.dev fallback.

## Content & positioning

- Single-page home: 3 pillars (GTM Leadership, Agentic Systems, Products Built), each linking to a deep-dive page. Career timeline is a compact home-page section, not a 4th deep-dive.
- Hero leads with the hybrid claim ("GTM leader who operates like a technical founder"), not GTM-first or builder-first.
- Design: terminal/markdown-native — JetBrains Mono accents, IBM Plex Sans body, custom workflow diagrams, technical-green accent. Light mode primary, dark toggle (persisted via localStorage).
- Softball-recruiting-tool story stays in, kept specific — Patrick's explicit call. Headshot: contact/footer section only, not the hero.
- Prior artifacts (`patrick-gtm-record/`, `patrick-builder-record/`, `patrick-agent-profile/` under `~/Personal/`) are source material only — not a base to extend. `patrick-gtm-record/patrick-severs-gtm-record.html` is redaction-sensitive (see Confidentiality below).

## Confidentiality (binding — check before adding any G2i content)

- Name G2i explicitly. No longer employed there — fully public, no visibility gating needed — but standard confidentiality obligations to a former employer still apply.
- Real ratios/percentages OK (122% growth, 2.7×, 21.7× EBITDA). Strip exact dollar figures, named prospects (Cohere, Mistral, DeepMind, Amazon AGI), and vendor names from the private GTM record.
- Exception: figures/clients Patrick already made public himself on LinkedIn are fair game — the "$10-15M → targeting $80M" framing, and Microsoft/Meta/Coinbase/Discover as enterprise clients.

## Contact

Email pvsevers@gmail.com · LinkedIn linkedin.com/in/pvsevers · booking link https://calendar.app.google/DJfJDwJz4SbvFGMg6

## Content sources

- Career history (1999–present): `~/Downloads/Profile.pdf` (LinkedIn export).
- Headshot: `src/assets/images/headshot.png`.

## Stack & deployment

Static HTML/CSS/JS, no build step.

- Redeploy: `npx wrangler pages deploy src --project-name=patrick-severs-site` from the project root (needs `wrangler login` once per machine).
- Cloudflare Web Analytics: auto-enabled (same-account hostname), no manual snippet.
- Resume PDF: `python3 scripts/build_resume.py` → writes `src/assets/pdf/patrick-severs-resume.pdf`.
- Still open: full career-progression color/context from Patrick (companies/dates sourced from his LinkedIn PDF export; the "why" behind each era still needs his input), and a mobile-viewport spot check on a real phone.

## Agent skills

- **Issue tracker** — GitHub Issues via the `gh` CLI. See `docs/agents/issue-tracker.md`.
- **Triage labels** — `needs-triage`, `needs-info`, `ready-for-agent`, `ready-for-human`, `wontfix`. See `docs/agents/triage-labels.md`.
- **Domain docs** — single-context: `CONTEXT.md` + `docs/adr/` at repo root. See `docs/agents/domain.md`.
