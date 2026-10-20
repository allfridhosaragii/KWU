"""Upgrade native WebGL2 GLB preview to handle embedded glTF baseColorTexture.
Supports PBR textures in GLB v2 while remaining fully offline / GitHub Pages.
"""
from pathlib import Path
p=Path(__file__).resolve().parent.parent/'src/viewer.ts'
s=p.read_text()
s=s.replace('layout(location=2) in vec4 aColor;', 'layout(location=2) in vec4 aColor;layout(location=3) in vec2 aUV;')
s=s.replace('out vec3 vNormal;out vec3 vColor;out vec3 vPos;out float vAlpha;', 'out vec3 vNormal;out vec3 vColor;out vec3 vPos;out float vAlpha;out vec2 vUV;')
s=s.replace('vPos=p;vAlpha=uAlpha;', 'vPos=p;vAlpha=uAlpha;vUV=aUV;')
s=s.replace('in float vAlpha;\nuniform float uSurface;', 'in float vAlpha;in vec2 vUV;\nuniform float uSurface;uniform sampler2D uMap;uniform float uHasMap;uniform float uPhoto;')
s=s.replace(' if(!gl_FrontFacing) N=-N;\n vec3 V=normalize(-vPos);', ''' if(!gl_FrontFacing) N=-N;
 vec4 texel=uHasMap>.5?texture(uMap,vUV):vec4(1.);
 if(texel.a<.08)discard;
 if(uPhoto>.5){outColor=vec4(texel.rgb,texel.a*vAlpha);return;}
 vec3 V=normalize(-vPos);''')
