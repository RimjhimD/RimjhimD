from common import *
import textpath as T
W,H=900,54
L=[("I build ","machine-learning pipelines."),
   ("I work in ","AI, deep learning and data."),
   ("I automate ","business workflows with n8n."),
   ("I ship ","REST backends that stay up.")]
N=len(L); SL=3.5; DUR=SL*N; body=''
for i,(a,b) in enumerate(L):
    size=28
    wa=T.width('italic',a,size); wb=T.width('italic',b,size); x0=(W-wa-wb)/2; y=36
    body+=f'<g class="l" style="animation-delay:{i*SL}s"><path d="{T.path("italic",a,size,x0,y)}" fill="#E0344F"/><path d="{T.path("italic",b,size,x0+wa,y)}" fill="#D9C9D0"/></g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {W} {H}" width="{W}" height="{H}" role="img" aria-label="I build machine-learning pipelines. I work in AI, deep learning and data. I automate business workflows with n8n. I ship REST backends that stay up.">
<style>
 .l {{ opacity:0; animation: cyc {DUR}s infinite; }}
 @keyframes cyc {{ 0% {{ opacity:0; transform:translateY(6px); }} 4% {{ opacity:1; transform:none; }} 22% {{ opacity:1; transform:none; }} 25% {{ opacity:0; transform:translateY(-4px); }} 100% {{ opacity:0; }} }}
 @media (prefers-reduced-motion: reduce) {{ .l {{ animation:none; }} .l:first-of-type {{ opacity:1; }} }}
</style>
{body}
</svg>'''
open(OUT+'i-build-line.svg','w').write(svg); print('ok')
