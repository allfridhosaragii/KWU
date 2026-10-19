# Stack Terpilih, Alternatif, dan Alasannya

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Pilihan produksi awal
| Layer | Dipilih | Alternatif yang tidak dipilih saat MVP | Rasional |
|---|---|---|---|
| Web | Next.js App Router, React, TypeScript | React SPA + Express terpisah | SSR/SEO katalog dan server actions terintegrasi |
| UI | Tailwind CSS, Radix UI, CSS tokens | Framework UI penuh dengan style dominan | Desain Warm Atelier fleksibel |
| 3D | Three.js + R3F + Drei | Babylon.js / Unity WebGL | Ekosistem React dan kontrol aset glTF |
| State editor | Zustand | Redux penuh | State action kecil dan subscription granular |
| Validation | Zod | Validasi TS saja | Perlindungan input runtime |
| Database | PostgreSQL + Prisma | MongoDB | Transaksi dan relasi katalog/pesanan kuat |
| Auth | Auth.js | Roll-your-own auth | Kerangka sesi yang mapan |
| Assets | Blender, GLB, Meshopt, KTX2 | OBJ dengan tekstur lepas | Format PBR animasi/rig dan delivery efektif |
| Storage | R2 + CDN custom domain | Menyimpan GLB dalam database | Streaming dan caching file besar |
| Pembayaran | Midtrans sandbox → production setelah siap | Custom QRIS tanpa PSP | Rekonsiliasi status via webhook resmi |
| Test | Vitest, Playwright, Lighthouse/Web Vitals, device lab | Screenshot manual saja | Menjamin flow dan kualitas UI |
| Workspace | pnpm + Turborepo | Banyak repo service awal | Dependensi paket terkendali |

## Pilihan bukan janji kompatibilitas otomatis
- Versi `next`, `react`, `three`, `@react-three/fiber`, `@react-three/drei` harus diuji matriks peer dependencies saat bootstrap; gunakan versi stabil yang saling cocok, lalu kunci lockfile.
- Versi Prisma dan driver PostgreSQL juga harus dipilih bersamaan dengan strategi deploy (pooling, runtime Node).
- Auth.js credentials berbasis email/password memerlukan password hashing Argon2id, reset token expiry, rate limiting, dan verifikasi email sesuai produk; library tidak otomatis menyelesaikan semuanya.
- `WebGPURenderer` dapat diprototipe terpisah; WebGL 2 dipilih agar fallback terukur.

## Kapan mengganti teknologi?
Buat Architecture Decision Record (ADR) saat ada hasil benchmark yang membuktikan kebutuhan berbeda, bukan karena tren. Pergantian framework baru dapat dipertimbangkan setelah ada bottleneck dan mitigasi murah gagal.
