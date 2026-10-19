# Dependensi per Package dan Aturan Import

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Usulan pembagian dependensi
| Workspace | Runtime | Dev |
|---|---|---|
| `apps/web` | next, react, react-dom, next-auth/Auth.js, zod, @kwu/ui, @kwu/contracts, @kwu/commerce, @kwu/three-customizers (lazy) | typescript, eslint |
| `packages/ui` | react, Radix primitives seperlunya, class-variance-authority, clsx (opsional) | tailwind build tooling |
| `packages/three-core` | three, @react-three/fiber, @react-three/drei, zustand | @types/three bila perlu |
| `packages/three-customizers` | @kwu/three-core, @kwu/contracts, three | tests |
| `packages/commerce` | @kwu/contracts, zod, decimal handling, adapter Midtrans | Vitest |
| `packages/database` | @prisma/client, Prisma adapter yang cocok, `pg` driver jika dipakai | prisma CLI |
| `packages/contracts` | zod | vitest |
| `packages/config` | konfigurasi compiler/linter | TS/ESLint |

## Graph dependensi (arah dibolehkan)
```text
apps/web -> ui, three-customizers, commerce, database, contracts
three-customizers -> three-core, contracts
three-core -> contracts (hanya tipe yang UI-independent)
commerce -> contracts; adapters ke database melalui interface
server data access -> database dan commerce
ui -> contracts tipe tampilan bila benar-benar perlu
```
Arah yang **dilarang**: `three-core -> commerce`, `commerce -> React`, `contracts -> database`, `packages/* -> apps/web`. Jika dependency melingkar, desain paketnya harus diperbaiki.

## Kebijakan instalasi
- Gunakan `pnpm install` setelah menentukan lockfile. Hindari `latest` pada deployment produksi.
- `workspace:*` untuk package internal dan `exports` terdefinisi; jangan import `../../src/internal` lintas package.
- Gunakan `pnpm audit` / dependency scanning, review perubahan besar, dan test setelah upgrade major.
- `transpilePackages` atau exports build strategy dipilih sesuai package dan kemampuan Next.js versi terpasang; pastikan server-only tidak masuk bundel client.
