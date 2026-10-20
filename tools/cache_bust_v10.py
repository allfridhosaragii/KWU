"""Prevent stale app/viewer/turntable JS after GPU-fallback deployment."""
from pathlib import Path
import re
app=Path('site/assets/app.js')
viewer=Path('site/assets/viewer.js')
html=Path('site/index.html')
s=app.read_text(encoding='utf-8')
if "from './viewer.js'" not in s:raise RuntimeError('Unexpected app viewer import')
app.write_text(s.replace("from './viewer.js'","from './viewer.js?v=v10-1'",1),encoding='utf-8')
s=viewer.read_text(encoding='utf-8')
if "from './turntable.js'" not in s:raise RuntimeError('Missing 360 fallback import')
viewer.write_text(s.replace("from './turntable.js'","from './turntable.js?v=v10-1'",1),encoding='utf-8')
s=html.read_text(encoding='utf-8')
s=re.sub(r'\?v=v\d+(?:-\d+)?', '?v=v10-1',s)
html.write_text(s,encoding='utf-8')
print('Web asset cache keys now V10-1')