s=s.replace('vec3 base=pow(clamp(vColor,0.,1.),vec3(2.0));', 'vec3 base=pow(clamp(vColor*texel.rgb,0.,1.),vec3(2.0));')
s=s.replace('outColor=vec4(pow(clamp(mapped,0.,1.),vec3(.84)),vAlpha);', 'outColor=vec4(pow(clamp(mapped,0.,1.),vec3(.84)),vAlpha*texel.a);')
s=s.replace('index:number }','index:number;texture:WebGLTexture|null;photo:boolean;hasAlpha:boolean }',1)
s=s.replace('private shapes:Shape[]=[]; private overlay:Shape|null=null;', 'private shapes:Shape[]=[]; private overlay:Shape|null=null;private textures:WebGLTexture[]=[];')
s=s.replace("'uSurface'])", "'uSurface','uMap','uHasMap','uPhoto'])")
# Extend makeShape with texture support and separate UV stream.
start=s.index(' private makeShape(')
end=s.index(' private disposeShape(',start)
s=s[:start]+''' private makeShape(pos:Float32Array,norm:Float32Array,color:Float32Array,indices:Uint16Array|Uint32Array,index:number,uv:Float32Array=new Float32Array(pos.length/3*2),texture:WebGLTexture|null=null,photo=false,hasAlpha=false):Shape{
 const g=this.gl!,vao=g.createVertexArray()!;g.bindVertexArray(vao);const buffers:WebGLBuffer[]=[];
 const arrays:[number,Float32Array,number][]=[[0,pos,3],[1,norm,3],[2,color,4],[3,uv,2]];
 for(const [slot,arr,stride] of arrays){const b=g.createBuffer()!;buffers.push(b);g.bindBuffer(g.ARRAY_BUFFER,b);g.bufferData(g.ARRAY_BUFFER,arr,g.STATIC_DRAW);g.enableVertexAttribArray(slot);g.vertexAttribPointer(slot,stride,g.FLOAT,false,0,0)}
 const ib=g.createBuffer()!;g.bindBuffer(g.ELEMENT_ARRAY_BUFFER,ib);g.bufferData(g.ELEMENT_ARRAY_BUFFER,indices,g.STATIC_DRAW);g.bindVertexArray(null);
 return {vao,count:indices.length,indexType:indices instanceof Uint32Array?g.UNSIGNED_INT:g.UNSIGNED_SHORT,vbo:buffers,ib,index,texture,photo,hasAlpha};}
 private async embeddedImages(json:any,bin:ArrayBuffer):Promise<(WebGLTexture|null)[]>{
   const g=this.gl!;const imgs:(WebGLTexture|null)[]=[];
   for(const im of (json.images||[])){
      if(im.bufferView===undefined){imgs.push(null);continue}
      const bv=json.bufferViews[im.bufferView];const off=bv.byteOffset||0;
      const data=bin.slice(off,off+bv.byteLength);
      const bitmap=await createImageBitmap(new Blob([data],{type:im.mimeType||'image/png'}),{premultiplyAlpha:'none'});
      const tex=g.createTexture();if(!tex){bitmap.close();imgs.push(null);continue}
      g.bindTexture(g.TEXTURE_2D,tex);g.pixelStorei(g.UNPACK_FLIP_Y_WEBGL,false);
      g.texImage2D(g.TEXTURE_2D,0,g.RGBA,g.RGBA,g.UNSIGNED_BYTE,bitmap);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_WRAP_S,g.CLAMP_TO_EDGE);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_WRAP_T,g.CLAMP_TO_EDGE);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MAG_FILTER,g.LINEAR);
      g.texParameteri(g.TEXTURE_2D,g.TEXTURE_MIN_FILTER,g.LINEAR_MIPMAP_LINEAR);
      g.generateMipmap(g.TEXTURE_2D);g.bindTexture(g.TEXTURE_2D,null);
      bitmap.close();imgs.push(tex);this.textures.push(tex);
   }
   return imgs;
 }
''' +s[end:]
# replace loader inner snippet
search='''if(this.dead||current!==this.modelLoad)return;this.shapes.forEach(s=>this.disposeShape(s));this.shapes=[];let idx=0;
 for(const m of json.meshes||[]){for(const pr of m.primitives||[]){if(pr.mode!==4)continue;const po=this.accessor(json,bin,pr.attributes.POSITION);if(!(po instanceof Float32Array))continue;const ii=this.accessor(json,bin,pr.indices);if(!(ii instanceof Uint16Array||ii instanceof Uint32Array))continue;const colRaw=pr.attributes.COLOR_0===undefined?null:this.accessor(json,bin,pr.attributes.COLOR_0);const colors=new Float32Array(po.length/3*4);for(let k=0;k<po.length/3;k++){for(let l=0;l<4;l++){const val=colRaw?colRaw[k*4+l]:255;colors[k*4+l]=colRaw instanceof Uint8Array?val/255:val}}const normals=this.smoothNormals(po,ii);this.shapes.push(this.makeShape(po,normals,colors,ii,idx++))}}
'''
replace='''if(this.dead||current!==this.modelLoad)return;
 const imgs=await this.embeddedImages(json,bin);if(this.dead||current!==this.modelLoad)return;
 this.shapes.forEach(s=>this.disposeShape(s));this.shapes=[];let idx=0;
 for(const m of json.meshes||[]){for(const pr of m.primitives||[]){if(pr.mode!==4)continue;const po=this.accessor(json,bin,pr.attributes.POSITION);if(!(po instanceof Float32Array))continue;const ii=this.accessor(json,bin,pr.indices);if(!(ii instanceof Uint16Array||ii instanceof Uint32Array))continue;const colRaw=pr.attributes.COLOR_0===undefined?null:this.accessor(json,bin,pr.attributes.COLOR_0);const colors=new Float32Array(po.length/3*4);for(let k=0;k<po.length/3;k++){for(let l=0;l<4;l++){const val=colRaw?colRaw[k*4+l]:255;colors[k*4+l]=colRaw instanceof Uint8Array?val/255:val}}
 const uvRaw=pr.attributes.TEXCOORD_0===undefined?null:this.accessor(json,bin,pr.attributes.TEXCOORD_0);
 const uv=uvRaw instanceof Float32Array?uvRaw:new Float32Array(po.length/3*2);
 const mat=pr.material===undefined?null:json.materials?.[pr.material];
 const ti=mat?.pbrMetallicRoughness?.baseColorTexture?.index;
 const imgID=ti===undefined?undefined:json.textures?.[ti]?.source;
 const tex=imgID===undefined?null:(imgs[imgID]||null);
 const photo=typeof mat?.name==='string'&&mat.name.startsWith('photo_projected_');
 const alphaMode=mat?.alphaMode==='BLEND'||mat?.alphaMode==='MASK';
 const normals=this.smoothNormals(po,ii);this.shapes.push(this.makeShape(po,normals,colors,ii,idx++,uv,tex,photo,alphaMode));}}
'''
assert search in s,'GLB loader passage not found'
s=s.replace(search,replace)
# each draw uniform and photo alpha
s=s.replace('const finish=kind===', 'const finish=kind===')
search='''g.uniform1f(this.u.uSurface,finish);const c=hexRGB(this.options.color);'''
replace='''g.uniform1f(this.u.uSurface,finish);
 g.uniform1f(this.u.uHasMap,s.texture?1:0);g.uniform1f(this.u.uPhoto,s.photo?1:0);
 g.activeTexture(g.TEXTURE0);g.bindTexture(g.TEXTURE_2D,s.texture);g.uniform1i(this.u.uMap,0);
 const c=hexRGB(this.options.color);'''
assert search in s
s=s.replace(search,replace)
s=s.replace('if(alpha<1){g.enable(g.BLEND)', 'if(alpha<1||s.hasAlpha){g.enable(g.BLEND)')
s=s.replace('g.uniform1f(this.u.uSurface,.35);g.bindVertexArray(this.overlay.vao);', '''g.uniform1f(this.u.uSurface,.35);g.uniform1f(this.u.uHasMap,0);g.uniform1f(this.u.uPhoto,0);g.bindTexture(g.TEXTURE_2D,null);g.bindVertexArray(this.overlay.vao);''')
s=s.replace('this.shapes.forEach(s=>this.disposeShape(s));if(this.overlay)', 'this.shapes.forEach(s=>this.disposeShape(s));this.textures.forEach(t=>this.gl!.deleteTexture(t));if(this.overlay)')
p.write_text(s)
print('patched TypeScript renderer',len(s))
