# Integrasi System dengan 34 Halaman UI/UX

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Pola route yang dikunci
11 publik: `/`, `/shop`, `/products/[slug]`, `/studio`, `/studio/[type]/[productId]`, `/cart`, `/checkout`, `/checkout/result`, `/help`, `/about`, `/legal/[slug]`.
4 auth: `/login`, `/register`, `/forgot-password`, `/reset-password`.
7 buyer: `/account`, `/account/designs`, `/account/wishlist`, `/account/orders`, `/account/orders/[id]`, `/account/addresses`, `/account/profile`.
12 owner: `/owner`, `/owner/orders`, `/owner/orders/[id]`, `/owner/products`, `/owner/products/new|[id]/edit` satu template, `/owner/components`, `/owner/assets`, `/owner/inventory`, `/owner/payments`, `/owner/customers`, `/owner/reports`, `/owner/settings`.

## Strategi server/client
| Route | Render | Boleh load 3D? | Akses |
|---|---|---|---|
| `/`, `/shop` | Server Components data dan image, filter via URL | Tidak | publik |
| `/products/[slug]` | Server data dan gallery | Preview bila ditekan | publik |
| `/studio/[type]/[productId]` | Server initial config + dynamic Client Canvas | Ya | preview guest mungkin |
| `/cart`, `/checkout` | Server session + client form | Hanya thumbnail | buyer untuk checkout |
| `/account/designs` | SSR list + preview thumbnail | Saat membuka desain | buyer |
| `/owner/orders/[id]` | Server authorization + detail | preview lazy bila diminta | owner |
| `/owner/assets` | Server list | lazy model inspector | owner |

## Kontrak navigasi
- Buyer navbar: Beranda, Belanja, Studio, Keranjang, Akun. Owner: Ringkasan, Pesanan, Produk, Lainnya.
- Auth dan checkout menampilkan header fokus tanpa nav penuh. Studio memakai bottom sheet kontekstual dan tidak menyisakan navbar yang memakan layar.
- Satu halaman editor untuk delapan tipe dengan strategi scene/rendering terpisah.

## Konsistensi desain
Token warna `--color-background: #FAF7F2`, `--color-primary: #8F503C`, `--color-text: #302822`, headline Cormorant Garamond, body Manrope. Detail dan kontras mengikuti `../Design Konsep/01_DESIGN_SYSTEM/`.

## Kewajiban desain error
Server → `error.tsx` dan inline error; Canvas → poster 2D + retry; checkout → tidak mengulang pembayaran secara diam-diam; jaringan offline → hindari kehilangan perubahan lokal.
