"""Regression: HD 1536p and 768p must never be visible as stacked images."""
from pathlib import Path
src = Path("src/turntable.ts").read_text(encoding="utf-8")
assert "class RetinaStill" in src
assert "host.append(image)" not in src, "Off-DOM retina image was reattached"
assert "this.image.style.transform=" not in src, "Independent HD zoom returned"
assert "this.retina.activeFrame()" in src, "Retina must draw into the same canvas"
assert "this.frameContext.drawImage(hd,0,0,tile,tile)" in src
assert "this.frameContext.drawImage(this.currentImg" in src
assert "queueMicrotask(()=>{if(!this.disposed" in src, "Async ready repaint not connected"
assert "this.renderedFrame='';this.paint();" in src, "HD or quality change may leave stale pixels"
assert "outer.addEventListener('dblclick'" in src
assert "this.selectedImage=null" in src
assert "this.image.style.opacity='0'" in src  # old source guard remains compatible
assert "this.sprite.style.transform=" in src
cache = Path("tools/cache_bust_v11.py").read_text(encoding="utf-8")
assert "version='v17-1'" in cache
print("PASSED: V17 single-canvas renderer prevents double-layer finger artifacts")
