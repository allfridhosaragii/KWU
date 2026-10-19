# Kontrak Folder dan Format Aset

## Source vs runtime
```
assets/metadata/SOURCE_ATTRIBUTION.md
3D Asset Research/                  # analisis, spesifikasi, QA
 tools/anatomical_hand.py             # surface generator
 tools/make_models_v2.py              # authored geometry, exports
 tools/render_previews.py             # render QA thumbnails
 site/models/*.glb                    # runtime browser 3D (21 + aliases)
 site/models/model-catalog.json       # inventory, official dims & palettes
 site/assets/previews/*.webp          # fallback 2D (21)
```

### Runtime naming rules
- `phone.glb` adalah alias `iphone-17.glb`. Sama untuk `tablet` dan `macbook`.
- `model-catalog.json` menjadi sumber daftar ID dan dimensi asli.
- Setiap nama file wajib stable serta URL-safe (huruf kecil, angka, tanda minus).
- Simpan `deviceModel` saat menyimpan desain agar konfigurasi tetap konsisten.

## Target pra-produksi
- Source master: file Blender (`.blend`) dengan bevel, UV, PBR, bones, dan output high-res.
- Runtime: glTF/GLB 2.0, KTX2 textures (jika tersedia), meshopt sesuai dukungan loader.
- Preview: `.webp` minimal ukuran 560×700 dan gambar square untuk katalog.
- Pilih `Balanced` pada mobile; turun ke `Low` saat perlu; pertahankan silhouette.

## Serah terima per aset
1. Model ID unik
2. `source_uri` dan hak pakai
3. `physical_dimensions_mm` serta sumbernya
4. Referensi gambar multi-angle
5. 1 GLB teroptimasi
6. Poster WebP
7. Titik pemasangan ornament/sticker
8. QA report + tanggal revisi
