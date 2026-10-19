# Spesifikasi Responsive Mobile-First

## Ukuran uji

| Viewport | Tujuan | Risiko |
|---|---|---|
| 320 × 640 | Android kecil | CTA dan nama produk terpotong |
| 360 × 800 | Android umum | Bottom sheet menutupi konten |
| 375 × 812 | iPhone kecil | Safe area, header, gesture |
| 390 × 844 | Baseline desain | Konsistensi antarhalaman |
| 430 × 932 | HP lebar | Komposisi dan ruang kosong |
| 768 × 1024 | Tablet portrait | Perubahan grid |
| 1024 × 768 | Tablet landscape | Sheet vs sidebar |
| 1440 × 900 | Desktop | Konten tidak terlalu meregang |

## Pola grid

- Homepage: satu hero berkolom tunggal di mobile; dua kolom editorial di desktop bila cocok.
- Katalog: dua kolom produk pada 360–430 px, satu kolom jika 320 px dan hasil audit keterbacaan membutuhkan; tablet 3–4 kolom.
- Detail produk: galeri di atas informasi pada mobile; desktop dua kolom (galeri kiri, info kanan).
- Studio: area canvas di atas, bottom sheet bawah pada mobile; canvas kiri dan kontrol kanan pada desktop.
- Checkout: satu kolom mobile; desktop formulir kiri dan ringkasan sticky kanan.
- Owner: daftar kartu di mobile; tabel desktop dengan kolom yang dapat disortir.

## Perilaku sticky

- Bottom nav menempel di bawah dan memperhitungkan safe inset.
- Studio hanya mempertahankan satu CTA sticky penting, sisanya di sheet.
- Saat keyboard muncul, sticky CTA jangan menutup input atau menyebabkan scroll-jank.
- Scroll hanya terjadi pada satu kontainer utama per halaman bila memungkinkan; hindari nested scroll tanpa alasan.

## Responsiveness bukan hanya ukuran

- Perhatikan pointer coarse/fine: hover tidak boleh satu-satunya jalan ke aksi.
- Orientasi lanskap: alihkan Studio ke pembagian kiri/kanan bila tinggi layar sempit.
- Touch-action di canvas tidak boleh merusak scroll seluruh halaman; atur mode gesture hanya di area scene.
- Jika pengguna menambah ukuran teks sistem, kontrol harus turun ke baris berikutnya atau panel dapat di-scroll.

## Pengujian manual wajib

Cek setiap page pada viewport di atas, lalu di iPhone Safari dan Chrome Android: tekan semua CTA, buka bottom sheet, gunakan keyboard, putar orientasi, zoom, scroll jauh, kembali, serta refresh dengan query URL.
