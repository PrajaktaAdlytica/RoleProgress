from pathlib import Path
from io import BytesIO
from fontTools.ttLib import TTFont
from fontTools.varLib.instancer import instantiateVariableFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.boundsPen import BoundsPen
import uharfbuzz as hb
out=Path('public/brand');out.mkdir(exist_ok=True)
font=TTFont('node_modules/@fontsource-variable/newsreader/files/newsreader-latin-wght-normal.woff2')
font=instantiateVariableFont(font,{'wght':550},inplace=False);font.flavor=None
buf=BytesIO();font.save(buf);hf=hb.Font(hb.Face(buf.getvalue()));b=hb.Buffer();b.add_str('RoleProgress');b.guess_segment_properties();hb.shape(hf,b,{'kern':True})
gs=font.getGlyphSet();order=font.getGlyphOrder();parts=[];x=0;bounds=[]
for g,pos in zip(b.glyph_infos,b.glyph_positions):
 name=order[g.codepoint];pen=SVGPathPen(gs);gs[name].draw(pen);bp=BoundsPen(gs);gs[name].draw(bp)
 if bp.bounds:bounds.append((bp.bounds[0]+x+pos.x_offset,bp.bounds[1]+pos.y_offset,bp.bounds[2]+x+pos.x_offset,bp.bounds[3]+pos.y_offset))
 parts.append(f'<path transform="translate({x+pos.x_offset} {pos.y_offset})" d="{pen.getCommands()}"/>');x+=pos.x_advance
xmin=min(a[0] for a in bounds);ymin=min(a[1] for a in bounds);xmax=max(a[2] for a in bounds);ymax=max(a[3] for a in bounds)
w=xmax-xmin;h=ymax-ymin
word='<g transform="translate('+str(-xmin)+' '+str(ymax)+') scale(1 -1)">'+''.join(parts)+'</g>'
leafs=['M192 0C165 25 87 40 86 100C84 142 121 160 132 297C140 222 155 197 175 175C200 150 192 111 192 0Z','M0 130C67 153 105 189 122 360C92 307 42 290 7 253C0 246 0 239 0 232Z','M250 166C173 194 158 223 140 354C170 312 215 287 243 258C251 247 250 233 250 166Z']
symbol=''.join(f'<path d="{d}"/>' for d in leafs)
micro=symbol.replace('132 297','132 270').replace('122 360','114 350').replace('140 354','149 348')
def svg(name,width,height,content):
 (out/name).write_text(f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {width} {height}" role="img" aria-labelledby="title"><title id="title">RoleProgress — Progress Folio</title>{content}</svg>')
for name,color in [('copper','#95543c'),('ink','#29212c'),('white','#ffffff')]:
 svg(f'symbol-{name}.svg',282,392,f'<g transform="translate(16 16)" fill="{color}">{symbol}</g>')
 svg(f'wordmark-{name}.svg',round(w,2),round(h,2),f'<g fill="{color}">{word}</g>')
scale=142/h;ww=w*scale
for name,sc,wc in [('primary','#95543c','#29212c'),('ink','#29212c','#29212c'),('copper','#95543c','#95543c'),('white','#ffffff','#ffffff')]:
 svg(f'logo-horizontal-{name}.svg',round(180+ww+8,2),212,f'<g transform="translate(8 8) scale(.54)" fill="{sc}">{symbol}</g><g transform="translate(180 36) scale({scale})" fill="{wc}">{word}</g>')
 svg(f'logo-stacked-{name}.svg',round(ww+40,2),480,f'<g transform="translate({(ww+40-175)/2} 20) scale(.7)" fill="{sc}">{symbol}</g><g transform="translate(20 318) scale({scale})" fill="{wc}">{word}</g>')
svg('favicon.svg',64,64,f'<rect width="64" height="64" rx="14" fill="#95543c"/><g transform="translate(15 7) scale(.135)" fill="#fff">{micro}</g>')
svg('app-icon.svg',512,512,f'<rect width="512" height="512" rx="108" fill="#95543c"/><g transform="translate(121 56) scale(1.08)" fill="#fff">{symbol}</g>')
print('Created',len(list(out.glob('*.svg'))),'outlined SVG assets')
