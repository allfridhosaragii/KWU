# 24. Daftar Pesanan Owner

**Route:** `/owner/orders`  
**Kelompok:** Owner  
**Pola visual:** Action Queue  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Membantu owner menemukan pesanan untuk diproses, dibayar, atau dikirim.

## 2. Komposisi 1 layar pertama (_above the fold_)

Judul Pesanan, badge kebutuhan tindakan, tab berdasarkan tahap pemenuhan, search nomor/nama, daftar kartu.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Filter & pencarian | Status pembayaran, status produksi, rentang tanggal, nomor/nama; filter aktif dapat dihapus. |
| 2 | Order list | Nomor, nama terbatas, thumbnail, produk, total, waktu, dua status berbeda. |
| 3 | Prioritas tindakan | Pesanan baru/belum diproses muncul jelas tetapi tidak menyembunyikan pesanan lain. |
| 4 | Bulk actions | Hanya tindakan yang aman dan memang diizinkan; fase awal boleh tidak ada. |
| 5 | Pagination | Load more/infinite terbatas dengan penanda hasil dan posisi list. |

## 4. Arah visual spesifik

Owner list card satu kolom, informasional, warna hanya untuk status relevan.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Tap kartu buka detail dan mempertahankan filter.
2. Search debounce agar tidak mengulang render berlebihan.
3. Perubahan filter tidak mereset seluruh halaman tanpa alasan.

## 6. Loading, empty, error, dan edge cases

- Kosong sesuai filter: Hapus Filter.
- API gagal: retry.
- Pembayaran pending: label fakta, bukan diproses.

## 7. Copy contoh

“7 pesanan perlu ditinjau.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop tabel sortable dengan kolom yang relevan.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan memberi status “dibayar” jika webhook belum diverifikasi.

## 9. Kriteria penerimaan UI/UX

- [ ] Status uang dan produksi dibedakan.
- [ ] Prioritas tindakan bisa ditemukan.
- [ ] Nomor order terbaca dan dapat disalin.
- [ ] Tidak membocorkan kontak penuh di list jika tidak perlu.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
