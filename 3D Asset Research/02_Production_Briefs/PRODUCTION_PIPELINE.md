# Production Pipeline — KWU 3D Assets

## 1. Research
- kumpulkan dimensi
- kumpulkan warna resmi
- kumpulkan multi-angle references
- analisis material

## 2. High-poly modeling
- Apple devices: hard-surface precision
- backpack: soft-surface cloth form
- bottle: hard/industrial shape
- hand: anatomical sculpt / realistic base mesh refinement

## 3. Retopology
- buat mesh web-friendly
- pertahankan silhouette dan detail penting
- siapkan deformasi untuk rigged assets

## 4. UV unwrapping
- jaga texel density konsisten
- pisahkan area penting

## 5. Texturing / baking
- normal map
- AO
- roughness
- metallic
- optional height for source

## 6. Rigging
- hand
- neck
- MacBook hinge

## 7. Export
- glb/gltf 2.0
- compressed textures jika perlu

## 8. Optimization
- mesh simplification terkontrol
- KTX2 / compressed textures
- Draco/Meshopt bila pipeline mendukung

## 9. Web integration
- React Three Fiber viewer
- touch controls
- sticker placement
- charm placement

## 10. QA
- visual QA
- performance QA
- device QA
