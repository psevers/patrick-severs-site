# Deploy and analytics runbook (v1 shipped 2026-07-17)

- Cloudflare Pages project: `patrick-severs-site` (account: pvsevers@gmail.com).
- Live at: https://patricksevers.com (custom domain) and https://patrick-severs-site.pages.dev (always-on fallback).
- Redeploy: `npx wrangler pages deploy src --project-name=patrick-severs-site` from the project root (requires `wrangler login` once per machine).
- Cloudflare Web Analytics: enabled via automatic setup (same-account hostname), no manual snippet needed.
- Resume PDF regenerated via `python3 scripts/build_resume.py` (writes `src/assets/pdf/patrick-severs-resume.pdf`).

## Open items (as of 2026-07-17)
- Full career-progression color/context from Patrick (companies/dates sourced from his LinkedIn PDF export; the "why" behind each era still needs his input).
- Mobile-viewport spot check on a real phone.

## Open items (redesign, 2026-09-08 UTC)
- Founder OK on the Agent Company page (pilot count, "no decision on what to sell", link to their site).
- Regenerate the resume PDF: `scripts/build_resume.py` still carries the pre-redesign headline and summary.
- Redraw `og-image.png` in the whiteboard language (still the terminal-green image).
- Product-marketing context updated to v4 with the six-page structure.
- Mobile-viewport spot check on a real phone (still open from v1).

## Release checks, 2026-09-09 21:27 UTC
- Standards review: unsafe loop-checker path handling, portrait graphics fallback, and footer nesting fixed; fresh reviewer confirmed all three fixes.
- Spec review: latest positioning, six thought-partner rules, typography, project groups, diagrams, and reversed-fork hero implemented. No blockers.
- Browser checks: desktop visuals and all six pages at 390px width. Source checks: generated pages current, local links/assets/fragments resolve, JS and Python syntax pass, candidate-file secret-pattern scan clear. Targeted tests cover rejected loop-check paths and portrait link-failure/context-loss fallback.
- No separate approved design packet or formal experience gate exists. Visual checks followed the current user rulings in `docs/decisions.md`.
