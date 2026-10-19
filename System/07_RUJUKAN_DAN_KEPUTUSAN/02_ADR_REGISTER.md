# Architecture Decision Records (ADR) dan Alasan

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## ADR-001 — Next.js TypeScript modular monolith
**Dipilih:** satu web app dengan server/backend internal, package modular. **Ditolak awal:** Laravel+Next API ganda atau microservice. **Alasan:** lebih sederhana deploy dan debugging. **Kaji ulang:** scale terukur memerlukan worker atau service independen.

## ADR-002 — WebGL2 / React Three Fiber
**Dipilih:** Three.js + R3F/Drei dengan dynamic import. **Ditunda:** WebGPU sebagai jalur utama. **Alasan:** dukungan browser/mobile yang dapat diuji dan banyak tooling glTF. **Kaji ulang:** benchmark menunjukkan keunggulan nyata dan matriks browser memenuhi target.

## ADR-003 — Versioned serializable design
**Dipilih:** data konfigurasi JSON typed Zod + anchor/UV, bukan simpan screenshot semata. **Alasan:** reproducible order dan produksi. **Kaji ulang:** tidak perlu, inti domain.

## ADR-004 — Surface UV untuk sticker
**Dipilih:** UV/parameter silinder source-of-truth, DecalGeometry opsional visual. **Alasan:** scale mm/print akurat dan sudut/silinder tidak mudah distorsi. **Kaji ulang:** setelah export uji print fisik.

## ADR-005 — Pemrosesan server authoritative
**Dipilih:** server revalidasi harga, stok, compatibility dan payment. **Ditolak:** harga berasal local store, sukses berdasarkan redirect. **Alasan:** risiko finansial dan audit.

## ADR-006 — R2+CDN asset version
**Dipilih:** public immutable hashed assets, private user content. **Alasan:** storage/file delivery terpisah dari server Next dan order lama reproducible.

## ADR-007 — Worker deferred
**Dipilih:** `apps/worker` sebagai rencana bukan dependency sekarang. **Alasan:** mencegah overengineering. **Trigger:** antrean file 3D, email atau thumbnail tidak dapat dikerjakan aman dalam request.

## ADR-008 — Two roles only
**Dipilih:** `BUYER/OWNER` sesuai produk. **Ditolak:** admin/seller tambahan tanpa kebutuhan. **Alasan:** UI dan RBAC konsisten dengan Design Konsep.

## Template ADR baru
`ID, status, tanggal, konteks, opsi, keputusan, konsekuensi, rollback, evidence, link PR`. Keputusan dengan dampak besar harus membuat ADR baru, bukan sekadar diam-diam ubah tool.
