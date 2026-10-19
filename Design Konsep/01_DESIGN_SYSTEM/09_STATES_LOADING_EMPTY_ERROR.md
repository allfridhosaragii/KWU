# State UI: Loading, Empty, Error, Offline, Success

## Matriks umum

| Tipe | Tampilan | Konten | Tindakan |
|---|---|---|---|
| Loading | Skeleton ukuran stabil | “Memuat koleksi…” bila menunggu lama | Boleh kembali |
| Empty | Ilustrasi lini halus | Penjelasan apa yang kosong | CTA ke langkah relevan |
| Error | Icon dan pesan singkat | Apa gagal dan apa yang tetap aman | Coba lagi / bantuan |
| Offline | Banner lembut | Koneksi terputus; pekerjaan lokal jika ada | Coba sinkron ulang |
| Success | Status singkat | Hasil tindakan yang nyata | Lihat hasil |
| Permission | Pesan netral | Akses tidak tersedia | Kembali ke akun / login |

## Spesifik 3D Studio

- **Aset belum mulai dimuat:** thumbnail produk dan tombol “Buka 3D”.
- **Aset sedang dimuat:** progress yang bermakna apabila tersedia, tetap tampil thumbnail dan nama.
- **Gagal WebGL/asset:** tampil gambar 2D; konfigurasi sederhana masih bisa dilihat bila produk mengizinkan, tetapi fungsi 3D yang tidak tersedia harus disebut dengan jelas.
- **GPU context lost:** tampil pesan dan retry untuk membangun scene ulang; jangan menghapus desain tersimpan.
- **Desain belum tersimpan saat keluar:** dialog “Simpan sebelum keluar?” dengan Simpan, Buang, Batal.
- **Stiker keluar area valid:** garis batas dan hint “Geser kembali ke area yang bisa ditempeli”.

## Spesifik transaksi

- **Stok berubah:** validasi ulang dan perlihatkan opsi pengganti atau hapus item.
- **Harga berubah:** tampil rincian perubahan dan minta persetujuan sebelum membayar.
- **Payment pending:** jangan menyatakan sukses; beri instruksi dan status.
- **Webhook terlambat:** status “Kami sedang memeriksa pembayaran”, bukan otomatis “Gagal”.
- **Order berhasil:** tampil nomor pesanan dan CTA detail pesanan.

## Spesifik owner

- Tidak ada pesanan: “Belum ada pesanan pada filter ini.”
- Data tidak tersedia: jelaskan apakah error jaringan atau hasil filter kosong.
- Save produk sukses: tampil toast singkat dan status draft/published terlihat pada daftar.
- Konflik edit: jelaskan perubahan terbaru dan sediakan cara memuat ulang tanpa diam-diam menimpa.

## Ketentuan visual

State sukses menggunakan teks + ikon, bukan hanya hijau. State error harus terbaca dengan kontras memadai. Skeleton tidak boleh berkedip berlebihan. Status sensitif keuangan selalu punya bahasa yang tidak ambigu.
