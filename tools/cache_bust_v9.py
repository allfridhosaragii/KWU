"""Ensures browsers do not reuse the previous 3D renderer after deployment."""
from pathlib import Path

app = Path("site/assets/app.js")
source = app.read_text(encoding="utf-8")
old = "from './viewer.js'"
if old not in source:
    raise RuntimeError("Viewer import no longer matches cache buster")
app.write_text(source.replace(old, "from './viewer.js?v=v9-1'", 1), encoding="utf-8")
print("Bundled app imports versioned renderer v9-1")
