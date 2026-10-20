/* Native WebGL2 / glTF 2.0 viewer used by the no-backend GitHub Pages preview.
 * Production migration target: Three.js + React Three Fiber, documented in /System.
 * Renderer only draws when dirty; no unnecessary continuous requestAnimationFrame. */
export type ModelKind='bracelet'|'ring'|'necklace'|'bag-charm'|'phone'|'tablet'|'macbook'|'bottle';
export interface ViewerOptions {kind:ModelKind;deviceModel:string;color:string;skinTone:'sawo-matang'|'kuning-langsat'|'light-beige'|'medium-tan'|'deep-brown';ornament:string;placement:number;scale:number;rotation:number;finger:number;caseType:string;pose:number;quality:'auto'|'low'|'high'}
const VERT=`#version 300 es
precision highp float;
layout(location=0) in vec3 aPosition;layout(location=1) in vec3 aNormal;layout(location=2) in vec4 aColor;layout(location=3) in vec2 aUV;
uniform mat4 uProjection;uniform float uYaw,uPitch,uDistance,uScale;
uniform vec3 uTint;uniform float uUseTint;uniform float uAlpha;uniform vec3 uOffset;uniform float uLidAngle;uniform float uFingerBend;
out vec3 vNormal;out vec3 vColor;out vec3 vPos;out float vAlpha;out vec2 vUV;
void main(){vec3 p=(aPosition+uOffset)*uScale;vec3 n=aNormal;
if(uLidAngle!=0.){float cy=cos(uLidAngle),sy=sin(uLidAngle);float py=p.y,pz=p.z-.13;p.y=cy*py-sy*pz;p.z=sy*py+cy*pz+.13;}
if(uFingerBend!=0. && p.y>.55){p.z+=uFingerBend*pow(max(0.,p.y-.55),2.);}

float c=cos(uYaw),s=sin(uYaw);p=vec3(c*p.x+s*p.z,p.y,-s*p.x+c*p.z);n=vec3(c*n.x+s*n.z,n.y,-s*n.x+c*n.z);
c=cos(uPitch);s=sin(uPitch);p=vec3(p.x,c*p.y-s*p.z,s*p.y+c*p.z);n=vec3(n.x,c*n.y-s*n.z,s*n.y+c*n.z);
p.z-=uDistance;gl_Position=uProjection*vec4(p,1.);
vNormal=normalize(n);vColor=mix(aColor.rgb,uTint,uUseTint);vPos=p;vAlpha=uAlpha;vUV=aUV;}`;
const FRAG=`#version 300 es
precision highp float;
in vec3 vNormal;
in vec3 vColor;
in vec3 vPos;
in float vAlpha;in vec2 vUV;
uniform float uSurface;uniform sampler2D uMap;uniform float uHasMap;uniform float uPhoto;uniform float uPhotoColorize;uniform vec3 uTintPhoto;
uniform float uSkin;uniform vec3 uSkinTone;uniform sampler2D uNormalMap;uniform float uHasNormal;
out vec4 outColor;

// Analytic studio key/fill. Retains one shader, no environment textures,
// IBL prefilter passes or postprocessing costs on low-end mobile devices.
void main(){
 vec3 N=normalize(vNormal);
 if(!gl_FrontFacing) N=-N;
 vec4 texel=uHasMap>.5?texture(uMap,vUV):vec4(1.);
 // Tangent-space skin normals reconstructed from mesh position / UV derivatives.
 if(uSkin>.5 && uHasNormal>.5){
    vec3 dpdx=dFdx(vPos), dpdy=dFdy(vPos);
    vec2 duvdx=dFdx(vUV), duvdy=dFdy(vUV);
    float determinant=duvdx.x*duvdy.y-duvdx.y*duvdy.x;
    if(abs(determin)>0.0000001){
      vec3 T=normalize(dpdx*duvdy.y-dpdy*duvdx.y);
      vec3 B=normalize(dpdy*duvdx.x-dpdx*duvdy.x);
      vec3 nMap=texture(uNormalMap,vUV).xyz*2.-1.;
      N=normalize(N*nMap.z + .30*(T*nMap.x+B*nMap.y));
    }
 }
 if(texel.a<.08)discard;
 if(uPhoto>.5){
 vec3 c=texel.rgb;
 if(uPhotoColorize>.5){float l=dot(c,vec3(.2126,.7152,.0722));
   c=clamp((.26+l*.75)*uTintPhoto*1.6+vec3(.07)*pow(l,7.),0.,1.);
 }
 outColor=vec4(c,texel.a*vAlpha);return;}
 vec3 V=normalize(-vPos);
 float metal=clamp(uSurface,0.,1.);
 float rough=uSkin>.5?.83:mix(.81,.23,metal);
 // For skin, the tone selector is a color-calibrated base, while the
 // anatomical texture contributes subtle variation. Avoid multiplying two
 // full warm albedos (the old renderer made all skin tones too dark).
 vec3 base=uSkin>.5
   ?pow(clamp(uSkinTone*clamp(texel.rgb/vec3(.72,.51,.38),vec3(.87),vec3(1.16)),0.,1.),vec3(2.0))
   :pow(clamp(vColor*texel.rgb,0.,1.),vec3(2.0));
 vec3 key=normalize(vec3(-.62,.88,.95));
 vec3 fill=normalize(vec3(.95,.36,.42));
 vec3 top=normalize(vec3(.18,1.0,-.48));
 float nl=max(dot(N,key),0.);
 float nf=max(dot(N,fill),0.);
 float nt=max(dot(N,top),0.);
 float wrap=max(.0,dot(N,key)*.68+.32);
 if(uSkin>.5)wrap=max(.0,dot(N,key)*.48+.52);
 float ambient=.20+.20*max(N.y,0.);
 float diffuse=(ambient+1.00*wrap+.24*nf+.13*nt);
 vec3 kd=base*(1.-metal*.78)*diffuse;
 vec3 H=normalize(V+key);
 vec3 H2=normalize(V+fill);
 float gloss=mix(13.,105.,1.-rough);
 float mainSpec=pow(max(dot(N,H),0.),gloss);
 float fillSpec=pow(max(dot(N,H2),0.),gloss*.42);
 vec3 F0=mix(vec3(.045),mix(base,vec3(.91,.93,.95),.38),metal);
 float fresnel=pow(1.-max(dot(N,V),0.),5.);
 vec3 F=F0+(1.-F0)*fresnel;
 float specStrength=mix(.18,.95,metal);
 vec3 spec=F*specStrength*(mainSpec*2.0+fillSpec*.42);
 float rim=pow(1.-max(dot(N,V),0.),3.);
 vec3 edge=F*(.08+.16*metal)*rim;
 // One-step dynamic range compression avoids harsh white clipping.
 vec3 linearColor=max(vec3(0.),kd+spec+edge);
 vec3 mapped=linearColor/(linearColor+vec3(.29));
 outColor=vec4(pow(clamp(mapped,0.,1.),vec3(.84)),vAlpha*texel.a);
}`;
interface Shape { vao:WebGLVertexArrayObject;count:number;indexType:number;vbo:WebGLBuffer[];ib:WebGLBuffer; index:number;texture:WebGLTexture|null;normalTexture:WebGLTexture|null;skin:boolean;photo:boolean;hasAlpha:boolean }
function hexRGB(s:string):[number,number,number]{const h=s.replace('#','');return [parseInt(h.slice(0,2),16)/255,parseInt(h.slice(2,4),16)/255,parseInt(h.slice(4,6),16)/255]}
const SKIN_HEX={ 'sawo-matang':'#B8825F','kuning-langsat':'#D5A27E','light-beige':'#E2BC9F','medium-tan':'#9F6D4F','deep-brown':'#6F4837'} as const;
const kindScale:Record<ModelKind,number>={bracelet:1,ring:1,necklace:1,'bag-charm':1,phone:1,tablet:1,macbook:1,bottle:1};
export class Viewer3D {
 private canvas:HTMLCanvasElement; private gl:WebGL2RenderingContext|null;private glVersion:1|2=2;private prog:WebGLProgram|null=null;private shapes:Shape[]=[]; private overlay:Shape|null=null;private textures:WebGLTexture[]=[];
 private u:Record<string,WebGLUniformLocation|null>={}; private yaw=.15;private pitch=-.11;private dist=5.5;private pointer=new Map<number,{x:number;y:number}>();private pinch=0;
 private resizeObserver:ResizeObserver|null=null;private visible=true;private pending=false;private dead=false;
 private readonly onVisibilityChange=()=>{this.visible=!document.hidden;if(this.visible)this.draw()};
 private fallback:HTMLElement;private fallbackImage:HTMLImageElement|null=null; private options:ViewerOptions; private modelLoad=0;private lastLoading='';
 constructor(el:HTMLElement, opts:ViewerOptions,private base:string,private onDrag:(n:number)=>void){
  this.options={...opts};if(opts.kind==='necklace')this.dist=6.15;this.canvas=document.createElement('canvas');this.canvas.setAttribute('aria-label',`Model 3D ${opts.kind}. Seret untuk memutar, cubit untuk zoom.`);this.canvas.tabIndex=0;this.canvas.draggable=false;this.canvas.style.touchAction='none';this.canvas.style.userSelect='none';
  this.fallback=document.createElement('div');this.fallback.className='screen-reader';this.fallback.setAttribute('role','status');
  el.append(this.canvas,this.fallback);const ctx:WebGLContextAttributes={antialias:true,alpha:true,depth:true,powerPreference:'low-power',preserveDrawingBuffer:false};
 this.gl=this.canvas.getContext('webgl2',ctx);
 if(!this.gl){
 const old=this.canvas.getContext('webgl',ctx) || this.canvas.getContext('experimental-webgl',ctx) as WebGLRenderingContext|null;
 const vao=old?.getExtension('OES_vertex_array_object');
 const uint=old?.getExtension('OES_element_index_uint');
 if(old&&vao&&uint){
 const legacy=old as WebGLRenderingContext&{createVertexArray?:()=>WebGLVertexArrayObject|null;bindVertexArray?:(node:WebGLVertexArrayObject|null)=>void;deleteVertexArray?:(node:WebGLVertexArrayObject|null)=>void};
 legacy.createVertexArray=()=>vao.createVertexArrayOES() as unknown as WebGLVertexArrayObject;
 legacy.bindVertexArray=node=>vao.bindVertexArrayOES(node as unknown as WebGLVertexArrayObjectOES|null);
 legacy.deleteVertexArray=node=>vao.deleteVertexArrayOES(node as unknown as WebGLVertexArrayObjectOES|null);
 this.gl=old as unknown as WebGL2RenderingContext;this.glVersion=1;
 }
 }
  if(!this.gl){this.fail('3D tidak tersedia: WebGL/GPU browser ini tidak aktif. Gunakan Safari atau Chrome terbaru dan pastikan akselerasi grafis aktif.');return}
  this.init();if(!this.prog)return;this.bind();this.resizeObserver=new ResizeObserver(()=>this.resize());this.resizeObserver.observe(el);this.resize();void this.load(opts.kind);
 }
 private fail(message:string){this.fallback.className='warning';this.fallback.style.position='absolute';this.fallback.style.top='58px';this.fallback.style.left='12px';this.fallback.style.right='12px';this.fallback.style.zIndex='4';this.fallback.textContent=message;this.canvas.style.display='none';if(!this.fallbackImage){this.fallbackImage=document.createElement('img');this.fallbackImage.alt='Pratinjau produk 2D ketika WebGL tidak tersedia';this.fallbackImage.draggable=false;this.fallbackImage.style.cssText='width:100%;height:100%;object-fit:contain;padding:30px;user-select:none;pointer-events:none;-webkit-user-drag:none';this.canvas.parentElement?.appendChild(this.fallbackImage)}
 const badge=this.canvas.parentElement?.querySelector('.viewer-top .pill');if(badge)badge.textContent='Preview 2D • GPU tidak aktif';
 console.warn('[KWU 3D]',message);this.fallbackImage.src=`${this.base}assets/previews/${this.options.deviceModel||this.options.kind}.webp`}
 private compile(kind:number,source:string){const g=this.gl!,s=g.createShader(kind)!;g.shaderSource(s,source);g.compileShader(s);if(!g.getShaderParameter(s,g.COMPILE_STATUS))throw Error(g.getShaderInfoLog(s)||'Shader gagal');return s}
 private shaderForLegacy(code:string,fragment:boolean){
 if(!fragment)return code.replace(/^#version 300 es\s*/,'').replace(/layout\(location=\d+\) in/g,'attribute').replace(/\bout (?=(?:vec[234]|float) )/g,'varying ');
 let output=code.replace(/^#version 300 es\s*/,'');
 const a=output.indexOf(' if(uSkin>.5 && uHasNormal>.5){'),b=output.indexOf(' if(texel.a<.08)discard;');
 if(a>=0&&b>a)output=output.slice(0,a)+output.slice(b);
 return output.replace(/\bin (?=(?:vec[234]|float) )/g,'varying ').replace(/out vec4 outColor;/,'').replace(/\boutColor\b/g,'gl_FragColor').replace(/\btexture\(/g,'texture2D(');
}
private init(){const g=this.gl!;try{const prog=g.createProgram()!;
 const vs=this.glVersion===2?VERT:this.shaderForLegacy(VERT,false);
 const fs=this.glVersion===2?FRAG:this.shaderForLegacy(FRAG,true);
 g.attachShader(prog,this.compile(g.VERTEX_SHADER,vs));g.attachShader(prog,this.compile(g.FRAGMENT_SHADER,fs));
 if(this.glVersion===1)for(const [i,name] of ['aPosition','aNormal','aColor','aUV'].entries())g.bindAttribLocation(prog,i,name);
 g.linkProgram(prog);if(!g.getProgramParameter(prog,g.LINK_STATUS))throw Error('Shader linker gagal');this.prog=prog;g.useProgram(prog);for(const n of ['uProjection','uYaw','uPitch','uDistance','uScale','uTint','uUseTint','uAlpha','uOffset','uLidAngle','uFingerBend','uSurface','uMap','uHasMap','uPhoto','uPhotoColorize','uTintPhoto','uSkin','uSkinTone','uNormalMap','uHasNormal'])this.u[n]=g.getUniformLocation(prog,n);g.enable(g.DEPTH_TEST);g.depthFunc(g.LEQUAL);g.enable(g.CULL_FACE);g.cullFace(g.BACK);}catch(e){this.fail('Grafis perangkat tidak mendukung renderer: '+String(e))}}
 private makeShape(pos:Float32Array,norm:Float32Array,color:Float32Array,indices:Uint16Array|Uint32Array,index:number,uv:Float32Array=new Float32Array(pos.length/3*2),texture:WebGLTexture|null=null,photo=false,hasAlpha=false,normalTexture:WebGLTexture|null=null,skin=false):Shape{
 const g=this.gl!,vao=g.createVertexArray()!;g.bindVertexArray(vao);const buffers:WebGLBuffer[]=[];
 const arrays:[number,Float32Array,number][]=[[0,pos,3],[1,norm,3],[2,color,4],[3,uv,2]];
 for(const [slot,arr,stride] of arrays){const b=g.createBuffer()!;buffers.push(b);g.bindBuffer(g.ARRAY_BUFFER,b);g.bufferData(g.ARRAY_BUFFER,arr,g.STATIC_DRAW);g.enableVertexAttribArray(slot);g.vertexAttribPointer(slot,stride,g.FLOAT,false,0,0)}
 const ib=g.createBuffer()!;g.bindBuffer(g.ELEMENT_ARRAY_BUFFER,ib);g.bufferData(g.ELEMENT_ARRAY_BUFFER,indices,g.STATIC_DRAW);g.bindVertexArray(null);
 return {vao,count:indices.length,indexType:indices instanceof Uint32Array?g.UNSIGNED_INT:g.UNSIGNED_SHORT,vbo:buffers,ib,index,texture,normalTexture,skin,photo,hasAlpha};}
 private async decodeImage(blob:Blob):Promise<HTMLImageElement>{
 const url=URL.createObjectURL(blob);
 try{const el=new Image();el.src=url;await el.decode();return el;}
 finally{URL.revokeObjectURL(url)}
 }
 private async embeddedImages(json:any,bin:ArrayBuffer):Promise<(WebGLTexture|null)[]>{
   const g=this.gl!;const imgs:(WebGLTexture|null)[]=[];
   for(const im of (json.images||[])){
     try{
      if(im.bufferView===undefined){imgs.push(null);continue}
      const bv=json.bufferViews[im.bufferView];const off=bv.byteOffset||0;
      const data=bin.slice(off,off+bv.byteLength);
      const blob=new Blob([data],{type:im.mimeType||'image/png'});
 let bitmap:ImageBitmap|HTMLImageElement;
 if(typeof createImageBitmap==='function'){try{bitmap=await createImageBitmap(blob,{premultiplyAlpha:'none'});}catch{bitmap=await this.decodeImage(blob);}}
 else bitmap=await this.decodeImage(blob);
      const tex=g.createTexture();if(!tex){if('close' in bitmap)bitmap.close();imgs.push(null);continue}
      g.bindTexture(g.TEXTURE_2D,tex);g.pixelStorei(g.UNPACK_FLIP_Y_WEBGL,false);
      g.texImage2D(g.TEXTURE_2D,0,g.RGBA,g.RGBA,g.UNSIGNED_BYTE,bitmap);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_WRAP_S,g.CLAMP_TO_EDGE);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_WRAP_T,g.CLAMP_TO_EDGE);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MAG_FILTER,g.LINEAR);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MIN_FILTER,g.LINEAR_MIPMAP_LINEAR);
      g.generateMipmap(g.TEXTURE_2D);g.bindTexture(g.TEXTURE_2D,null);
      if('close' in bitmap)bitmap.close();imgs.push(tex);this.textures.push(tex);
     }catch(error){console.warn('[KWU 3D] Satu tekstur gagal, geometri tetap digunakan:',error);imgs.push(null)}
   }
   return imgs;
 }
 private disposeShape(s:Shape){const g=this.gl!;g.deleteVertexArray(s.vao);s.vbo.forEach(b=>g.deleteBuffer(b));g.deleteBuffer(s.ib)}
 private accessor(json:any,bin:ArrayBuffer,i:number):Float32Array|Uint16Array|Uint32Array|Uint8Array{const a=json.accessors[i],view=json.bufferViews[a.bufferView];const size:{[k:string]:number}={SCALAR:1,VEC2:2,VEC3:3,VEC4:4};const num=a.count*size[a.type];const offset=(view.byteOffset||0)+(a.byteOffset||0);const length=a.componentType===5126?4:a.componentType===5125?4:a.componentType===5123?2:1;const slice=bin.slice(offset,offset+num*length);
 if(a.componentType===5126)return new Float32Array(slice);if(a.componentType===5125)return new Uint32Array(slice);if(a.componentType===5123)return new Uint16Array(slice);return new Uint8Array(slice)}
 private smoothNormals(p:Float32Array,indices:Uint32Array|Uint16Array){const n=new Float32Array(p.length);for(let i=0;i<indices.length;i+=3){const i0=indices[i]*3,i1=indices[i+1]*3,i2=indices[i+2]*3;const ax=p[i1]-p[i0],ay=p[i1+1]-p[i0+1],az=p[i1+2]-p[i0+2],bx=p[i2]-p[i0],by=p[i2+1]-p[i0+1],bz=p[i2+2]-p[i0+2];const nx=ay*bz-az*by,ny=az*bx-ax*bz,nz=ax*by-ay*bx;for(const j of [i0,i1,i2]){n[j]+=nx;n[j+1]+=ny;n[j+2]+=nz}}for(let j=0;j<n.length;j+=3){const len=Math.hypot(n[j],n[j+1],n[j+2])||1;n[j]/=len;n[j+1]/=len;n[j+2]/=len}return n}
 // GLB texture UV seams can duplicate vertices at identical 3D coordinates.
 // Smooth those coincident anatomical vertices together; otherwise a hand
 // looks faceted or develops artificial creases when the view rotates.
 private smoothAnatomicalNormals(p:Float32Array,indices:Uint32Array|Uint16Array){
   const normals=this.smoothNormals(p,indices);
   const groups=new Map<string,[number,number,number]>();
   const keyFor=(i:number)=>`${Math.round(p[i*3]*100000)},${Math.round(p[i*3+1]*100000)},${Math.round(p[i*3+2]*100000)}`;
   for(let i=0;i<p.length/3;i++){
     const key=keyFor(i);const n=groups.get(key);
     if(n){n[0]+=normals[i*3];n[1]+=normals[i*3+1];n[2]+=normals[i*3+2];}
     else groups.set(key,[normals[i*3],normals[i*3+1],normals[i*3+2]]);
   }
   for(let i=0;i<p.length/3;i++){
     const n=groups.get(keyFor(i))!;
     const len=Math.hypot(n[0],n[1],n[2])||1;
     normals[i*3]=n[0]/len;normals[i*3+1]=n[1]/len;normals[i*3+2]=n[2]/len;
   }
   return normals;
 }
 async load(kind:ModelKind){if(!this.gl)return;this.modelLoad++;const current=this.modelLoad;try{this.lastLoading=kind;const allow:Record<string,string[]>={phone:['iphone-17','iphone-air','iphone-17-pro','iphone-17-pro-max','iphone-17e'],tablet:['ipad-pro-11','ipad-pro-13','ipad-air-11','ipad-air-13'],macbook:['macbook-air-13','macbook-air-15','macbook-pro-14','macbook-pro-16']};const selection=(allow[kind]||[]).includes(this.options.deviceModel)?this.options.deviceModel:kind;const res=await fetch(`${this.base}models/${selection}.glb`);if(!res.ok)throw Error(`${res.status} ${res.statusText}`);const all=await res.arrayBuffer();const view=new DataView(all);if(view.getUint32(0,true)!==0x46546c67)throw Error('Bukan format GLB');const jLen=view.getUint32(12,true);const j=new TextDecoder().decode(new Uint8Array(all,20,jLen));const json=JSON.parse(j);const next=20+jLen;const bLen=view.getUint32(next,true);const bin=all.slice(next+8,next+8+bLen);if(this.dead||current!==this.modelLoad)return;
 this.textures.forEach(t=>this.gl!.deleteTexture(t));this.textures=[];
 const imgs=await this.embeddedImages(json,bin);if(this.dead||current!==this.modelLoad)return;
 this.shapes.forEach(s=>this.disposeShape(s));this.shapes=[];let idx=0;
 for(const m of json.meshes||[]){for(const pr of m.primitives||[]){if(pr.mode!==4)continue;const po=this.accessor(json,bin,pr.attributes.POSITION);if(!(po instanceof Float32Array))continue;const ii=this.accessor(json,bin,pr.indices);if(!(ii instanceof Uint16Array||ii instanceof Uint32Array))continue;const colRaw=pr.attributes.COLOR_0===undefined?null:this.accessor(json,bin,pr.attributes.COLOR_0);const colors=new Float32Array(po.length/3*4);for(let k=0;k<po.length/3;k++){for(let l=0;l<4;l++){const val=colRaw?colRaw[k*4+l]:255;colors[k*4+l]=colRaw instanceof Uint8Array?val/255:val}}
 const uvRaw=pr.attributes.TEXCOORD_0===undefined?null:this.accessor(json,bin,pr.attributes.TEXCOORD_0);
 const uv=uvRaw instanceof Float32Array?uvRaw:new Float32Array(po.length/3*2);
 const mat=pr.material===undefined?null:json.materials?.[pr.material];
 const ti=mat?.pbrMetallicRoughness?.baseColorTexture?.index;
 const imgID=ti===undefined?undefined:json.textures?.[ti]?.source;
 const tex=imgID===undefined?null:(imgs[imgID]||null);
 const nt=mat?.normalTexture?.index;const ni=nt===undefined?undefined:json.textures?.[nt]?.source;const normalTexture=ni===undefined?null:(imgs[ni]||null);
 const isSkin=(kind==='bracelet'||kind==='ring'||kind==='necklace')&&idx===0;
 const photo=typeof mat?.name==='string'&&mat.name.startsWith('photo_projected_');
 const alphaMode=mat?.alphaMode==='BLEND'||mat?.alphaMode==='MASK';
 const normals=isSkin?this.smoothAnatomicalNormals(po,ii):this.smoothNormals(po,ii);this.shapes.push(this.makeShape(po,normals,colors,ii,idx++,uv,tex,photo,alphaMode,normalTexture,isSkin));}}
 this.fallback.textContent=`3D aktif (${this.glVersion===2?'WebGL 2':'WebGL 1'})`;const badge=this.canvas.parentElement?.querySelector('.viewer-top .pill');if(badge)badge.textContent=`● 3D Aktif (${this.glVersion===2?'WebGL 2':'WebGL 1'})`;this.overlayRebuild();this.draw();}catch(e){if(current===this.modelLoad&&!this.dead)this.fail('Model 3D belum berhasil dimuat. '+String(e))}}
 update(opts:ViewerOptions){const changed=opts.kind!==this.options.kind||opts.deviceModel!==this.options.deviceModel;this.options={...opts};if(!this.gl){if(this.fallbackImage){const file=opts.deviceModel||opts.kind;this.fallbackImage.src=`${this.base}assets/previews/${file}.webp`;}return}if(changed){this.reset();void this.load(opts.kind)}else{this.overlayRebuild();this.draw()}}
 reset(){this.yaw=.15;this.pitch=-.11;this.dist=this.options.kind==='necklace'?6.15:5.5;this.draw()}
 rotate(degrees:number){if(!Number.isFinite(degrees))return;this.yaw+=degrees*Math.PI/180;this.draw()}
 zoom(delta:number){if(!Number.isFinite(delta))return;this.dist=Math.max(2.5,Math.min(11,this.dist+delta));this.draw()}
 hasInteractive3D(){return Boolean(this.gl&&this.prog&&!this.dead)}
 private overlayRebuild(){if(!this.gl)return;if(this.overlay){this.disposeShape(this.overlay);this.overlay=null}const o=this.options,scene=o.kind;const n=32;let coords:number[]=[];let z=.3,x=(o.placement-50)/100*1.15,y=0;
 if(scene==='bracelet'){x=(o.placement-50)/100*.30;y=-1.10;z=.355}
 if(scene==='ring'){const pos=[[-.16,.32,.24],[.57,.80,-.12],[.82,.60,-.43],[.90,.30,-.56],[.78,0,-.64]][Math.max(0,Math.min(4,o.finger))];x=pos[0];y=pos[1];z=pos[2]}
 if(scene==='necklace'){x=(o.placement-50)/100*.50;y=-.86;z=.615}
 if(scene==='bag-charm'){x=.86+(o.placement-50)/100*.32;y=-.70;z=.71}
 if(scene==='phone'){y=(o.placement-50)/100*1.85;z=.18}
 if(scene==='tablet'){y=(o.placement-50)/100*1.24;z=.095}
 if(scene==='macbook'){y=(o.placement-50)/100*1.22+.85;z=.32}
 if(scene==='bottle'){y=(o.placement-50)/100*1.65;z=.455}
 const radius=(scene==='bracelet'?.09:scene==='necklace'?.12:.17)*Math.max(.55,Math.min(1.55,o.scale));const heart=o.ornament==='heart';const flower=o.ornament==='flower';const pearl=o.ornament==='pearl';const r=o.ornament==='star'?10:flower?16:heart?52:n;
 coords=[x,y,z];const inds:number[]=[];for(let j=0;j<=r;j++){let th=(j/r)*Math.PI*2 +o.rotation*Math.PI/180;let rr=radius;
 if(o.ornament==='star')rr=j%2===0?radius:radius*.47;
 else if(flower)rr=radius*(.75+.23*Math.cos(j/r*Math.PI*2*5));
 let vx=x+rr*Math.sin(th),vy=y+rr*Math.cos(th);
 if(heart){const t=(j/r)*Math.PI*2;vx=x+radius*.065*(16*Math.pow(Math.sin(t),3));vy=y+radius*.065*(13*Math.cos(t)-5*Math.cos(2*t)-2*Math.cos(3*t)-Math.cos(4*t))}
 let vz=z;if(scene==='bottle'){const theta=(o.placement-50)/100*Math.PI+(vx-x)/.44;vz=.44*Math.cos(theta)+.014;vx=.44*Math.sin(theta)}
 coords.push(vx,vy,vz);if(j>0)inds.push(0,j,j+1)}const count=coords.length/3;const pos=new Float32Array(coords);const norms=new Float32Array(count*3);for(let i=0;i<count;i++)norms[i*3+2]=1;
 const c=o.ornament==='heart'?[.71,.36,.31,1]:o.ornament==='star'?[.90,.72,.37,1]:o.ornament==='flower'?[.75,.57,.61,1]:pearl?[.97,.92,.82,1]:[.81,.63,.4,1];const colors=new Float32Array(count*4);for(let i=0;i<count;i++)colors.set(c,i*4);this.overlay=this.makeShape(pos,norms,colors,new Uint16Array(inds),9999)}
 private resize(){const gl=this.gl;if(!gl||this.dead)return;const w=this.canvas.clientWidth,h=this.canvas.clientHeight;if(!w||!h)return;const dpr=this.options.quality==='low'?1:this.options.quality==='high'?Math.min(devicePixelRatio,innerWidth<768?1.6:2):Math.min(devicePixelRatio,innerWidth<768?1.25:1.7);const tw=Math.round(w*dpr),th=Math.round(h*dpr);if(this.canvas.width!==tw||this.canvas.height!==th){this.canvas.width=tw;this.canvas.height=th;gl.viewport(0,0,tw,th)}this.draw()}
 private schedule(){if(this.dead||this.pending)return;this.pending=true;requestAnimationFrame(()=>{this.pending=false;this.render()})}
 draw(){this.schedule()}
 private render(){const g=this.gl;if(!g||!this.prog||this.dead||!this.visible)return;g.viewport(0,0,this.canvas.width,this.canvas.height);g.clearColor(0,0,0,0);g.clear(g.COLOR_BUFFER_BIT|g.DEPTH_BUFFER_BIT);g.useProgram(this.prog);
 const aspect=this.canvas.width/Math.max(1,this.canvas.height),fov=38*Math.PI/180,near=.1,far=80,f=1/Math.tan(fov/2),p=new Float32Array([f/aspect,0,0,0,0,f,0,0,0,0,(far+near)/(near-far),-1,0,0,(2*far*near)/(near-far),0]);g.uniformMatrix4fv(this.u.uProjection,false,p);g.uniform1f(this.u.uYaw,this.yaw);g.uniform1f(this.u.uPitch,this.pitch+(this.options.pose-50)/400);g.uniform1f(this.u.uDistance,this.dist);g.uniform1f(this.u.uScale,kindScale[this.options.kind]);g.uniform3f(this.u.uOffset,0,0,0);g.uniform1f(this.u.uLidAngle,0);g.uniform1f(this.u.uFingerBend,0);
 for(const s of this.shapes){let tint=0;let alpha=1;const kind=this.options.kind;
  g.uniform3f(this.u.uOffset,0,0,0);g.uniform1f(this.u.uLidAngle,0);g.uniform1f(this.u.uFingerBend,0);
  if(kind==='ring'&&s.index>=this.shapes.length-2){const finger=[[-.16,.32,.10],[.57,.80,-.21],[.82,.60,-.52],[.90,.30,-.66],[.78,0,-.77]][Math.max(0,Math.min(4,this.options.finger))];g.uniform3f(this.u.uOffset,finger[0]-.82,finger[1]-.60,finger[2]+.52)}
  if(kind==='macbook'&&s.index>=this.shapes.length-3&&s.index<this.shapes.length-1)g.uniform1f(this.u.uLidAngle,(this.options.pose-50)/100*.72);
  // Hand poses are baked into the procedural mesh; true skeletal rigging is a future production task.

 const skinRgb=hexRGB(SKIN_HEX[this.options.skinTone]||SKIN_HEX['sawo-matang']);
 const isSkin=s.skin;
 if(isSkin){tint=1;}
 else if(kind==='phone'&&(s.index===0||s.index===1||s.index===this.shapes.length-1)){tint=1;if(s.index===this.shapes.length-1)alpha=this.options.caseType==='clear'?.18:.94}
 else if(kind==='bottle'&&s.index===0)tint=1;
 else if(kind==='bag-charm'&&s.index===0)tint=1;
 else if(kind==='tablet'&&s.index===0)tint=1;
 else if(kind==='macbook'&&(s.index===0||s.index===this.shapes.length-3))tint=1;
 const finish=kind==='bag-charm'?(s.index===0?.02:.12):kind==='bracelet'||kind==='ring'?(s.index===0?.02:.70):kind==='necklace'?(s.index<2?.025:.70):kind==='bottle'?(s.index===2||s.index===3?.12:.95):kind==='phone'||kind==='tablet'||kind==='macbook'?.78:.18;g.uniform1f(this.u.uSurface,finish);
 g.uniform1f(this.u.uHasMap,s.texture?1:0);g.uniform1f(this.u.uPhoto,s.photo?1:0);
 g.uniform1f(this.u.uSkin,isSkin?1:0);g.uniform3f(this.u.uSkinTone,...skinRgb);
 g.uniform1f(this.u.uHasNormal,s.normalTexture?1:0);g.activeTexture(g.TEXTURE1);g.bindTexture(g.TEXTURE_2D,s.normalTexture);g.uniform1i(this.u.uNormalMap,1);
 const photoTint=kind==='bottle'&&s.photo&&this.options.color.toUpperCase()==='#3E4141';
 g.uniform1f(this.u.uPhotoColorize,photoTint?1:0);
 const tc=hexRGB(this.options.color);g.uniform3f(this.u.uTintPhoto,tc[0],tc[1],tc[2]);
 g.activeTexture(g.TEXTURE0);g.bindTexture(g.TEXTURE_2D,s.texture);g.uniform1i(this.u.uMap,0);
 const c=isSkin?skinRgb:hexRGB(this.options.color);g.uniform3f(this.u.uTint,c[0],c[1],c[2]);g.uniform1f(this.u.uUseTint,tint);g.uniform1f(this.u.uAlpha,alpha);g.bindVertexArray(s.vao);if(alpha<1||s.hasAlpha){g.enable(g.BLEND);g.blendFunc(g.SRC_ALPHA,g.ONE_MINUS_SRC_ALPHA);g.depthMask(false)}else{g.disable(g.BLEND);g.depthMask(true)}g.drawElements(g.TRIANGLES,s.count,s.indexType,0)}
 if(this.overlay){g.uniform3f(this.u.uOffset,0,0,0);g.uniform1f(this.u.uLidAngle,0);g.uniform1f(this.u.uFingerBend,0);g.disable(g.BLEND);g.depthMask(true);g.uniform1f(this.u.uUseTint,0);g.uniform1f(this.u.uAlpha,1);g.uniform1f(this.u.uSurface,.35);g.uniform1f(this.u.uHasMap,0);g.uniform1f(this.u.uSkin,0);g.uniform1f(this.u.uHasNormal,0);g.uniform1f(this.u.uPhoto,0);g.uniform1f(this.u.uPhotoColorize,0);g.bindTexture(g.TEXTURE_2D,null);g.bindVertexArray(this.overlay.vao);g.disable(g.CULL_FACE);g.drawElements(g.TRIANGLES,this.overlay.count,this.overlay.indexType,0);g.enable(g.CULL_FACE)}g.bindVertexArray(null)}
 private bind(){this.canvas.addEventListener('dragstart',e=>e.preventDefault());this.canvas.addEventListener('pointerdown',e=>{e.preventDefault();this.pointer.set(e.pointerId,{x:e.clientX,y:e.clientY});this.canvas.setPointerCapture(e.pointerId)});this.canvas.addEventListener('pointermove',e=>{const old=this.pointer.get(e.pointerId);if(!old)return;e.preventDefault();this.pointer.set(e.pointerId,{x:e.clientX,y:e.clientY});if(this.pointer.size>1){const ps=[...this.pointer.values()];const d=Math.hypot(ps[0].x-ps[1].x,ps[0].y-ps[1].y);if(this.pinch)this.dist=Math.max(3.5,Math.min(9,this.dist-(d-this.pinch)*.015));this.pinch=d}else{const dx=e.clientX-old.x,dy=e.clientY-old.y;if(e.shiftKey){this.onDrag(Math.max(0,Math.min(100,this.options.placement+dx*.35)))}else{this.yaw+=dx*.009;this.pitch=Math.max(-.7,Math.min(.7,this.pitch+dy*.007))}}this.draw()});const stop=(e:PointerEvent)=>{this.pointer.delete(e.pointerId);if(this.pointer.size<2)this.pinch=0};this.canvas.addEventListener('pointerup',stop);this.canvas.addEventListener('pointercancel',stop);this.canvas.addEventListener('lostpointercapture',stop);this.canvas.addEventListener('wheel',e=>{e.preventDefault();this.dist=Math.max(3.5,Math.min(9,this.dist+e.deltaY*.006));this.draw()},{passive:false});this.canvas.addEventListener('keydown',e=>{if(e.key==='ArrowLeft')this.yaw-=.16;if(e.key==='ArrowRight')this.yaw+=.16;if(e.key==='ArrowUp')this.dist=Math.max(3.5,this.dist-.3);if(e.key==='ArrowDown')this.dist=Math.min(9,this.dist+.3);this.draw()});this.canvas.addEventListener('webglcontextlost',e=>{e.preventDefault();this.fallback.textContent='Sambungan grafis terputus, mencoba memulihkan 3D...';this.fallback.className='warning';});this.canvas.addEventListener('webglcontextrestored',()=>{if(this.dead)return;this.shapes=[];this.textures=[];this.overlay=null;this.prog=null;this.init();if(this.prog){this.canvas.style.display='block';this.fallback.className='screen-reader';this.resize();void this.load(this.options.kind);}});document.addEventListener('visibilitychange',this.onVisibilityChange)}
 screenshot(){try{return this.canvas.toDataURL('image/png')}catch{return ''}}
 dispose(){this.dead=true;this.modelLoad++;this.resizeObserver?.disconnect();document.removeEventListener('visibilitychange',this.onVisibilityChange);if(this.gl){this.shapes.forEach(s=>this.disposeShape(s));this.textures.forEach(t=>this.gl!.deleteTexture(t));if(this.overlay)this.disposeShape(this.overlay);if(this.prog)this.gl.deleteProgram(this.prog)}this.canvas.remove();this.fallback.remove();this.fallbackImage?.remove()}
}
