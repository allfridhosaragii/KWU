# Status Nyata Asset Pack KWU v2

Tanggal: 20 Oktober 2026

## Yang sudah dibuat secara nyata
- 8 scene utama: bracelet, ring, necklace, bag charm, phone, tablet, macbook, bottle.
- 13 varian Apple: 5 keluarga iPhone, 4 iPad, 4 MacBook.
- Total **21 file GLB berbeda** (8 kategori utama + 13 varian) plus 21 preview WebP.
- Tangan kontinu dibuat dengan implicit smooth surface, bukan lagi gabungan bulatan silinder yang terpisah.
- Ransel hitam: front-panel, top carry handle, side pockets, front zipper, patch label, hook.
- Botol: body stainless per profil putar, tutup hitam, loop dan karabiner.
- Pilihan model Apple, warna yang tersedia, dan mode casing polos/transparan di UI studio.
- Simpan desain menyertakan deviceModel, material color, caseType, ornament, position, rotation, scale.

## Batas yang BELUM terpenuhi
- **Belum fotorealistik 1:1**. Tangan bukan scan manusia. Ransel dan botol berasal dari satu foto depan, jadi geometri sisi/belakang belum terverifikasi.
- Material masih vertex color + iluminasi shader demo, bukan PBR texture 4K dan fisika refleksi yang lengkap.
- Hand mannequin belum true skeletal skinning/rigged mesh. Gerakan kamera ada, tetapi belum rig tangan nyata.
- Stiker demo saat ini satu ornament layer sederhana, belum artwork layer multi-sticker maupun file cetak produksi.
- Warna perangkat berupa perkiraan monitor. Belum diuji menggunakan color calibration.
- Chrome headless di lingkungan pengujian tidak menyediakan WebGL 2. Pengujian interaktif GPU dan FPS pada HP fisik masih **belum lolos karena belum dilaksanakan**, bukan dianggap passed.
- Proyek GitHub Pages hanyalah demo frontend statis, bukan transaksi/pembayaran sungguhan.

## Kriteria sebelum menyebut "siap produksi"
1. Fotografi orthographic multi-angle asli untuk semua objek.
2. 3D scan / licensed photo-real hand, retopology, rigging, texture baking.
3. PBR materials / color verification untuk metal, kulit, kain, kaca.
4. Validasi skala, posisi titik custom, tekstur, dan harga.
5. Uji performa WebGL 2 nyata di iPhone Safari, Android Chrome, iPadOS, desktop.
6. Backend autentikasi, pembayaran, dan data transaksi sungguhan terpisah dari GitHub Pages.
