"""QA for retina 360° fallback atlases after generator completes on GitHub CI."""
from __future__ import annotations
from pathlib import Path
import json
from PIL import Image
BASE=Path(__file__).resolve().parent.parent/'site/assets/turntables'
manifest=json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
assert manifest['version']==11,manifest['version']
assert len(manifest['models'])>=21,('missing legacy device model',len(manifest['models']))
valid_tones=('sawo-matang','kuning-langsat','light-beige','medium-tan','deep-brown')
checked=[]
for category in ('bracelet','ring','necklace'):
    m=manifest['models'][category]
    assert m['tileSize']==768 and m['splitElevations'] and m['atlasFormat']=='png'
    assert m['columns']==4 and m['rows']==6 and m['azimuthFrames']==24
    assert m['skinVariants']==list(valid_tones)
    for row in (0,1):
        for suffix in ['']+[f'--{tone}' for tone in valid_tones]:
            path=BASE/f'{category}{suffix}--e{row}.png'
            assert path.exists() and path.stat().st_size>100_000,path
            with Image.open(path) as image:
                image.verify()
            with Image.open(path) as image:
                assert image.size==(3072,4608),[path,image.size]
            checked.append(str(path.relative_to(BASE)))
# The other 18 device model variants must retain a real V10 atlas.
for name,meta in manifest['models'].items():
    if name in ('bracelet','ring','necklace'):continue
    if not meta.get('splitElevations'):
        assert (BASE/f'{name}.webp').exists(),name
print('V11 retina atlas integrity: PASS',len(checked),'HD images; legacy models preserved')
