# Sitemap 34 Template dan Navigasi

## Definisi hitungan

**34 template halaman inti** = 11 publik/toko + 4 autentikasi + 7 pembeli + 12 owner. Satu template customizer mencakup **8 scene/perilaku kategori**. URL editor baru/edit dan dokumen legal menggunakan template ulang sehingga jumlah URL aktual dapat lebih dari 34, tanpa dihitung sebagai desain halaman baru.

## Public/store (11)

1. `/` Beranda
2. `/shop` Katalog; filter kategori + kata kunci memakai query string
3. `/products/[slug]` Detail Produk
4. `/studio` Pilih Studio
5. `/studio/[type]/[productId]` Customizer 3D, delapan pengalaman
6. `/cart` Keranjang
7. `/checkout` Checkout
8. `/checkout/result` Hasil Pembayaran
9. `/help` Pusat Bantuan
10. `/about` Tentang Brand
11. `/legal/[slug]` Kebijakan

## Auth (4)

12. `/login` Login
13. `/register` Register
14. `/forgot-password` Lupa Password
15. `/reset-password` Reset Password

## Buyer account (7)

16. `/account` Akun Saya
17. `/account/designs` Desain Tersimpan
18. `/account/wishlist` Wishlist
19. `/account/orders` Riwayat Pesanan
20. `/account/orders/[id]` Detail Pesanan
21. `/account/addresses` Buku Alamat
22. `/account/profile` Profil dan Pengaturan

## Owner (12)

23. `/owner` Dashboard
24. `/owner/orders` Daftar Pesanan
25. `/owner/orders/[id]` Detail Pesanan
26. `/owner/products` Manajemen Produk
27. `/owner/products/new` dan `/owner/products/[id]/edit` Editor Produk (1 template)
28. `/owner/components` Library Komponen
29. `/owner/assets` Manajemen Aset 3D
30. `/owner/inventory` Manajemen Stok
31. `/owner/payments` Pembayaran
32. `/owner/customers` Pelanggan
33. `/owner/reports` Laporan
34. `/owner/settings` Pengaturan Toko

## Navigasi utama

Pembeli: **Beranda · Belanja · Studio · Keranjang · Akun**. Owner: **Ringkasan · Pesanan · Produk · Lainnya**. Auth dan checkout memakai header fokus; Studio memakai header scene khusus dan bottom sheet kontekstual.

## Route bukan halaman tersendiri

- Filter katalog: `/shop?category=ring&sort=latest`.
- Kebijakan spesifik: `/legal/privacy`, `/legal/returns` memakai satu template.
- Preset, warna, ukuran, posisi, material, pilihan jari/casing/stiker: interaksi lokal Studio.
- Edit alamat, pengaturan kecil, pilih pembayaran: form/section dalam halaman induk, bukan wajib route baru.

## Matriks hak akses

| Bagian | Publik | Login Pembeli | Login Owner |
|---|---|---|---|
| Browse katalog | Ya | Ya | Ya bila diizinkan |
| Preview Studio | Ya bila mode guest aktif | Ya | Ya untuk QA produk |
| Simpan ke akun | Login diminta | Ya | Tergantung preview internal |
| Checkout | Login jika kebijakan memerlukan | Ya | Tidak sebagai owner kecuali akun customer terpisah |
| Pesanan pribadi | Tidak | Miliknya sendiri | Akses operasional melalui owner |
| Owner dashboard | Tidak | Tidak | Ya |

Pemblokiran route harus dicek server, tidak cukup hanya menyembunyikan menu.
