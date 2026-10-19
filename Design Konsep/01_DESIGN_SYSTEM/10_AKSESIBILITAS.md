# Aksesibilitas dan Inklusivitas

Target: desain mengikuti WCAG 2.2 AA sebagai pedoman evaluasi. Ketaatan akhir membutuhkan pemeriksaan implementasi dan pengujian pengguna, bukan hanya file Figma.

## Kontras

- Teks normal minimal 4,5:1; teks besar minimal 3:1.
- Komponen nonteks penting dan focus indicator diuji terhadap background final.
- Copper `#C78962` **tidak** digunakan dengan teks putih kecil (rasio 2,92:1).
- State aktif/error/sukses harus memakai label/ikon tambahan, tidak cuma warna.

## Target sentuh

- Pilih ukuran target ideal sekitar 44 × 44 CSS px untuk icon dan kontrol kecil.
- WCAG 2.2 AA menetapkan minimum 24 × 24 CSS px dengan pengecualian; 44 px adalah target internal desain yang lebih nyaman, bukan pernyataan minimum AA.
- Kontrol dekat pinggir layar mendapat jarak dari safe area.

## Gestur 3D

- Semua tindakan penting yang memakai drag memiliki alternatif tombol: geser kiri/kanan, rotasi ±, ubah skala ±, pilih anchor.
- Mengetuk objek yang dipilih menampilkan nama, posisi, dan aksi yang dapat diakses melalui keyboard jika tersedia.
- Tersedia tombol Reset View dan Kembali.
- Hindari gerak otomatis tidak terkendali; hormati reduced motion.
- Pastikan pilihan mode kamera/objek dapat dikenali lewat label, bukan hanya warna.

## Struktur dan screen reader

- Satu H1 per halaman utama sesuai konteks; landmark `main`, `nav`, `header` masuk akal.
- Dialog menahan fokus, punya judul, Escape/Close.
- Input dengan label nyata, error terhubung secara semantik.
- Thumbnail produk punya alt ringkas: nama, material, sudut relevan; gambar dekoratif dapat alt kosong.
- Canvas 3D diberi alternatif deskripsi tekstual ringkas tentang desain terpilih, karena geometri visual tidak otomatis dapat dibaca oleh screen reader.
- Perubahan hasil simpan dan harga yang penting diumumkan dengan status yang tidak spam.

## Pembesaran dan preferensi pengguna

- Zoom browser 200% tidak boleh memotong isi atau tombol utama.
- Text spacing dan dynamic font tidak membuat harga/label hilang.
- Hindari fixed-height pada konten dinamis.
- Kurangi motion saat pengguna memilih preferensi tersebut.

## Uji minimum

- Keyboard: tab order, fokus, modal, form, undo/redo, control alternatif 3D.
- Screen reader: iOS VoiceOver dan Android TalkBack pada alur kunci.
- Pengguna hanya dengan satu jari dapat memanipulasi elemen melalui alternatif tanpa drag.
- Kontras visual dan label tidak bergantung pada perubahan warna saja.

Sumber: https://www.w3.org/TR/WCAG22/ dan https://www.w3.org/WAI/WCAG22/Understanding/dragging-movements
