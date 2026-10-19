# Strategi Testing Unit, Integrasi, E2E dan Mobile

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Test pyramid
- Unit (Vitest): price calculator, tax/discount rounding, constraint validators, serializer/hydrator, schema migration, order state transitions.
- Component: bottom sheet state, error/empty/loading, accessibility semantics, reduced motion.
- Integration: Prisma test DB transactions, stock reservation under concurrency, authenticated Server Actions, webhook signatures/idempotency.
- E2E (Playwright): login buyer/owner, search, 8 category customizers smoke, save design, cart, checkout sandbox, order owner.
- Manual real-device: gesture multi-touch, WebGL context loss, Safari iOS, memory growth, texture quality and performance.

## Folder tes
```text
tests/
  e2e/{auth,catalog,studio-bracelet,studio-ring,studio-necklace,studio-bag,studio-stickers,cart,checkout,owner}.spec.ts
  integration/{pricing,stock,payment,design-persistence}.test.ts
  visual/{mobile,desktop}.spec.ts
  performance/{fps,drawcalls,memory,loadtime}.ts
  security/{rbac,price-tampering,webhook-replay}.test.ts
```

## Input gesture
Playwright mobile emulation **tidak sama** dengan pengukuran GPU perangkat fisik. Gunakan emulasi untuk layout dan flow, lalu real device untuk FPS/interaksi dua jari. Visual regression thumbnails dengan toleransi render yang masuk akal karena driver GPU dapat berbeda.

## Kasus yang sering terlupakan
- 2 produk SKU sama dengan dua desain berbeda di cart.
- Harga berubah saat checkout, harus ada konfirmasi.
- Webhook sukses datang dua kali; tidak mengurangi stok dua kali.
- Browser back/refresh selama payment pending.
- Saved design dibuka setelah assetVersion naik.
- Owner mengganti material tapi order historis tetap.
- Scene berpindah 30 kali tanpa memory leak.
- Ketika 3D mati, user masih bisa melihat detail produk dan status cart secara jelas.

## Bukti tes
Setiap acceptance dicatat `{device, os, browser, commitSHA, testData, steps, result, screenshot/report, timestamp}`. Tidak menyebut 100% bebas bug berdasarkan satu pass.
