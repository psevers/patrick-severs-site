# Deploy and analytics runbook (v1 shipped 2026-07-17)

- Cloudflare Pages project: `patrick-severs-site` (account: pvsevers@gmail.com).
- Live at: https://patricksevers.com (custom domain) and https://patrick-severs-site.pages.dev (always-on fallback).
- Redeploy: direct upload to production branch `main`. See the October 27 release note below before uploading a full directory (requires `wrangler login` once per machine).
- Cloudflare Web Analytics: enabled via automatic setup (same-account hostname), no manual snippet needed.
- Current approved resume: `src/assets/pdf/patrick-severs-enterprise-ai-resume.pdf`. The old `scripts/build_resume.py` produces the prior resume; do not use it to replace the approved asset.

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

## Enterprise sales and AI adoption release, October 27, 2026 UTC

Patrick approved the website calibration and requested production release with the new resume. Content, responsive layouts, themes, keyboard interactions, generated output, and exact resume bytes were reviewed; see `docs/openai-website-calibration.md`. The new social asset is `enterprise-ai-social.png`; the previous image and PDF remain available.

**Full-directory upload precaution:** `/glg/90-day/` is already public but its source is still uncommitted in the original checkout. For this release, copy `src` into an isolated upload bundle and add the byte-verified live GLG HTML and PDF unchanged. Deploy that bundle with `npx --yes wrangler@4.154.0 pages deploy <bundle> --project-name=patrick-severs-site --branch=main --commit-hash=<release-sha> --commit-dirty=true`. The dirty flag reflects the preservation overlay outside the committed release. Do not upload the original dirty checkout.

After deployment, verify the custom domain's new page content, resume link and PDF hash, social asset, existing routes, and preserved GLG artifacts. Cloudflare's previous deployment is available for rollback; do not delete it. Physical-device and Safari checks remain open.
