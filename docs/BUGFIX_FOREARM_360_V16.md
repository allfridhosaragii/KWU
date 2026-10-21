# V16 — Repair 360 sprite duplication and ragged forearm

The old hand GLB already contains white sawtooth holes in its cut lower forearm; this is visible in original 1536px GLB renders and cannot be solved by increasing resolution. The old zoomed CSS sprite could also expose parts of neighboring frames.

- Anatomical skin is clipped to y=-1.230 and sealed by a PBR-textured cap.
- Bracelet, ring, nails, tone selections and all other GLB nodes are retained.
- Atlas selection is now exact Canvas2D tile cropping, never CSS background-position.
- Source atlas and retina caches have version 16 keys; turntable frames are regenerated.
- Build checks all model and atlas assets and the repaired forearm invariant.

Local QA: cleaned both original textured GLBs; a synthetic 4x6 atlas shows only the selected frame after 2.8x zoom at 320, 390, 768, 1440px viewports.

These changes fix specific artifacts, not prove photo-realism or physical GPU performance on every device.
