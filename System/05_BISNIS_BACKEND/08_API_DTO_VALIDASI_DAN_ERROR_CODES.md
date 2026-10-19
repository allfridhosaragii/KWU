# Kontrak API, DTO, Validasi, dan Error Codes

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Pola DTO
Data yang keluar dari server harus berupa typed DTO, bukan Prisma raw model. Gunakan envelope konsisten dan jangan bocorkan internal IDs bila tidak dibutuhkan.

```json
{
  "ok": false,
  "error": {
    "code": "PRICE_CHANGED",
    "message": "Harga produk diperbarui. Periksa total baru sebelum lanjut.",
    "fields": {},
    "requestId": "req_example"
  }
}
```

## Daftar error penting
| Code | HTTP | Penyebab | Perilaku UI |
|---|---|---|---|
| `UNAUTHENTICATED` | 401 | belum login | arahkan login, simpan intention |
| `FORBIDDEN` | 403 | role/resource tak berhak | halaman 403 atau dialog |
| `NOT_FOUND` | 404 | item tidak ada/akses disamarkan | not found |
| `INVALID_DESIGN` | 422 | keluar constraint | sorot elemen invalid |
| `OUT_OF_STOCK` | 409 | stok habis | pilih varian lain |
| `PRICE_CHANGED` | 409 | server quote beda | review harga |
| `DESIGN_VERSION_UNSUPPORTED` | 409 | perlu migration | recovery/duplicate |
| `REVISION_CONFLICT` | 409 | autosave bentrok | reconcile/duplicate |
| `PAYMENT_PENDING` | 202 | status belum final | refresh status, bukan success |
| `RATE_LIMITED` | 429 | terlalu banyak request | retry later |
| `INTERNAL_ERROR` | 500 | kegagalan server | retry + requestId |

## Schema Zod
Validasi `productId`/`designId` string size/format, `quantity` integer positif, size mm wajar, sticker transform finite, enum studioType 8 kategori, max elements/per-user limits. Pastikan canonicalizer clamp jika UI preview bisa toleran namun server reject produk tak mungkin diproduksi.

## Version headers
Jika perubahan kontrak besar, gunakan schemaVersion di body dan migration. API endpoint dapat tetap stabil; jangan memaksa browser lama membuat order dengan format yang tak dikenali.

## Logging
requestId merujuk log server sanitized; audit event pada order/stock/payment state. Jangan tampilkan SQL/error stack penuh pada client.
