# Peta pengerjaan kemiripan 3D dan kelancaran mobile

## Tahap yang sudah dimiliki proyek
- 21 GLB prosedural: 8 kategori inti serta varian perangkat Apple.
- Rendering berbasis vertex color dan shader WebGL2 ringan.
- Ukuran fisik dasar device mengacu pada spesifikasi Apple untuk sebagian besar SKU.
- Kontrol kamera, pilihan warna/casing, sticker/charm mockup, serta owner asset navigator.
- Dua foto asli pengguna untuk tas dan botol sebagai pembanding di owner model library.

## Batas saat ini
- Tidak ada model pemindaian tangan, normal/roughness/displacement map kulit 4K, skeletal skinning, dan full physically-based transmission.
- Renderer ringan saat ini hanya menafsirkan `POSITION`, `COLOR_0`, indeks dan sebagian efek transform; tidak menggambar texture PBR, skinned mesh, maupun material extensions dari GLB eksternal.
- Karena itu **mengunduh high-poly GLB lalu mengganti namanya tidak akan menghasilkan upgrade visual yang benar**. Dibutuhkan modul rendering modern (Three.js GLTFLoader + MeshPhysicalMaterial) atau konversi terkontrol.

## Pipeline final yang direkomendasikan
1. Simpan master asset Blender/scan terotorisasi dengan unit meter atau mm yang jelas.
2. Samakan pivot dan hierarki: `ROOT`, `DEVICE`, `SURFACE`, `ANCHORS`, `STICKERS`, `JEWELRY`, `SKELETON`.
3. Buat 2–3 tingkat LOD; mobile LOD0 detail fokus, LOD1 saat zoom out, LOD2 mode Low.
4. Bake normal, AO, roughness dan metalness. UV untuk stiker wajib stabil.
5. Ekspor `.glb`, lalu kompres mesh dengan Meshopt dan tekstur KTX2, sesuai dukungan GLTFLoader.
6. Pada runtime gunakan lazy import 3D studio, render-on-demand saat idle, adaptive DPR, cache GLB, matikan shadow mahal ketika interaksi berat.
7. Uji di perangkat fisik berbasis chipset berbeda, bukan hanya emulasi browser yang tidak menyediakan WebGL.

## Target performa awal (bukan hasil pengukuran)
- Interaksi: 30 FPS minimum pada HP kelas bawah yang didukung; mengusahakan 60 FPS pada kelas menengah.
- Total geometri scene mobile: 75k–150k triangles sebagai batas kerja awal, bukan batas mutlak.
- Tekstur mobile: 512–1.024 px per material biasa; 2.048 px hanya untuk closeup signifikan.
- GLB utama awal: target transfer 1–3 MB per scene (bergantung kategori), sisanya on demand.
- Tidak ada 8 canvas 3D aktif bersamaan di katalog.
- Pengujian memori GPU dan suhu wajib di HP fisik.

## Kriteria penerimaan visual
- Siluet referensi front/back/samping dibandingkan dengan set foto terukur.
- Kamera perangkat Apple dan tombol dicek pada SKU masing-masing.
- Tas harus mempunyai panel, handle, dua kantong samping, label dan posisi zipper sesuai foto referensi, serta struktur bagian belakang berdasarkan data tambahan atau asumsi terdokumentasi.
- Botol harus memiliki cap hitam, ring, carabiner, kontur shoulder dan stainless finish sesuai referensi.
- Tangan menunjukkan anatomi natural dari semua sudut dan deformation tidak pecah ketika berganti jari.
- Klaim '1:1' hanya setelah ada ukuran benda fisik, referensi semua sisi dan evaluasi ketelitian.

## Tindakan langsung dari release ini
- Hapus banner demo yang terus tampil di setiap halaman.
- Pertahankan disclosure simulasi di formulir login/checkout/hasil pembayaran.
- Perbaiki transform normal selama rotasi kamera dan pencahayaan studio di WebGL2.
- Tambah compare reference tas/botol pada Library Model 3D owner.
- Pertahankan 21 GLB lama untuk mencegah kehilangan seluruh navigasi saat upgrade render.

## Blokir kualitas fotorealistis
Tidak ada lisensi pengunduhan scan hasil riset yang diotorisasi/diunduh ke proyek ini dan tidak ada base mesh high-poly untuk tangan maupun bahan tekstur PBR. Versi ini **tidak** dapat dinyatakan 200× lebih mirip ataupun 1:1.
