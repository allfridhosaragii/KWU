# Komponen Dasar: Tombol, Input, Form, dan Feedback

## Buttons

| Variant | Tampilan | Penggunaan |
|---|---|---|
| Primary | Terracotta solid, teks putih | Satu tindakan utama per konteks |
| Secondary | Border kuat, teks espresso/terracotta | Tindakan pendamping |
| Ghost | Tanpa background, label jelas | Toolbar/aksi tersier |
| Destructive | Error dark dengan konfirmasi | Hapus desain/akun bila ada |
| Icon button | Ikon 20–22 px pada hitbox ideal 44 px | Kembali, wishlist, zoom |

States wajib: default, hover (pointer), pressed, focus-visible, loading, disabled, success bila relevan. Disabled harus memiliki alasan yang ditampilkan di dekat kontrol bila pengguna perlu memperbaiki input.

## Input dan form

- Gunakan label di atas field; placeholder hanya contoh, **bukan** pengganti label.
- Input punya border kontrol yang terlihat, field hint jika perlu, error inline di bawahnya, dan ring fokus yang jelas.
- `inputmode` harus sesuai: numerik untuk telepon/kuantitas, email untuk email.
- Saat submit error, fokus dipindah ke rangkuman/error pertama dan field bermasalah diberi pesan spesifik.
- Password punya toggle visibilitas dengan nama aksesibel.
- Jangan kosongkan seluruh form setelah error jaringan.

## Chips, tabs, segmented controls

- Chip kategori boleh scroll horizontal tetapi berikan petunjuk visual bahwa ada opsi berikutnya.
- Tab status pesanan harus mempertahankan posisi serta jumlah item terfilter.
- Segmented control untuk mode preset/custom bebas harus menunjukkan mode aktif melalui teks, bukan warna saja.
- Swatch warna wajib memiliki nama terlihat saat dipilih dan label screen reader.

## Toasts dan dialog

- Toast sukses 2–4 detik, tidak membawa satu-satunya informasi penting.
- Dialog konfirmasi hanya untuk perubahan berdampak: hapus desain, buang perubahan, batalkan pesanan jika diizinkan.
- Loading penting harus mempunyai teks: “Menyimpan desain…”, “Memverifikasi pembayaran…”.
- Jangan memunculkan toast untuk setiap gerakan drag ornamen karena mengganggu.

## Praktik microinteractions

- Tekan tombol: perubahan warna/scale sangat kecil tanpa layout shift.
- Input fokus: perubahan border + ring, tanpa animasi yang menggoyangkan form.
- Tambah wishlist: ikon berubah dan `aria-pressed` diperbarui.
- Tambah keranjang: badge jumlah diperbarui, lalu tampil feedback “Ditambahkan ke keranjang”.

## Checklist komponen

- [ ] Semua variant di Figma dan React konsisten.
- [ ] Menggunakan token warna dan spacing, bukan hardcode acak.
- [ ] Fokus keyboard terlihat.
- [ ] Loading tidak mengubah lebar tombol secara signifikan.
- [ ] Teks tombol tetap jelas pada layar 320 px.
- [ ] Komponen punya state error dan empty bila relevan.
