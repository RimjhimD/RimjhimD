from fontTools.ttLib import TTFont
from fontTools.pens.svgPathPen import SVGPathPen
from fontTools.pens.transformPen import TransformPen
import os
F=os.path.join(os.path.dirname(os.path.abspath(__file__)),'fonts')
_cache={}
FONTS={
 'goth':(os.path.join(F,'UnifrakturMaguntia-Book.ttf'),None),
 'serif':(os.path.join(F,'Cormorant-SemiBold.ttf'),None),
 'italic':(os.path.join(F,'Cormorant-MediumItalic.ttf'),None),
 'jp':('/usr/share/fonts/opentype/noto/NotoSerifCJK-Bold.ttc',0),
 'meme':(os.path.join(F,'Anton-Regular.ttf'),None),
 'jpl':('/usr/share/fonts/opentype/noto/NotoSerifCJK-Regular.ttc',0),
}
def font(k):
    if k not in _cache:
        p,n=FONTS[k]; f=TTFont(p,fontNumber=n) if n is not None else TTFont(p)
        _cache[k]=(f,f.getGlyphSet(),f.getBestCmap(),f['hmtx'],f['head'].unitsPerEm)
    return _cache[k]
def width(k,text,size,ls=0):
    f,gs,cmap,hmtx,upm=font(k); s=size/upm
    return sum(hmtx[cmap.get(ord(ch),'.notdef')][0]*s+ls for ch in text)-ls
def path(k,text,size,x,y,anchor='start',ls=0,vertical=False):
    """Return SVG path d for text. vertical: stack chars top-down, x = center."""
    f,gs,cmap,hmtx,upm=font(k); s=size/upm
    pen=SVGPathPen(gs, ntos=lambda v: ('%.1f' % v).rstrip('0').rstrip('.'))
    if vertical:
        cy=y
        for ch in text:
            g=cmap.get(ord(ch),'.notdef'); adv=hmtx[g][0]*s
            gs[g].draw(TransformPen(pen,(s,0,0,-s,x-adv/2,cy+size*0.88)))
            cy+=size+ls
        return pen.getCommands()
    w=width(k,text,size,ls)
    cx=x-(w if anchor=='end' else w/2 if anchor=='middle' else 0)
    for ch in text:
        g=cmap.get(ord(ch),'.notdef')
        gs[g].draw(TransformPen(pen,(s,0,0,-s,cx,y)))
        cx+=hmtx[g][0]*s+ls
    return pen.getCommands()
