# Material PBR, Warna Realistis, dan Lighting

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Look target
Barang terasa nyata melalui kombinasi geometry silhouette, PBR, environment, texture maps dan skala fisik, bukan melalui triangle sebanyak mungkin atau efek fullscreen berat. UI hangat, studio 3D boleh netral agar produk hitam/silver/transparan akurat.

## Pipeline PBR
- `baseColor`: warna produk; **jangan bake highlight ke albedo**.
- `metallic`/`roughness`: stainless silver/hitam powder-coated, polished metal charm, leather bag, plastic case, vinyl stickers.
- `normal`: detail permukaan kulit, tekstur tas/jahitan, brush metal; ukur frekuensi tekstur agar tidak tampak kasar saat zoom.
- `ambient occlusion`: baked untuk lipatan/kontak; gunakan UV channel sesuai pipeline.
- `transmission`/opacity: untuk casing transparan pilih kualitas adaptif karena real transparency mahal pada GPU lemah.

## Environment lighting
Studio memakai soft HDRI/environment map terkompresi ditambah beberapa lampu sederhana sesuai kategori. Ground contact shadow dapat dibake atau dibuat satu efek ringan. Refleksi metal perlu sumber highlight yang besar, bukan puluhan point lights.

## Per-surface guidelines
| Benda | Material | Tantangan |
|---|---|---|
| Tangan/leher | skin-like matte | Tone kulit dan bayangan realistis tanpa memuat mesh wajah penuh |
| Charm/kalung/cincin | metallic PBR | Specular aliasing/metal black tanpa environment |
| Tas | leather/fabric PBR | Jahitan lewat normal map dan geometry budget |
| Casing polos | plastic | Warna netral vs UI hangat |
| Casing bening | clear plastic | Ketebalan, alpha/transmission, kamera terlihat |
| Tablet/MacBook | aluminum finish | Konsistensi material tanpa menggunakan logo tak berizin |
| Botol stainless | brushed/powder coat | Warna hitam/abu dan refleksi cilindris |
| Stiker vinyl | matte/satin | Layer di permukaan tanpa z-fighting |

## QA visual
Bandingkan foto sumber di white/neutral light, sudut 0°/45°/180°, zoom dekat dan jauh, layar mobile high/low gamut. Hindari tone mapping yang membuat warna produk berbeda setelah ditambahkan ke cart thumbnail.
