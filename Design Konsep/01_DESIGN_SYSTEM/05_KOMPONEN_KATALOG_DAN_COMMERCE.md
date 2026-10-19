# Komponen E-Commerce dan Konten Produk

## Product Card

Anatomi: `thumbnail rasio 4:5 atau 1:1` → `kategori bila membantu` → `nama produk maksimal 2–3 baris` → `harga` → `swatch/jumlah varian` → `aksi wishlist`. Area kartu harus mengarah ke detail produk. Hindari CTA ganda yang membuat target kecil.

### Ketentuan kartu

- Foto statis/thumbnail final; **jangan** menjalankan renderer WebGL per kartu.
- Thumbnail sesuai varian yang sedang dipilih, tetapi tetap jelas harga yang bersangkutan.
- Harga sejak/ rentang jika pilihan custom memengaruhi harga: contoh “Mulai Rp45.000”.
- Badge “Baru” atau “Custom” hanya ketika benar-benar memberi nilai informasi.
- Gambar tidak boleh melebihi batas modal mobile ketika diperbesar.

## Product Gallery

Urutan foto: hero nyata → sudut kedua → detail bahan → konteks skala → hasil custom contoh. Pada perangkat dengan layar sentuh, jelaskan jumlah gambar dan tampilkan indikator posisi. Zoom harus mungkin untuk material dan detail.

## Price Summary

- Tampilkan harga dasar dan biaya setiap komponen custom bila relevan.
- Tunjukkan total item sebelum pengiriman; ongkir dijelaskan saat alamat/metode dipilih.
- Perubahan harga akibat swatch, ornamen, atau jumlah diberi feedback yang tidak mengganggu.
- Harga yang tampil harus bersumber dari konfigurasi tervalidasi saat checkout.

## Cart Item

Wajib memuat thumbnail hasil custom, nama, jumlah, varian, konfigurasi ringkas, harga, edit desain, dan hapus. Pada keranjang mobile, gunakan kartu satu kolom daripada tabel. Setelah revisi desain, thumbnail dan ringkasan harus diperbarui.

## Checkout Summary

Jelas memisahkan subtotal, ongkir, diskon terverifikasi, biaya tambahan jika ada, dan total. CTA utama: “Bayar Sekarang”. Jangan ada biaya muncul mendadak setelah CTA ditekan. Untuk status pending, gunakan istilah akurat sesuai gateway.

## Status pesanan

| Status | Label pembeli | Visual |
|---|---|---|
| Belum dibayar | Menunggu pembayaran | Teks jelas, warna netral/amber dengan kontras teruji |
| Dibayar | Pembayaran diterima | Sage/Forest + ikon check |
| Diproses | Sedang dibuat | Status netral + timeline |
| Dikemas | Sedang dikemas | Timeline |
| Dikirim | Dalam pengiriman | Timeline + resi |
| Selesai | Pesanan selesai | Forest + tanggal |
| Dibatalkan | Pesanan dibatalkan | Error/neutral + alasan |

## Empty, loading, error

- Katalog loading memakai placeholder card dengan dimensi tetap.
- Keranjang kosong memiliki CTA ke katalog.
- Gagal memuat harga menyembunyikan CTA pembayaran dan menawarkan retry.
- Gagal thumbnail 3D memakai foto produk fallback dengan label “Pratinjau gambar”.

## Uji UX utama

- Dapat membedakan produk stiker dengan perangkat pratinjau.
- Bisa melihat biaya total tanpa menggali accordion panjang.
- Bisa kembali mengedit custom tanpa kehilangan keranjang.
- Wishlist tidak menghalangi navigasi detail kartu.
