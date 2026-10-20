"""Offline software/VTK render of complete GLB, including embedded images.
For product cards; interactive viewer separately handles WebGL2.
"""
from pathlib import Path
import vtk,io
from PIL import Image
BASE=Path(__file__).resolve().parent.parent
OUT=BASE/'site/assets/previews'
NAMES=['bracelet','ring','necklace','bag-charm','bottle','phone','tablet','macbook',
 'iphone-17','iphone-air','iphone-17-pro','iphone-17-pro-max','iphone-17e',
 'ipad-pro-11','ipad-pro-13','ipad-air-11','ipad-air-13',
 'macbook-air-13','macbook-air-15','macbook-pro-14','macbook-pro-16']
import os
only=os.environ.get("KWU_PREVIEW_MODELS")
if only:NAMES=[n for n in NAMES if n in set(only.split(","))]
for name in NAMES:
 src=BASE/'site/models'/f'{name}.glb'
 if not src.exists():continue
 imp=vtk.vtkGLTFImporter();imp.SetFileName(str(src))
 ren=vtk.vtkRenderer();win=vtk.vtkRenderWindow();win.SetSize(700,700);win.SetOffScreenRendering(True)
 win.AddRenderer(ren);imp.SetRenderWindow(win);imp.Update()
 ren.SetBackground(.974,.964,.946)
 ren.ResetCamera();cam=ren.GetActiveCamera()
 cam.Azimuth(5 if name=='bag-charm' else 10)
 cam.Elevation(2 if name in ('bag-charm','bottle') else 1)
 ren.ResetCameraClippingRange();win.Render()
 snap=vtk.vtkWindowToImageFilter();snap.SetInput(win);snap.Update()
 writer=vtk.vtkPNGWriter();writer.WriteToMemoryOn();writer.SetInputConnection(snap.GetOutputPort());writer.Write()
 from vtk.util.numpy_support import vtk_to_numpy
 raw=bytes(memoryview(writer.GetResult()))
 im=Image.open(io.BytesIO(raw)).convert('RGB')
 im.save(OUT/f'{name}.webp','WEBP',quality=86,method=5)
 print(name,(OUT/f'{name}.webp').stat().st_size)
 win.Finalize()
