"""Generate high-resolution, mobile-safe 360-degree product atlases.

V11 fixes V10's 400px render tiles, low-quality WebP, and giant full-height
atlases by splitting each elevation into a separate atlas. The active elevation
is downloaded on demand rather than decoding all 48 frames on a phone.
These are camera renders of the real GLB, not photographs or true WebGL.
"""
from __future__ import annotations
import os, math, json, time, sys, subprocess
from pathlib import Path
import numpy as np
from PIL import Image, ImageFilter
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
    """Memory-bounded skin-tone conversion in 128-row strips (<100 MB peak).
    Preserve 3D illumination, leave gold/steel jewellery mostly unchanged.
    """
    src=np.asarray(base.convert('RGB'),dtype=np.uint8)
    out=np.empty_like(src)
    desired=np.asarray(SKIN_PALETTE[tone],dtype=np.float32)
    base_color=np.asarray(SKIN_PALETTE['sawo-matang'],dtype=np.float32)
    multiplier=np.clip((desired/base_color)**.87,.52,1.5)
    for y in range(0,len(src),128):
        c=src[y:y+128].astype(np.float32)
        r,g,b=c[:,:,0],c[:,:,1],c[:,:,2]
        gr=b/np.maximum(g,1);rg=r/np.maximum(g,1)
        mask=(np.clip((gr-.63)/.12,0,1)*np.clip((.99-gr)/.08,0,1)
             *np.clip((rg-1.08)/.15,0,1)*np.clip((215-r)/42,0,1)
             *np.clip((r-35)/25,0,1))
        result=c+np.clip(c*multiplier[None,None,:]-c,-255,255)*mask[:,:,None]
        out[y:y+128]=np.clip(result,0,255).astype(np.uint8)
    return Image.fromarray(out,'RGB')


def smooth_imported_geometry(renderer):
    """Fix angular facets at polygon/UV seams of anatomical GLTF meshes.
    UV and PBR textures remain owned by the original vtkPolyData mapper.
    """
    n=0
    for actor in renderer.GetActors():
        mapper=actor.GetMapper()
        if not mapper or not mapper.GetInput():continue
        normals=vtk.vtkPolyDataNormals()
        normals.SetInputData(mapper.GetInput())
        normals.ComputePointNormalsOn()
        normals.ComputeCellNormalsOff()
        normals.SplittingOff()
        normals.ConsistencyOff()
        normals.AutoOrientNormalsOff()
        normals.Update()
        mapper.SetInputConnection(normals.GetOutputPort())
        n+=1
    return n


