# Deployment, Hosting, PostgreSQL, CDN, dan Observability

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Deployment baseline
- `apps/web` di hosting Next.js yang mendukung App Router, Node runtime, environment secrets, HTTPS, dan callback publik Midtrans.
- PostgreSQL managed dengan pooling yang kompatibel dengan Prisma deployment, migrasi terkontrol, backup dan monitoring koneksi.
- Cloudflare R2 untuk GLB, KTX2, poster, public model dengan CDN custom domain; file private di bucket/key terproteksi.
- Tidak wajib `apps/worker`/Redis sampai ada kebutuhan background asset processing atau email volume besar.

## Environment staging
`dev` local, `staging` preview dengan Midtrans Sandbox dan DB nonproduction, `production` setelah review konfigurasi PSP, legal, payment dan backups. Staging tidak mengirim transaksi sungguhan.

## Release workflow
1. CI build/test.
2. Apply migration backward-compatible.
3. Deploy web release immutable.
4. Verifikasi HTTP health, katalog, login, studio GLB CDN, webhook sandbox (staging).
5. Audit Core Web Vitals dan performance report.
6. Jika gagal, rollback app; database migration reversal direncanakan terlebih dahulu.

## Cloud CDN
GLB dan KTX2 memakai key versioned+hash; cache immutable satu tahun hanya untuk hashed files, manifest lebih pendek. Domain custom R2 diperlukan untuk Cloudflare edge caching. Gunakan CORS origin produksi dan `Content-Type` benar.

## Monitoring
- Server errors (structured logs requestId + status), auth errors, checkout failures, webhook verification rejects.
- Performance telemetry: page LCP, INP, CLS; studio GPU class/anonymized fps when opted in if diperlukan; jangan simpan fingerprint unik device.
- Alert: payment webhook failing, DB unavailable, abnormal stock count, asset CDN 404, owner errors.

## Cost
Lakukan perhitungan biaya hosting/R2/DB/Midtrans berdasarkan volume nyata dan harga provider terbaru saat deploy. Dokumen tidak mengklaim gratis selamanya; quota provider bisa berubah.
