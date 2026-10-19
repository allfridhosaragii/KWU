# 16. Akun Saya

**Route:** `/account`  
**Kelompok:** Akun Pembeli  
**Pola visual:** Personal Utility  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menjadi titik masuk aktivitas personal tanpa memadatkan terlalu banyak informasi.

## 2. Komposisi 1 layar pertama (_above the fold_)

Salam pendek dengan nama, foto/inisial, ringkasan pesanan berjalan dan jumlah desain tersimpan.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Profil ringkas | Nama, email terpotong dengan aman, tautan Edit Profil. |
| 2 | Aktivitas prioritas | Kartu status pesanan terakhir dan tombol Detail. |
| 3 | Desain tersimpan | Thumbnail 1–2 desain yang dapat dilanjutkan. |
| 4 | Menu akun | Pesanan, Wishlist, Alamat, Profil, Bantuan, Logout. |
| 5 | Pemberitahuan | Pesan yang benar-benar penting, bukan promo berulang. |

## 4. Arah visual spesifik

List card putih dan border lembut, tanpa grafik penjualan atau dekorasi 3D.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Menu menavigasi ke halaman tepat.
2. Pesanan aktif tampil paling atas bila ada.
3. Logout memiliki konfirmasi bila relevan.

## 6. Loading, empty, error, dan edge cases

- Akun baru: ajakan Buat Desain Pertama.
- Tidak ada pesanan: tautan katalog.
- Load gagal: menu dasar masih bisa diakses.

## 7. Copy contoh

“Halo, selamat datang kembali.” CTA: “Lanjutkan Desain”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop layout kartu aktivitas kiri dan menu samping kanan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menjejalkan semua transaksi ke beranda akun.

## 9. Kriteria penerimaan UI/UX

- [ ] Status pesanan ditemukan tanpa scroll panjang.
- [ ] Link profil dan bantuan jelas.
- [ ] Tidak menampilkan data sensitif secara terbuka.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
