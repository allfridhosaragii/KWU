# Desain Tersimpan, Thumbnail, dan Preview Konsisten

## Mengapa ini kritis

Pembeli melihat desain pada Studio, kemudian di keranjang dan pesanan; owner perlu melihat desain final yang sama untuk produksi. Screenshot saja bukan sumber kebenaran. Sumber kebenaran adalah **konfigurasi terstruktur berversi**, sedangkan thumbnail membantu manusia membaca pesanan dengan cepat.

## Data representasi UI

- `schemaVersion` dan `assetVersion`.
- Produk dasar + varian material/warna/ukuran.
- Komponen tambahan: ID dan urutan.
- Posisi: `anchorId`/jalur, atau permukaan UV (`u`,`v`) untuk stiker.
- Rotasi dan skala pada batas produksi yang diketahui.
- Urutan layer stiker jika overlap diizinkan.
- Total harga snapshot disimpan saat order terbentuk; rancangan UI menampilkan beda harga draft vs final jika ada.

## Preview thumbnail

| Konteks | Bentuk preview | Tindakan |
|---|---|---|
| Desain Tersimpan | Foto/render thumbnail 4:5 atau 1:1 | Lanjut Edit |
| Keranjang | Thumbnail kotak 1:1 | Edit Desain |
| Detail Pesanan pembeli | Thumbnail final + tombol Lihat 3D | View only |
| Owner order | Thumbnail final + konfigurasi produksi | Lihat 3D read-only |

## Alur simpan

1. Edit desain pada scene.
2. Tekan Simpan atau autosave jika kebijakan mengizinkan.
3. Sistem validasi konfigurasi dan mengembalikan status berhasil yang nyata.
4. UI menampilkan “Tersimpan” dan thumbnail baru.
5. Jika gagal, status tidak berubah ke sukses; tampil Coba Lagi.

## Kondisi konflik

- Produk katalog berubah: desain lama tetap memakai versi/snapshot yang diketahui; tampil pesan kalau elemen tidak lagi tersedia untuk pembelian baru.
- Komponen stok habis: desain dapat dipreview, tetapi checkout harus menampilkan opsi penggantian atau perubahan yang jelas.
- User mengedit dari dua perangkat: tampil konflik versi jika perlu, jangan menimpa diam-diam.
- Offline: perubahan selama sesi bisa dijaga lokal, status bertuliskan “Belum tersinkron”, bukan “Tersimpan”.

## UX design library

Grid thumbnail, tanggal edit, nama desain yang bisa diubah, aksi Duplikat, Lanjut Custom, Hapus. Berikan undo/konfirmasi untuk aksi hapus. Tekstur dan warna model harus kompatibel dengan hasil visual sebelumnya sehingga customer dan owner tidak mendapat interpretasi berbeda.

## Acceptance

- [ ] Memuat desain kembali menjaga urutan/posisi semua elemen.
- [ ] Thumbnail terbarui setelah simpan.
- [ ] Cart dan order memakai konfigurasi yang sesuai.
- [ ] Fallback gambar tersedia tanpa WebGL.
- [ ] Versi aset lama tetap terlacak pada pesanan historis.
- [ ] Customer tidak dapat mengedit snapshot final order setelah pembayaran tanpa alur revisi terdefinisi.
