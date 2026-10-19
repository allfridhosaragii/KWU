# Hand Mannequin Research

## Goal
Membuat hand mannequin yang sangat dekat dengan tangan manusia asli untuk gelang dan cincin.

## Reality check
Tuntutan “1:1 seperti tangan asli” untuk aset web membutuhkan:
- anatomi proporsional,
- mesh berkualitas tinggi,
- texturing kulit meyakinkan,
- rigging yang baik,
- dan optimasi web yang hati-hati.

Tanpa 3D scan atau multi-angle hand references, hasil terbaik yang realistis adalah **hyper-real inspired mannequin**, bukan salinan biologis absolut.

## Spesifikasi visual yang direkomendasikan
- Gender style: unisex elegant
- Shape: ramping natural, cocok untuk jewelry presentation
- Nail: natural, pendek, rapi
- Skin tone: medium-light neutral as base template
- Wrist shape: natural dengan tendon lembut, tidak terlalu menonjol

## Modeling requirements
### High-poly
- knuckle form
- finger segment volume
- nail beds
- subtle creases
- wrist transitions

### Low-poly web mesh
- retopo bersih
- normal baked dari high-poly
- minimal distortion di joint bending

## Rigging requirements
- palm root
- wrist
- metacarpal control ringan
- setiap jari minimal 3 joint utama
- pose preset untuk gelang dan cincin

## Texturing requirements
- albedo natural
- roughness variation halus
- micro normal/skin pores sangat halus
- nail roughness sedikit berbeda

## Web requirements
- satu hero hand untuk bracelet
- satu variant pose untuk ring overview
- 1 material skin master dengan opsi tone jika dibutuhkan nanti
