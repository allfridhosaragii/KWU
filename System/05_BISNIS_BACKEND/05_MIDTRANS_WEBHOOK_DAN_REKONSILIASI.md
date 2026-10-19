# Midtrans: Sandbox, Signature, Status, dan Rekonsiliasi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Integrasi dipilih
Gunakan Midtrans sandbox untuk pengembangan. Server membuat transaksi dengan credential server-only; client hanya membuka halaman/SDK pembayaran sesuai metode integration yang akhirnya dipilih. Sebelum production wajib atur public HTTPS callback, verifikasi seluruh alur, dan proses legal/onboarding PSP.

## Verifikasi webhook
1. Terima POST JSON dari provider pada `/api/payment/webhook`.
2. Validasi content type, schema, order ID dan gross amount terhadap order server.
3. Verifikasi signature menggunakan formula yang dijelaskan Midtrans: `SHA512(order_id + status_code + gross_amount + ServerKey)`; dapat juga cross-check melalui GET Status API server-side.
4. Periksa `transaction_status` (settlement/capture sesuai metode), `status_code` dan `fraud_status` sesuai aturan resmi. Status `pending` bukan paid.
5. Terapkan perubahan status dengan transaction DB dan unique event key agar idempotent.
6. Catat event untuk audit dan response cepat; pemrosesan nonkritikal (email/thumbnail) asynchronous.

## Tabel state
| Provider status | Internal payment | Aksi bisnis |
|---|---|---|
| pending | PENDING | jangan mulai produksi |
| settlement | PAID | tandai sukses setelah verifikasi |
| capture | PAID bila status fraud valid | sesuai metode dan verifikasi |
| deny/failure | FAILED | mark dan release reservation bila policy |
| expire | EXPIRED | release reservation |
| cancel | CANCELED | jangan fulfil |
| refund/partial_refund | REFUNDED/PARTIAL_REFUND | update ledger, stok sesuai kebijakan |

## Rekonsiliasi
Webhook dapat terlambat/duplikat. Jalankan status query dari backend ketika order lama pending, dengan rate control. Order owner tidak boleh menjadi 'lunas' hanya karena browser menampilkan URL `.../result?success=true`.

## Keamanan
Jangan log ServerKey, signature string full, token sensitif. Gunakan constant-time compare bila memungkinkan, cek nominal/currency/order relation, hindari overselling karena event berulang.

## Referensi resmi
https://docs.midtrans.com/docs/https-notification-webhooks
https://docs.midtrans.com/reference/handle-notifications
