# KWU — V12 Audit Fungsi dan Tombol

## Tujuan
Seluruh tombol dan fitur yang dapat berfungsi tanpa backend dikerjakan sebagai alur demonstrasi nyata, disimpan di localStorage. Pembayaran, akun sungguhan, pengiriman email, manajemen pelanggan lintas perangkat, dan sinkronisasi database tidak diaktifkan secara palsu.

## Peningkatan
- Form editor delapan produk demo, nama, deskripsi, harga, dan stok tersimpan.
- Form pengaturan nama toko dan email kontak demo tersimpan dan ditampilkan di halaman Bantuan.
- Hak akses role owner diuji sebelum perubahan inventori, produk, dan status pesanan.
- Konfirmasi sebelum menghapus alamat.
- Harga SKU berubah di katalog setelah owner menyimpan pengeditan.
- Menjaga navigasi 21 model 3D owner, delapan studio, dan lima tone kulit.

## Cakupan tes otomatis
- 42 route pada setiap viewport: 320, 390, 768, dan 1440 piksel.
- Alur studio, ornament, tone kulit, simpan desain, keranjang, dan checkout demo.
- Akses owner, editing produk, perbarui stok, pengaturan toko, kontak bantuan.
- Buku alamat, profil, dan pengembalian perubahan katalog.
- JavaScript console exceptions dan overflow horizontal.

## Batasan yang belum dapat diklaim
- Autentikasi production-grade: belum ada
- Pembayaran sungguhan: belum ada
- Email reset password: belum ada
- Sinkronisasi pesanan antar-perangkat: belum ada
- Real-time WebGL GPU seluruh jenis HP: belum dapat diklaim hanya dari CI Chromium
- Preview 360° prarender: perubahan ornament atau material di UI belum seluruhnya tercermin dalam hasil render per-frame. Konfigurasi disimpan sebagai data desain.

## Rekomendasi produksi
Implementasikan backend Next.js/API, PostgreSQL, identitas pengguna berbasis server, verifikasi pembayaran Midtrans, database pesanan nyata, penanganan pengiriman dan rendering GLB realtime sebelum peluncuran sebagai toko sungguhan.
