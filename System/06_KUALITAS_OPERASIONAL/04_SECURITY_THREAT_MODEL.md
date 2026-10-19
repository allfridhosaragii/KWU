# Threat Model, OWASP, Privasi, dan Keamanan Transaksi

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Aset bernilai tinggi
Akun buyer/owner, alamat dan data pelanggan, saved designs, master sticker files, catalog/product prices, stock, payment state, CDN publish pipeline dan auth secrets.

## Ancaman dan mitigasi
| Ancaman | Contoh | Kontrol |
|---|---|---|
| IDOR/BOLA | buyer ganti orderId user lain | `userId` scoped DAL dan authorization server |
| Role escalation | register `role=OWNER` | ignore client role, owner provisioning terpisah |
| Price tampering | client kirim total Rp1 | server pricing + quote revalidation |
| Payment spoofing | frontend mengklaim paid | verified webhook + status API + amount match |
| Webhook replay | notifikasi duplikat | event uniqueness + idempotent state transition |
| Invalid 3D payload | NaN/Infinity, offset jauh | Zod, finite numeric clamp/reject, maximum complexity |
| Malicious upload | SVG with script, polyglot file, huge GLB | server allowlist/size/decode validation, sanitize, quotas |
| XSS | deskripsi produk berbahaya | escape framework, sanitize rich text, CSP |
| CSRF/session abuse | unauthorized mutation | cookies SameSite, auth checks, framework defenses |
| SSRF | arbitrary asset URL | storage key curated, no proxy fetch arbitrary URL |
| Supply chain | malicious dependency | lockfile, audit, restricted CI secrets |
| Data leakage | public private preview bucket | bucket separation, signed URL/private proxy |

## Checklist keamanan
- Force HTTPS untuk live; secure/session cookie and signout expiration.
- Rate limit login/password reset/upload/checkout/status polling.
- Password hashing Argon2id (atau library approved yang setara), reset token one-time hashed, login audit.
- CORS ketat untuk asset upload dan API bila cross-origin; security headers (CSP khusus Three.js dan PSP diuji).
- Secrets tidak diekspos dalam bundle dan tidak di-commit.
- SQL injection dicegah parameterized ORM/raw query binding; server-only DB access.
- Authorization check pada semua action dan DAL; bukan client nav.
- Backup encrypted, monitoring error, incident rollback plan.

## Standard acuan
OWASP ASVS 5.0 untuk control verification, terutama auth/access control, input validation dan API. Checklist ini belum menggantikan pentest production.
https://github.com/OWASP/ASVS
