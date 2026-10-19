# Monorepo, Modul, dan Batas Dependensi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Strategi: modular monolith yang siap dibagi
Satu aplikasi `apps/web` memuat halaman dan endpoint Next.js. Domain disusun menjadi library internal. Ini cukup untuk MVP dan memudahkan debugging dibanding microservices sebelum trafik nyata. Workspace menggunakan `pnpm-workspace.yaml` berisi `apps/*` dan `packages/*` serta `turbo.json` untuk pipeline build/test/lint.

## Workspace final
```text
KWU/
  Design Konsep/        <- dokumentasi UI/UX yang sudah ada; jangan diganti
  System/              <- dokumentasi sistem ini
  apps/
    web/               <- Next.js full-stack, satu deployment awal
    worker/            <- RESERVED; aktif hanya jika kebutuhan async terbukti
  packages/
    ui/                <- design components dan tokens
    three-core/        <- renderer/controls/asset handling
    three-customizers/ <- scene rules 8 kategori
    commerce/          <- pricing/order/cart/payment contracts
    database/          <- Prisma dan DB access
    contracts/         <- Zod, DTO, API schema, domain enums
    config/            <- shared TS/ESLint configs
  assets/              <- Blender source (sesuai strategi LFS), manifests, presets
  scripts/             <- audit, optimize, publish assets
  tests/               <- cross-package e2e/perf/security
  infra/               <- deployment, storage dan monitoring
  .github/workflows/   <- CI/CD
```

## Monorepo bukan berarti semua dibuat sekaligus
Tahap bootstrap: `apps/web`, `packages/contracts`, `packages/ui`, `packages/three-core`, `packages/three-customizers`, `packages/commerce`, `packages/database`, `packages/config`; `worker/` belum perlu package.json bila tidak digunakan.

## Batas import
- `packages/three-core` bebas import UI global dan commerce; scene menerima prop & event dengan tipe `contracts`.
- `packages/commerce` tidak import Three.js. Engine 3D hanya produsen `DesignConfiguration` yang divalidasi ulang server.
- `packages/database` bertugas persistensi, bukan aturan diskon/price formula.
- `packages/ui` tidak memanggil API langsung dari setiap Button.
- `apps/web/src/server/dal` adalah adapter penggabung domain + DB + auth.

## Lapisan
- Presentation: pages, components, hooks.
- Application services: use cases/cart/order/pricing.
- Domain: aturan validasi produksi, harga, stok, status.
- Infrastructure: Prisma, Midtrans, R2, mail adapter.

## Tooling
`pnpm -r test`, `pnpm exec turbo run build`, lint, typecheck, validate manifest. Semua script yang merusak data memerlukan environment yang eksplisit.

## Sumber
https://turborepo.dev/docs/crafting-your-repository/structuring-a-repository
