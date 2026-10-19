# Aturan Customizer Jewelry dan Bag Charm

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Gelang (bracelet)
- `CharmRail` adalah spline/jalur attachment pada bracelet; posisi elemen ditulis normalized `t∈[0,1]` atau discrete slot yang sesuai proses produksi.
- Jumlah charm maksimal tergantung panjang bracelet dan ruang fisik; minimal spacing berdasar bbox mm, bukan pixels.
- Perubahan preset mengubah base chain/bracelet color/type, tetapi periksa kompatibilitas charm. Jika tidak kompatibel, minta user konfirmasi penghapusan elemen tertentu.
- Undo/redo mencatat `ADD_CHARM`, `MOVE_CHARM`, `REMOVE_CHARM`, `CHANGE_MATERIAL`.

## Cincin (ring)
- Anchor untuk `thumb/index/middle/ring/pinky`. Perpindahan hanya jika diameter/size tersedia; clamp posisi ke area pemakaian yang realistis di ruas bawah jari.
- Material metal, model, ornament stone; jangan buat kebebasan geser melewati kulit atau ruas jari.
- Simpan `fingerId`, `ringSizeId` dan `ringPreset` dalam design configuration.

## Kalung (necklace)
- Rantai mengikuti neck anchor dan panjang yang tersedia; pilih dari panjang fisik valid misalnya enumerasi SKU, bukan drag bebas tak terhingga.
- Liontin bergeser dalam batas chain slider atau pendant anchor; rotasi dibatasi agar konektor tidak terbalik.
- Gerak leher dan kamera harus mempertahankan posisi kalung; untuk mobile gunakan pose animation bukan real-time cloth simulation.

## Gantungan tas (bag-charm)
- Tas preview mempunyai beberapa `hookAnchorId` tergantung model tas. Charm dapat dipindah ke anchor yang kompatibel.
- Rantai/gantungan berada pada grup pengait yang sama agar gerak sinkron. Efek sway opsional dibatasi waktu 0.4–0.8 s untuk kualitas Balanced/High, bukan physics loop kontinu.
- Pilihan bag model untuk preview tidak otomatis membuat tas sebagai barang yang dijual.

## Shared validation
`validatePlacement(component, anchor, variant, sceneRules) -> valid | reasons[]`. Server mengecek ulang kompatibilitas dan batas jumlah komponen sebelum save/order. Semua operasi editor memicu autosave revision setelah debounce.
