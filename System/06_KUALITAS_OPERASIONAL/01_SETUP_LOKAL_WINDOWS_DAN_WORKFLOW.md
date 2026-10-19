# Setup Developer Windows, Toolchain, dan Workflow Harian

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Kebutuhan workstation
Windows 11 + VS Code, Git, Node.js LTS yang kompatibel dengan Next.js/Prisma versi terpasang, Corepack + pnpm, Docker Desktop opsional untuk PostgreSQL, Blender untuk authoring assets, browser Chrome/Edge dan device iPhone/Android untuk QA.

## Bootstrap usulan
```powershell
# Setelah root workspace dan package manifest benar-benar dibuat:
corepack enable
pnpm install
pnpm exec turbo run lint
pnpm exec turbo run typecheck
pnpm exec turbo run test
pnpm --filter @kwu/web dev
```
Nama package `@kwu/web` adalah **contoh yang perlu cocok dengan package.json aktual**; jangan jalankan tanpa bootstrap source.

## Database lokal
Gunakan Docker Compose PostgreSQL volume persistent atau hosted development instance. Environment `.env` lokal tidak di-commit. Migration `prisma migrate dev` hanya di lingkungan development; `prisma migrate deploy` untuk deployment terkontrol.

## Workflow branch
`main` protected bila memungkinkan; fitur memakai branch `feat/studio-bracelet`, `feat/payment`, `fix/gesture-ios`. PR kecil, jelas, tests+preview, code review, squash/merge sesuai tim.

## Review per perubahan
- Perubahan UI: cek Figma design tokens dan 320/390 px.
- Perubahan 3D: ukur delta asset transfer, triangles, draw calls, fps, screenshot golden scene.
- Perubahan backend: test auth negative dan data integrity, migrations review.
- Perubahan payment: sandbox test webhook statuses dan idempotency.

## Windows pitfalls
Jangan taruh asset authoring file raksasa ke node_modules/public tanpa optimasi; hindari path sensitif/ber-spasi di script shell yang tidak dikutip. Git line endings dinormalisasi `.gitattributes`; gunakan `pnpm` bukan campur npm lockfiles.
