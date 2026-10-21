
/** A single, 1536px still frame is decoded only after rotation stops.
 * The existing 768px turntable sprite remains active throughout drag/zoom.
 * No huge retina atlas is downloaded on a mobile browser.
 */
class RetinaStill {
 private readonly image:HTMLImageElement;
 private lastKey='';
 private currentKey='';
 private requestId=0;
 private disposed=false;
 private previousAngle:number|null=null;
 private readonly cachedFrames=new Map<string,HTMLImageElement>();
 private readonly pendingFrames=new Map<string,Promise<HTMLImageElement|null>>();
 private readonly maxCache=7;
 constructor(host:HTMLElement,private base:string){
   const image=new Image();image.draggable=false;image.alt='';
   image.decoding='async';image.setAttribute('aria-hidden','true');
   image.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:contain;pointer-events:none;user-select:none;opacity:0;transition:opacity .07s linear;transform-origin:center center;z-index:1;image-rendering:auto';
   host.append(image);this.image=image;
 }
 private frameUrl(model:string,tone:string,row:number,angle:number){
   const colors=['sawo-matang','kuning-langsat','light-beige','medium-tan','deep-brown'];
   const safeTone=colors.includes(tone)?tone:'sawo-matang';
   const safeRow=Math.max(0,Math.min(1,Math.round(row)));
   const safeAngle=((Math.round(angle)%24)+24)%24;
   return this.base+'assets/turntables/hires/'+model+'/'+safeTone+'/e'+safeRow+'/a'+String(safeAngle).padStart(2,'0')+'.webp?v=16-1';
 }
 private touch(url:string,img:HTMLImageElement){
   this.cachedFrames.delete(url);
   this.cachedFrames.set(url,img);
   while(this.cachedFrames.size>this.maxCache){
     const oldest=this.cachedFrames.keys().next().value;
     if(oldest===undefined)break;
     this.cachedFrames.delete(oldest);
   }
 }
 private fetchFrame(url:string,highPriority:boolean):Promise<HTMLImageElement|null>{
   const cached=this.cachedFrames.get(url);
   if(cached){this.touch(url,cached);return Promise.resolve(cached);}
   const previous=this.pendingFrames.get(url);
   if(previous)return previous;
   // These are separate 1536px stills, not a giant atlas. Keep decoded
   // frames bounded in memory to avoid Safari tab reloads on mobile.
   const image=new Image();image.decoding='async';image.draggable=false;
   if('fetchPriority' in image)image.fetchPriority=highPriority?'high':'low';
   image.src=url;
   const pending=image.decode().then(()=>{
     if(this.disposed)return null;
     this.touch(url,image);
     return image;
   }).catch(()=>{
     return null;
   }).finally(()=>this.pendingFrames.delete(url));
   this.pendingFrames.set(url,pending);
   return pending;
 }
 private prefetch(model:string,tone:string,row:number,angle:number,direction:number){
   const offsets=direction===0?[-1,1]:[direction,2*direction,-direction];
   for(const offset of offsets){
     const url=this.frameUrl(model,tone,row,angle+offset);
     if(this.cachedFrames.has(url)||this.pendingFrames.has(url))continue;
     // High-res prefetch should not starve the frame actively being displayed.
     if(this.pendingFrames.size>=4)break;
     void this.fetchFrame(url,false);
   }
 }
 private showFrame(url:string,image:HTMLImageElement){
   if(this.disposed)return;
   this.image.src=image.src;
   this.image.dataset.hdFrame='1536';
   this.image.style.opacity='1';
   this.currentKey=url;
 }
 display(model:string,tone:string,row:number,angle:number,zoom:number){
   if(this.disposed)return;
   this.image.style.transform='scale('+Math.max(.8,Math.min(zoom,2.8)).toFixed(3)+')';
   if(!['bracelet','ring','necklace'].includes(model))return;
   const a=((Math.round(angle)%24)+24)%24;
   const previous=this.previousAngle;
   const diff=previous===null?0:((a-previous+36)%24)-12;
   const direction=diff===0?0:diff>0?1:-1;
   this.previousAngle=a;
   const url=this.frameUrl(model,tone,row,a);
   if(url===this.lastKey)return;
   this.lastKey=url;
   const request=++this.requestId;
   const hot=this.cachedFrames.get(url);
   if(hot){
     this.touch(url,hot);
     this.showFrame(url,hot);
   }else{
     // The lower-resolution turntable stays responsive until the current
     // 1536px frame arrives. No 75ms idle delay: decode begins immediately.
     this.image.style.opacity='0';
     void this.fetchFrame(url,true).then(image=>{
       if(!image||this.disposed||request!==this.requestId||url!==this.lastKey)return;
       this.showFrame(url,image);
     });
   }
   this.prefetch(model,tone,row,a,direction);
 }
 screenshot(){
   if(!this.currentKey||this.currentKey!==this.lastKey||!this.image.complete||this.image.naturalWidth<1000)return '';
   const canvas=document.createElement('canvas');
   canvas.width=this.image.naturalWidth;canvas.height=this.image.naturalHeight;
   const ctx=canvas.getContext('2d');if(!ctx)return '';
   try{ctx.drawImage(this.image,0,0);return canvas.toDataURL('image/png');}
   catch{return ''}
 }
 reset(){
   if(this.disposed)return;
   ++this.requestId;
   this.lastKey='';this.currentKey='';this.previousAngle=null;
   this.image.style.opacity='0';
 }
 dispose(){
   if(this.disposed)return;
   this.reset();this.disposed=true;
   this.cachedFrames.clear();this.pendingFrames.clear();this.image.remove();
 }
}

