# Audit sumber model fotorealistis KWU — 20 Oktober 2026

Status: **hasil riset dan kandidat, belum diunduh atau dibeli**, kecuali aset prosedural orisinal yang sudah ada di `site/models/`. Dokumen ini bukan surat izin pemakaian; setiap aset wajib diperiksa lagi pada halaman sumber saat akan diunduh.

## Tujuan kualitas
Bukan sekadar menambah polygon. Target tertinggi adalah bentuk, dimensi, warna, material dan interaksi yang layak dibandingkan dengan barang nyata. Rasio peningkatan seperti "200x" tidak memiliki metrik baku dan tidak digunakan sebagai klaim kualitas.

## Shortlist sumber yang dapat dipertimbangkan

| Aset | Sumber (tautan spesifik) | Detail | Lisensi di halaman ketika diteliti | Keputusan |
|---|---|---|---|---|
| **Tangan hasil scan** | https://sketchfab.com/3d-models/female-hand-0144539af191427fb6b8185a17bac675 | Foto-scan 192,6k triangles / 96,3k verts | CC Attribution | **Prioritas A** sebagai high-poly reference, memerlukan atribusi dan retopologi; bukan rigged siap pakai. |
| **Tangan rigged** | https://sketchfab.com/3d-models/rigged-hand-eae97cc2a742413cb5338ab942b12c1e | 29k triangles | CC Attribution-ShareAlike | **Prioritas B** sebagai rig/reference, turunan memiliki syarat ShareAlike. |
| **Hand rig sederhana** | https://sketchfab.com/3d-models/rigged-hand-6fa0664093b5489da73cfc6c2dd6e4f3 | 12,2k triangles | CC Attribution | **Prioritas B** untuk rig animasi, bentuk kurang photoreal. |
| **Hand photogrammetry mannequin** | https://sketchfab.com/3d-models/mannequin-hand-photogrammetry-vr-ready-fe78bb31fce2484187c22c1a86fa7e24 | ~2k triangles | CC Attribution | **Alternatif** untuk studi deformation dan rig. |
| **Backpack modular** | https://sketchfab.com/3d-models/backpack-dd087558c1a24a9ea82d50d764ad4b78 | 14,2k triangles; zippers, side/front pockets | CC Attribution | **Prioritas A** sebagai topology/material reference, bukan tas yang identik. |
| **Backpack hasil scan** | https://sketchfab.com/3d-models/backpack-a1f13ea2ce7f418a94ca0aa680d2d1f8 | 495k triangles | CC Attribution | **Prioritas B** sebagai sculpt reference, perlu poly reduction besar. |
| **Water bottle hard surface** | https://sketchfab.com/3d-models/water-bottle-885543a7679c4026abbd6499185caf08 | ~1,8k triangles, textured | CC Attribution | **Prioritas A** untuk teknik modeling silhouette dan material, bukan botol berkarabiner identik. |
| **Water bottle detail** | https://sketchfab.com/3d-models/water-bottle-4988fdcc01ec42f28ea7234c0cf06c41 | 42,1k triangles | CC Attribution | **Alternatif** sebagai material reference. |
| **HDRI Studio Small 09** | https://polyhaven.com/a/studio_small_09 | Studio neutral-softbox HDRI | CC0 | **Boleh dipakai**. Turunkan resolusi HDRI untuk mobile jika diintegrasikan di renderer Three.js. |
| **Material, HDRI, texture** | https://polyhaven.com/ | CC0 PBR material library | CC0 | **Prioritas A** untuk permukaan realistik tanpa kendala atribusi. |
| **Commercial hand scan** | https://www.3dscanstore.com/unreal-engine-rigged-hands | Photogrammetry rigged | Lisensi proprietari | **Jangan masukkan ke repo publik** sebelum ada izin yang mencakup distribusi dalam aplikasi web. |
| **Commercial iPhone 17 Pro Max** | https://www.cgtrader.com/3d-models/electronics/phone/apple-iphone-17-pro-max | Model 3D PBR/BLEND komersial | Royalty Free bersyarat | **Referensi opsi berbayar**, model raw GLB tidak boleh dipublikasikan begitu saja ke repo/download langsung. |

