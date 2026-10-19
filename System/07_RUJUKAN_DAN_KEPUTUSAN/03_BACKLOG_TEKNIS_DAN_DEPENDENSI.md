# Backlog Teknis dan Dependency Map

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Track A — Workspace/DevOps
A01 scaffold, A02 TS strict + configs, A03 env validation, A04 GitHub CI, A05 deployment staging, A06 observability. Blokir rilis sebelum A01–A04.

## Track B — Commerce/Auth
B01 Prisma schema, B02 auth BUYER/OWNER, B03 catalog CRUD, B04 inventory, B05 server price quote, B06 cart, B07 order snapshots, B08 Midtrans sandbox+webhook, B09 production spec, B10 reports.

## Track C — 3D
C01 asset standards/mannequin, C02 renderer camera and gesture, C03 bracelet rail+charm, C04 serializer+Zod, C05 saved design+owner replay, C06 sticker phone UV, C07 bottle UV, C08 tablet and MacBook, C09 ring finger anchors, C10 necklace neck rig, C11 bag charm hooks, C12 mobile performance.

## Track D — UI/UX
D01 tokens, D02 navigation buyer/owner, D03 catalog/detail, D04 studio mobile sheet, D05 cart/checkout, D06 account/owner pages, D07 accessibility states, D08 QA responsive.

## Critical path
`A01 → B01 → B02/B03 → C01 → C02 → C03 → C04 → B05/B06 → B07/B08 → B09 → E2E`. Sticker C06/C07 dapat paralel setelah shared C02/C04 matang. Jangan mengklaim 34 halaman dapat selesai ketika UI critical path belum lolos.

## Issue format
- Summary, linked Design Konsep doc, linked System doc, acceptance criteria, sample data, test matrix, security consideration, performance target, screenshot evidence.
- Label `frontend`, `backend`, `3d`, `asset`, `security`, `qa`, `docs` sesuai ownership.
