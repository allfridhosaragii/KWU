# Navigasi Global, Header, Footer, dan Layout

## Pembeli: 5-item bottom navigation

| Item | Target | Ikon |
|---|---|---|
| Beranda | `/` | house |
| Belanja | `/shop` | shopping-bag/store |
| Studio | `/studio` | cube/box |
| Keranjang | `/cart` | bag |
| Akun | `/account` | user |

- Label teks selalu terlihat di samping/bawah ikon; jangan icon-only.
- State terpilih memakai warna terracotta + penanda yang bukan warna saja.
- Navigasi bawah tidak muncul pada checkout, auth, dan editor 3D fullscreen.
- Header umum menampung brand, search, wishlist, dan akses cart sesuai breakpoint. Hindari lebih dari 2–3 ikon dalam viewport sangat sempit.

## Owner: 4-item bottom navigation

`Ringkasan` → `/owner`; `Pesanan` → `/owner/orders`; `Produk` → `/owner/products`; `Lainnya` membuka daftar Stok, Komponen, Aset 3D, Pembayaran, Pelanggan, Laporan, Pengaturan.

Menu owner tidak boleh muncul di role pembeli dan pemeriksaan izin harus dilakukan backend. Di desktop, owner memakai sidebar yang ringkas.

## Headers

- **Editorial Header:** logo brand, dua aksi utama; beranda dan katalog.
- **Context Header:** panah kembali, judul ringkas, aksi kanan; akun, detail pesanan, studio.
- **Owner Header:** judul halaman, tombol aksi paling relevan, filter bila perlu.
- **Checkout Header:** logo/judul checkout, kembali; menekan gangguan navigasi.

## Bottom Sheet

- State: collapsed/peek, half, expanded. Batas tinggi menyesuaikan perangkat.
- Handle visual, heading panel, tombol tutup bila bersifat modal.
- Area canvas 3D dan panel punya aturan gesture terpisah.
- Ketika modal dialog terbuka, fokus keyboard berpindah ke dialog; background tidak dapat diakses sampai dialog ditutup.

## Footer

Storefront menampilkan navigasi bantuan, kontak, kebijakan, dan brand story. Footer tidak perlu selalu terlihat di halaman utility. Jangan mendorong user melihat footer untuk menemukan status pesanan.

## Deep-link dan back behavior

- Katalog menyimpan query/filter di URL; Back kembali pada scroll position yang wajar.
- Dari daftar desain ke editor, tombol Back kembali ke daftar, bukan homepage.
- Setelah checkout, jangan memberikan tautan kembali yang memungkinkan pembayaran tergandakan karena kesalahan navigasi.
- Jika desain belum disimpan, beri konfirmasi saat pengguna meninggalkan customizer bila memang ada perubahan.
