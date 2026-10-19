# Ikonografi, Fotografi, Ilustrasi, dan Aset UI

## Ikon

Rekomendasi satu library konsisten (misal Lucide): outline dengan stroke konsisten; ukuran tampak 18–22 px di tombol, hit area tetap ideal 44 px. Jangan mencampur ikon solid iOS, emoji, dan outline Lucide di satu navigasi.

Nama aksi penting harus disertai label: Simpan, Reset, Ubah ukuran, Tambah stiker, Bayar. Ikon Heart boleh dipakai tanpa label visual di product card jika screen reader tetap diberi nama jelas.

## Fotografi

- Produk harus mendominasi, background netral dan tidak berbenturan dengan warna item.
- Gunakan 1 atau 2 arah cahaya konsisten lintas katalog.
- Foto hasil custom dan thumbnail 3D perlu framing serupa agar tidak terasa produk berbeda.
- Foto tangan/manekin menonjolkan ukuran dan penggunaan produk, bukan wajah atau komposisi yang tidak relevan.
- Jangan memakai foto referensi kompetitor sebagai aset final.

## Ilustrasi

Gunakan ilustrasi garis sederhana hanya pada empty state, bantuan interaksi, dan petunjuk gesture. Ilustrasi tidak perlu menjadi latar belakang seluruh halaman.

## 3D vs foto nyata

- Foto nyata diprioritaskan pada kampanye dan katalog bila tersedia.
- Preview 3D aktif hanya di Studio, detail produk opsional, serta pesanan ketika pengguna menekan “Lihat 3D”.
- Area preview memberi penanda “Pratinjau 3D”; jangan menyamakan gambar render dengan foto barang jadi jika produksi akhir belum pasti.
- Bahan metalik dan casing transparan memerlukan pembanding cahaya netral agar warna tidak menipu.

## Fallback

Jika foto/model gagal: pertahankan aspek rasio placeholder, tampil nama produk, deskripsi singkat, dan tombol coba lagi apabila relevan. Jangan memunculkan ikon broken image browser sebagai UI utama.

## Panduan ekspor aset Figma

- Ikon diekspor SVG dari komponen legal/berlisensi jelas.
- Foto produk WebP/AVIF dengan resolusi sesuai ukuran layar dan `srcset`/image optimization.
- Preview card statis; sumber aset GLB dikelola di pipeline terpisah.
- Nama file konsisten: `product-id__angle__variant__v1.webp`.
