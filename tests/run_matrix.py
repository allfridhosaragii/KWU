"""Run isolated offline Chromium tests per viewport to avoid GPU/browser state sharing."""
import json,subprocess,sys
from pathlib import Path
root=Path(__file__).parent.parent
cases=[];failed=[]
for w in [320,390,768,1440]:
 p=subprocess.run([sys.executable,str(root/'tests/e2e_inline.py'),str(w)],capture_output=True,text=True,timeout=50)
 try:
  data=json.loads(p.stdout)
 except Exception:
  data={'raw':p.stdout[-1000:],'stderr':p.stderr[-1000:]}
 cases.append({'width':w,'exit_code':p.returncode,'result':data})
 if p.returncode!=0:failed.append(w)
 print(f'{w}px: {"PASS" if p.returncode==0 else "FAIL"} | tests={data.get("route_breakpoint_tests")}, workflows={data.get("workflow_passes")}',flush=True)
report={'viewports':cases,'total_route_checks':sum(c['result'].get('route_breakpoint_tests',0) for c in cases),'total_workflows':sum(c['result'].get('workflow_passes',0) for c in cases),'failed_viewports':failed}
(root/'qa-viewport-matrix.json').write_text(json.dumps(report,indent=2,ensure_ascii=False))
if failed:raise SystemExit(1)
