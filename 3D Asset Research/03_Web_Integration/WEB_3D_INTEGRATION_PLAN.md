# Web 3D Integration Plan

## Objective
Menampilkan aset 3D berkualitas tinggi tetapi tetap ringan dan usable di mobile web.

## Core stack
- Next.js
- TypeScript
- Three.js
- React Three Fiber
- Drei
- Zustand

## Scene policy
- Jangan memuat engine 3D pada katalog biasa.
- 3D hanya dimuat di halaman studio/detail yang relevan.
- Gunakan loading state dan poster image.

## Asset policy
- Satu asset master dapat memiliki beberapa level kualitas.
- Mobile default menggunakan quality balanced.
- Tambahkan fallback static preview.

## Product-specific integration
### Bracelet
- hand mannequin + bracelet anchors + charm track

### Ring
- hand/fingers + finger switch logic

### Necklace
- neck mannequin + chain length presets

### Bag charm
- backpack + attachment anchors

### Phone sticker
- iPhone 17 + case switch + sticker transform tools

### Tablet sticker
- iPad Pro + printable zone

### MacBook sticker
- MacBook Air + hinge open/close

### Bottle sticker
- bottle + cylindrical placement

## Performance rules
- lazy load assets
- demand-based rendering when idle if possible
- texture compression
- adaptive DPR
- profiling on low-end and mid-range mobile
