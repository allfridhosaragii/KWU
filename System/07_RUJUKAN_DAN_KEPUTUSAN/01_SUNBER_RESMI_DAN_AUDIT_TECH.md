# Sumber Resmi, Status Verifikasi, dan Batas Klaim

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Sumber teknis diverifikasi 20 Oktober 2026
1. Next.js App Router — https://nextjs.org/docs/app
2. Server/Client Components — https://nextjs.org/docs/app/getting-started/server-and-client-components
3. Next.js lazy loading (`ssr:false` client wrapper) — https://nextjs.org/docs/app/guides/lazy-loading
4. Next.js authentication authorization — https://nextjs.org/docs/app/guides/authentication
5. Turborepo repository structure — https://turborepo.dev/docs/crafting-your-repository/structuring-a-repository
6. React Three Fiber performance, frameloop demand, PerformanceMonitor — https://r3f.docs.pmnd.rs/advanced/scaling-performance
7. Three.js GLTFLoader — https://threejs.org/docs/pages/GLTFLoader.html
8. Three.js KTX2Loader — https://threejs.org/docs/pages/KTX2Loader.html
9. Three.js DecalGeometry — https://threejs.org/docs/pages/DecalGeometry.html
10. glTF Transform — https://gltf-transform.dev/
11. Zustand re-render and selectors — https://zustand.docs.pmnd.rs/
12. Prisma Auth.js guide — https://docs.prisma.io/docs/guides/authentication/authjs/nextjs
13. Midtrans HTTP webhook, signature, idempotency — https://docs.midtrans.com/docs/https-notification-webhooks
14. Cloudflare R2 custom domain cache — https://developers.cloudflare.com/cache/interaction-cloudflare-products/r2/
15. MDN WebGL best practices — https://developer.mozilla.org/en-US/docs/Web/API/WebGL_API/WebGL_best_practices
16. OWASP ASVS v5 — https://github.com/OWASP/ASVS
17. WCAG 2.2 pointer/drag accessibility — https://www.w3.org/WAI/standards-guidelines/wcag/new-in-22/
18. Web Vitals — https://web.dev/articles/vitals

## Status fakta vs usulan
- *Diverifikasi dokumentasi resmi*: fitur Server Components, dynamic import client boundary, R3F on-demand loop, GLTFLoader Meshopt/KTX2, glTF compression, Midtrans verification, R2 cache custom domain, WCAG drag alternative.
- *Keputusan engineering*: folder, package names, DB schema, auth provider konfigurasi, profile budget, nama API, demo roadmap.
- *Belum diverifikasi di kode*: compatibility exact dependency versions, FPS dan ukuran scene, tampilan manekin final, deployment hosting dan pembayaran real.

## Bagaimana memvalidasi setelah bootstrap
Buat branch, install dependencies dengan versions locked, `pnpm exec turbo run typecheck`, run tests, build, test GLB on real phones, compare Web Vitals dan payment sandbox outcomes. Perbarui ADR jika hasil tidak sesuai estimasi.
