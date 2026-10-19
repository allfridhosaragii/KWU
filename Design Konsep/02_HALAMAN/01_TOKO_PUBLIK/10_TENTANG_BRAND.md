# 10. Tentang Brand

**Route:** `/about`  
**Kelompok:** Toko & Publik  
**Pola visual:** Brand Storytelling  
**Prioritas perangkat:** mobile 390 × 844 CSS px, adaptif.  
**Status:** spesifikasi desain; belum dibangun.

## 1. Tujuan layar

Menciptakan kepercayaan dan menjelaskan mengapa personalisasi 3D relevan untuk usaha ini.

## 2. Komposisi 1 layar pertama (_above the fold_)

Foto editorial bahan/hasil desain, heading serif “Made personal, by design.” dan satu paragraf cerita singkat.

Pada mobile, tindakan utama harus terlihat atau mudah dijangkau tanpa terdorong oleh gambar dekoratif. Header, sticky CTA, dan safe area tidak boleh bertabrakan.

## 3. Urutan bagian dari atas ke bawah

| Urutan | Bagian UI | Isi, prioritas, dan tata letak |
| --- | --- | --- |
| 1 | Hero brand | Foto makro benda kecil, headline tidak menutupi produk. |
| 2 | Cerita usaha | Mengapa menyediakan aksesoris/stiker custom, ditulis secara faktual. |
| 3 | Cara kerja | Dari pilihan komponen ke preview 3D ke produksi nyata. |
| 4 | Material dan proses | Tampilkan proses nyata jika ada; bila belum ada, hindari klaim pabrik/handmade yang belum diverifikasi. |
| 5 | CTA eksplorasi | Mulai Custom dan Jelajahi Koleksi. |

## 4. Arah visual spesifik

Serif editorial besar, banyak whitespace, palet warm ivory + foto tactile, divider minimal.

Semua elemen tetap memakai warna dan font dari [Design System Warna](../../01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md) dan [Tipografi](../../01_DESIGN_SYSTEM/02_TIPOGRAFI.md). Jangan membuat palet khusus tanpa alasan fungsional.

## 5. Interaksi pengguna

1. CTA kembali ke toko/studio.
2. Scroll reveal hanya sekali dan mengikuti reduced motion.
3. Image captions membantu memahami produk.

## 6. Loading, empty, error, dan edge cases

- Foto belum ada: gunakan placeholder editorial yang diberi label, bukan klaim produksi.
- Koneksi lambat: teks tetap tampil.
- Contact detail belum tersedia: sembunyikan block terkait.

## 7. Copy contoh

“Rancang produk kecil yang terasa milikmu.”

Teks placeholder tidak boleh dipakai sebagai informasi bisnis yang belum diketahui. Pastikan title/button/error konsisten dalam Bahasa Indonesia.

## 8. Responsive dan aksesibilitas

- **Mobile 320–430 px:** fokus satu tugas utama, tombol ber-target sentuh ideal 44 × 44 px, safe-area bottom diperhitungkan, tidak ada horizontal scroll yang tidak disengaja.
- **Tablet/Desktop:** Desktop layout editorial alternating image/text tetapi tetap mudah dibaca.
- **Semantik:** satu heading utama per layar, label input jelas, fokus keyboard terlihat, kontras teks sesuai WCAG 2.2 AA, dan alternatif tanpa drag bila dibutuhkan.
- **Batas desain:** Jangan memakai stok foto kompetitor sebagai bukti proses usaha.

## 9. Kriteria penerimaan UI/UX

- [ ] Cerita tidak menciptakan klaim tidak terbukti.
- [ ] CTA belanja tetap jelas.
- [ ] Foto alternatif bermakna.
- [ ] Mobile tidak menjadi halaman teks terlalu panjang.

## 10. Handoff Figma dan developer

- Frame yang harus tersedia: Default Mobile, Loading, Empty bila relevan, Error, Interaction, dan Desktop Adaptation.
- Gunakan komponen reusable: Header sesuai konteks, Button, IconButton, Card, Sheet/Dialog, Status, dan Loading/EmptyState.
- Ikuti [Navigasi](../../01_DESIGN_SYSTEM/06_NAVIGASI_DAN_LAYOUT.md), [Motion](../../01_DESIGN_SYSTEM/08_MOTION_DAN_MICROINTERACTIONS.md), dan [State UI](../../01_DESIGN_SYSTEM/09_STATES_LOADING_EMPTY_ERROR.md).
- Untuk fitur 3D, rujuk [Aturan Studio 3D](../../03_STUDIO_3D/00_PRINSIP_STUDIO.md). Untuk transaksi, jangan menyamakan animasi dengan status backend.
