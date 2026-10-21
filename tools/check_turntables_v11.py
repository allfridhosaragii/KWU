"""QA for retina 360° fallback atlases after generator completes on GitHub CI."""
from __future__ import annotations
from pathlib import Path
import json
from PIL import Image
BASE=Path(__file__).resolve().parent.parent/'site/assets/turntables'
manifest=json.loads((BASE/'manifest.json').read_text(encoding='utf-8'))
assert manifest['version']==16,manifest['version']
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
# All remaining device models must now use true 640px tiles, not old 320px sprites.
for name,meta in manifest['models'].items():
    if name in ('bracelet','ring','necklace'):continue
    assert meta['tileSize']>=640 and meta['splitElevations'] and meta['atlasFormat']=='png',(name,meta)
    for row in (0,1):
        path=BASE/f'{name}--e{row}.png'
        assert path.exists() and path.stat().st_size>5000,path
        with Image.open(path) as image:
            assert image.size==(4*meta['tileSize'],4*meta['tileSize']),[name,image.size]
print('V14 turntable atlas integrity: PASS',len(checked),'HD jewelry variants plus',len(manifest['models'])-3,'640px device models')


# V12 progressive retina still images: all skin tones, two elevations and all
# 24 azimuths must be present and decodable for the three jewelry scenes.
retina_count=0
for name in ('bracelet','ring','necklace'):
    for tone in valid_tones:
        for row in (0,1):
            for angle in range(24):
                path=BASE/'hires'/name/tone/f'e{row}'/f'a{angle:02d}.webp'
                assert path.exists() and path.stat().st_size>3000,path
                with Image.open(path) as im:
                    assert im.size==(1536,1536) and im.format=='WEBP',path
                    im.verify()
                retina_count+=1
print('V12 retina 360 still images: PASS',retina_count,'frames')
