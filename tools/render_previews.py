from pathlib import Path
import trimesh,numpy as np,vtk
from vtk.util.numpy_support import numpy_to_vtk,numpy_to_vtkIdTypeArray
root=Path(__file__).parent.parent
out=root/'site/assets/previews';out.mkdir(exist_ok=True,parents=True)
for name in ['bracelet','ring','necklace','bag-charm','phone','tablet','macbook','bottle']:
 scene=trimesh.load(root/'site/models'/f'{name}.glb',force='scene')
 ren=vtk.vtkRenderer();ren.GradientBackgroundOn();ren.SetBackground(.92,.87,.82);ren.SetBackground2(.99,.975,.95)
 win=vtk.vtkRenderWindow();win.SetOffScreenRendering(1);win.SetSize(560,700);win.SetMultiSamples(8);win.AddRenderer(ren)
 for geom in scene.dump():
  if not isinstance(geom,trimesh.Trimesh):continue
  pd=vtk.vtkPolyData();pts=vtk.vtkPoints();pts.SetData(numpy_to_vtk(np.asarray(geom.vertices,dtype=np.float32),deep=True));pd.SetPoints(pts)
  faces=np.asarray(geom.faces,dtype=np.int64);ids=np.column_stack([np.full(len(faces),3),faces]).ravel();cells=vtk.vtkCellArray();cells.SetCells(len(faces),numpy_to_vtkIdTypeArray(ids,deep=True));pd.SetPolys(cells)
  colors=np.asarray(geom.visual.vertex_colors)
  if colors.ndim==2 and len(colors)==len(geom.vertices):
   arr=numpy_to_vtk(np.asarray(colors,dtype=np.uint8),deep=True,array_type=vtk.VTK_UNSIGNED_CHAR);arr.SetNumberOfComponents(4);arr.SetName('RGBA');pd.GetPointData().SetScalars(arr)
  norms=vtk.vtkPolyDataNormals();norms.SetInputData(pd);norms.ComputePointNormalsOn();norms.SplittingOff();norms.ConsistencyOn();norms.Update()
  mapper=vtk.vtkPolyDataMapper();mapper.SetInputConnection(norms.GetOutputPort());mapper.ScalarVisibilityOff()
  actor=vtk.vtkActor();actor.SetMapper(mapper);prop=actor.GetProperty();prop.SetInterpolationToPhong();prop.SetAmbient(.4);prop.SetDiffuse(.7);prop.SetSpecular(.3);prop.SetSpecularPower(34);prop.SetColor(*((np.asarray(geom.visual.vertex_colors)[0][:3] / 255.).tolist()));ren.AddActor(actor)
 l=vtk.vtkLight();l.SetPosition(-4,8,10);l.SetFocalPoint(0,0,0);l.SetIntensity(1.1);ren.AddLight(l)
 l2=vtk.vtkLight();l2.SetPosition(6,2,-5);l2.SetFocalPoint(0,0,0);l2.SetIntensity(.45);ren.AddLight(l2)
 ren.ResetCamera();cam=ren.GetActiveCamera();cam.SetPosition(3,1.4,8);cam.SetFocalPoint(0,0,0);cam.SetViewUp(0,1,0);ren.ResetCameraClippingRange();cam.Zoom(1.2 if name not in ['phone','tablet','macbook'] else 1.30)
 win.Render();f=vtk.vtkWindowToImageFilter();f.SetInput(win);f.SetInputBufferTypeToRGB();f.ReadFrontBufferOff();f.Update();write=vtk.vtkPNGWriter();write.SetFileName(str(out/f'{name}.png'));write.SetInputConnection(f.GetOutputPort());write.Write()
 print(name,(out/f'{name}.png').stat().st_size)
 win.Finalize()
