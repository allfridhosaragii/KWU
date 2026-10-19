# Dashboard Owner, Produksi, Pengiriman, Laporan

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Owner operations
- Dashboard: total omzet periode, jumlah order, butuh diproses, low-stock, recent activity. Hitung revenue dari paid order, bedakan payment/refund dan pending.
- Produk: create/edit/archive SKU/variants, link 3D manifest, poster, presets, components, price rules.
- Asset management: upload/validate/publish GLB, preview anchors/surfaces, version history.
- Orders: filter status, detail final customized design, jumlah komponen, packlist dan shipping label info.
- Payment panel: status PSP terverifikasi, audit webhook, refund request sesuai hak dan dukungan provider.
- Inventory: stock movement, reservation dan low stock alerts.
- Reports: date range Asia/Jakarta, omzet, gross sales, refunds, best-selling category dan export sanitized CSV.

## Production specification
`OrderItem` membuat `ProductionSpec` dengan komponen SKU, quantity, warna/bahan, ukuran fisik, anchor position normalized, artwork file untuk stiker, printer size mm, dan notes. Untuk barang jewelry jangan kirim hanya thumbnail. Untuk stiker, media preview yang bukan item dagangan tidak masuk packlist.

## Workflow status
`NEW`, `IN_PRODUCTION`, `READY_TO_SHIP`, `SHIPPED`, `DELIVERED`, `COMPLETED`; cancel/refund mempunyai aturan sendiri. Owner mengganti status via server action, dengan audit event. Transisi tidak boleh mundur acak kecuali action koreksi sah dan tercatat.

## UX mobile owner
Gunakan card list bukan tabel lebar, sidebar/More menu, sticky actions relevan; 3D hanya di detail order saat owner meminta. Upload/edit anchor kompleks boleh lebih nyaman di desktop, tetapi aktivitas harian order/stock harus mudah di HP.

## Reporting correctness
Penyajian tanggal pakai timezone Asia/Jakarta namun DB UTC; `grossSales` bukan otomatis `netRevenue`, dan refunded/failed tidak masuk paid totals. Rekonsiliasi dengan payment ledger dan sample manual.
