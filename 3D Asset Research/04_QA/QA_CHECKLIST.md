# 3D Asset QA Checklist

## Visual accuracy
- silhouette cocok dengan referensi
- proporsi utama benar
- warna sesuai referensi
- material believable
- tidak ada shading artifacts besar

## Functional checks
- model bisa dimuat
- pivot masuk akal
- scale konsisten
- sticker/charm placement berfungsi
- rig tidak patah saat pose dasar

## Web checks
- load di mobile portrait
- load di mobile landscape
- load di tablet
- load di desktop
- pinch zoom dan rotate bekerja
- tidak ada overlap UI fatal

## Performance checks
- frame rate acceptable
- texture memory tidak berlebihan
- ukuran GLB sesuai target
- no major stutter on interaction

## Commerce checks
- preview yang dilihat user mewakili barang custom
- saved design reload konsisten
- thumbnail hasil desain muncul benar
