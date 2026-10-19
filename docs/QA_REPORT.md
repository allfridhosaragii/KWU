# QA Record — KWU Pages Prototype

Baseline: 2026-10-20. This report is about the **prototype**, not a certified production commerce platform.

## Test matrix

- TypeScript compile: `tsc --project tsconfig.json`.
- Asset correctness: GLB header/JSON/accessors and mesh triangle counts, all eight previews, file-size checks.
- Chromium injected-document browser tests: 320×720, 390×844, 768×1024, 1440×900; each includes route template checks, horizontal overflow checks, owner demo pages and critical workflow.
- Functional path: studio -> change ornament -> move placement -> save design -> cart -> checkout demo -> owner order list.
- Screenshots: home, studio, owner mobile; home and studio desktop. Stored locally, not served as production assets.

## Limits and residual risk

- The test Chromium is blocked by a policy from opening localhost/files and reports WebGL2 unavailable, so browser tests use offline inline injection and confirm the 2D fallback. This does **not** certify GPU behavior, shader compilation under actual WebGL2, FPS, thermal load or mobile touch gestures.
- No physical phones or tablets were connected; viewport emulation is not a substitute.
- No database, real authentication or payment gateway is active in GitHub Pages.
- Modeling assets are handmade procedural prototype GLBs. Visual realism is preliminary.
- The user should verify the deployed Pages workflow status and GitHub Pages URL after enabling Pages in Settings.

## Bug fixes already applied

- Prevented product wishlist buttons from floating outside cards by adding a positioned card container.
- Ensured selected ring moves to the selected finger via per-part scene transform.
- Fixed wrap mapping of bottle sticker on cylindrical surface.
- Adjusted MacBook cover geometry and hinge transform in render path.
- Added image-based fallback on devices without WebGL2.
- Added demo-safe identifier fallback in insecure local browser contexts.
- Fixed desktop test selector to target visible add-to-cart action.

## Release decision

**Approved only as a public academic interactive demo**, not for collecting real payments or representing photoreal finished products.
