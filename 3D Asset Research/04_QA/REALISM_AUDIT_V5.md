# KWU V5 — Fidelity, Material, and Release QA

Date: 2026-10-20. Scope: eight customizable categories and 13 Apple device variants.

## Verified work done

1. Backpack `site/models/bag-charm.glb`: user-supplied front image projected onto a curved 3D mesh. The image matte retains the handle hole, fabric shading, seams, pockets, and small label. Existing sides/back remain procedural approximations. Default decorative demonstrator charm is removed; interactive user charm is a viewer overlay.
2. Bottle `site/models/bottle.glb`: user-supplied stainless body front image projected on a curved cylindrical front mesh, with 3D cap/loop/carabiner retained. Upper cap is not photographically projected because the projection would conflict with the real 3D carabiner. Black variant can darken the photographic highlight material.
3. Bracelet/ring `site/models/bracelet.glb`, `ring.glb`: denser procedural contiguous hand surface (around 80,000 triangles), curved nail plates fitted using nearest-surface projection, subtle colour variation, more detailed jewelry elements. **Not a genuine human scan or natural articulated skeleton.**
4. Necklace `site/models/necklace.glb`: higher-density joined neck/shoulder bust with flat neck crop and reattached chain, rather than separate ellipsoid beads. **Not a photographed human neck scan.**
5. Apple reference devices: 13 dimensioned procedural shapes improved with lens rings, highlights, and compatibility backmark. They are not official CAD geometry and are not identical in side-button/camera tolerances.
6. Renderer `src/viewer.ts` now reads glTF embedded baseColorTexture (`TEXCOORD_0`, `images`, `textures`, `materials`), textured photo surfaces, alpha modes, and releases GPU textures during switching. GitHub Pages build remains static. Photo material uses photographed RGB without an extra lighting bake.

## Source and licensing
- User supplied reference photos: `site/assets/references/backpack-user.jpeg`, `bottle-user.jpeg`. Stored under the user's KWU project; photographer/product rights should be verified before public commercial use.
- Additional icon: Font Awesome Free `brands/apple.svg`, CC BY 4.0, acknowledged in `assets/licenses/FONT_AWESOME_ICONS.md`. This is a compatibility rendering, not official manufacturer artwork.
- All other procedural geometry was generated for this project.
- Prospective scanned hand: https://www.innerscene.com/tools/library/3d-parts/posable-anatomical-right-hand-f6098b4f (public-domain CC0, 16 bones), but it **has not been downloaded or integrated** in V5. Its licensing is suitable but the binary was inaccessible to this environment.
- Poly Haven CC0 textures and HDRIs: https://polyhaven.com/ . Not downloaded in this release.

## Tests performed
- TypeScript `tsc --project tsconfig.json` succeeded.
- `tools/check_site.py` and `tools/check_models_v2.py` passed 21 GLB file integrity checks.
- VTK GLB importer produced front render previews for all 21 models including embedded textures. Inspect `site/assets/previews/`.
- Automated mobile/owner fallback and UI tests run at 320/390/768/1440 pixels. WebGL2 GPU was unavailable in the test browser; no real FPS claims are valid.
- Do not claim measured silhouette % accuracy, manufacturer CAD equivalence, or human-scan 1:1 without multiperspective ground-truth images / scanned meshes.

## Unmet acceptance tests
1. Compare five/six viewpoints of bag/bottle with real photos; the user gave only one front view each.
2. Integrate a verified photoreal hand scan and actual rig; target finger deformation, nail and skin maps.
3. Use calibrated PBR environment capture and physically based lighting for metals, plastic, skin, nylon, and transparent case.
4. Test WebGL2 and texture upload on real iPhone Safari, iPad Safari, Android Chrome mid-range/low-end, laptop/desktop, including 30/60 FPS and memory.
5. Add accurate per-model sticker printable zones, collisions, and physical production output.

## Release status
V5 is a **reference-photo-backed, significantly refined 3D prototype**, not a finished photogrammetric 1:1 asset pack. Photo-matched front views have higher fidelity; unobserved sides are authored approximations. User's size preference permits source masters to be large, but per-model web transfer is still optimized by loading only a selected category/model.
