from common import *
import textpath as T
# ---------- sakura divider (like hexdiv) ----------
W,H=900,40
fl=''
for i,x in enumerate(range(-84,85,28)):
    r=7 if i!=3 else 9
    petals_=''.join(f'<ellipse cx="0" cy="{-r*0.6:.1f}" rx="{r*0.4:.1f}" ry="{r*0.6:.1f}" transform="rotate({a})"/>' for a in range(0,360,72))
    fl+=f'<g class="p" style="animation-delay:{i*0.18:.2f}s" transform="translate({450+x} 20)">{petals_}</g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="sakura divider">
<style>
 .p {{ fill:#3A0A12; animation: pulse 3.4s ease-in-out infinite; }}
 @keyframes pulse {{ 0%,100% {{ fill:#2A070D; opacity:.35; }} 50% {{ fill:#C21F3A; opacity:.9; }} }}
 #l {{ animation: sweep 3.4s ease-in-out infinite; }} @keyframes sweep {{ 0%,100% {{ opacity:.06; }} 50% {{ opacity:.22; }} }}
 @media (prefers-reduced-motion: reduce) {{ * {{ animation:none !important; }} }}
</style>
<line id="l" x1="20" y1="20" x2="880" y2="20" stroke="#C21F3A" stroke-width="1"/>
{fl}
</svg>'''
open(OUT+'sakura-divider.svg','w').write(svg)
# ---------- quotes as one thin cycling line ----------
W,H=900,48
Q=[("Mine has been a life of much shame.","Osamu Dazai"),
   ("Hiding places there are innumerable, escape is only one…","Franz Kafka"),
   ("Now I have neither happiness nor unhappiness. Everything passes.","Osamu Dazai"),
   ("A cage went in search of a bird.","Franz Kafka")]
N=len(Q); DUR=5*N; body=''
for i,(q,a) in enumerate(Q):
    size=20; A='  —  '+a
    while T.width('italic',q,size)+T.width('italic',A,size)>W-40: size-=1
    wq=T.width('italic',q,size); wa=T.width('italic',A,size); x0=(W-wq-wa)/2; y=30
    body+=f'<g class="l" style="animation-delay:{i*5}s"><path d="{T.path("italic",q,size,x0,y)}" fill="#8E7A84"/><path d="{T.path("italic",A,size,x0+wq,y)}" fill="#C21F3A"/></g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="Mine has been a life of much shame — Osamu Dazai; Hiding places there are innumerable, escape is only one — Franz Kafka; Now I have neither happiness nor unhappiness. Everything passes — Osamu Dazai; A cage went in search of a bird — Franz Kafka">
<style>
 .l {{ opacity:0; animation: cyc {DUR}s infinite; }}
 @keyframes cyc {{ 0% {{ opacity:0; }} 3% {{ opacity:1; }} 22% {{ opacity:1; }} 25% {{ opacity:0; }} 100% {{ opacity:0; }} }}
 @media (prefers-reduced-motion: reduce) {{ .l {{ animation:none; }} .l:first-child {{ opacity:1; }} }}
</style>
{body}
</svg>'''
open(OUT+'quote-line.svg','w').write(svg)
print('ok')
