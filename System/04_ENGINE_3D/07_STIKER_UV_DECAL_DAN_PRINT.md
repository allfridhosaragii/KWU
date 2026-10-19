# Sistem Stiker UV, Decal, Area Valid, dan Cetak

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Prinsip geometri
Stiker adalah 2D artwork terikat surface 3D. Posisi produksi harus berupa `surfaceId`, local UV/parameter surface, lebar dan tinggi mm, rotasi radian; bukan proyeksi piksel layar.

## Strategi per media
| Media | Placement default | Constraint |
|---|---|---|
| HP belakang case polos/transparan | UV pada casing outer back | mask kamera, margin tepi, varian casing |
| iPad/tablet Apple belakang | UV plane belakang | kamera, radius sudut, penempatan portrait/landscape |
| MacBook cover luar | UV plane lid | area hinge/logo (jika relevan), safe edge |
| Botol stainless | cylindrical UV / angle-height parameter | seam wrapping, area lengkung bahu/tutup terlarang |

## Raycaster ke UV
Saat pengguna menyentuh permukaan, raycast mesh target, baca `intersection.uv`, konversi ke koordinat local permukaan sesuai transform dan mask. Pada silinder simpan angle normalized dan posisi tinggi mm agar stiker mengikuti kelengkungan dan wrap seam secara deterministik.

## DecalGeometry
Dapat dipakai untuk pratinjau sticker projector pada permukaan nyaris datar. **Jangan mengandalkan decal di sudut tajam** karena dapat terdistorsi; botol perlu UV mapping yang mempertahankan skala fisik. Uji z-fighting dan transparency sorting, terutama ketika banyak stiker bertumpuk.

## Editor
- Select sticker, drag, rotate, scale dengan handle; snapping ke margin/garis tengah opsi; layer ordering bila overlap diizinkan.
- Undo/redo, duplicate sticker (jika stok/produksi memungkinkan), delete, reset to preset.
- Validasi `widthMm`, `heightMm`, `minPrintableMm`, `maxPrintableMm`, no-go mask, jumlah maksimum.
- Preview overlay garis area valid saat edit, sembunyikan saat melihat hasil final.

## Produksi stiker fisik
- Simpan original vector/source artwork SVG atau raster resolusi cukup untuk ukuran fisik, **bukan screenshot 3D** sebagai master print.
- Metadata file: jenis bahan (vinyl), dimensi mm, bleed/cut contour jika vendor printer meminta, ICC/profile warna vendor, quantity, SKU.
- Siapkan export komposisi cetak dalam 2D koordinat mm secara terpisah dari rendering produk, dengan PDF/SVG bila produksi memerlukan.
- Jika stiker hanyalah barang lepas, jelaskan di checkout bahwa HP/tablet/MacBook/botol hanya mockup.

## Sumber
https://threejs.org/docs/pages/DecalGeometry.html
