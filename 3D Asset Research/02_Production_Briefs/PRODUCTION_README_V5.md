# KWU V5 — Reproducible 3D Source Pipeline

## File arrangement
- `site/models/*.glb` — runtime assets (21 models incl. Apple variants and aliases)
- `site/assets/previews/*.webp` — product thumbnails rendered from GLB
- `site/assets/references/*.jpeg` — buyer-provided front reference images
- `assets/materials/*` — RGBA foreground textures for photographic materials
- `assets/sources/apple-symbol-fontawesome.svg` — attributed brand symbol reference
- `tools/photoreal_projection_v5.py` — photo-to-curved-surface mapping for bag/bottle
- `tools/anatomy_refinement_v5.py` — higher-density hand and neck mannequins
- `tools/device_detail_v5.py` — lens/hardware detail on Apple-like geometry
- `tools/render_v5_previews.py` — offline GLB render to WebP
- `tools/check_models_v2.py` — integrity and size checks

## Rebuild order
Do **not** run `make_models_v2.py` as the last step because it overwrites new detailed GLB files. To rebuild all geometry:

```bash
python tools/make_models_v2.py
python tools/photoreal_projection_v5.py
python tools/anatomy_refinement_v5.py
python tools/device_detail_v5.py
python tools/render_v5_previews.py
npm run build
python tools/check_models_v2.py
```

Requirements: Python trimesh, numpy, Pillow, scipy, scikit-image, opencv-python, vtk, cairosvg. For display: WebGL2 browser, WebGL textures enabled, static CDN hosting.

## Asset fidelity
- Projection is **not** multi-view reconstruction. It retains source-photo details from the front, but turning the object reveals inferred geometry.
- The in-browser renderer supports embedded RGB/RGBA textures, opaque hardware material, and simple studio lighting. It is not a full physically correct IBL shader, so some differences from a studio photograph are expected.
- The current hand is a denser procedural sculpt, not a photoreal human scan or fully weighted finger rig.
- The user-requested ultra-realistic final standard still requires high-quality scanned source meshes or multicamera photogrammetry. Making the `.glb` huge does not by itself improve physical accuracy.

## Product architecture
- Buyer sees one model at a time. The code only fetches a GLB when that category is active.
- Owner asset library keeps the complete 21-model navigation.
- Master files can remain high-resolution in GitHub or separate asset storage; web delivery should continue using per-model lazy loading and GPU-independent fallbacks.
