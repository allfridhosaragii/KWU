# 11. Kebijakan dan Ketentuan

**Route:** `/legal/[slug]`  
**Kelompok:** Toko & Publik  
**Pola visual:** Editorial Document  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menyediakan informasi pengiriman, privasi, dan ketentuan custom secara terbaca dan mudah diakses.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul dokumen, tanggal revisi, intro singkat, daftar isi jika panjang. Isi dalam satu kolom tekstual.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Document selector | Privasi, Syarat Layanan, Pengiriman, Pengembalian tersedia sebagai tautan jelas. |
| 2 | Isi pasal | Heading H2/H3 semantik, paragraf, bullet ringkas, definisi istilah. |
| 3 | Info khusus produk custom | Kebijakan retur untuk item personalisasi harus berdasarkan aturan nyata yang dikonfirmasi. |
| 4 | Kontak | Channel pertanyaan dan tautan bantuan. |
| 5 | Riwayat revisi | Tanggal perubahan dokumen bila diperlukan. |

## 4. Arah visual spesifik

Tidak menggunakan canvas, animasi dekoratif, atau card bertumpuk. Lebar baca terbatas; warna teks espresso.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Daftar isi jump link menuju section.
2. Tautan bantuan aktif dan jelas.
3. Cetak/copy teks tidak diblokir.

## 6. Loading, empty, error, dan edge cases

- Dokumen belum tersedia: tampil informasi sementara yang jujur, jangan halaman kosong.
- Tautan tidak dikenal: tampil not-found.
- Offline: konten cache bila ada.

## 7. Copy contoh

Judul: “Kebijakan Pengiriman”. Label: “Terakhir diperbarui: [tanggal valid]”.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop body max-width sekitar 720–800 px, sidebar daftar isi opsional.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengarang kebijakan hukum sebagai sudah berlaku.

## 9. Kriteria penerimaan UI/UX

- [ ] Teks mudah dibaca pada zoom 200%.
- [ ] Judul/pasal berstruktur.
- [ ] Informasi dasar ditemukan dari footer dan checkout.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
