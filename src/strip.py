import re
from common import *
import textpath as T
import cats as C   # regenerates cat-meme.svg / cat-rain.svg as a side effect
meme=open(OUT+'cat-meme.svg').read(); rain=open(OUT+'cat-rain.svg').read()
def inner(svg):
    g=svg[svg.index('<g clip-path="url(#c)">')+len('<g clip-path="url(#c)">'):svg.rindex('</g>')]
    return g
# meme: drop background rect and caption groups (captions re-laid out in the middle)
m=inner(meme)
m=m.replace('<rect width="300" height="420" fill="#0C0609"/>','',1)
m=re.sub(r'<style>@keyframes m\d.*?</style><g opacity="0" style="animation: m\d[^"]*">.*?</g>(?=<style>|\s*$)','',m,flags=re.S)
r=inner(rain).replace('<rect width="300" height="420" fill="#0C0609"/>','',1)
meme_style=re.search(r'<defs><style>(.*?)</style>',meme,re.S).group(1)
rain_style=re.search(r'<defs><style>(.*?)</style>',rain,re.S).group(1)
W,H=900,250; S=.58
def cap(txt,y,size,maxw=330):
    while T.width('meme',txt,size,1)>maxw: size-=1
    return f'<path d="{T.path("meme",txt,size,W/2,y,"middle",ls=1)}" fill="#fff" stroke="#000" stroke-width="{max(3,size/8):.1f}" stroke-linejoin="round" paint-order="stroke"/>'
SL=4.5; TOT=SL*len(C.M); caps=''
for i,(a,b) in enumerate(C.M):
    s0=i/len(C.M)*100; e=(i+1)/len(C.M)*100
    caps+=f'<style>@keyframes s{i} {{ 0%,100% {{ opacity:0; transform:translateY(6px); }} {s0:.1f}% {{ opacity:0; transform:translateY(6px); }} {s0+2:.1f}% {{ opacity:1; transform:none; }} {e-2:.1f}% {{ opacity:1; transform:none; }} {e:.1f}% {{ opacity:0; }} }}</style><g opacity="0" style="animation: s{i} {TOT}s infinite">{cap(a,112,52)}{cap(b,166,32)}</g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Two black cats: one with rotating meme captions (I'm fine, 404 motivation not found, it works on my machine), one loafing in a box under a rain cloud">
<title>mood</title>
<defs><style>{meme_style}
{rain_style.replace('@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }','')}</style>
<radialGradient id="win" cx=".5" cy=".4" r=".6"><stop offset="0" stop-color="#3A1624"/><stop offset="1" stop-color="#0C0609"/></radialGradient>
<clipPath id="card"><rect width="{W}" height="{H}" rx="16"/></clipPath>
<clipPath id="lc"><rect width="300" height="420"/></clipPath></defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="#0C0609"/>
  <rect y="{H-44}" width="{W}" height="44" fill="#070406"/>
  <g transform="translate(46 {H-420*S+2}) scale({S})"><g clip-path="url(#lc)">{m}</g></g>
  <g transform="translate({W-300*S-46} {H-420*S+2}) scale({S})"><g clip-path="url(#lc)">{r}</g></g>
  {caps}
  <path d="{T.path('italic','— mood, currently —',17,W/2,214,'middle')}" fill="#8E7A84"/>
</g>
</svg>'''
open(OUT+'cats-strip.svg','w').write(svg); print('strip',len(svg))

import os
for f in ('cat-meme.svg','cat-rain.svg'): os.remove(OUT+f)   # intermediates from cats.py
