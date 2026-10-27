# Website calibration

**Status:** reviewed by Patrick; production release requested October 27, 2026 UTC.

## User direction

Calibrate the portfolio for enterprise GTM and AI adoption after the resume review. Preserve the existing style. Apply Apple Design and Emil Design Engineering to hierarchy, readability, feedback, and accessibility.

## Design baseline and implementation judgments

- Baseline is the live site and commit `6a0929b6469653e274ac593a76e7765de76933c5`: Inter, white and blue light mode, green-black and sage dark mode, editorial sections, the existing portrait and illustrations. Older handwritten and terminal-era records are historical.
- Keep the four existing page routes and legacy redirects. Add a Building navigation link to the home page's `#now` section, which also repairs the legacy Agent Company destination.
- Home leads with account growth and hands-on AI work. Box leads customer evidence; G2i growth and the existing illustration remain. Use existing work-row patterns for SROS and the personal claims agent.
- Previous work gains the Box adoption/expansion story and clearly labeled individual attainment. Preserve G2i content and testimonials.
- How I operate adds the seven-person adoption effort and the recurring claims workflow. Career reflects attainment and current work instead of a VP-only ask.
- No new motion library or decorative animation. Preserve the site's assets and palette. Improve press/focus feedback, mobile menu state, Escape dismissal, skip navigation, and reduced-motion visibility.
- Link to an exact copy of the approved resume under a new asset filename. Keep the prior PDF intact.
- Replace the old social-preview reference with a new image in the site's existing visual language. Its editable HTML source is `scripts/site-gen/social-card.html`.

## Content evidence and boundaries

The source interview and resume drafts are in the original checkout under `docs/research/` and `output/openai-resume/`. Do not pull private G2i source material into this work.

- G2i company revenue growth is 122% from 2024 to 2025.
- Box expanded from 100 to 3,000 seats on a three-year agreement over approximately a year. Omit uncertain deal dollars and the unconfirmed formal customer name.
- ADP President's Club was in 2018 at 176% of quota. Braintrust attainment is 125% to 140% against annual billings quotas of $2.5 million to $3 million.
- Seven G2i team members adopted Codex or Claude within six weeks. Team size and agent-fleet count are separate facts.
- Parents and athletes use SROS today, per Patrick. The authenticated app showed 1,414 programs. Do not claim complete contact/camp coverage, user counts, paying customers, or recruiting outcomes.
- OpenAI supports SROS development, research, and information maintenance. A recruiting agent that drafts/sends communications is planned.
- The personal claims agent's initial 27 claims resulted in approximately $3,500 reimbursed within a week. Omit disputed execution timing and the uncertain original model version.

## Verification plan

Use the actual static site at 320, 390, 768, and 1440 CSS pixels. These widths are implementation checks, not an invented approval gate. Inspect light/dark mode, layout overflow, menus, focus, keyboard navigation, reduced motion, anchors, images, generated output, and local links. Keep fresh independent review separate from implementation. There is no newly approved design packet; evaluate against the user's preservation requirement and the observed baseline.

## Review record

Verified October 27, 2026 UTC against the uncommitted worktree diff from the baseline above.

- Browser checks passed for all four pages at 320, 390, 768, and 1440 CSS pixels in light and dark mode. The enumeration and results are in `output/website-calibration/verification.json`.
- Verified one main landmark and heading per page, no document overflow, no overlapping logo/controls, loaded images, reduced-motion visibility, static loop alternatives, correct theme labels and heading colors, and no browser runtime errors.
- Exercised menu opening, Escape dismissal and focus restoration, Building-link dismissal, theme persistence, skip navigation, and the Box anchor's position below the sticky header.
- Sampled home text contrast passes 4.5:1. This is a targeted check, not a claim of a full accessibility audit.
- Generator consistency, local links/assets/anchors, unique IDs, JavaScript syntax, and diff whitespace checks pass. Approved resume bytes match the original draft; the prior resume remains unchanged.

Independent reviews used fresh GPT-6.1 Sol sessions, medium reasoning, against this local work. Standards and Spec reviewed source; visual QA inspected screenshots and the verification record without independently rerunning the browser suite.

| Before | After | Why |
| --- | --- | --- |
| Standards found the new Box anchor lacked a sticky-header offset. | Box and the other new section destinations have an offset; the browser check confirms the heading is visible. | The primary customer-work link must land on readable content. |
| At 320px, existing 12-column gaps overflowed the stacked footer and rules. | Stacked layouts use one column. All checked widths fit. | Preserve reading order without horizontal clipping. |
| Initial mobile captures caught heading colors between theme states. | Captures wait for rendering to settle; final visual QA found both themes readable. | Screenshots must represent the settled interface. |
| Dark-mode proof text and the inverted section label had insufficient contrast. | Theme-specific tint and label values retain the palette and improve readability. | Small text needs sufficient contrast in both themes. |

Spec/evidence review found no issues. The final independent visual QA found no remaining findings. No new design packet or approval gate was inferred.

The integrated preview's save-screenshot operation timed out twice with `Preview automation snapshot timed out after 15000ms.` Saved artifacts therefore use a local Chromium capture. Desktop and mobile layouts were inspected; no physical-device, Safari, or deployed-site verification is claimed. The local preview runs at `http://127.0.0.1:8047/`.

## Production release preparation, October 27, 2026 UTC

Patrick said, “this is approved. how do we get this pushed to production along with the new resume?” Release includes the reviewed website and the approved resume under its new filename.

Cloudflare Pages is a direct-upload project with production branch `main`. The prior production deployment is `5c36fc62-df03-4821-99f8-d8b59b2fd8ce`. The source release excludes unrelated GLG edits and local capture output.

The already-live `/glg/90-day/` HTML and PDF are not in the committed baseline. Both were downloaded and compared byte-for-byte with the original checkout before preparation. The production upload preserves these exact existing artifacts in a temporary bundle; no unpublished GLG source changes are included. Their SHA-256 values are:

- HTML: `6ca2f87f2cfe399da634b151a3dbd183325e39a83e102734722e72f68cdbbf91`
- PDF: `c188ea1266144af0df260cd9fba5061e0ec1113777e1064b5a018b3f234386fc`

Until the separate GLG source work is committed, a plain upload of this checkout's `src` would remove that route. Preserve the live artifacts in future full-directory uploads.
