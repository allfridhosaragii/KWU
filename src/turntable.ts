
/** A single, 1536px still frame is decoded only after rotation stops.
 * The existing 768px turntable sprite remains active throughout drag/zoom.
 * No huge retina atlas is downloaded on a mobile browser.
 */
class RetinaStill {
 private image:HTMLImageElement;
 private timer:number|undefined;
 private lastKey='';
 private sequence=0;
 private disposed=false;
 constructor(host:HTMLElement,private base:string){
   const image=new Image();image.draggable=false;image.alt='';image.decoding='async';
   image.setAttribute('aria-hidden','true');
   image.style.cssText='position:absolute;inset:0;width:100%;height:100%;object-fit:contain;pointer-events:none;user-select:none;opacity:0;transition:opacity .11s linear;transform-origin:center center;z-index:1';
   host.append(image);this.image=image;
 }
 display(model:string,tone:string,row:number,angle:number,zoom:number){
   if(this.disposed)return;
   this.image.style.transform='scale('+Math.max(.8,Math.min(zoom,2.8)).toFixed(3)+')';
   if(!['bracelet','ring','necklace'].includes(model))return;
   const colors=['sawo-matang','kuning-langsat','light-beige','medium-tan','deep-brown'];
   const t=colors.includes(tone)?tone:'sawo-matang';
   const r=Math.max(0,Math.min(1,Math.round(row)));
   const a=((Math.round(angle)%24)+24)%24;
   const url=this.base+'assets/turntables/hires/'+model+'/'+t+'/e'+r+'/a'+String(a).padStart(2,'0')+'.webp?v=12';
   if(url===this.lastKey)return;
   this.lastKey=url;this.image.style.opacity='0';
   if(this.timer!==undefined)clearTimeout(this.timer);
   const seq=++this.sequence;
   this.timer=window.setTimeout(async()=>{
     this.timer=undefined;
     try{
       const candidate=new Image();candidate.decoding='async';candidate.src=url;
       await candidate.decode();
       if(this.disposed||seq!==this.sequence||url!==this.lastKey)return;
       this.image.src=url;this.image.style.opacity='1';
     }catch{
       if(seq===this.sequence)this.image.style.opacity='0';
     }
   },190);
 }
 reset(){if(this.disposed)return;this.sequence++;if(this.timer!==undefined)clearTimeout(this.timer);this.timer=undefined;this.lastKey='';this.image.style.opacity='0';}
 dispose(){this.reset();this.disposed=true;this.image.remove();}
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
 private retina:RetinaStill;
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
   this.element=outer;this.sprite=sprite;this.retina=new RetinaStill(outer,base);
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
     this.sprite.style.backgroundImage='none';
     this.sprite.style.backgroundRepeat='no-repeat';
     this.sprite.style.backgroundSize=`${meta.columns*100}% ${meta.rows*100}%`;
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
     this.sprite.style.backgroundImage=`url("${url}")`;
     this.sprite.style.backgroundSize=`${m.columns*100}% ${m.rows*100}%`;
     this.paint();
     this.onStatus(`360° HD dapat diputar • ${m.tileSize}px per sudut • tanpa GPU`);
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
   const xPct=m.columns>1?100*x/(m.columns-1):0;
   const yPct=m.rows>1?100*y/(m.rows-1):0;
   this.sprite.style.backgroundPosition=`${xPct.toFixed(4)}% ${yPct.toFixed(4)}%`;
   this.element.dataset.frame=String(elevation*m.azimuthFrames+horizontal);
   this.retina.display(m.name,this.skinTone,elevation,horizontal,this.magnification);
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
 screenshot(){const im=this.currentImg,m=this.meta;if(!im||!m)return '';
   const absolute=Number(this.element.dataset.frame||0);const frame=m.splitElevations?absolute%m.azimuthFrames:absolute;const tile=m.tileSize;
   const c=document.createElement('canvas');c.width=tile;c.height=tile;
   const ctx=c.getContext('2d');if(!ctx)return '';
   ctx.drawImage(im,(frame%m.columns)*tile,Math.floor(frame/m.columns)*tile,tile,tile,0,0,tile,tile);
   try{return c.toDataURL('image/png')}catch{return ''}
 }
 dispose(){this.retina.dispose();this.disposed=true;this.atlasSequence++;this.element.remove();this.picture=null;this.meta=null;this.currentImg=null;this.pointers.clear()}
}
