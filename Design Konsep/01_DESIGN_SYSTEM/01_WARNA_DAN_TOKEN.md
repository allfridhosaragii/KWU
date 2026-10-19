# Sistem Warna, Kontras, dan Token

## Filosofi

Warm Modern Atelier: warna netral terang membuat produk terlihat apa adanya; terracotta menyatakan tindakan utama; sage mendukung status aman atau aksen yang tenang; copper dipakai sebagai detail. Latar rendering 3D harus dikalibrasi terpisah agar foto/perangkat berwarna netral tidak tampak terlalu kuning.

## Palet dasar final v1

| Token basis | Nama | HEX | Penggunaan utama |
|---|---|---|---|
| `warm-ivory` | Warm Ivory | `#FAF7F2` | Latar seluruh toko |
| `soft-white` | Soft White | `#FFFCF8` | Card, sheet, input |
| `oat-beige` | Oat Beige | `#F3EAE0` | Section alternatif, preview |
| `terracotta` | Terracotta | `#8F503C` | CTA dan state aktif |
| `terracotta-pressed` | Deep Terracotta | `#743E2E` | Pressed/active |
| `sage-olive` | Sage Olive | `#64735B` | Aksen sekunder/status sesuai konteks |
| `copper` | Copper | `#C78962` | Dekorasi, ilustrasi |
| `espresso` | Espresso | `#302822` | Teks utama |
| `muted-taupe` | Muted Taupe | `#695C52` | Teks penjelasan |
| `border-sand` | Border Sand | `#DBCEC1` | Divider/dekorasi |
| `border-strong` | Strong Sand | `#8D715F` | Input border kuat |
| `focus-brown` | Focus Brown | `#79513F` | Focus ring |
| `success-dark` | Forest | `#416C50` | Status sukses |
| `error-dark` | Error Red | `#A6423D` | Status gagal |

## Rasio kontras terhitung (WCAG relative luminance)

| Warna depan | Background | Rasio | Keputusan |
|---|---|---:|---|
| Espresso `#302822` | Warm Ivory `#FAF7F2` | **13,53:1** | Teks reguler lolos AA/AAA |
| White `#FFFFFF` | Terracotta `#8F503C` | **6,21:1** | CTA putih lolos AA |
| Muted Taupe `#695C52` | Warm Ivory | **6,04:1** | Teks sekunder lolos AA |
| White `#FFFFFF` | Sage Olive `#64735B` | **5,07:1** | Teks kecil bisa, bila perlu |
| Espresso | Copper `#C78962` | **4,95:1** | Teks normal lolos AA |
| White | Copper `#C78962` | **2,92:1** | **Jangan** memakai teks putih biasa |
| Terracotta | Warm Ivory | **5,81:1** | Link/teks penting lolos AA |

Target WCAG 2.2 AA: teks biasa setidaknya 4,5:1; teks besar setidaknya 3:1; indikasi visual UI nonteks penting setidaknya 3:1 dalam kondisi yang dipersyaratkan. Warna `border-sand` dekoratif **tidak** otomatis cocok sebagai satu-satunya batas input. Gunakan `border-strong`/focus ring yang terverifikasi terhadap background sebenarnya.

## Token semantik

| Token UI | Nilai Light | Tujuan |
|---|---|---|
| `color.bg.canvas` | warm-ivory | Background utama |
| `color.bg.surface` | soft-white | Card/modal |
| `color.bg.subtle` | oat-beige | Area netral pendukung |
| `color.text.primary` | espresso | Isi/heading |
| `color.text.secondary` | muted-taupe | Metadata dan caption |
| `color.action.primary.bg` | terracotta | CTA utama |
| `color.action.primary.text` | white | Teks CTA |
| `color.action.primary.pressed` | terracotta-pressed | State pressed |
| `color.action.secondary.text` | terracotta | Outline/quiet button |
| `color.status.success` | success-dark | Label sukses |
| `color.status.danger` | error-dark | Label error |
| `color.border.decorative` | border-sand | Divider |
| `color.border.control` | border-strong | Input/focus yang terlihat |

## Aturan pemakaian

1. Dalam satu viewport, hanya **satu CTA utama** yang paling menonjol.
2. Terracotta bukan background setiap card; gunakan sebagai tombol, chip terpilih, dan link penting.
3. Sage jangan digunakan untuk seluruh teks informasi karena dapat terasa terlalu monoton.
4. Copper lebih cocok untuk aksen visual; pakai teks espresso jika dipakai sebagai background.
5. Status sukses/pending/error tidak boleh bergantung pada warna saja. Sertakan ikon dan teks.
6. Dalam 3D Studio, warna lingkungan harus netral agar material silver/gray/transparent tetap tepat.
7. Dark mode belum menjadi requirement final. Jangan memalsukan dark mode dengan membalik semua warna otomatis. Jika dibuat nanti, audit ulang seluruh rasio.

## Penamaan variabel Figma

`Color/Canvas/Default`, `Color/Surface/Default`, `Color/Text/Primary`, `Color/Text/Secondary`, `Color/Action/Primary`, `Color/Action/Pressed`, `Color/Status/Success`, `Color/Status/Error`, `Color/Border/Control`.

## Rujukan

https://www.w3.org/TR/WCAG22/#contrast-minimum
https://www.w3.org/TR/WCAG22/#non-text-contrast
