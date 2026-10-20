"""Pre-render genuinely rotatable turntable frames from the same GLB models
for browsers without WebGL. Frame strips are responsive and support touch gestures.
These are offline camera views, not arbitrary realtime GPU 3D.
"""
from __future__ import annotations
import os, math, io, json, time
from pathlib import Path
from PIL import Image
import numpy as np
import vtk
from vtk.util.numpy_support import vtk_to_numpy

ROOT=Path(__file__).resolve().parent.parent
MODELS=ROOT/'site/models'
OUTPUT=ROOT/'site/assets/turntables'
OUTPUT.mkdir(parents=True,exist_ok=True)
ANATOMY={'bracelet','ring','necklace'}
ALL=['bracelet','ring','necklace','bag-charm','phone','tablet','macbook','bottle',
 'iphone-17','iphone-air','iphone-17-pro','iphone-17-pro-max','iphone-17e',
 'ipad-pro-11','ipad-pro-13','ipad-air-11','ipad-air-13',
 'macbook-air-13','macbook-air-15','macbook-pro-14','macbook-pro-16']


SKIN_PALETTE={
 'sawo-matang':(184,130,95),
 'kuning-langsat':(213,162,126),
 'light-beige':(226,188,159),
 'medium-tan':(159,109,79),
 'deep-brown':(111,72,55),
}

def skin_variant(base:Image.Image,tone:str)->Image.Image:
    """Preserve 3D illumination while altering only chroma ranges resembling skin.
    The rendered gold/steel jewellery and ivory background are left largely untouched.
    GPU render uses true PBR tint; these are approximations for offline fallback.
    """
    c=np.asarray(base.convert('RGB'),dtype=np.float32)
    r,g,b=c[:,:,0],c[:,:,1],c[:,:,2]
    gr=b/np.maximum(g,1)
    rg=r/np.maximum(g,1)
    mask=(np.clip((gr-.63)/.12,0,1)*np.clip((.99-gr)/.08,0,1)
         *np.clip((rg-1.08)/.15,0,1)*np.clip((215-r)/42,0,1)
         *np.clip((r-35)/25,0,1))
    desired=np.asarray(SKIN_PALETTE[tone],dtype=np.float32)
    base_color=np.asarray(SKIN_PALETTE['sawo-matang'],dtype=np.float32)
    multiplier=np.clip((desired/base_color)**.87,.52,1.5)
    transformed=np.clip(c*multiplier[np.newaxis,np.newaxis,:],0,255)
    out=c*(1-mask[:,:,np.newaxis])+transformed*mask[:,:,np.newaxis]
    return Image.fromarray(out.astype(np.uint8),'RGB')

def render(name:str)->dict:
    src=MODELS/f'{name}.glb'
    high=name in ANATOMY
    ncol=24 if high else 16
    nrow=2
    size=400 if high else 320
    elevations=(-10,12)
    ren=vtk.vtkRenderer()
    window=vtk.vtkRenderWindow();window.SetOffScreenRendering(True)
    window.SetSize(size,size); window.SetMultiSamples(0)
    window.AddRenderer(ren)
    importer=vtk.vtkGLTFImporter();importer.SetFileName(str(src));importer.SetRenderWindow(window)
    importer.Update()
    ren.SetBackground(0.980,0.972,0.957)
    ren.AutomaticLightCreationOff()
    lights=[]
    for strength in (1.4,.85,.42):
      l=vtk.vtkLight();l.SetLightTypeToSceneLight();l.SetIntensity(strength);ren.AddLight(l);lights.append(l)
    # Keep the same framing for all camera angles: no jumps during rotation.
    ren.ResetCamera()
    camera=ren.GetActiveCamera()
    focal=camera.GetFocalPoint()
    bounds=ren.ComputeVisiblePropBounds()
    dx,dy,dz=(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4])
    largest=max(dx,dy,dz,.001)
    camera.SetParallelProjection(True)
    camera.SetParallelScale(largest*.67)
    camera.SetFocalPoint(*focal);camera.SetViewUp(0,1,0)
    camera.OrthogonalizeViewUp()
    radius=largest*3.0
    snap=vtk.vtkWindowToImageFilter();snap.SetInput(window)
    snap.ReadFrontBufferOff();snap.SetInputBufferTypeToRGB()
    frames=[]
    for elevation in elevations:
      elev=math.radians(elevation)
      for i in range(ncol):
        angle=2*math.pi*i/ncol
        camera.SetPosition(focal[0]+radius*math.sin(angle)*math.cos(elev), focal[1]+radius*math.sin(elev), focal[2]+radius*math.cos(angle)*math.cos(elev))
        camera.SetFocalPoint(*focal);camera.SetViewUp(0,1,0)
        # Headlights follow the camera so the model stays visible even from the back.
        forward=(math.sin(angle)*math.cos(elev), math.sin(elev), math.cos(angle)*math.cos(elev))
        right=(math.cos(angle),0,-math.sin(angle))
        for light,(rgt,up,fwd) in zip(lights,[(.50,.58,.72),(-.66,.34,.60),(0,.14,-.40)]):
          light.SetPosition(focal[0]+radius*(fwd*forward[0]+rgt*right[0]),focal[1]+radius*(fwd*forward[1]+up),focal[2]+radius*(fwd*forward[2]+rgt*right[2]))
          light.SetFocalPoint(*focal)
        ren.ResetCameraClippingRange()
        window.Render();snap.Modified();snap.Update()
        scalars=snap.GetOutput().GetPointData().GetScalars()
        if scalars is None:raise RuntimeError(f'Empty raster from {name} frame {i}')
        arr=vtk_to_numpy(scalars).reshape(size,size,3)[::-1].copy()
        frames.append(Image.fromarray(arr,'RGB'))
    # Avoid max texture width; use 4 columns x 6/12/18 rows.
    sheetCols=4;sheetRows=math.ceil(len(frames)/sheetCols)
    atlas=Image.new('RGB',(sheetCols*size,sheetRows*size), '#FAF8F4')
    for i,frame in enumerate(frames):atlas.paste(frame,((i%sheetCols)*size,(i//sheetCols)*size))
    dest=OUTPUT/f'{name}.webp'
    atlas.save(dest,'WEBP',quality=81,method=5)
    variants=[]
    if high:
      for tone in SKIN_PALETTE:
        toneImage=skin_variant(atlas,tone) if tone!='sawo-matang' else atlas
        out=OUTPUT/f'{name}--{tone}.webp'
        toneImage.save(out,'WEBP',quality=81,method=5)
        variants.append(tone)
    window.Finalize()
    return {'name':name,'columns':sheetCols,'rows':sheetRows,'frames':len(frames),'azimuthFrames':ncol,'elevations':list(elevations),'tileSize':size,'bytes':dest.stat().st_size,'skinVariants':variants}


def main():
    selected=os.getenv('KWU_TURNTABLE_MODELS','')
    names=[x for x in ALL if (not selected or x in selected.split(',')) and (MODELS/f'{x}.glb').exists()]
    start=time.monotonic()
    data={}
    for name in names:
      t=time.monotonic()
      item=render(name);data[name]=item
      print(name,'frames',item['frames'],'bytes',item['bytes'],'seconds',round(time.monotonic()-t,2),flush=True)
    (OUTPUT/'manifest.json').write_text(json.dumps({'version':10,'models':data},indent=2),encoding='utf-8')
    print('rendered',len(data),'in',round(time.monotonic()-start,1),'sec',flush=True)
if __name__=='__main__':main()
