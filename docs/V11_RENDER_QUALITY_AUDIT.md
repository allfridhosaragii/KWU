# KWU V11 — High Resolution 360° Render Fix

## Laporan masalah
Pada 20 Oktober 2026, tampilan manekin saat rotasi terlihat seperti video 144p. Penyebabnya bukan sekadar ukuran file GLB. Saat perangkat menggunakan fallback 360° tanpa WebGL, V10 memperbesar satu frame berukuran 400 × 400 px ke viewport desktop atau layar HP dengan DPR 2–3. Selain itu, semua 48 frame digabung dalam satu atlas WebP kualitas 81.

## Solusi V11
1. Gelang, cincin, dan kalung dirender ulang langsung dari GLB menggunakan 768 × 768 piksel per sudut.
2. Tetap 24 sudut horizontal × 2 elevasi (48 sudut). Dua elevasi disimpan ke PNG atlas berbeda 3072 × 4608 untuk meminimalkan risiko decode gambar sangat tinggi pada Safari.
3. Format PNG tanpa lossy compression agar tepi perhiasan dan shading kulit tidak rusak saat zoom.
4. Aktifkan vtkPolyDataNormals dengan point normals dan `SplittingOff()` pada renderer offline agar UV seam tidak terlihat sebagai garis facet.
5. Pembuatan atlas dan recolor lima tone dilakukan pada subprocess berbeda untuk menjaga penggunaan memori pada CI.
6. Atlas kedua hanya diunduh ketika pengguna mengubah sudut ketinggian, bukan saat membuka halaman.
7. Lima tone kulit tetap ada, dengan default Sawo Matang.
8. Sebanyak 18 model perangkat lain mempertahankan file V10 yang masih bisa diputar, agar deploy tidak mengubah fungsionalitas yang tidak diminta.
9. Koreksi kuku bersifat bersyarat. Bila koordinat anatomi pada GLB produksi tidak sesuai titik referensi, script tidak akan mengubah mesh. Ini mencegah kerusakan model dan menggagalkan deploy HD.
10. Browser cache diperbarui ke V11 agar JavaScript lama tidak terus terpakai.

## Hasil perbandingan teknis
- V10 manekin: 400² = 160.000 piksel per sudut, atlas WebP kualitas 81.
- V11 manekin: 768² = 589.824 piksel per sudut, atlas PNG tanpa kehilangan detail.
- Resolusi meningkat 1,92× tiap sumbu dan 3,69× total piksel per sudut.
- Pada HP 390 CSS px / DPR 2, 768 px hampir memenuhi resolusi perangkat untuk ukuran satu frame.
- Gambar tetap berupa fallback sudut kamera prarender, bukan rendering GPU real-time. Zoom ekstrem di atas ukuran sumber masih dapat terlihat lembut.

## Hasil QA yang relevan
- Browser Playwright tanpa WebGL: 17 pemeriksaan lulus pada 320, 390, 768, dan 1440 CSS px untuk putar, drag, zoom, tone, dan lazy-load elevasi.
- Validasi model GLB / source TypeScript tetap dijalankan melalui CI.
- Atlas PNG per kategori dan tone diverifikasi setelah job generator menghasilkan semua file.

## Keterbatasan
Prototipe ini belum dapat diklaim fotorealistis 1:1. Mesh MakeHuman yang dipakai masih artistik, bukan foto-scan tangan manusia. Performa GPU HP fisik juga belum diuji secara langsung. V11 berfokus pada ketajaman fallback 360°, koreksi kuku, dan stabilitas pemuatan.
