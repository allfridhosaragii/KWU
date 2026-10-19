# Risk Register dan Mitigasi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

| ID | Risiko | Dampak | Kemungkinan | Mitigasi dan bukti |
|---|---|---|---|---|
| R01 | GLB terlalu besar | loading mobile lama | tinggi | asset size budget, Meshopt/KTX2, CDN, progressive preview |
| R02 | GPU HP panas/drop FPS | UX patah | tinggi | adaptive DPR, frameloop demand, real-device benchmarks |
| R03 | Ornamen melayang/clip | desain tak bisa diproduksi | tinggi | anchors, constraints, server validation, golden poses |
| R04 | Stiker melengkung salah | hasil preview tak sesuai cetak | tinggi | UV surface mm, print template, QA bottle seam |
| R05 | Stiker/preview beda dengan order | sengketa | tinggi | immutable snapshot, versions, replay tests |
| R06 | Harga bisa diubah browser | rugi finansial | tinggi | price calculator server, idempotency, negative tests |
| R07 | Double payment/webhook | stok double deduct | sedang | verified idempotent webhook, unique event index |
| R08 | Kebocoran privasi | dampak pelanggan | sedang | RBAC DAL, private asset URLs, audit |
| R09 | Aset tidak berlisensi | masalah hak pakai | sedang | lisensi dokumen, desain original/artwork owner |
| R10 | Overengineering monorepo | pengerjaan lambat | tinggi | modular monolith, worker deferred, phase gates |
| R11 | Warna 3D berbeda fisik | keluhan | sedang | material color calibration, disclaimer ukuran/warna, reference photo |
| R12 | Vendor deployment berubah | biaya/konfigurasi gagal | sedang | lockfile, ADR, deploy smoke tests, cost monitoring |
| R13 | iOS gesture bentrok scroll | studio tidak nyaman | tinggi | pointer state machine dan real iPhone testing |
| R14 | Browser tab kehilangan WebGL | kehilangan desain | sedang | serialized state, context recovery, fallback |

## Prioritas
Awali dengan R01, R02, R03, R04, R06, R13. Satu risiko dapat menutup release jika memengaruhi checkout atau integritas data. Jika bukti mitigasi belum ada, tulis status Open bukan Completed.
