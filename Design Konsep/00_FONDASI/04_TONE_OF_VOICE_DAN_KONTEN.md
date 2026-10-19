# Voice, Microcopy, dan Standar Konten

## Karakter penulisan

Hangat, personal, ringkas, santun, tidak terlalu formal. Kalimat UI harus membantu pengguna memahami tindakan berikutnya. Bahasa utama Indonesia. English editorial tagline boleh dipakai terbatas, tetapi jangan mencampur istilah pada label fungsi penting.

## Aturan kalimat

- Gunakan kata kerja untuk CTA: “Mulai Custom”, “Simpan Desain”, “Lihat Pesanan”.
- Aksi merusak data harus spesifik: “Hapus Desain”, bukan sekadar “Oke”.
- Status pembayaran harus faktual: “Menunggu pembayaran”, bukan “Pesanan sukses” sebelum terverifikasi.
- Harga memakai format Indonesia, contoh `Rp85.000`; hindari hasil harga placeholder saat final release.
- Gunakan `Anda` atau bentuk netral sesuai keputusan brand, jangan berganti acak antara `kamu`, `Anda`, dan `sobat`.
- Istilah “Studio 3D” konsisten di menu dan judul utama; jenis produk memakai nama Indonesia.

## Kamus istilah UI

| Pakai | Hindari | Alasannya |
|---|---|---|
| Mulai Custom | Generate Now | Lebih mudah dipahami |
| Desain Tersimpan | My Creative Assets | Jelas untuk pembeli |
| Pindahkan ornamen | Transform object | Tidak teknis |
| Kembali ke tampilan awal | Reset camera transform | Mudah dipahami |
| Menunggu pembayaran | Pembayaran dalam proses sukses | Hindari ambigu |
| Lihat status pesanan | Trace fulfillment | Konsisten |
| Casing transparan | Case glass | Tepat secara material |

## Template pesan penting

| Keadaan | Teks utama | Tindakan |
|---|---|---|
| Katalog kosong | “Belum ada produk yang cocok.” | “Hapus filter” |
| Wishlist kosong | “Belum ada yang kamu simpan.” | “Lihat koleksi” |
| Studio gagal memuat | “Preview 3D belum bisa dibuka.” | “Coba lagi” / “Lihat gambar” |
| Aset belum ada | “Model ini belum tersedia dalam 3D.” | “Lihat detail produk” |
| Desain tersimpan | “Desain berhasil disimpan.” | “Lihat desain” |
| Pembayaran pending | “Kami sedang menunggu konfirmasi pembayaran.” | “Lihat instruksi” |
| Kesalahan checkout | “Periksa alamat dan metode pembayaran.” | “Perbaiki data” |
| Pesanan owner | “Pesanan baru siap ditinjau.” | “Buka pesanan” |

## Pola error yang baik

**Apa yang terjadi → Mengapa jika diketahui → Apa yang bisa dilakukan.** Jangan menyalahkan pengguna, jangan menampilkan error database mentah, dan jangan membuat pesan sukses palsu.

## Aturan detail produk

Setiap kartu wajib memuat: nama, harga awal atau rentang jika bervariasi, foto/thumbnail, tautan detail. Detail SKU menambahkan: komponen utama, varian, ukuran, durasi produksi jika sudah tersedia, kebijakan pengiriman, dan penjelasan apa yang benar-benar dibeli. Untuk stiker, nyatakan jelas bahwa perangkat 3D hanya media pratinjau kecuali dijual sebagai item terpisah.
