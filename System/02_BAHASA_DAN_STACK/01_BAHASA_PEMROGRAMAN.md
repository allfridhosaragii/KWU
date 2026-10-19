# Bahasa Pemrograman, Format, dan Perannya

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Bahasa wajib dan penggunaannya
| Bahasa/format | Kategori | Digunakan pada | Alasan |
|---|---|---|---|
| **TypeScript** | Bahasa utama | Next.js, components, R3F scenes, backend, domain services, tests, tooling | Strong typing dan kontrak frontend/backend dalam satu ekosistem |
| **TSX** | Sintaks TypeScript + JSX | React components dan React Three Fiber | Deklaratif untuk UI dan graph 3D |
| **CSS** | Stylesheet | Tailwind utilities, tokens semantik, CSS variables, komponen khusus | Layout responsif dan desain tanpa JS berlebih |
| **SQL** | Query DB | PostgreSQL migrations yang memerlukan constraint/index/view khusus | Keutuhan data dan query terukur |
| **Prisma Schema Language** | DSL DB | `schema.prisma` | Model dan migrasi yang bertipe |
| **JSON** | Data interchange | Kontrak scene, saved design, manifest 3D, API payload | Interoperabilitas dan validasi versi |
| **YAML** | CI/konfigurasi | GitHub Actions, pnpm-workspace | Konfigurasi workflow |
| **GLSL** | Shader opsional | Material custom yang benar-benar diperlukan | Kontrol rendering spesifik setelah profiling |
| **Python** | Skrip opsional | Blender pipeline headless atau asset audit | Tidak diperlukan untuk runtime web |
| **Bash / PowerShell** | Otomasi opsional | Setup, deployment scripts | Membantu developer lintas OS |

## Penegasan yang sering salah
- HTML tetap dihasilkan oleh React/Next.js, tetapi **tidak membangun banyak file `.html` manual** sebagai kerangka utama.
- Tidak ada alasan memakai PHP/Laravel *dan* Next.js API secara bersamaan pada baseline. Satu backend cukup.
- Tidak memakai Unity WebGL sebagai runtime inti; umumnya lebih berat untuk studio produk ringan di web HP.
- Blender bukan engine browser; Blender membuat/mengolah GLB. Runtime Three.js memakai hasil export tersebut.
- TypeScript tidak memvalidasi payload saat runtime; **Zod dan pemeriksaan server** tetap wajib.

## Contoh batas kode
- `packages/contracts`: TypeScript + Zod, bebas React dan database.
- `packages/three-core`: TS/TSX + Three.js/R3F, tidak tahu Midtrans atau Prisma.
- `packages/commerce`: TypeScript server, tidak mengimpor Canvas.
- `apps/web`: TSX route/layout dan server functions untuk menggabungkan modul.

## Disiplin
Gunakan strict TypeScript, kurangi `any`, lakukan schema parsing di boundary, hindari double truth antara class renderer dan React, dan tambahkan type tests untuk format desain.
