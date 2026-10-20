# KWU V13: Audit Kontrol Studio 360°

Sumber masalah: 360° memakai foto sudut-sudut kamera yang sudah dirender. Sebelumnya slider perubahan ornamen, warna, posisi, ukuran, jari, dan kualitas mengubah state desain tanpa memberikan feedback visual yang jelas. Selain itu renderer WebGL tidak memanggil resize setelah kualitas diganti.

Perbaikan:
- Preview ornamen 2D yang diberi label eksplisit di atas model 360°, sinkron dengan pilihan simbol, warna, posisi, skala, rotasi, dan jari.
- Slider posisi manekin dipahami sebagai perubahan sudut kamera yang tersedia, bukan rigging.
- Kualitas rendah tidak memakai still 1536 px, auto/tinggi memakai still saat tersedia.
- Renderer WebGL menerapkan perubahan resolusi ketika pilihan kualitas berubah.
- Dokumen menjelaskan bahwa overlay 360° tidak memiliki presisi pemasangan manufacturing.
- Navigasi owner, lima tone kulit, katalog, checkout demo dan aset GLB tetap ada.

Pengujian: CI lama untuk semua route pada viewport 320, 390, 768, 1440 tetap aktif. Ditambah pengujian kondisi visual kontrol 360°, termasuk posisi, ukuran, warna, rotasi, jenis ornamen dan perpindahan jari. Tidak mengklaim material produk asli sudah simulasi fisika 3D.
