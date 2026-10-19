# Roadmap Implementasi Bertahap dan Prioritas

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Fase 0 — validasi rancangan
Kunci halaman dari Design Konsep, kontrak domain, persona, target devices, dua role. Pilih sku demonstrasi asli dan artwork dengan lisensi yang jelas. Siapkan acceptance test minimum.

## Fase 1 — web & data base
Bootstrap pnpm + Turborepo, Next.js TypeScript, design tokens, Prisma PostgreSQL migrations, Auth.js Buyer/Owner, katalog, detail produk, owner CRUD minimum. CI lint/typecheck/unit.

## Fase 2 — 3D core proof of concept (risiko terbesar)
Satu manekin tangan realistic optimized, kamera orbit+pinch, gelang, satu rail charm, add/move/delete, quality low/balanced/high, poster fallback. Uji iPhone dan Android nyata. **Jangan lanjut kategori lain sebelum fondasi stabil.**

## Fase 3 — studio data end-to-end
Serialization Zod versioned, save/load/autosave, undo/redo, thumbnail, compatibility/price quote. Test desain tahan reload dan identik di owner view.

## Fase 4 — sticker core
HP casing plain/clear, raycast UV, sticker drag/rotate/scale, print dimensions; lanjut botol silinder, tablet, MacBook setelah test engine.

## Fase 5 — sisa jewelry
Ring 5 finger anchors, kalung leher, tas attachment. Library komponen dan preset owner.

## Fase 6 — commerce/payment
Cart variant snapshots, checkout, Midtrans Sandbox, verified webhook, owner order production, stock reservation, shipment, reports minimal. E2E 2 role.

## Fase 7 — polish/mobile/performance
34 template halaman, accessibility, smooth UX, 8 category visual consistency, CDNs, caching, error states, real-device perf, security review, staging then production decisions.

## Urutan demonstrasi KWU
Buyer buka homepage → katalog → detail gelang → custom charm → save → cart → sandbox checkout → owner buka order dan melihat specs. Ini MVP vertikal yang dapat ditunjukkan kepada dosen meskipun kategori lain bertahap.

## Exit criteria
Setiap fase memiliki test evidence dan commit tag; status Not Started/In Progress/Ready to Validate/Validated. Jangan menilai proyek 100% hanya dari folder docs.
