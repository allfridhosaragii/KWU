# Kebutuhan Fungsional dan Kriteria Penerimaan

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Requirements ID tetap
| ID | Kebutuhan | Acceptance minimum |
|---|---|---|
| FR-AUTH-01 | Dua role Buyer/Owner | Register publik hanya membuat BUYER; owner route 403 untuk buyer |
| FR-CAT-01 | Katalog dan pencarian | Filter dan query kembali dengan URL; pagination stabil |
| FR-3D-01 | Delapan tipe scene | Satu shared engine, modul kategori lazy loaded |
| FR-3D-02 | Preset + free placement | Pergeseran menghasilkan konfigurasi valid; tidak bisa keluar constraint |
| FR-3D-03 | Manipulasi manekin | Kamera dan rig dibedakan; reset sudut bekerja |
| FR-3D-04 | Stiker permukaan | Posisi di UV/anchor, skala mm, area kamera dilarang |
| FR-3D-05 | Konsistensi desain | Save/load sama versi dan checksum; reload tanpa drift |
| FR-CART-01 | Cart konfigurasi | Dua desain untuk SKU sama tetap dua cart item jika konfig beda |
| FR-ORDER-01 | Snapshot pesanan | Edit catalog setelah order tidak mengubah item pesanan |
| FR-PAY-01 | Pembayaran | Redirect bukan bukti sukses; webhook diverifikasi di backend |
| FR-OWNER-01 | Produksi | Owner melihat thumbnail, komponen, varian dan aturan valid |
| FR-PERF-01 | Mobile performance | Profil Low/Balanced/High dan 2D fallback, pengukuran device nyata |
| FR-SEC-01 | Isolasi data | Buyer hanya dapat melihat desain dan order miliknya |

## Non-functional requirements
- Mobile touch nyaman, pointer target desain 44×44 px; teks dan fungsi sesuai Design Konsep.
- Tahan jaringan lambat: skeleton, retry, resume setelah gagal, tidak hilang desain saat koneksi sementara putus.
- Data uang menggunakan `Decimal` / satuan integer IDR; tidak gunakan floating-point JS untuk perhitungan pembayaran.
- Autentikasi dan input server-side diuji; upload dibatasi jenis/ukuran dan hak akses.
- R3F scene dilepas saat pindah halaman dan context loss ditangani.

## Definition of Done per fitur
- Implementasi, tes positif-negatif, handling loading/error/empty, a11y mobile, dokumentasi schema/API, pengukuran performa jika terkait 3D, dan security review sebelum merge.
- Catat perangkat/uji dengan timestamp; angka benchmark tak boleh diterbitkan tanpa hasil nyata.

## Alur traceability
`Requirement ID → spesifikasi Design Konsep → route → service → test case → acceptance evidence`. Nama ID tidak boleh berubah tanpa memutakhirkan matriks.
