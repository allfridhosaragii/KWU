# 06. Keranjang

**Route:** `/cart`  
**Kelompok:** Toko & Publik  
**Pola visual:** Commerce Utility  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membuat pembeli memahami isi pesanan dan biaya sebelum checkout, termasuk konfigurasi custom.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul “Keranjang” dan jumlah item, diikuti kartu item besar dengan thumbnail desain, nama, ringkasan komponen, kuantitas, dan harga.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Daftar item | Setiap kartu memuat thumbnail custom, varian, ringkasan posisi/ornamen utama, harga item. |
| 2 | Kelola item | Edit desain, hapus, atur kuantitas, dan lihat detail tanpa menghapus item lain. |
| 3 | Ringkasan biaya | Subtotal, jumlah item, informasi ongkir dihitung saat checkout, diskon jika tersedia. |
| 4 | CTA checkout | Sticky CTA Lanjut ke Checkout dengan total sementara yang tidak menipu. |
| 5 | Saran terkait | Jika ada, bagian kecil di bawah yang tidak menggeser CTA utama. |

## 4. Arah visual spesifik

Card putih pada ivory, divider tipis, tanpa banner promo. Gambar produk lebih besar daripada foto pada order list.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Edit desain membuka Studio dengan config existing.
2. Ubah kuantitas memperbarui subtotal setelah tervalidasi.
3. Hapus item meminta konfirmasi bila risikonya signifikan.
4. Lanjut Checkout mengirim semua item dan menampilkan rincian lagi.

## 6. Loading, empty, error, dan edge cases

- Empty: visual ringan, CTA Jelajahi Koleksi.
- Stok/harga berubah: jelaskan masalah pada item terkait.
- Gagal update: pertahankan item dan tampil Retry.

## 7. Copy contoh

Empty: “Keranjangmu masih kosong.” CTA: “Lihat Koleksi”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop daftar dua pertiga dan ringkasan sticky kanan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan otomatis checkout saat item ditambah; jangan sembunyikan biaya yang diketahui.

## 9. Kriteria penerimaan UI/UX

- [ ] Setiap item punya bukti visual hasil custom.
- [ ] Total terlihat dan benar terhadap item.
- [ ] CTA tidak tertutup safe area.
- [ ] Edit tidak mereset desain lain.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
