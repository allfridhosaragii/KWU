# Design Tokens Siap Handoff

File ini mendefinisikan **kontrak tampilan**. Implementasi dapat memilih CSS variables, Tailwind theme, atau Figma Variables, tetapi nilainya harus sama. Nilai dapat direvisi melalui design decision log, bukan secara acak di komponen.

## Draft CSS variables

```css
:root {
  --color-background: #FAF7F2;
  --color-surface: #FFFCF8;
  --color-surface-soft: #F3EAE0;
  --color-primary: #8F503C;
  --color-primary-pressed: #743E2E;
  --color-secondary: #64735B;
  --color-accent: #C78962;
  --color-text: #302822;
  --color-text-muted: #695C52;
  --color-border-subtle: #DBCEC1;
  --color-border-strong: #8D715F;
  --color-focus: #79513F;
  --color-success: #416C50;
  --color-error: #A6423D;

  --font-display: 'Cormorant Garamond', Georgia, serif;
  --font-body: 'Manrope', system-ui, sans-serif;

  --space-1: 4px;
  --space-2: 8px;
  --space-3: 12px;
  --space-4: 16px;
  --space-5: 20px;
  --space-6: 24px;
  --space-8: 32px;
  --space-10: 40px;
  --space-12: 48px;
  --space-16: 64px;

  --radius-sm: 8px;
  --radius-md: 12px;
  --radius-card: 16px;
  --radius-sheet: 24px;
  --radius-pill: 999px;

  --touch-target: 44px;
  --button-height: 52px;
  --input-height: 52px;
  --motion-fast: 160ms;
  --motion-standard: 240ms;
  --motion-gentle: 420ms;
}
```

## Naming Figma

- `Color / Text / Primary`
- `Color / Surface / Default`
- `Color / Action / Primary / Default`
- `Radius / Card`
- `Space / 4`
- `Typography / Body / Regular`
- `Motion / Fast`

## Konvensi token

1. Komponen memakai token semantik, bukan HEX literal.
2. Kontras tetap perlu dihitung pada pasangan sesungguhnya (terutama overlay di atas gambar).
3. Material 3D mempunyai pengaturan yang berbeda dari palet UI; warna fisik varian tidak dikunci ke token brand.
4. Dark mode tidak dideklarasikan aktif sampai semua kombinasi warna diuji.
5. Bila nilai direvisi, catat alasan, halaman terdampak, dan pemeriksaan QA ulang.
