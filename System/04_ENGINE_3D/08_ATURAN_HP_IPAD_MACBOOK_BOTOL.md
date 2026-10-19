# Spesifikasi Teknis Empat Customizer Stiker

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## HP
`PhoneModel` menampilkan body dan casing. Casing memiliki preset `plain` dengan warna yang disediakan serta `clear`. Saat user mengganti casing, surface UV dan safe area dapat berubah; migrasi posisi sticker diperlukan jika surface kompatibel, jika tidak tampilkan konfirmasi. Semua kamera/port fisik mempunyai mask aman.

## Tablet Apple
`TabletModel` memiliki back-surface dengan orientasi landscape/portrait. Camera preset rear/back/angle; tempel hanya di rear-surface; jangan meletakkan artwork melewati modul kamera. Model perangkat pilihan harus konsisten dengan dimensi thumbnail dan ukuran printable mm.

## MacBook
`MacBookModel` memiliki rig engsel atau transform group sederhana untuk membuka/menutup. Edit mode memaksa preview lid luar yang mudah disentuh. Saat animasi engsel berjalan, hit test dimatikan sementara supaya sentuhan tidak salah memilih permukaan. Stiker disimpan pada lid local UV supaya tidak bergerak di ruang ketika laptop diputar.

## Botol stainless
Warna preset `black`, `gray`. Mesh botol terdiri body dan cap; `PrintableSurface` hanya badan cylindrical zone dengan no-go band dekat lengkung bahu dan dasar. UV seam harus terjaga agar stiker wrap ke sisi berlawanan tanpa jump. Opsi stiker besar wrap-around perlu batas ukuran/pola khusus dari vendor cetak.

## Model detail vs mobile
Setiap tipe device mempunyai `mobile` dan `high` GLB profile dengan siluet dan zone anchors kompatibel. Tidak perlu menampilkan detail port yang tak pernah terlihat jika membuat drawcall mahal.

## Aturan status cart
Sistem harus membedakan `saleItemKind=STICKER_ONLY` dengan `BUNDLE_WITH_CASE`/`BOTTLE_SKU` bila suatu saat owner menjual fisik media tersebut. Jangan mengasumsikan viewer body dianggap item di cart.

## Acceptance spesifik
- Rotate+zoom tidak mengubah UV atau ukuran stiker.
- Semua varian casing dan dua warna botol dapat dipilih pada mobile.
- Posisi stiker tetap setelah save/reload, ganti kamera, dan masuk order owner.
- Pada desain print, dimensi mm sesuai konfigurasi pesanan dan artwork source tetap tersedia.
