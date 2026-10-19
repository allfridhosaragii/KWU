# QA Report: Procedural Asset Pack v2

## Lulus
- Export GLB 2.0 dan header BIN/JSON valid pada 21 model, diaudit lewat script.
- Pemeriksaan statis delapan model utama lulus dengan ukuran relatif ringan.
- Build TypeScript tanpa error.
- 168 pemeriksaan route × viewport dan empat alur demo (320, 390, 768, 1440 px).
- 105 pemeriksaan untuk pilihan 13 varian pada 390, 768, 1440 px, fallback 2D, penyimpanan desain, dan tidak adanya JS runtime error.

## Tidak diuji atau belum memenuhi standar
- WebGL 2 renderer fisik: Chromium lingkungan terbatasi tidak mempunyai konteks WebGL 2.
- Uji FPS 30/60 real-device: belum berjalan.
- Fotoreal 1:1 terhadap barang: tidak dapat dibuktikan tanpa multi-angle, scan, dan calibrated material.
- Casing dan stiker produksi: hanya prototipe visual.

## Bug yang ditemukan lalu diperbaiki
- Produk tas awal berupa handbag krem, diganti backpack hitam mengikuti referensi frontal.
- Botol awal silinder grafit, diganti profil stainless + cap hitam + carabiner.
- Hand awal dari bola/cylinder terpisah, diganti continuous surface.
- Perangkat Apple sebelumnya satu model generik, kini spesifik 13 model dan opsi warna.
- MacBook hinge shader sebelumnya memutar komponen terlalu banyak; dibatasi ke komponen lid/screen.
- Saat WebGL tidak tersedia, perubahan deviceModel sekarang mengubah fallback WebP sesuai pilihan.

## Risiko produksi tersisa
- Konfigurasi model harus diverifikasi dengan model Blender lengkap, bukan hanya mesh prosedural.
- Warna HDR/PBR ditentukan ketika pipeline Three.js/R3F produksi aktif.
- Viewer demo custom glTF ringan mungkin belum mendukung semua struktur glTF/texture production; migrasi ke loader Three.js direkomendasikan.
