# 23. Dashboard Owner

**Route:** `/owner`  
**Kelompok:** Owner  
**Pola visual:** Quiet Operations  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menunjukkan kondisi toko hari ini dan prioritas tindakan owner tanpa membuat dashboard terlalu penuh.

## 2. Komposisi 1 layar pertama (_above the fold_)

Salam owner, periode data, satu kartu omzet utama; tiga metrik ringkas dan daftar tindakan paling mendesak.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Ringkasan utama | Omzet periode dengan keterangan periode jelas, bukan angka tanpa konteks. |
| 2 | Metrik operasional | Pesanan baru, sedang dibuat, produk aktif, stok kritis. |
| 3 | Action queue | Daftar pesanan yang harus ditinjau berdasarkan prioritas yang nyata. |
| 4 | Tren singkat | Mini chart yang menyampaikan tren tanpa 10 grafik bersaing. |
| 5 | Shortcut | Tambah Produk, Lihat Pesanan, Laporan. |
| 6 | Info sinkron | Waktu pembaruan data dan error bila API gagal. |

## 4. Arah visual spesifik

Satu card utama oat/beige, lainnya card putih. Angka Manrope kuat; aksen terracotta hanya pada tindakan.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Klik metrik membawa ke daftar terfilter.
2. Periode diperbarui dengan label eksplisit.
3. Quick action membuka halaman terkait.

## 6. Loading, empty, error, dan edge cases

- Toko baru: dashboard onboarding dan Tambah Produk.
- Data parsial: tandai metrik tidak tersedia.
- API gagal: retry, jangan menunjukkan Rp0 palsu.

## 7. Copy contoh

“Pesanan yang perlu ditangani hari ini.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop sidebar + metrik empat kolom dan tabel singkat.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan membuat angka contoh terlihat sebagai data penjualan nyata.

## 9. Kriteria penerimaan UI/UX

- [ ] Prioritas pesanan terlihat tanpa scroll panjang.
- [ ] Periode metrik jelas.
- [ ] Statistik tidak disamakan dengan saldo kas nyata.
- [ ] Tiap aksi memenuhi otorisasi owner.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
