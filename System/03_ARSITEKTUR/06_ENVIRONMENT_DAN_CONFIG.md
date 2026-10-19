# Environment Variables, Rahasia, dan Konfigurasi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## `.env.example` konseptual
```dotenv
# General
NODE_ENV=development
NEXT_PUBLIC_APP_URL=http://localhost:3000
APP_TIMEZONE=Asia/Jakarta

# Database (server only)
DATABASE_URL=postgresql://user:password@localhost:5432/kwu_dev

# Authentication (server only)
AUTH_SECRET=replace_me_random_secret

# Payment (server only except public client identifier)
MIDTRANS_SERVER_KEY=replace_me
MIDTRANS_CLIENT_KEY=replace_me
MIDTRANS_IS_PRODUCTION=false

# Assets
NEXT_PUBLIC_ASSET_CDN_BASE=https://assets.example.com
R2_ACCOUNT_ID=replace_me
R2_BUCKET_NAME=kwu-assets
R2_ACCESS_KEY_ID=replace_me
R2_SECRET_ACCESS_KEY=replace_me
```

## Aturan
- Ini contoh placeholder; **jangan push `.env` berisi rahasia**. `.env.example` boleh committed.
- Secret harus ditempatkan di secret store hosting / CI GitHub Secrets; token jangan dicetak dalam log.
- `NEXT_PUBLIC_*` di-bundle ke browser. Jangan awali token server dengan prefix ini.
- Pisahkan DB, storage, callback payment, email dan auth environment dev/staging/production; sandbox Midtrans hanya di dev/staging.
- Validasi environment startup menggunakan Zod dan fail fast jika variabel wajib tidak tersedia.
- Rotasi key jika bocor, audit commit history, dan gunakan hak minimum untuk R2 serta database.

## Konfigurasi yang bukan secret
Quality budget, ukuran tekstur, batas komponen, jumlah elemen per desain, dan camera presets berada di file configuration terversi serta dapat diubah owner melalui UI hanya setelah validasi.
