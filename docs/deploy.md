# Deploy and analytics runbook (v1 shipped 2026-07-17)

- Cloudflare Pages project: `patrick-severs-site` (account: pvsevers@gmail.com).
- Live at: https://patricksevers.com (custom domain) and https://patrick-severs-site.pages.dev (always-on fallback).
- Redeploy: `npx wrangler pages deploy src --project-name=patrick-severs-site` from the project root (requires `wrangler login` once per machine).
- Cloudflare Web Analytics: enabled via automatic setup (same-account hostname), no manual snippet needed.
- Resume PDF regenerated via `python3 scripts/build_resume.py` (writes `src/assets/pdf/patrick-severs-resume.pdf`).

## Open items (as of 2026-07-17)
- Full career-progression color/context from Patrick (companies/dates sourced from his LinkedIn PDF export; the "why" behind each era still needs his input).
- Mobile-viewport spot check on a real phone.
