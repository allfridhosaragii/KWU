# Apple Device Research — KWU 3D Asset Planning

## Catatan penting
Dokumen ini dipakai untuk **membuat aset yang sangat mirip**, bukan untuk mengklaim replika legal atau produksi resmi Apple. Untuk hasil 1:1 secara teknis, kita tetap membutuhkan referensi multi-sudut tambahan, ukuran lengkap per model, dan validasi visual saat modeling.

## Scope yang direkomendasikan
### iPhone family
Prioritas fase 1:
- iPhone 17
- iPhone 17 clear case
- iPhone 17 plain case

Prioritas fase 2:
- iPhone Air
- iPhone 17e
- varian Pro / Pro Max jika benar-benar dibutuhkan untuk katalog

### iPad
Prioritas fase 1:
- iPad Pro 11-inch
- iPad Pro 13-inch

### MacBook
Prioritas fase 1:
- MacBook Air 13-inch
- MacBook Air 15-inch

Prioritas fase 2:
- MacBook Pro 14-inch
- MacBook Pro 16-inch

## Official research findings
### iPhone 17
Apple menyebutkan iPhone 17 memiliki ukuran tinggi 149,6 mm, lebar 71,5 mm, ketebalan 7,95 mm, dan berat 177 gram. Warna resminya adalah Black, White, Mist Blue, Sage, dan Lavender. Desain yang disebutkan meliputi bodi aluminium, Ceramic Shield 2 di depan, serta color-infused glass back.【turn422730search1】

Selain itu, Apple juga menekankan bahwa iPhone 17 memakai layar 6,3 inci, tombol Action, Dynamic Island, dan desain ujung berkontur dengan tepi lebih tipis.【turn422730search6】

#### Implikasi modeling
- Base body harus memakai sudut membulat dengan fillet halus.
- Backplate kaca berwarna harus sedikit lebih reflektif dibanding frame.
- Kamera belakang memakai sistem dual camera layout pada sudut kiri atas.
- Tombol samping, action button, dan port harus menjadi detail hard-surface yang presisi.
- Perlu dua casing untuk customizer stiker: clear case dan plain silicone-like case.

### iPad Pro
Apple menampilkan iPad Pro dalam ukuran 11 inci dan 13 inci.【turn731012view1】

#### Implikasi modeling
- Buat satu master language design, lalu turunkan menjadi dua ukuran.
- Fokus utama untuk web customizer stiker adalah permukaan belakang, kamera, sudut, dan frame.
- Area printable zone harus dibatasi dari kamera dan tepi perangkat.

### MacBook Air
Apple menunjukkan MacBook Air dalam ukuran 13-inch dan 15-inch.【turn731012view2】 Warna yang disebutkan Apple untuk MacBook Air adalah Sky Blue, Silver, Starlight/Putih Pucat Metalik, dan Midnight/Biru Temaram.【turn422730search2】【turn422730search4】

#### Implikasi modeling
- Untuk customizer stiker, yang paling penting adalah tampak belakang lid (cover luar), ketebalan bodi, chamfer tepi, bukaan engsel, dan interior dasar.
- Buat rig sederhana untuk membuka-tutup layar.
- Surface stiker cukup dipusatkan pada outer lid, bukan seluruh body.

### MacBook Pro
Apple menampilkan MacBook Pro dalam ukuran 14-inch dan 16-inch.【turn731012view3】【turn731012view4】

#### Implikasi modeling
- Jika dipilih sebagai produk lanjutan, buat language yang lebih tebal dari Air.
- Pertahankan fokus pada lid luar untuk kebutuhan stiker.

## Keputusan teknis yang direkomendasikan
1. **Jangan buat semua model Apple sekaligus di fase pertama.**
2. Fase 1 paling realistis untuk web KWU:
   - iPhone 17 + casing plain + casing clear
   - iPad Pro 11 dan 13
   - MacBook Air 13 dan 15
3. Setelah stabil dan lulus QA mobile, baru tambah varian lain.

## Data lanjutan yang masih perlu dikumpulkan
- Multi-angle photos per device.
- Detail kamera belakang close-up.
- Detail tombol samping dan port.
- Official or measured corner radius approximation.
- Surface reflectance reference di pencahayaan netral.
