# Kalkulator Harga, Stok, Reservasi, dan Race Condition

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Formula sumber kebenaran
`basePrice + Σ(component.priceDelta * quantity) + selectableOptions + packagingFee + deliveryCharge - promotionDiscount = orderPayable` (semua validasi dilakukan server). Pajak berlaku sesuai kewajiban bisnis dan konfigurasi resmi; tidak mengarang nominal pajak.

## Tipe uang
Gunakan integer IDR (`bigint` bila perlu) atau Prisma Decimal untuk calculation. Jangan menggunakan bilangan float JS lalu menyimpan nominal yang dapat berbeda antara browser dan PSP. Konversi ke nilai string/format hanya pada presentasi.

## Protokol quote
1. UI mengirim design config (IDs dan transform), **bukan harga yang harus dipercaya**.
2. Server mengambil product, variants, components, stock/rules, mengecek validity.
3. Server memberi quote breakdown, idempotency/quoteId bila diperlukan, expiry singkat.
4. Saat checkout, server menghitung ulang. Jika harga berubah, UI meminta user menyetujui nominal baru sebelum membuat pembayaran.

## Stok
`StockItem` dapat merepresentasikan bahan atau komponen fisik; `InventoryMovement` append-only menelusuri penambahan/penjualan/adjust. Saat transaksi dibuat pilih strategi **reservasi stok sementara** berbatas waktu, dengan release saat expire/failure; atau pengurangan saat paid sesuai risiko over-selling. Tidak boleh decrement dua kali ketika webhook duplikat.

## Atomisitas
Gunakan DB transaction dengan isolation/conditional update yang sesuai untuk stock reservation dan order creation. Periksa concurrent checkout untuk komponen terakhir. Payment provider side effect tidak berada dalam DB transaction panjang; gunakan state machine dan compensation/reconciliation.

## Contoh breakdown
Gelang Rp55.000 + charm hati 2×Rp8.000 + giftbox Rp10.000 = Rp81.000 sebelum ongkir/biaya lain. Contoh angka untuk tes, bukan daftar harga nyata.

## Test adversarial
Buyer ubah harga request ke 1, negative quantity, component SKU dihapus, expired quote, dua browser bayar stok terakhir, replay webhook, oversized elements, invalid size/case compatibility.
