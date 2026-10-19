# Autentikasi, Sesi, RBAC Buyer–Owner

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Model peran
Enum aplikasi `BUYER`, `OWNER` saja. Guest tanpa akun boleh mengakses halaman public/katalog; save ke akun, checkout, akun pribadi menuntut BUYER login. Owner memakai portal `/owner`, bukan role yang boleh dipilih di register.

## Auth.js
Gunakan session management Auth.js + Prisma adapter yang cocok dengan versi terpasang, cookie HttpOnly, Secure pada HTTPS, SameSite yang sesuai. Pilihan credential email/password memerlukan provider dan service sendiri untuk password hash Argon2id, email verification, lockout/rate limiting, password reset one-time token hashed, expiry, dan logging keamanan.

## Policy per fitur
| Resource | Guest | BUYER | OWNER |
|---|---|---|---|
| Katalog publik | read | read | read/preview |
| Studio publik | preview opsional | edit & save miliknya | preview produk |
| Wishlist/designs | tidak | CRUD miliknya saja | bukan akses per-buyer kecuali kebutuhan operasional sah |
| Cart & checkout | harus masuk menurut kebijakan | checkout dirinya | tidak otomatis checkout sebagai owner |
| Order pribadi | tidak | read miliknya | read operational seluruh order |
| Produk/stok/aset | tidak | tidak | create/update/archive |
| Payment configuration | tidak | tidak | hanya pengaturan terbatas, secret tetap backend |

## Server enforcement
`requireBuyer()`, `requireOwner()`, `assertResourceOwner(userId, design/orderId)`. Periksa pada DAL/service/Server Action/Route Handler, **jangan percaya** redirect layout atau hidden button. Query private harus memasukkan `userId` sehingga IDOR tidak terjadi.

## Audit
Log role-sensitive actions (create product, stock edit, order status, asset publish, refund) dengan actor, waktu UTC, requestId dan target. Jangan log password, auth cookies, payment keys.

## Security test
Guest → /owner returns deny, buyer cannot read other buyer order/design via UUID substitution, direct Server Action tampering, reset token replay, brute-force throttling, session invalidation after password change.

## Sumber
https://nextjs.org/docs/app/guides/authentication
https://docs.prisma.io/docs/guides/authentication/authjs/nextjs
