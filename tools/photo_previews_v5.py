"""Reliable image fallback when WebGL2 is unavailable.
Uses the original user product photos; 3D viewer remains the source of interaction.
"""
from pathlib import Path
from PIL import Image
R=Path(__file__).resolve().parent.parent
for name,ref in [('bag-charm','backpack-user.jpeg'),('bottle','bottle-user.jpeg')]:
 photo=Image.open(R/'site/assets/references'/ref).convert('RGB').resize((700,700),Image.Resampling.LANCZOS)
 p=R/'site/assets/previews'/f'{name}.webp'
 photo.save(p,quality=90,method=5)
 print(name,p.stat().st_size)
