# Owner 3D Model Navigation — KWU

Owner harus dapat mengakses **seluruh** model 3D dari setiap halaman owner tanpa kembali ke toko. Sistem ini memiliki 21 model: 8 kategori utama dan 13 varian perangkat Apple.

## Mobile
- Navigasi bawah memuat tab `Model 3D` langsung ke `/owner/assets`.
- Navigasi kategori 3D horizontal tetap muncul di seluruh halaman owner dan dapat digeser dengan sentuhan.
- Item terpilih memperlihatkan highlight aktif.
- Pengguna dapat memilih model dan melihat pratinjau tanpa membuat 21 canvas WebGL sekaligus.

## Desktop
- Sidebar utama menampilkan seluruh 21 model di bawah seksi `Semua Model 3D`.
- Daftar dapat di-scroll mandiri jika lebih panjang dari viewport.
- Bar model horizontal tersedia sebagai jalan pintas.

## Routing
- `/owner/assets` default ke model gelang.
- `/owner/assets?model=iphone-17-pro` memilih iPhone 17 Pro.
- Query tidak mengubah akses role. Hak akses UI demo tetap memerlukan mode owner.

## Referensi data
Sumber nama dan ID model ialah `OWNER_3D_MODELS` di `src/app.ts`, yang diturunkan dari `PRODUCT_TYPES` dan `DEVICE_VARIANTS` untuk mencegah daftar tidak sinkron.

## Batasan
Ini adalah library aset 3D untuk demo. Upload dan manajemen metadata produksi memerlukan backend aman. Kualitas model yang tersedia masih prosedural, belum scan 1:1.
