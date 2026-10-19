# Koneksi Design Konsep ke Kode UI

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Mapping design tokens
- `Design Konsep/01_DESIGN_SYSTEM/01_WARNA_DAN_TOKEN.md` → `packages/ui/src/tokens/colors.css`.
- `02_TIPOGRAFI.md` → `typography.css` dan config font di Next.js.
- `03_GRID_SPACING_DAN_UKURAN.md` → `spacing.css`, `radii.css`, responsive utilities.
- `08_MOTION_DAN_MICROINTERACTIONS.md` → motion tokens, `prefers-reduced-motion`, animasi CSS sedapat mungkin.
- `04_TOMBOL_INPUT_DAN_FORM.md` → `Button`, `Input`, `Select`, `Dialog`, `BottomSheet`, `Toast`.

## Aturan komponen reusable
- `Button` punya varian primary/secondary/ghost/danger; state loading/disabled/focus.
- `ProductCard` memakai image statis, nama, harga, variants dan wishlist, **bukan Canvas 3D permanen**.
- `MobileBottomNavigation` menyala di halaman toko/akun buyer, tersembunyi saat checkout dan studio.
- `OwnerBottomNavigation` empat kategori; daftar panjang lewat area Lainnya.
- `CustomizerMobileSheet` dikelola Client, harus bisa ditutup dan tak menutup tombol final.

## Figma handoff
Setiap desain harus punya component ID dan state; developer memetakan token dan komponen, bukan memilih hex bebas. Layout diset dari 390×844 dan diuji 320/360/375/390/430/768/1024/1440 px. Interaksi drag harus memiliki alternatif tombol/slider.

## Implementasi responsif
`100dvh` untuk area utama dengan fallback; safe-area `env(safe-area-inset-bottom)` untuk sticky CTA; jangan block scroll body secara global di luar modal aktif. Saat keyboard mobile terbuka, footer CTA tidak boleh menutupi input penting.
