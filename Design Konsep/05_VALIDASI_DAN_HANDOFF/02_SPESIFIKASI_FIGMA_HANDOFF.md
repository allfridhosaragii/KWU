# Struktur File Figma dan Developer Handoff

## Struktur halaman Figma yang direkomendasikan

```text
KWU — DIGITAL ATELIER
├── 00 — Cover & Research
├── 01 — Foundations (Color, Type, Grid, Motion)
├── 02 — Components (Buttons, Inputs, Cards, Sheets, Nav)
├── 03 — Storefront (Pages 01–11)
├── 04 — Authentication (Pages 12–15)
├── 05 — Buyer Account (Pages 16–22)
├── 06 — Owner (Pages 23–34)
├── 07 — 3D Studio (8 Category Variants)
├── 08 — Tablet / Desktop Adaptation
├── 09 — Prototypes, Flows & States
└── 10 — Developer Handoff
```

## Figma Variables

- Color primitives, Color semantic light, Spacing, Radius, Typography styles.
- Variants tombol: primary/secondary/ghost, default/pressed/loading/disabled.
- Variants product card: normal/saved/unavailable/loading.
- Status: pending/success/error/processing.
- Studio toolbar: camera/edit, selected/not selected, sheet state.

## Penamaan frame

`P01_Home_Mobile_Default`, `P05_StudioBracelet_Mobile_Edit`, `P05_StudioBottle_Mobile_SelectedSticker`, `P25_OwnerOrder_Mobile_PaymentPending`, `P07_Checkout_Mobile_Error`.

## Ukuran awal

- 390 × 844 mobile baseline.
- 320 × 640 dan 430 × 932 untuk overflow QA.
- 768 × 1024 tablet.
- 1440 × 900 desktop.

## States minimal per halaman

1. Normal/default.
2. Loading data atau asset.
3. Empty jika mungkin.
4. Error/validation.
5. Interaksi penting: selected, expanded, pending, success sesuai konteks.
6. Tablet/Desktop adaptation untuk layout kritis.

## Handoff ke developer

- Gunakan Auto Layout untuk komponen dan frame utama.
- Gunakan grid constraints, bukan posisi absolut yang pecah ketika konten panjang.
- Tulis nama token, bukan hanya nilai HEX di komentar.
- Lampirkan behavior spec gesture/scroll, bukan sekadar garis panah prototype.
- Sertakan contoh panjang teks Indonesia dan state harga berubah.
- Cantumkan asset image dengan izin pakai; gambar riset tidak otomatis legal untuk produksi.
- Serahkan string UI dan desain fallback 2D Studio.

## Komponen prioritas dibangun sebagai library

Button, IconButton, TextField, Select, SegmentedControl, Tabs, ProductCard, ProductGallery, PriceBreakdown, StatusBadge, BottomNavigation, OwnerNavigation, BottomSheet, Toast, ConfirmDialog, EmptyState, ErrorState, Skeleton, StickerLayerList, OrnamentPicker, SceneToolbar.

## Validasi Figma

- Tidak ada komponen terlepas dari tokens tanpa catatan.
- Semua CTA utama punya loading/disabled state.
- Handoff 3D menyertakan batas anchor/surface dan alternatif drag.
- Naming dan urutan 34 halaman sesuai indeks paket ini.
