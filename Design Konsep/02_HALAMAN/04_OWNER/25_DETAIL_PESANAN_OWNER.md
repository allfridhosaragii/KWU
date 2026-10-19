# 25. Detail Pesanan Owner

**Route:** `/owner/orders/[id]`  
**Kelompok:** Owner  
**Pola visual:** Order Operations  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Memastikan owner dapat memproduksi pesanan custom sesuai preview final dan mencatat pengiriman.

## 2. Komposisi 1 layar pertama (_above the fold_)

Nomor order dan dua status (bayar/produksi) di atas, tombol tindakan operasional, lalu visual desain.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Status utama | Pembayaran, proses produksi, pengiriman; jangan satu chip untuk semua. |
| 2 | Preview final | Thumbnail resolusi tinggi, tombol Lihat 3D; konfigurasi snapshot tidak boleh berubah. |
| 3 | Production sheet | Daftar bahan/ornamen/stiker, posisi, ukuran fisik, jumlah, catatan pembeli. |
| 4 | Kontak/pengiriman | Alamat tujuan, kurir, nomor resi, tombol salin. |
| 5 | Payment details | Nominal, referensi transaksi, status gateway. |
| 6 | Action timeline | Riwayat perubahan state dan owner yang melakukan. |

## 4. Arah visual spesifik

Data terbagi menjadi card dengan heading jelas; preview 3D dibuka on demand.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. Proses Pesanan mengubah state bila syarat pembayaran terpenuhi.
2. Tambahkan resi melalui form validasi.
3. Lihat 3D memuat scene versi aset sesuai snapshot.
4. Perubahan state sensitif memberi konfirmasi dan feedback.

## 6. Loading, empty, error, dan edge cases

- Preview 3D gagal: thumbnail + daftar komponen tetap bisa diproduksi.
- Status pembayaran belum jelas: blok proses yang tidak boleh dilakukan.
- Update gagal: state tidak berubah optimistis tanpa rekonsiliasi.

## 7. Copy contoh

CTA: “Mulai Produksi”, “Tandai Dikemas”, “Catat Pengiriman” sesuai state.

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop detail dua kolom dengan panel informasi dan preview yang bisa diperbesar.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan mengedit pesanan pelanggan diam-diam; perlu jejak persetujuan jika ada revisi.

## 9. Kriteria penerimaan UI/UX

- [ ] Owner menemukan semua bahan dalam satu panel.
- [ ] Preview sesuai pesanan yang dibayar.
- [ ] Resi dan status punya audit trail.
- [ ] Aksi role-protected.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
