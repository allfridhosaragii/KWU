# Grid, Spacing, Ukuran, dan Safe Area

## Baseline

Frame desain utama Figma: **390 × 844 CSS px**. Ini ukuran acuan, bukan ukuran semua HP. Uji minimal 320, 360, 375, 390, 430, 768, 1024, 1440 px. Landscape dan device dengan punch-hole/notch harus diperiksa.

## Grid dan container

| Rentang | Susunan yang direkomendasikan | Margin | Gap |
|---|---|---:|---:|
| 320–359 | 1–2 kolom sesuai jenis konten | 16 px | 10–12 px |
| 360–599 | 4-column layout grid konseptual, katalog dua kartu | 16 px | 12 px |
| 600–767 | 6–8 kolom konseptual | 20–24 px | 16 px |
| 768–1023 | 8 kolom, sidebar bila relevan | 24–32 px | 20 px |
| 1024+ | 12 kolom, max-width content | 32–48 px | 24 px |

Untuk 3D Studio pada HP, scene tampil di atas sheet; pada desktop scene di kiri dan alat di kanan. Jangan memaksakan grid produk dua kolom untuk ukuran 320 px jika nama produk dan harga tidak terbaca.

## Spacing scale

`space-0=0` · `1=4` · `2=8` · `3=12` · `4=16` · `5=20` · `6=24` · `8=32` · `10=40` · `12=48` · `16=64` · `20=80` dalam px.

- Antar ikon dan teks: 8 px.
- Antarfield formulir: 16–20 px.
- Antarbagian form: 24–32 px.
- Antarsection landing: 48–80 px tergantung tinggi konten.
- Antarcard katalog: 12 px mobile; gunakan ratio gambar konsisten.

## Dimensi komponen

| Elemen | Ukuran dasar | Alasan |
|---|---|---|
| Tombol primary | tinggi 52 px | Area sentuh nyaman |
| Tombol secondary | tinggi 44–48 px | Fleksibel pada ruang terbatas |
| Input | tinggi 52 px | Mendukung label dan touch |
| Hit target ikon | ideal 44 × 44 px | Kesalahan sentuh rendah |
| Bottom nav | konten sekitar 64 px + safe inset | Area navigasi stabil |
| Bottom sheet radius | 24 px di sudut atas | Lembut dan kontemporer |
| Card radius | 12–16 px | Konsisten dengan bentuk foto |
| Form/card padding | 16–20 px | Ruang yang cukup |
| Modal desktop | lebar adaptif 480–640 px | Mudah fokus |

## Safe area dan keyboard

- Semua sticky bottom actions harus memperhitungkan `env(safe-area-inset-bottom)`.
- Saat keyboard virtual muncul, formulir harus bisa scroll dan tombol tidak tertutup.
- Bottom sheet tidak boleh mengunci 3D canvas yang sedang dipakai kecuali pengguna memang fokus ke setting.
- Hindari `100vh` kaku di mobile; gunakan strategi dynamic viewport height yang teruji.
- Konten tidak boleh tertutup bottom nav; sediakan padding bawah yang cukup.

## Batas area baca

Body artikel/kebijakan ditargetkan 60–75 karakter per baris pada layar lebar. Grafik laporan owner tidak boleh menyusut sampai label sumbu tak terbaca; sediakan detail tabel atau horizontal scroll terbatas bila diperlukan.
