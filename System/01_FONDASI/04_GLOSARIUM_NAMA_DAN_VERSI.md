# Glosarium, Penamaan, dan Versi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Nama domain
- `Product`: SKU/jasa yang dibeli; `Variant`: ukuran/warna/bahan; `Component`: charm/rantai/ornamen/stiker; `PreviewDevice`: media display bukan otomatis SKU.
- `ModelAsset`: file GLB + metadata dan versi; `Rig`: rangka tulang manekin; `Anchor`: titik pemasangan; `PlacementZone`: area valid; `Design`: konfigurasi yang disimpan; `DesignElement`: satu item yang ditempatkan.
- `OrderSnapshot`: rekaman final yang immutable; `Payment`: usaha pembayaran dan status provider; `ProductionSpec`: rincian barang/komponen yang harus dibuat.
- `Buyer` dan `Owner` adalah role. Jangan menambah `ADMIN` diam-diam karena keputusan user hanya dua role.

## Penamaan folder/file
- Folder package: kebab-case, misalnya `three-customizers`, bukan `3DCustomiser`.
- TS utilities: kebab-case seperti `price-calculator.ts`; React Component PascalCase `.tsx`; test `*.test.ts(x)` dan E2E `*.spec.ts`.
- DB: Prisma model PascalCase (`CustomDesign`), field camelCase; SQL table yang dihasilkan mengikuti mapping migration.
- Aset 3D: `[category]-[model]-[quality]-v[major].glb` pada CDN, disertai hash saat publish.

## Versioning
- Konfigurasi desain memiliki `schemaVersion`, `assetVersion`, `rulesVersion` serta ID yang stabil. Ada migrator eksplisit untuk perubahan schema.
- File model dan texture immutable dengan URL berhash; manifest dapat menunjuk versi terbaru.
- Framework/library memakai versi yang kompatibel dan dicatat `pnpm-lock.yaml` saat coding; jangan menebak angka versi hanya dari rancangan dokumen.
- Mata uang IDR dan ukuran mm; rotasi radian internal, UI derajat bila ditampilkan.
