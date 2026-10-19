# Kamus Komponen, Istilah, dan Struktur Informasi

## Komponen UI lintas halaman

| Komponen | Kapan dipakai | Tidak untuk |
|---|---|---|
| `ProductCard` | Katalog, wishlist, rekomendasi | Menampilkan WebGL 8 scene sekaligus |
| `DesignCard` | Desain tersimpan | Mengganti sumber konfigurasi 3D |
| `OrderCard` | Riwayat pembeli, daftar owner | Menyamakan payment/fulfillment status |
| `StatusBadge` | Status ringkas | Satu-satunya indikator tanpa teks |
| `BottomSheet` | Filter, pilihan studio, form ringkas | Halaman legal panjang |
| `StickyActionBar` | Studio, detail, checkout bila relevan | Menghalangi safe-area/form |
| `SceneToolbar` | Kamera, reset, undo/save | Mengontrol input pembayaran |
| `OrnamentPicker` | Charm, liontin, ornamen tas | Menempel stiker UV langsung tanpa adapter |
| `StickerLayerList` | HP/tablet/MacBook/botol | Cincin dan gelang jika tidak relevan |
| `PriceBreakdown` | Studio/cart/checkout/order | Menampilkan harga final tanpa verifikasi |
| `ErrorState` | Semua halaman data-driven | Menggantikan error field yang spesifik |

## Istilah domain

- **Preset:** desain default dengan konfigurasi komponen valid.
- **Custom bebas:** modifikasi user dalam batas yang ditentukan owner.
- **Anchor:** titik/jalur pemasangan 3D yang valid untuk komponen.
- **UV:** koordinat pada permukaan model yang memetakan posisi stiker.
- **Decal:** proyeksi tekstur pada mesh; tidak selalu ideal untuk permukaan lengkung panjang.
- **Snapshot desain:** keadaan desain pada saat pesanan dibuat, disimpan agar tidak berubah saat katalog diperbarui.
- **Thumbnail:** gambar pratinjau desain, bukan data konfigurasi utama.
- **Production sheet:** daftar detail ukuran/material/posisi untuk proses produksi owner.
- **Pending:** pembayaran atau proses sedang menunggu konfirmasi, **bukan** sukses.
- **Safe area:** ruang layar yang mungkin tertutup notch, home indicator, atau UI browser.

## UI states yang harus seragam

`idle`, `loading`, `selected`, `editing`, `saving`, `saved`, `unsaved`, `invalid`, `error`, `disabled`, `empty`, `offline`.

## Contoh struktur label pada customizer

- Nama panel: “Ornamen”, “Warna”, “Ukuran”, “Posisi”, “Preset”.
- Tombol: “Putar Kiri”, “Putar Kanan”, “Geser”, “Hapus”, “Simpan Desain”, “Tambah ke Keranjang”.
- Hint: “Ketuk stiker untuk mengubah posisinya.”
- Status: “Perubahan belum disimpan.” atau “Tersimpan.”

## Checklist penamaan

- Semua nama komponen di Figma dan kode memakai konsep yang sama.
- Istilah bisnis tidak berganti antara halaman pembeli dan owner tanpa alasan.
- Semua string yang terlihat pengguna menggunakan bahasa yang disepakati.
