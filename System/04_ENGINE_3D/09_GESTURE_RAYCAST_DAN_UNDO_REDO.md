# Gesture, Hit-Test, State Mesin, Undo/Redo

> Proyek: KWU Digital Atelier | Baseline: 20 Oktober 2026 | Status: spesifikasi teknis, bukan implementasi

## State machine input
`IDLE`, `ORBITING`, `PINCH_ZOOM`, `SELECTED`, `DRAGGING_ELEMENT`, `TRANSFORMING`, `ANIMATING_PRESET`, `LOADING`, `ERROR`. Hanya satu mode input aktif per pointer interaction. `pointercancel` wajib melepas drag state.

## Aturan pointer
- Tap satu kali di mesh interaktif → selected; tap background → deselect.
- Drag background → orbit camera. Drag element terpilih → reposition dalam constraint.
- Pinch 2 jari → zoom kamera, nonaktifkan element drag. Kontrol wajib menghormati page scroll bila event terjadi di luar canvas.
- Rotate selected element via handle atau tombol sudut, tidak berarti rotate keseluruhan rig.
- Gesture capture di canvas hanya selama editor aktif; jangan `touch-action:none` global pada seluruh halaman.

## Raycast
Gunakan interseksi hanya pada collision proxy/mesh yang punya `interactive=true` dan layer relevan. Hindari raycast ribuan triangle setiap pointermove jika bisa memakai simplified proxy. Transform hit world ke local point/UV lalu clamp/nearest valid slot.

## Undo/redo model
Record semantic commands (`ADD_STICKER`, `MOVE_ELEMENT`, `CHANGE_CASE`, `CHANGE_RING_FINGER`). History dibatasi jumlah dan memori, simpan sebelum/after JSON minimal, group continuous drag sebagai satu history entry on pointerup. `UNDO` membuat valid state baru dan mengubah preview; autosave sesuai debounce.

## Aksesibilitas
Semua drag harus punya opsi dengan tombol arah, slider, pilih slot atau input posisi yang setara; label screen reader untuk elemen; focus visible, keyboard arrow di desktop; quality/performance controls tidak mengganggu checkout.

## Test
Multi-touch saat ornament selected, pinch dengan sheet terbuka, rotate orientation, gesture interupsi karena panggilan/tombol back, 100 undo/redo, layout 320 px, reduce-motion.
