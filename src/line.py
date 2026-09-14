from common import *
import textpath as T
W,H=900,50
WORDS=["MACHINE LEARNING","AI","N8N WORKFLOWS","AUTOMATION"]
FS=22; LS=3; SEP=40
ws=[T.width('serif',w,FS,LS) for w in WORDS]
total=sum(ws)+SEP*(len(WORDS)-1)
while total>W-60:
    FS-=1; ws=[T.width('serif',w,FS,LS) for w in WORDS]; total=sum(ws)+SEP*(len(WORDS)-1)
x=(W-total)/2; y=H/2+FS*0.34; parts=''; css=''
for i,(w,wd) in enumerate(zip(WORDS,ws)):
    d=T.path('serif',w,FS,x,y,ls=LS)
    css+=f".w{i} {{ animation: up 1s cubic-bezier(.22,1,.36,1) {0.2+i*0.35:.2f}s both; }}\n"
    parts+=f'<g class="w{i}"><path d="{d}" fill="url(#red)"/></g>'
    x+=wd
    if i<len(WORDS)-1:
        cx=x+SEP/2
        parts+=f'<g class="w{i}"><path d="M{cx} {H/2-5} L{cx+5} {H/2} L{cx} {H/2+5} L{cx-5} {H/2}Z" fill="#F2A7BF" opacity=".8"/></g>'
        x+=SEP
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Machine Learning · AI · n8n Workflows · Automation">
<title>Machine Learning · AI · n8n Workflows · Automation</title>
<defs>
<linearGradient id="red" gradientUnits="userSpaceOnUse" x1="-400" y1="0" x2="0" y2="0">
  <stop offset="0" stop-color="#E0344F"/><stop offset=".45" stop-color="#E0344F"/><stop offset=".5" stop-color="#FFB3C4"/><stop offset=".55" stop-color="#E0344F"/><stop offset="1" stop-color="#E0344F"/>
  <animateTransform attributeName="gradientTransform" type="translate" values="0 0;1400 0;1400 0" keyTimes="0;.6;1" dur="6s" begin="1.8s" repeatCount="indefinite"/>
</linearGradient>
<style>
{css}@keyframes up {{ from {{ opacity: 0; transform: translateY(10px); }} to {{ opacity: 1; transform: none; }} }}
@media (prefers-reduced-motion: reduce) {{ * {{ animation: none !important; }} }}
</style></defs>
{parts}
</svg>'''
open(OUT+'keywords-line.svg','w').write(svg); print('line',len(svg),FS)
