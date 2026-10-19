# Pipeline Blender ke GLB/GLTF, Manifest, dan CDN

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Tahapan asset authoring
1. Brief produk fisik: ukuran millimeter, foto referensi legal, material, area custom, jumlah varian.
2. Blender modeling: ukuran nyata dalam meter world space (contoh 100 mm = 0.1 unit jika 1 unit = meter), origin konsisten, apply transform, mesh/winding/normal benar.
3. Topologi untuk rig: tangan/lengan dengan bone weights; jangan gunakan subdiv modifier pada export tanpa cek budget.
4. UV unwrapping non-overlap untuk printable surfaces; textured materials PBR sesuai metallic/roughness workflow.
5. Anchor empties disematkan dengan penamaan stabil, misal `anchor_wrist_01`, `anchor_ring_index`, `surface_bottle_main`.
6. Export glTF 2.0 binary `.glb`, animasi/rig disimpan jika digunakan.
7. Validasi otomatis: GLB parse, rig/bone names, bounding box, unit scale, texture dimensions, missing/material extension, jumlah vertices/triangles/drawcall estimate.
8. Generate profile mobile/high: Meshopt geometry, KTX2/BasisU GPU texture, baked shadows as needed, LOD.
9. Publish immutable hashed filename ke R2/CDN, update manifest `assetVersion` dan metadata, cek CORS dan cache.
10. Runtime load via GLTFLoader/Meshopt/KTX2 decoders dan beri error fallback.

## Struktur sumber
`assets/source/mannequins/hand.blend`, `neck.blend`, `jewelry/`, `devices/`, `objects/`, `ornaments/`, `stickers/`, ditambah `assets/manifests/*.json` dan `assets/optimization/*.json`.

## Contoh manifest ringkas
```json
{
  "id":"hand-neutral-01",
  "type":"mannequin",
  "version":"v1",
  "unit":"meter",
  "profiles":{
    "mobile":{"url":"/models/hand-neutral-mobile-a12.glb"},
    "high":{"url":"/models/hand-neutral-high-a12.glb"}
  },
  "anchors":["anchor_wrist_01"],
  "rig":"armature_hand_v1",
  "bboxMeters":[0.1,0.28,0.08]
}
```

## Perbandingan kompresi
Meshopt cocok untuk geometri/animasi; Draco sebagai alternatif jika aset tertentu lebih efektif; pilih berdasarkan uji size, decode time mobile, memory dan compatibility. KTX2 fokus pada memori GPU; WebP/AVIF gambar biasa bisa lebih hemat transfer tetapi tidak sama manfaatnya untuk GPU texture. Jangan hanya mengejar file `.glb` terkecil jika waktu decode menjadi besar.

## Akurasi warna
Gunakan workflow linear-sRGB yang benar dan periksa output pada iPhone/Android. Produk tidak boleh berubah warna hanya karena warm UI; metal/transparent case butuh environment studio netral terkontrol.

## Sumber
https://gltf-transform.dev/
https://threejs.org/docs/pages/GLTFLoader.html
https://threejs.org/docs/pages/KTX2Loader.html
