# Next.js, React, SSR dan Batas Server–Client

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## Tanggung jawab Server Component
Route `/`, `/shop`, `/products/[slug]`, `/account/orders`, dan `/owner` memuat data secara server-side agar akses data, SEO katalog, dan jumlah JavaScript awal terjaga. Komponen yang hanya menampilkan data tidak memerlukan `use client`.

## Tanggung jawab Client Component
Studio 3D, bottom sheet, drag/zoom, form interaktif, dan state editor harus di client. Gunakan boundary sekecil mungkin agar `three` tidak masuk semua route.

## Pola lazy 3D yang benar
`next/dynamic(...,{ssr:false})` harus diletakkan dalam **Client Component wrapper**, bukan langsung dipakai dengan opsi tersebut dari Server Component. Server `page.tsx` mengambil metadata produk/konfigurasi lalu menyerahkan ke wrapper.

```tsx
// Client component: apps/web/src/features/customizer/CustomizerClient.tsx
'use client'
import dynamic from 'next/dynamic'
const StudioCanvas = dynamic(() => import('./StudioCanvas'), {
  ssr: false,
  loading: () => <div aria-label="Memuat studio">Menyiapkan pratinjau…</div>,
})
export function CustomizerClient({ initialData }: { initialData: unknown }) {
  return <StudioCanvas initialData={initialData} />
}
```
Contoh bersifat ilustratif; pengetikan props final mengikuti kontrak Zod.

## Cache dan keamanan
- Metadata katalog public dapat dicache sesuai kebijakan invalidasi publish produk.
- Harga final, persediaan, alamat, data owner, dan pesanan harus dievaluasi saat request dan tidak dibagikan lintas pengguna.
- Server Action adalah endpoint yang bisa dipanggil. Setiap mutasi ulangi auth, authorization, validasi, dan idempotency jika diperlukan.
- Gunakan React Error Boundaries dan error Next.js route; WebGL context error punya fallback sendiri.

## Data yang tidak boleh diserialisasi ke client
Server Key pembayaran, database URL, storage secret, password hash, token reset, signing secret, serta data buyer lain. Hanya public manifest asset dan data kategori yang memang boleh publik.

## Sumber
https://nextjs.org/docs/app/getting-started/server-and-client-components
https://nextjs.org/docs/app/guides/lazy-loading
https://nextjs.org/docs/app/guides/authentication
