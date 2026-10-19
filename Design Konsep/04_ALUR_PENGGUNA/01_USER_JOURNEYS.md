# User Journeys dan Jobs To Be Done

## Persona kerja (hipotesis, bukan hasil wawancara)

1. **Pembeli eksplorasi:** ingin menemukan aksesori/stiker yang sesuai gaya; bingung bila pilihan terlalu banyak.
2. **Pembeli personalisasi:** ingin menempatkan charm/stiker sesuai ide sendiri lalu yakin dengan hasil.
3. **Pembeli cepat:** sudah tahu produk; ingin checkout cepat tanpa merancang rumit.
4. **Owner operasional:** ingin mengetahui pesanan masuk, pembayaran, spesifikasi produksi, dan stok.

## Journey A: Jelajah → Custom → Checkout

| Tahap | Tujuan pengguna | Halaman | Risiko UX | Respons desain |
|---|---|---|---|---|
| Temukan | Memahami toko dan produk | Beranda/Katalog | Hero terlalu konseptual | CTA + kategori jelas |
| Evaluasi | Melihat harga, bahan, varian | Detail Produk | Harga tersembunyi | Info utama dekat gallery |
| Pilih | Memulai dari desain siap pakai | Studio | Terlalu banyak tools | Preset default, sheet kontekstual |
| Edit | Atur charm/stiker | Studio | Drag sulit, kamera ikut berputar | Mode berbeda + tombol alternatif |
| Review | Periksa harga dan visual | Studio/Keranjang | Konfigurasi hilang | Thumbnail + ringkasan item |
| Beli | Melengkapi alamat/pembayaran | Checkout | Form panjang dan biaya berubah | Form fokus, total jelas |
| Pantau | Tahu status produksi/kirim | Pesanan | Status uang vs produksi ambigu | Timeline dua status jelas |

## Journey B: Lanjutkan Desain

`Login → Akun → Desain Tersimpan → Edit 3D → Simpan → Keranjang`

Kriteria: model, bahan, jumlah ornamen, posisi, layer, ukuran harus kembali. Jika versi aset berubah, sistem memberi opsi yang jelas; tidak boleh diam-diam mengganti desain.

## Journey C: Beli Stiker dari HP

`Katalog → Stiker HP → Detail → Phone Canvas → pilih casing polos/transparan → pilih warna (jika polos) → tambah stiker → atur posisi → review → bayar`

Kriteria: pembeli memahami bahwa HP adalah media preview. Jika yang dijual hanya stiker, total tidak mencakup HP/casing. Area kamera selalu aman.

## Journey D: Owner dari HP

`Login owner → Dashboard → Pesanan perlu diproses → Detail Order → Tinjau preview & production sheet → Ubah status → Input resi → Selesai`

Kriteria: owner dapat memahami permintaan custom tanpa bertanya kembali; tidak perlu membuka desktop untuk tugas harian seperti melihat dan mengubah status pesanan. Tugas presisi model/anchor boleh tetap menjadi pengalaman desktop terbaik.

## Skenario pengujian manusia

- Tanpa instruksi, temukan dan kustom satu gelang dengan dua charm lalu simpan.
- Pilih stiker HP transparan, letakkan dua stiker tanpa menutupi kamera.
- Kembali ke keranjang setelah mengedit desain dan pastikan total benar.
- Cari status pembayaran pending dan jelaskan apa yang harus dilakukan.
- Owner membuka pesanan dan menyebutkan daftar komponen serta ukuran yang perlu diproduksi.

Catat keberhasilan, waktu, salah ketuk, dan kebingungan. Jangan mengganti metrik keberhasilan dengan opini bahwa layar “sudah premium”.
