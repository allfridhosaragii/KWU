# ATELIER — KWU 3D Commerce

Mobile-first interactive design studio and e-commerce **prototype** for the KWU entrepreneurship project.

## Preview

GitHub Pages **deployment target**: https://allfridhosaragii.github.io/KWU/

**Important:** This public Pages build is a working **simulation**, not a production shop. The login modes do not authenticate real users; browser `localStorage` holds demo designs/orders. Checkout **never charges money**. There is no deployed PostgreSQL database, Next.js server, Midtrans gateway, real stock reserve, or secure owner session. Do not enter real credentials or sensitive data.

## Current prototype features

- Eight GLB models (`site/models`), exported by `tools/make_models.py`: bracelet on hand mannequin, ring on hand, necklace on bust, bag charm, phone/case, tablet, laptop, stainless bottle.
- Low-bandwidth WebP previews (`site/assets/previews`); no 3D canvas in catalog cards.
- WebGL2 viewer with touch orbit, wheel/pinch zoom, keyboard controls, active elements, color, ornaments, placement, scale, rotation, selectable fingers, phone cases, and adaptive pixel ratio.
- WebGL-unavailable fallback previews.
- 34 route **templates** and eight selectable studio scenes, buyer and owner layouts.
- Wishlist, saved designs, cart, checkout demonstration, order overview, owner order status, inventory counters, demo report.
- Warm Modern Atelier design tokens based on `Design Konsep/` documentation.
- Static GitHub Pages deployment workflow and offline tests.

## Project structure

```text
Design Konsep/            # Previously approved 73 Markdown UX docs (retain in repo)
System/                   # Previously approved 52 Markdown architecture docs (retain in repo)
src/app.ts                # Typed client-side route templates, demo state and user flows
src/viewer.ts             # Native WebGL2 + glTF GLB 2.0 renderer
site/index.html           # Static entry
site/404.html             # GitHub Pages nested-path SPA fallback
site/assets/app.js        # Compiled runtime
site/assets/viewer.js     # Compiled renderer
site/assets/style.css     # Mobile-first design system
site/assets/previews/     # WebP previews
site/models/              # Downloadable 3D GLB assets
tools/make_models.py      # Generate model prototypes (trimesh, numpy)
tools/render_previews.py  # Export visual previews (VTK)
tools/check_site.py       # No-dependency export validation
tests/e2e_inline.py       # Offline Chromium UI navigation and workflow tests
.github/workflows/       # CI + GitHub Pages deploy
```

## Build

Requires Node.js 22 and TypeScript 5.8+. Code is written in **TypeScript**, compiled to browser ES Modules using `tsc`.

```bash
npm install
npm run build
python tools/check_site.py
```

For the optional asset regeneration, install Python `numpy`, `trimesh`, and `vtk`, then:

```bash
python tools/make_models.py
python tools/render_previews.py
```

## Deployment

Push `main` and configure **Settings → Pages → Source: GitHub Actions**. The `Publish KWU demo to GitHub Pages` workflow deploys `site/`. See [Deployment](docs/DEPLOYMENT.md).

## Architecture decision

This preview intentionally uses **native TypeScript + WebGL2** because GitHub Pages hosts only static files, and network restrictions prevented installing and testing the planned Next.js/R3F stack in this environment. It is **not** a substitute for the full `System/` production architecture. The next production phase should integrate Next.js, React Three Fiber, Zustand, PostgreSQL/Prisma, Auth.js, R2, verified Midtrans callbacks, and real stock/fulfillment services on a server-capable host.

## Quality / honesty

The downloadable models are functional geometric **prototypes**, not photorealistic scanned assets. Realistic skinned hands, detailed material PBR, full rigging, accurate MacBook hinge mechanics, precision-cut sticker UV/print exports, and mobile GPU validation on physical phones remain future work.

Current browser regression suite covers route templates, visual overflow at selected emulated viewports, and demo buyer/owner workflows. Chromium under the test container is policy-blocked from network navigation and WebGL2, so native WebGL shaders/gestures cannot be certified on real hardware from these tests alone. See [QA](docs/QA_REPORT.md).
