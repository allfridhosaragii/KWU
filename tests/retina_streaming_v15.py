"""Static guards for the V15 on-demand 1536p turntable streaming path."""
from pathlib import Path

src = Path('src/turntable.ts').read_text(encoding='utf-8')
assert 'class RetinaStill' in src
assert "this.fetchFrame(url,true)" in src, 'HD frame should start downloading immediately'
assert 'this.prefetch(model,tone,row,a,direction)' in src
assert "private readonly maxCache=7" in src
assert "screenshot(){const hd=this.retina.screenshot()" in src
assert '75ms idle delay' in src  # documented as removed
assert "this.timer=window.setTimeout" not in src, 'Old stop-only decoder still exists'
assert 'HD 1536p dimuat otomatis' in src
assert "this.image.style.opacity='0'" in src
print('V15 HD path: source guards passed')