**Sumber data spesifikasi fisik perangkat Apple** (bukan sumber model bebas pakai):
- iPhone 17: https://www.apple.com/id/iphone-17/specs/
- iPhone 17 Pro Max: https://support.apple.com/id-id/125091
- iPhone Air: https://www.apple.com/id/iphone-air/specs/
- iPhone 17e: https://www.apple.com/id/iphone-17e/specs/
- iPad Pro: https://www.apple.com/id/ipad-pro/specs/
- iPad Air: https://www.apple.com/id/ipad-air/specs/
- MacBook Air: https://www.apple.com/id/macbook-air/specs/
- MacBook Pro: https://www.apple.com/id/macbook-pro/specs/

## Lisensi dan hak komersial
1. **CC0**: aset dapat digunakan dan dimodifikasi untuk komersial tanpa atribusi wajib. Tetap simpan URL sumber dan versi.
2. **CC BY**: atribusi nama pencipta, judul, lisensi, dan URL harus tersedia pada hasil penggunaan. Rekam modifikasi dan simpan bukti lisensi.
3. **CC BY-SA**: turunan mempunyai kewajiban share-alike. Audit lebih dalam sebelum menggabungkan dengan aset proprietary.
4. **CC BY-NC**: **jangan gunakan** pada e-commerce yang berpotensi bertransaksi komersial tanpa izin tertulis.
5. **CGTrader Royalty Free / 3D Scan Store / beberapa lisensi Fab**: tidak berarti model mentah boleh diunggah terbuka di `/site/models/*.glb`. Model yang dapat langsung diunduh oleh pengunjung pada web statis umumnya tidak memenuhi larangan redistribusi raw file. Butuh izin tambahan, atau buat aset orisinal sendiri.
6. Semua tautan kandidat harus diverifikasi ulang saat asset acquisition. Tidak ada pembelian atau klaim hak tambahan dilakukan dalam tahap riset ini.

Referensi ketentuan:
- https://polyhaven.com/license
- https://sketchfab.com/developers/download-api/guidelines
- https://sketchfab.com/licenses
- https://help.cgtrader.com/hc/en-us/articles/360015124437-Royalty-Free-License
- https://www.3dscanstore.com/terms-and-conditions-licensing

## Kesesuaian dengan target 1:1
- **Apple**: dimensi dari pabrikan dapat akurat, tetapi model casing dan konfigurasi kamera harus diverifikasi terhadap foto multi-angle. Data spesifikasi saja belum memberikan seluruh CAD.
- **Tas dari foto pengguna**: foto yang tersedia hanya tampak depan, belum bisa membuktikan ketebalan, ransel belakang, bahan dan ukuran asli. Gunakan model dari sumber di atas sebagai studi teknik, **bukan** mengganti ransel referensi dengan model tas lain.
- **Botol pengguna**: profil silinder dan carabiner dapat dibuat mirip depan, tetapi tinggi/diameter asli dan bentuk tutup dari belakang belum dapat dipastikan.
- **Tangan**: scan CC BY adalah lompatan terbesar dibanding tangan geometri buatan. Dibutuhkan retopologi dan rigging untuk lima jari, normal/roughness kulit, dan LOD agar tetap ringan.

## Cara mendapatkan sumber tanpa melanggar lisensi
- Sketchfab meminta pengguna terautentikasi untuk mengunduh. Jangan bypass OAuth atau mengambil model dari cache/preview.
- Semua file pihak ketiga disimpan di folder kerja privat untuk audit dan optimasi, **bukan** langsung ke GitHub Pages.
- Setelah lisensi dinyatakan sesuai, buat GLB yang disesuaikan, metadata sumber, dan atribusi di UI jika diwajibkan.
- Jika lisensi melarang redistribusi file mentah, pilih alternatif CC0 / izin eksplisit / pemodelan orisinal.
