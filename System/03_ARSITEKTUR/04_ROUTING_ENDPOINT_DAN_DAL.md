# Router, Endpoint, dan Data Access Layer

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Klasifikasi endpoint
| Operasi | Implementasi awal | Auth | Catatan |
|---|---|---|---|
| GET katalog & produk | Server Component DAL | publik | query filter/pagination schema |
| GET detail konfigurasi model | Server read method | publik | public data yang tidak sensitif |
| POST/PUT desain | Server Action / `/api/designs/[id]` | buyer | ownership + validasi |
| Cart actions | Server Actions | buyer | server quote, CSRF/session defense |
| Create order/payment | `POST /api/payment/create` atau service checkout | buyer | transaction + idempotency |
| PSP webhook | `POST /api/payment/webhook` | signature PSP | tidak bergantung cookie session |
| Upload asset sign | `POST /api/assets/sign-upload` | owner untuk aset katalog | MIME allowlist + size limits |
| Owner CRUD | Server Actions | OWNER | otorisasi di fungsi, bukan hanya layout |
| Health endpoint | `GET /api/health` | public sanitized | jangan bocorkan env/DB credentials |

## DAL
`src/server/dal/{product,design,order,user}.ts` menangani query, paginasi, mapping ke DTO. DAL harus memeriksa identitas/role sebelum mengambil data privat, menormalisasi respons dan tidak mengirim seluruh row DB ke browser.

## Validasi
Gunakan Zod untuk pathname slug, query filters, body JSON, transform designs, dan order payload. Batasi ukuran request untuk `designElements`; jangan terima matriks 4x4 bebas tanpa normalisasi.

## Penanganan error
Respons aplikasi yang stabil: `{ code, message, requestId, fieldErrors? }`. Contoh `DESIGN_VERSION_UNSUPPORTED`, `OUT_OF_STOCK`, `PRICE_CHANGED`, `UNAUTHORIZED`, `PAYMENT_PENDING`. Pesan user ramah; detail stack hanya log server.

## Server action dan webhook
Server Action yang mutasi order harus mengontrol race conditions dan return minimal. Webhook harus diverifikasi origin/signature/status, di-ACK cepat dan memproses perubahan status sekali. Jangan expose handler webhook tanpa validasi.
