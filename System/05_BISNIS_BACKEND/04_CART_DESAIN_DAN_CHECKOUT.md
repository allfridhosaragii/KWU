# Keranjang, Snapshot Desain, Checkout, dan Idempotency

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Struktur CartItem
`id, buyerId, productId, variantId, designId? atau embedded design snapshot, quantity, lastQuotedAt, serverPriceBreakdown, previewAssetId?`. Dua konfigurasi berbeda dari product yang sama adalah cart item berbeda; merge hanya apabila hash konfigurasi identik dan aturan quantity mengizinkan.

## Checkout state machine
```text
CART_READY -> CHECKOUT_VALIDATING -> ORDER_PENDING_PAYMENT
                                  -> OUT_OF_STOCK | PRICE_CHANGED
ORDER_PENDING_PAYMENT -> PAID -> PROCESSING -> SHIPPED -> COMPLETED
                      -> EXPIRED | CANCELED | FAILED
```
Status order dan payment **dipisahkan**. `PAID` belum tentu `PROCESSING` jika owner belum memulai produksi.

## Langkah membuat order
1. Verify buyer session & addresses.
2. Load semua cart item di server, validasi produk masih published dan semua design valid.
3. Re-quote harga, ongkir, promo dan stok. Minta persetujuan jika ada perubahan.
4. Dalam transaksi DB: simpan order draft/pending, snapshot data barang+design+harga, reservasi stok, set idempotency key.
5. Panggil payment adapter untuk membuat transaksi. Jika gagal, catat status dan release resource sesuai policy.
6. Redirect ke pembayaran resmi. Jangan menyimpan detail kartu sensitif.
7. Callback browser hanya memperbarui UI sementara; payment status final dari verified backend notification/status query.

## Immutable snapshot
Order Item memuat product name/SKU, variant, image, size, material, list komponen, transform normalized, asset/rules version, unit price. Ketika owner edit produk, pesanan lama tidak berubah.

## Idempotency
Checkout punya token request unik per buyer/cart state agar double-tap Pay tidak menciptakan dua order/pembayaran. Implement provider integration memastikan satu merchant order ID unik untuk satu payment attempt.

## Recovery
Refresh checkout tidak membuat payment baru otomatis; UI dapat mengambil status order yang ada, retry secara eksplisit jika eligible. Error payment jangan menghapus desain di cart.
