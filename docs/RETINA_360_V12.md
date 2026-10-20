# KWU V12 — Retina 360° frame upgrade

## Root cause
V10 used 400px atlas tiles, enlarged to fill the 3D Studio, causing visible pixelation. V11 added 768px tiles, but enlarging and zooming could still appear soft.

## Changes
- Retain 768px atlas frames for instantaneous drag and pinch.
- Render 1536×1536 images directly from the latest GLB for 24 angles, 2 elevations, bracelet, ring and necklace.
- Save one compressed WebP file per angle and skin tone (5 tones, default Sawo Matang).
- After 190ms without camera motion, load only the selected retina still frame and fade it over the low-res preview.
- When a new angle is selected, drop the old retina frame immediately; cancel outdated image decodes.
- Keep fallback rotatable when a high-resolution file cannot be loaded.
- Never preload all 720 frames on a phone.

## Quality and safety
Actual anatomy still depends on the underlying GLB and MakeHuman-derived mesh. Increasing render resolution improves sharpness, not biological accuracy. WebGL devices continue using realtime 3D; GPU-less browsers use an interactive 360° turntable. CI verifies the frame dimensions, format, and completeness after build.