/** Interactive 360° frame renderer. Rotates offline-rendered GLB views without WebGL.
 *  This is NOT continuous realtime 3D, and is labelled as such in the UI.
 *  The atlas assets are self-hosted on GitHub Pages so they work in in-app browsers.
 */
export type TurntableMeta={name:string;columns:number;rows:number;frames:number;azimuthFrames:number;elevations:number[];tileSize:number;bytes:number;skinVariants?:string[];splitElevations?:boolean;atlasCount?:number;atlasFormat?:string};
type Manifest={version:number;models:Record<string,TurntableMeta>};
const bound=(n:number,low:number,high:number)=>Math.min(high,Math.max(low,n));
export class Turntable360 {
 readonly element:HTMLDivElement;
 private sprite:HTMLDivElement;
 private frameCanvas:HTMLCanvasElement;
 private frameContext:CanvasRenderingContext2D;
 private renderedFrame='';
 private retina:RetinaStill;
 private detailPreview:HTMLDivElement;
 private detailBadge:HTMLDivElement;
 private requestedQuality:'auto'|'low'|'high'='auto';
 private designParams: {kind:string;ornament:string;color:string;placement:number;rotation:number;scale:number;finger:number;caseType:string;pose:number;quality:'auto'|'low'|'high'}|null=null;
 private picture:HTMLImageElement|null=null;
 private meta:TurntableMeta|null=null;
 private azimuth=0;
 private pitchRow=0;
 private magnification=1;
 private pointers=new Map<number,{x:number;y:number}>();
 private pinchDistance=0;
 private currentImg:HTMLImageElement|null=null;
 private disposed=false;
 private lastName='';
 private skinTone='sawo-matang';
 private manifestVersion=10;
 private renderedAtlas='';
 private loadingAtlas='';
 private atlasSequence=0;
 constructor(private host:HTMLElement,private base:string,private onStatus:(text:string)=>void,initialTone='sawo-matang'){
   this.skinTone=initialTone;
   const outer=document.createElement('div');outer.className='kwu-turntable';outer.tabIndex=0;
   outer.setAttribute('role','group');outer.setAttribute('aria-label','Pratinjau 360 derajat. Geser ke kiri dan kanan untuk memutar; ke atas atau bawah untuk mengubah sudut. Cubit untuk zoom.');
   outer.style.touchAction='none';outer.style.userSelect='none';
   const sprite=document.createElement('div');sprite.className='kwu-turntable-sprite';outer.append(sprite);
   const frameCanvas=document.createElement('canvas');frameCanvas.width=1;frameCanvas.height=1;
   frameCanvas.style.cssText='display:block;width:100%;height:100%;pointer-events:none;image-rendering:auto';
   const ctx=frameCanvas.getContext('2d',{alpha:false});
   if(!ctx)throw new Error('Canvas2D tidak tersedia');
   sprite.append(frameCanvas);
   this.element=outer;this.sprite=sprite;this.frameCanvas=frameCanvas;this.frameContext=ctx;
   this.retina=new RetinaStill(outer,base);
   const ornamentPreview=document.createElement('div');
   ornamentPreview.className='kwu-decoration-preview';
   ornamentPreview.setAttribute('aria-label','Ilustrasi ornamen yang dipilih');
   ornamentPreview.style.display='none';
   outer.append(ornamentPreview);
   this.detailPreview=ornamentPreview;
   const info=document.createElement('div');
   info.className='kwu-design-readout';
   info.setAttribute('role','status');
   info.setAttribute('aria-live','polite');
   info.style.display='none';
   outer.append(info);this.detailBadge=info;
   host.append(outer);
   outer.addEventListener('dragstart',event=>event.preventDefault());
   outer.addEventListener('pointerdown',e=>{
     e.preventDefault();outer.setPointerCapture(e.pointerId);this.pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
     if(this.pointers.size>=2)this.pinchDistance=this.distance();
   });
   outer.addEventListener('pointermove',e=>{
     const old=this.pointers.get(e.pointerId);if(!old)return;e.preventDefault();
     this.pointers.set(e.pointerId,{x:e.clientX,y:e.clientY});
     if(this.pointers.size>=2){const now=this.distance();if(this.pinchDistance>0){this.magnification=bound(this.magnification*(now/this.pinchDistance),.8,2.8)}this.pinchDistance=now;}
     else if(this.meta){const dx=e.clientX-old.x,dy=e.clientY-old.y;
       this.azimuth-=dx/13;this.pitchRow=bound(this.pitchRow-dy/85,0,this.meta.elevations.length-1);}
     this.paint();
   });
   const end=(e:PointerEvent)=>{this.pointers.delete(e.pointerId);if(this.pointers.size<2)this.pinchDistance=0;};
   outer.addEventListener('pointerup',end);outer.addEventListener('pointercancel',end);outer.addEventListener('lostpointercapture',end);
   outer.addEventListener('wheel',e=>{e.preventDefault();this.zoom(e.deltaY>0?.12:-.12);},{passive:false});
   outer.addEventListener('keydown',e=>{
     if(e.key==='ArrowLeft')this.rotate(-15);
     else if(e.key==='ArrowRight')this.rotate(15);
     else if(e.key==='ArrowUp')this.zoom(-.15);
     else if(e.key==='ArrowDown')this.zoom(.15);
     else return;
     e.preventDefault();
   });
 }
 setCustomization(options:{kind:string;ornament:string;color:string;placement:number;rotation:number;scale:number;finger:number;caseType:string;pose:number;quality:'auto'|'low'|'high'}){
   if(this.disposed)return;
   const prev=this.designParams;
   this.designParams={...options};
   this.requestedQuality=options.quality;
   // These images are fixed 3D camera renders. Decorations below are clearly
   // marked as 2D approximate previews, not manufacturing-accurate placement.
   const symbols:Record<string,string>={heart:'♥',star:'★',flower:'✿',pearl:'●'};
   const names:Record<string,string>={heart:'Hati',star:'Bintang',flower:'Bunga',pearl:'Pearl'};
   const symbol=symbols[options.ornament]||symbols.heart;
   const title=names[options.ornament]||names.heart;
   const position=bound(Number(options.placement)||50,0,100);
   const scale=bound(Number(options.scale)||1,.55,1.55);
   const rotation=Number(options.rotation)||0;
   const color=/^#[0-9a-f]{6}$/i.test(options.color)?options.color:'#B49376';
   this.detailPreview.textContent=symbol;
   this.detailPreview.style.display='flex';
   this.detailPreview.style.color=color;
   this.detailPreview.style.transform=`translate(-50%, -50%) rotate(${rotation}deg) scale(${scale})`;
   this.detailPreview.style.left=`${45+(position-50)*.4}%`;
   const fingerY=[55,45,40,43,49];
   this.detailPreview.style.top=`${options.kind==='bracelet'?72:options.kind==='ring'?fingerY[bound(options.finger,0,4)]||45:options.kind==='necklace'?67:options.kind==='bag-charm'?35:50}%`;
   this.detailPreview.classList.toggle('kwu-decoration-sticker', ['phone','tablet','macbook','bottle'].includes(options.kind));
   this.detailBadge.style.display='block';
   this.detailBadge.textContent=`Preview ornamen 2D: ${title} · Posisi ${Math.round(position)}% · ${scale.toFixed(2)}×`;
   // The pose slider is mapped to available camera elevation in GPU-free mode,
   // which makes its effect visible without falsely claiming skeletal posing.
   if(this.meta && (prev===null || prev.pose!==options.pose)){
     this.pitchRow=bound(Number(options.pose)||50,0,100)/100*(this.meta.elevations.length-1);
     this.paint();
   }
   if(prev?.quality!==options.quality){
     if(options.quality==='low')this.retina.reset();
     else this.paint();
   }
 }
 private distance(){const [a,b]=[...this.pointers.values()];return a&&b?Math.hypot(a.x-b.x,a.y-b.y):0;}
 async load(name:string){
   this.lastName=name;this.retina.reset();
   ++this.atlasSequence;
   this.meta=null;this.currentImg=null;
   this.renderedAtlas='';this.loadingAtlas='';
   this.onStatus('Memuat gambar 360° kualitas tinggi…');
   try{
     const response=await fetch(`${this.base}assets/turntables/manifest.json`,{cache:'no-cache'});
     if(!response.ok)throw new Error(`HTTP ${response.status}`);
     const manifest=await response.json() as Manifest;
     if(this.disposed||name!==this.lastName)return;
     const meta=manifest.models[name]||manifest.models[name.split('-')[0]];
     if(!meta)throw new Error(`360° ${name} belum tersedia`);
     this.manifestVersion=manifest.version;
     this.meta=meta;this.azimuth=0;this.pitchRow=0;this.magnification=1;
     if(this.picture){this.picture.remove();this.picture=null;}
     if(this.designParams)this.setCustomization(this.designParams);
     this.sprite.replaceChildren(this.frameCanvas);
     this.sprite.style.backgroundImage='none';
     this.frameCanvas.width=meta.tileSize;this.frameCanvas.height=meta.tileSize;
     this.renderedFrame='';
     await this.useAtlas(0);
   }catch(error){
     if(this.disposed||name!==this.lastName)return;
     this.fail2D(name,error);
   }
 }
 private fail2D(name:string,error:unknown){
   this.onStatus('Hanya gambar 2D • 360° belum berhasil dimuat');
   this.sprite.style.backgroundImage='none';
   const image=document.createElement('img');
   image.src=`${this.base}assets/previews/${name}.webp`;
   image.draggable=false;image.alt='Gambar produk 2D sementara';
   image.style.cssText='width:100%;height:100%;object-fit:contain;pointer-events:none';
   this.sprite.replaceChildren(image);this.picture=image;
   console.warn('[KWU 360]',error);
 }
 private atlasUrl(row:number){
   const m=this.meta!;
   const tone=m.skinVariants?.includes(this.skinTone)?`--${this.skinTone}`:'';
   const elevation=m.splitElevations?`--e${row}`:'';
   const ext=m.splitElevations?(m.atlasFormat||'png'):'webp';
   return `${this.base}assets/turntables/${m.name}${tone}${elevation}.${ext}?v=${this.manifestVersion}`;
 }
 private async useAtlas(row:number){
   const m=this.meta;if(!m||this.disposed)return;
   const url=this.atlasUrl(row);
   if(url===this.renderedAtlas){
     if(this.loadingAtlas&&this.loadingAtlas!==url){this.atlasSequence++;this.loadingAtlas='';}
     return;
   }
   if(this.loadingAtlas===url)return;
   const seq=++this.atlasSequence;
   this.loadingAtlas=url;
   const image=new Image();image.decoding='async';image.draggable=false;image.src=url;
   try{
     await image.decode();
     if(this.disposed||seq!==this.atlasSequence||url!==this.atlasUrl(Math.round(bound(this.pitchRow,0,m.elevations.length-1))))return;
     this.currentImg=image;this.renderedAtlas=url;this.loadingAtlas='';
     this.renderedFrame='';this.sprite.style.backgroundImage='none';
     this.paint();
     this.onStatus(['bracelet','ring','necklace'].includes(m.name)?'360° bisa diputar • HD 1536p dimuat otomatis':'360° bisa diputar • '+m.tileSize+'p per sudut');
   }catch(error){
     if(this.disposed||seq!==this.atlasSequence)return;
     this.loadingAtlas='';
     if(!this.currentImg)this.fail2D(this.lastName,error);
     else console.warn('[KWU 360] Sudut lain gagal dimuat:',error);
   }
 }
 private paint(){
   if(this.disposed)return;
   this.sprite.style.transform=`scale(${this.magnification.toFixed(3)})`;
   const m=this.meta;if(!m)return;
   const horizontal=((Math.round(this.azimuth)%m.azimuthFrames)+m.azimuthFrames)%m.azimuthFrames;
   const elevation=Math.round(bound(this.pitchRow,0,m.elevations.length-1));
   if(m.splitElevations){
     const url=this.atlasUrl(elevation);
     if(this.renderedAtlas!==url){void this.useAtlas(elevation);}
     // One atlas contains exactly one elevation. Vertical drag lazy-loads the other.
   }
   const frame=m.splitElevations?horizontal:elevation*m.azimuthFrames+horizontal;
   const x=frame%m.columns,y=Math.floor(frame/m.columns);
   // Explicitly isolate the frame, otherwise zoom may reveal adjacent atlas tiles.
   if(this.currentImg && this.renderedAtlas===this.atlasUrl(elevation)){
     const key=this.renderedAtlas+':'+frame;
     if(this.renderedFrame!==key){
       const tile=m.tileSize;
       if(this.frameCanvas.width!==tile||this.frameCanvas.height!==tile){
         this.frameCanvas.width=tile;this.frameCanvas.height=tile;
       }
       if(this.currentImg.naturalWidth>=(x+1)*tile && this.currentImg.naturalHeight>=(y+1)*tile){
         this.frameContext.drawImage(this.currentImg,x*tile,y*tile,tile,tile,0,0,tile,tile);
         this.renderedFrame=key;
       }else console.warn('[KWU 360] Atlas dimensions mismatch',m);
     }
   }
   this.element.dataset.frame=String(elevation*m.azimuthFrames+horizontal);
   if(this.requestedQuality!=='low')this.retina.display(m.name,this.skinTone,elevation,horizontal,this.magnification);
 }
 async setSkinTone(tone:string){
   if(tone===this.skinTone)return;
   this.skinTone=tone;this.retina.reset();
   const m=this.meta;if(!m||!m.skinVariants?.includes(tone))return;
   const row=Math.round(bound(this.pitchRow,0,m.elevations.length-1));
   await this.useAtlas(row);
 }
 reset(){this.azimuth=0;this.pitchRow=0;this.magnification=1;this.paint();}
 rotate(degrees:number){if(!Number.isFinite(degrees)||!this.meta)return;this.azimuth+=degrees/(360/this.meta.azimuthFrames);this.paint();}
 zoom(delta:number){if(!Number.isFinite(delta))return;this.magnification=bound(this.magnification-delta,.8,2.8);this.paint();}
 screenshot(){const hd=this.retina.screenshot();if(hd)return hd;const im=this.currentImg,m=this.meta;if(!im||!m)return '';
   const absolute=Number(this.element.dataset.frame||0);const frame=m.splitElevations?absolute%m.azimuthFrames:absolute;const tile=m.tileSize;
   const c=document.createElement('canvas');c.width=tile;c.height=tile;
   const ctx=c.getContext('2d');if(!ctx)return '';
   ctx.drawImage(im,(frame%m.columns)*tile,Math.floor(frame/m.columns)*tile,tile,tile,0,0,tile,tile);
   try{return c.toDataURL('image/png')}catch{return ''}
 }
 dispose(){this.retina.dispose();this.disposed=true;this.atlasSequence++;this.element.remove();this.picture=null;this.meta=null;this.currentImg=null;this.pointers.clear()}
}
