"""Prevent old V9-V14 modules from being served after V11 atlas deployment."""
from pathlib import Path
import re
version='v17-1'
app=Path('site/assets/app.js')
viewer=Path('site/assets/viewer.js')
html=Path('site/index.html')
s=app.read_text(encoding='utf-8')
assert "from './viewer.js'" in s,'Compiled app import changed'
app.write_text(s.replace("from './viewer.js'",f"from './viewer.js?v={version}'",1),encoding='utf-8')
s=viewer.read_text(encoding='utf-8')
assert "from './turntable.js'" in s,'Compiled viewer import changed'
viewer.write_text(s.replace("from './turntable.js'",f"from './turntable.js?v={version}'",1),encoding='utf-8')
s=html.read_text(encoding='utf-8')
s=re.sub(r'\?v=v\d+(?:-\d+)?',f'?v={version}',s)
assert f'assets/app.js?v={version}' in s
html.write_text(s,encoding='utf-8')
print('KWU frontend cache keys updated:',version)
