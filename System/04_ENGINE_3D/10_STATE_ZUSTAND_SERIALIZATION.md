# Zustand, State 3D, Serialization, dan Autosave

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Pembagian state
1. `DesignDomainState`: daftar elemen, varian, scene type, preset, schemaVersion; serializable.
2. `InteractionUIState`: selectedElementId, activeSheet, edit mode, undo/redo; tidak semua dipersist.
3. `RendererTransient`: refs Object3D, camera matrices, GPU resource handles, FPS; **jangan masuk JSON saved design**.

## Zustand
Pakai selector granular. Komponen harga hanya subscribe `quote`, scene render tidak re-render karena nilai unrelated. Untuk objek turunan gunakan `useShallow` bila sesuai. Hindari `setState` pada setiap frame dari animation loop; Three.js object refs di-update imperatively lalu scene invalidate.

## Reducer/actions
`applyPreset`, `selectComponent`, `placeElement`, `moveElement`, `rotateElement`, `updateVariant`, `removeElement`, `undo`, `redo`, `reset`. Setiap action mengembalikan state valid atau error alasan; jangan diam-diam terima transform invalid.

## Save lifecycle
- Debounce autosave sekitar 500–1500 ms sebagai target tuning; persist hanya setelah user authorized dan payload lulus Zod.
- Simpan local draft ringan jika offline untuk mengurangi kehilangan progres; tetap beri notifikasi belum tersinkron server dan jangan menyimpan sensitive payment data.
- Request bawa `revision`, server mengembalikan revision + `updatedAt`, handle konflik edit dua perangkat.
- Thumbnail generation berjalan tersendiri sehingga gagal thumbnail tidak membatalkan data JSON.

## Serializer
`serializeDesign(domainState)` menghasilkan hanya stable IDs, numbers finite, transform normalized, schemaVersion dan assetVersion. `hydrateDesign` validasi schema, migrasi bila perlu, lalu resolve asset manifest. Unit test roundtrip dan snapshot semantik, bukan membandingkan pointer objek Three.js.

## Sumber
https://zustand.docs.pmnd.rs/
https://github.com/pmndrs/zustand/blob/main/docs/learn/guides/prevent-rerenders-with-use-shallow.md
