# Status Repository dan Langkah Implementasi yang Belum Dilakukan

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Status baseline pada penyusunan dokumen
Repository `allfridhosaragii/KWU` sudah memiliki folder `Design Konsep/` untuk UI/UX. Folder `System/` ditambahkan sebagai **spesifikasi engineering**. Isi folder ini tidak menginstal Next.js, membuat PostgreSQL, atau menyediakan `.glb` produksi.

## Yang belum boleh diklaim selesai
- 34 halaman TSX yang berfungsi.
- Delapan model 3D/rig dengan pengalaman mobile nyata.
- Auth.js dan role enforcement yang lolos tes.
- Koneksi database/migration/backup.
- Midtrans Sandbox workflow, webhook dan log payment.
- Deployment, CDN R2, SSL, domain, PSP production.
- FPS 30/60 atau target Core Web Vitals.

## Checklist implementasi pertama
1. Tentukan asset dan SKU demo asli (gelang dan stiker HP).
2. Lock versi `next`, `react`, `three`, `r3f`, `drei`, `prisma`, driver DB kompatibel; commit lockfile.
3. Scaffold workspace dengan `.env.example` dan CI.
4. Buat DB migrations dasar auth/products/designs/orders.
5. Buat satu Browser 3D yang dapat menerima GLB custom dan demo dummy dengan poster fallback.
6. Uji di HP nyata sebelum melanjutkan kategori lain.

## Validasi terhadap Design Konsep
Pastikan routes, palet, tipografi, navigasi 34 template, 8 kategori, dua role, dan states UX konsisten. Jika ada perubahan, update kedua folder bersamaan dalam PR.
