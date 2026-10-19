# Tipografi dan Hierarki Teks

## Dua keluarga font

- **Cormorant Garamond**: display dan judul editorial besar. Bobot 400–600; hindari pemakaian pada input dan paragraf panjang.
- **Manrope**: seluruh body, tombol, harga, form, navigasi, informasi status, tabel, dan dashboard owner. Bobot 400–700.
- Fallback serif: `Georgia, 'Times New Roman', serif`. Fallback sans: `system-ui, -apple-system, 'Segoe UI', sans-serif`.
- Sumber: https://fonts.google.com/specimen/Cormorant+Garamond dan https://fonts.google.com/specimen/Manrope. Font dari Google Fonts memiliki opsi open-source, tetapi periksa metadata lisensi saat mengemas aplikasi. **Jangan membagikan file font tanpa izin.**

## Tipe skala mobile (390 CSS px)

| Style | Font | Size | Line-height | Weight | Penerapan |
|---|---|---:|---:|---:|---|
| `display-xl` | Cormorant | 52 px | 0,98 | 500 | Hero utama beranda |
| `display-lg` | Cormorant | 42 px | 1,02 | 500 | Opening section / About |
| `heading-1` | Manrope | 26 px | 1,20 | 650 | Judul halaman utility |
| `heading-2` | Manrope | 22 px | 1,27 | 650 | Section title |
| `heading-3` | Manrope | 18 px | 1,33 | 650 | Judul card/panel |
| `body-lg` | Manrope | 17 px | 1,56 | 400 | Intro pendek |
| `body` | Manrope | 16 px | 1,50 | 400 | Paragraf, formulir |
| `body-sm` | Manrope | 14 px | 1,50 | 400 | Keterangan dan metadata jelas |
| `label` | Manrope | 14 px | 1,30 | 600 | Input, button, status |
| `caption` | Manrope | 12 px | 1,50 | 500 | Metadata nonkritis |
| `overline` | Manrope | 11 px | 1,35 | 700 | Label editorial, letter spacing +0,08em |
| `price` | Manrope | 20 px | 1,20 | 700 | Harga utama |

Ukuran tersebut adalah desain awal; lakukan uji wrapping pada teks Indonesia, zoom 200%, dan text-size user. Hindari memaksa text-overflow ellipsis pada nama produk yang dibutuhkan untuk membedakan varian.

## Skala desktop

Hero display dapat naik bertahap ke 68–88 px; body tetap 16–18 px. Jangan sekadar meningkatkan semua ukuran dua kali. Perlebar area baca hingga sekitar 60–75 karakter per baris untuk paragraf.

## Cara memakai serif

- Beranda, Brand Story, pembuka Studio, dan heading promosi singkat.
- Tidak untuk: label kontrol, harga, tombol, badge, input, tabel, status pembayaran, laporan.
- Hindari Cormorant italic panjang; maksimal satu aksen editorial pada headline jika memang membantu.
- Jika hero bertabrakan dengan produk, pindahkan teks ke area tersendiri, bukan menambah shadow tebal.

## Pemformatan angka

- Rupiah: `Rp85.000`, `Rp1.250.000`. Pemakaian jarak setelah `Rp` harus konsisten; disarankan tanpa spasi pada komponen compact.
- Kuantitas: `2 item`, bukan `02 items`.
- Tanggal: `20 Oktober 2026`; waktu `14.30 WIB` jika tampil bagi pengguna Indonesia.
- Harga jangan memakai serif dekoratif yang membuat angka sulit dipindai.

## Pemeriksaan

- Nama produk dua baris tetap terbaca tanpa menggeser tombol secara tak terduga.
- Label input tetap terlihat ketika pengguna mengetik.
- Hirarki H1/H2/H3 tetap mengikuti struktur isi, tidak dipilih hanya karena ukuran font.
- Semantik dan aksesibilitas tetap dipertahankan di kode HTML.
