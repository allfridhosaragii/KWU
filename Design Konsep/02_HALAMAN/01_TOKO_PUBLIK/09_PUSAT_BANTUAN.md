# 09. Pusat Bantuan

**Route:** `/help`  
**Kelompok:** Toko & Publik  
**Pola visual:** Calm Support  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menjawab pertanyaan pembeli soal custom, material, pengiriman, pembayaran, dan pesanan.

## 2. Komposisi 1 layar pertama (_above the fold_)

Heading “Ada yang bisa kami bantu?” diikuti search dan empat kategori utama.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Pencarian bantuan | Pencarian FAQ dengan hasil singkat dan jelas. |
| 2 | Kategori bantuan | Cara Custom, Pembayaran, Pengiriman, Pengembalian. |
| 3 | FAQ accordion | Pertanyaan ringkas, satu jawaban terbaca dengan heading/link bila perlu. |
| 4 | Hubungi bantuan | Kontak nyata yang tersedia, jam operasional jika telah ditetapkan. |
| 5 | Panduan gesture | Ilustrasi 2–3 langkah untuk memutar, zoom, dan edit ornamen. |

## 4. Arah visual spesifik

Minim foto, fokus tipografi Manrope dan card berborder, aksen sage seperlunya.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Accordion dapat dibuka dengan keyboard.
2. Pencarian menampilkan hasil/empty.
3. Kontak mendukung membuka channel yang valid.

## 6. Loading, empty, error, dan edge cases

- Tidak ada hasil: alternatif kata kunci.
- FAQ belum tersedia: CTA kontak.
- Gagal memuat: retry tanpa form rusak.

## 7. Copy contoh

“Pilih topik atau cari jawaban.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop search center dengan grid kategori dua kolom.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan menulis estimasi pengiriman palsu atau kontak belum ada.

## 9. Kriteria penerimaan UI/UX

- [ ] Cara custom ditemukan maksimal dua tahap.
- [ ] Semua accordion berlabel jelas.
- [ ] Tidak mengandalkan video autoplay.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