def render(name:str)->dict:
    src=MODELS/f'{name}.glb'
    if not src.exists():raise FileNotFoundError(src)
    anatomy=name in ANATOMY
    ncol=24 if anatomy else 16
    elevations=(-10,12)
    size=768 if anatomy else 640
    override=int(os.getenv('KWU_TURNTABLE_TILE','0'))
    if override:size=override
    if size>1024:raise ValueError('Tiles larger than 1024 risk excessive mobile image memory')
    max_frames=int(os.getenv('KWU_TURNTABLE_TEST_MAX_FRAMES','0'))
    if max_frames and max_frames<ncol:raise ValueError('Test cap must include whole elevation row')

    ren=vtk.vtkRenderer()
    window=vtk.vtkRenderWindow()
    window.SetOffScreenRendering(True)
    window.SetSize(size,size)
    window.SetMultiSamples(4)
    window.AddRenderer(ren)
    importer=vtk.vtkGLTFImporter()
    importer.SetFileName(str(src))
    importer.SetRenderWindow(window)
    importer.Update()
    smoothed=smooth_imported_geometry(ren)
    ren.SetBackground(.980,.972,.957)
    ren.AutomaticLightCreationOff()
    try:pass  # FXAA disabled for consistent offscreen rendering
    except AttributeError:pass
    lights=[]
    for strength in (1.4,.85,.42):
        l=vtk.vtkLight();l.SetLightTypeToSceneLight();l.SetIntensity(strength)
        ren.AddLight(l);lights.append(l)
    ren.ResetCamera()
    camera=ren.GetActiveCamera()
    focal=camera.GetFocalPoint()
    bounds=ren.ComputeVisiblePropBounds()
    dx,dy,dz=(bounds[1]-bounds[0],bounds[3]-bounds[2],bounds[5]-bounds[4])
    largest=max(dx,dy,dz,.001)
    camera.SetParallelProjection(True)
    camera.SetParallelScale(largest*.67)
    camera.SetFocalPoint(*focal)
    camera.SetViewUp(0,1,0)
    camera.OrthogonalizeViewUp()
    radius=largest*3
    snap=vtk.vtkWindowToImageFilter()
    snap.SetInput(window)
    snap.ReadFrontBufferOff()
    snap.SetInputBufferTypeToRGB()
    sheetCols=4
    rows=math.ceil(ncol/sheetCols)
    atlases=[]
    wanted=os.getenv('KWU_TURNTABLE_ONLY_ELEVATION')
    idxs=[int(wanted)] if wanted is not None else range(len(elevations))
    for elev_idx in idxs:
        elevation=elevations[elev_idx]
        elev=math.radians(elevation)
        atlas=Image.new('RGB',(sheetCols*size,rows*size),'#FAF8F4')
        for i in range(ncol):
            angle=2*math.pi*i/ncol
            fwd=(math.sin(angle)*math.cos(elev),math.sin(elev),math.cos(angle)*math.cos(elev))
            camera.SetPosition(focal[0]+radius*fwd[0],focal[1]+radius*fwd[1],focal[2]+radius*fwd[2])
            camera.SetFocalPoint(*focal)
            camera.SetViewUp(0,1,0)
            right=(math.cos(angle),0,-math.sin(angle))
            for l,(rgt,up,forward) in zip(lights,[(.50,.58,.72),(-.66,.34,.60),(0,.14,-.40)]):
                l.SetPosition(focal[0]+radius*(forward*fwd[0]+rgt*right[0]),
                              focal[1]+radius*(forward*fwd[1]+up),
                              focal[2]+radius*(forward*fwd[2]+rgt*right[2]))
                l.SetFocalPoint(*focal)
            ren.ResetCameraClippingRange()
            window.Render()
            snap.Modified()
            snap.Update()
            scalars=snap.GetOutput().GetPointData().GetScalars()
            if scalars is None:raise RuntimeError(f'Empty raster from {name} angle {i}')
            arr=vtk_to_numpy(scalars).reshape(size,size,3)[::-1].copy()
            frame=Image.fromarray(arr,'RGB')
            atlas.paste(frame,((i%sheetCols)*size,(i//sheetCols)*size))
            # The quick 768px sprite keeps gestures smooth. When the viewer
            # stops moving, the client requests just ONE 1536px WebP angle.
            # Avoid a multi-hundred-megapixel full 1536px atlas on Safari.
            if anatomy:
                retina=1536
                window.SetSize(retina,retina)
                ren.ResetCameraClippingRange();window.Render()
                snap.Modified();snap.Update()
                hi_scalars=snap.GetOutput().GetPointData().GetScalars()
                if hi_scalars is None:raise RuntimeError(f'Empty retina raster for {name} {elev_idx}/{i}')
                high_rgb=vtk_to_numpy(hi_scalars).reshape(retina,retina,3)[::-1].copy()
                high_frame=Image.fromarray(high_rgb,'RGB').filter(
                    ImageFilter.UnsharpMask(radius=.6,percent=40,threshold=4))
                for skin_tone in SKIN_PALETTE:
                    out_frame=OUTPUT/'hires'/name/skin_tone/f'e{elev_idx}'/f'a{i:02d}.webp'
                    out_frame.parent.mkdir(parents=True,exist_ok=True)
                    variant=high_frame.copy() if skin_tone=='sawo-matang' else skin_variant(high_frame,skin_tone)
                    variant.save(out_frame,'WEBP',quality=94,method=5)
                    variant.close()
                    if out_frame.stat().st_size<3000:raise RuntimeError(f'Invalid retina frame: {out_frame}')
                high_frame.close()
                window.SetSize(size,size)

        # Keep each atlas < 23MP, safe for Safari and most integrated GPUs.
        assert atlas.width*atlas.height<24_000_000,(name,atlas.size)
        out=OUTPUT/f'{name}--e{elev_idx}.png'
        atlas.save(out,'PNG',compress_level=1)
        generated=[out.name]
        if anatomy:
            # The default PNG needs no recolor. Other tones run in separate
            # processes to avoid Pillow/VTK allocating many huge buffers at once.
            target=OUTPUT/f'{name}--sawo-matang--e{elev_idx}.png'
            target.write_bytes(out.read_bytes())
            generated.append(target.name)
        atlases.append(generated)
        print(name,'row',elev_idx,'size',atlas.size,'bytes',out.stat().st_size,
              'smoothedActors',smoothed,flush=True)
        if os.getenv('KWU_TURNTABLE_WORKER_MODE')=='1':
            # This worker owns a single row; all images have been saved.
            # Hard-exit avoids a VTK software-render teardown deadlock after
            # retaining several 14MP skin image encoders in memory.
            os._exit(0)
        if max_frames and (elev_idx+1)*ncol>=max_frames:break
    window.Finalize()
    return {'name':name,'columns':sheetCols,'rows':rows,'frames':ncol*len(elevations),
            'azimuthFrames':ncol,'elevations':list(elevations),'tileSize':size,
            'bytes':sum((OUTPUT/f'{name}--e{e}.png').stat().st_size for e in range(len(elevations)) if (OUTPUT/f'{name}--e{e}.png').exists()),
            'skinVariants':list(SKIN_PALETTE) if anatomy else [],'splitElevations':True,
            'atlasCount':len(elevations),'atlasFormat':'png'}


def render_variant(name:str,row:int,tone:str):
    if name not in ANATOMY or row not in (0,1) or tone not in SKIN_PALETTE:
        raise ValueError('Invalid skin variant')
    base=Image.open(OUTPUT/f'{name}--e{row}.png').convert('RGB')
    target=OUTPUT/f'{name}--{tone}--e{row}.png'
    if tone=='sawo-matang':target.write_bytes((OUTPUT/f'{name}--e{row}.png').read_bytes())
    else:
        recolored=skin_variant(base,tone)
        recolored.save(target,'PNG',compress_level=1)
        recolored.close()
    base.close()
    with Image.open(target) as im:
        assert im.size[0]*im.size[1]<24_000_000
        assert im.size==(3072,4608) or os.getenv('KWU_TURNTABLE_TILE')
    print(name,'row',row,'tone',tone,target.stat().st_size,'bytes',flush=True)


def main():
    if len(sys.argv)>=4 and sys.argv[1]=='--worker':
        name=sys.argv[2];row=sys.argv[3]
        if name not in ALL or row not in {'0','1'}:raise SystemExit('Invalid 360 atlas worker arguments')
        os.environ['KWU_TURNTABLE_ONLY_ELEVATION']=row
        render(name)
        return
    if len(sys.argv)>=5 and sys.argv[1]=='--variant':
        render_variant(sys.argv[2],int(sys.argv[3]),sys.argv[4]);return
    selected=os.getenv('KWU_TURNTABLE_MODELS','')
    names=[x for x in ALL if (not selected or x in selected.split(',')) and (MODELS/f'{x}.glb').exists()]
    start=time.monotonic()
    data={}
    for name in names:
        t=time.monotonic()
        for row in (0,1):
            env={**os.environ,'KWU_TURNTABLE_ONLY_ELEVATION':str(row),'KWU_TURNTABLE_WORKER_MODE':'1'}
            subprocess.run([sys.executable,str(Path(__file__).resolve()),'--worker',name,str(row)],env=env,check=True)
            if name in ANATOMY and os.getenv('KWU_TURNTABLE_SKIP_SKIN_VARIANTS')!='1':
                tones=os.getenv('KWU_TURNTABLE_TONE_LIST','').split(',') if os.getenv('KWU_TURNTABLE_TONE_LIST') else list(SKIN_PALETTE)
                for tone in tones:
                    if tone=='sawo-matang':continue
                    subprocess.run([sys.executable,str(Path(__file__).resolve()),'--variant',name,str(row),tone],env=os.environ.copy(),check=True)
            wanted=[f'{name}--e{row}.png']
            if name in ANATOMY:
                wanted+=[f'{name}--sawo-matang--e{row}.png']
                if os.getenv('KWU_TURNTABLE_SKIP_SKIN_VARIANTS')!='1':
                    wanted += [f'{name}--{tone}--e{row}.png' for tone in tones if tone!='sawo-matang']
            missing=[file for file in wanted if not (OUTPUT/file).is_file() or (OUTPUT/file).stat().st_size==0]
            if missing:raise RuntimeError(f'Missing output atlases: {missing}')
        anatomy=name in ANATOMY
        ncol=24 if anatomy else 16
        tile=int(os.getenv('KWU_TURNTABLE_TILE','0')) or (768 if anatomy else 640)
        data[name]={
           'name':name,'columns':4,'rows':math.ceil(ncol/4),
           'frames':ncol*2,'azimuthFrames':ncol,'elevations':[-10,12],
           'tileSize':tile,
           'bytes':sum((OUTPUT/f'{name}--e{row}.png').stat().st_size for row in (0,1)),
           'skinVariants':list(SKIN_PALETTE) if anatomy else [],
           'splitElevations':True,'atlasCount':2,'atlasFormat':'png'
        }
        print(name,'done in',round(time.monotonic()-t,1),'sec',flush=True)
    prior=OUTPUT/'manifest.json'
    if selected and prior.exists():
        old=json.loads(prior.read_text(encoding='utf-8'))['models']
        for name,meta in old.items():
            if name not in data:data[name]=meta
    prior.write_text(json.dumps({'version':14,'models':data},indent=2),encoding='utf-8')
    print('generated',len(names),'of',len(data),'in',round(time.monotonic()-start,1),'sec',flush=True)
if __name__=='__main__':main()
