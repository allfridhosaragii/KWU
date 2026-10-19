# Thumbnail Desain, Foto Pesanan, dan Versi Aset

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Kenapa diperlukan
Desain yang disimpan perlu preview yang terlihat sama di daftar desain, cart, order detail dan dashboard owner. Namun screenshot canvas bukan sumber kebenaran bentuk/ukuran untuk produksi.

## Arsitektur preview
- Saat save, editor mengirim serialisasi desain lengkap. `thumbnail` dapat dihasilkan client dengan capture satu frame terkontrol atau server render service di fase berikutnya.
- Untuk MVP: render thumbnail pada device user setelah scene stabil, ukuran target 512–768 px, lossy WebP/AVIF atau PNG sesuai alpha; jangan render besar terus menerus.
- Upload preview via signed URL R2 ke key privat/terotorisasi; backend menyimpan metadata file, owner memiliki akses sesuai policy.
- Bila export client gagal (termasuk privacy settings WebGL), simpan desain dulu dan beri placeholder. Thumbnail bisa diregenerasi kemudian menggunakan scene config yang sama.

## Asset versioning
Reproducibility membutuhkan `assetVersion`, `rulesVersion`, `designSchemaVersion`, preset IDs dan parameter transform. Untuk order finalized jangan rewrite snapshots saat produk diedit atau GLB lama dihapus.

## Export untuk printing
Stiker memerlukan master artwork 2D pada dimensi cetak dan bleed. Ekspor harus berasal dari source illustration + posisi UV/logical layout, bukan JPEG thumbnail pada botol/macam-macam device.

## Audit visual
Kirim desain A, reload dengan browser B, tampilkan owner: cocokkan IDs, ukuran fisik, warna pilihan, jumlah komponen; thumbnail dibandingkan secara toleransi warna/angle.
