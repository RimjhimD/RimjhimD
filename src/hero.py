import random, math
from common import *
import textpath as T
W,H=1200,500
R=random.Random(7)
name=T.path('goth','Rimjhim Dey',118,80,290)
role=T.path('serif','ML ENGINEER   ·   FULL-STACK   ·   N8N AUTOMATION',18,86,310,ls=3)
# sakura branch (filled tapered polygons approximated with strokes)
branch='''
<g class="branch" fill="none" stroke="#2A0E17" stroke-linecap="round">
  <path d="M-20 40 C60 30 110 70 190 58 C250 50 290 80 360 72" stroke-width="16"/>
  <path d="M190 58 C220 90 230 120 280 138" stroke-width="7"/>
  <path d="M360 72 C400 66 430 90 470 84" stroke-width="6"/>
  <path d="M110 52 C130 20 160 10 200 -5" stroke-width="6"/>
  <path d="M280 138 C300 150 320 150 340 168" stroke-width="3.5"/>
  <path d="M300 76 C320 100 350 106 370 128" stroke-width="3.5"/>
  <path d="M470 84 C500 80 520 96 540 100" stroke-width="3"/>
  <path d="M60 40 C70 70 60 90 80 110" stroke-width="4"/>
</g>'''
blos=''
for (x,y,sp,n) in [(200,40,40,10),(280,130,26,6),(350,72,36,9),(470,84,34,8),(540,100,20,5),(80,100,22,5),(200,-2,30,7),(340,160,20,4),(370,125,22,5),(130,48,30,7)]:
    for _ in range(n):
        blos+=flower(x+R.uniform(-sp,sp), y+R.uniform(-sp*.6,sp*.6), R.uniform(5,9.5), R.uniform(0,72), R.choice(['#F2A7BF','#E88AAA','#F7C6D5']), op=R.uniform(.75,1))
# samurai silhouette, feet at (0,0)
samurai='''
<g class="cape"><path fill="#030103" d="M-18 -104 C10 -100 40 -90 58 -72 C70 -60 84 -58 96 -62 C84 -48 66 -46 52 -52 C40 -40 26 -34 14 -38 Z">
  <animate attributeName="d" dur="3.2s" repeatCount="indefinite" values="M-18 -104 C10 -100 40 -90 58 -72 C70 -60 84 -58 96 -62 C84 -48 66 -46 52 -52 C40 -40 26 -34 14 -38 Z;M-18 -104 C12 -104 46 -98 66 -84 C80 -76 96 -78 108 -86 C98 -68 78 -62 62 -64 C46 -50 28 -40 14 -38 Z;M-18 -104 C10 -100 40 -90 58 -72 C70 -60 84 -58 96 -62 C84 -48 66 -46 52 -52 C40 -40 26 -34 14 -38 Z"/></path></g>
<g fill="#030103">
  <path d="M-46 -132 C-20 -142 -8 -160 0 -164 C8 -160 20 -142 46 -132 C30 -128 -30 -128 -46 -132Z"/>
  <path d="M-9 -131 H9 V-114 H-9Z"/>
  <path d="M-30 -114 C-12 -120 12 -120 30 -114 L25 -72 H-25Z"/>
  <path d="M-25 -76 H25 L40 0 H8 L3 -34 H-3 L-8 0 H-40Z"/>
  <path d="M-30 -112 C-38 -96 -40 -84 -34 -74 L-26 -74 C-30 -86 -26 -98 -22 -106Z"/>
  <path d="M-4 -84 L-78 -52 L-76 -47 L-2 -78Z"/>
  <path d="M-4 -84 L34 -100 L36 -96 L-2 -79Z"/>
  <ellipse cx="-4" cy="-81" rx="3" ry="7" transform="rotate(-24 -4 -81)"/>
</g>
<path d="M-46 -132 C-20 -142 -8 -160 0 -164 C8 -160 20 -142 46 -132" fill="none" stroke="#C21F3A" stroke-opacity=".45" stroke-width="1.2"/>
<path d="M30 -114 L25 -72 L40 0" fill="none" stroke="#C21F3A" stroke-opacity=".35" stroke-width="1.2"/>
'''
crows=''
for i,(y,dur,delay,s) in enumerate([(70,34,-4,1),(98,40,-18,.8),(56,46,-30,.65)]):
    crows+=f'<g transform="translate(0 {y})"><g style="animation: crow {dur}s linear {delay}s infinite"><g transform="scale({s})"><path class="flap" style="animation-delay:{-i*.2}s" d="M-16 0 Q-8 -8 0 0 Q8 -8 16 0 Q8 -3 0 3 Q-8 -3 -16 0Z" fill="#050204"/></g></g></g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Rimjhim Dey, ML engineer, full-stack and n8n automation — a samurai stands under a blood moon while sakura petals and snow fall">
<title>Rimjhim Dey</title>
<defs>
<style>{fall_css(H+60)}
  .tw {{ animation: tw 3s ease-in-out infinite; }} @keyframes tw {{ 50% {{ opacity: .1; }} }}
  .moonglow {{ transform-box: fill-box; transform-origin: center; animation: mg 6s ease-in-out infinite; }} @keyframes mg {{ 50% {{ transform: scale(1.08); opacity: .55; }} }}
  .cloud {{ animation: cloud 70s linear infinite; }} .cloud.c2 {{ animation-duration: 95s; animation-delay: -40s; }}
  @keyframes cloud {{ from {{ transform: translateX(-700px); }} to {{ transform: translateX(1300px); }} }}
  .fog {{ animation: fog 26s ease-in-out infinite alternate; }} .fog.f2 {{ animation-duration: 34s; animation-direction: alternate-reverse; }}
  @keyframes fog {{ to {{ transform: translateX(-160px); }} }}
  .branch, .blos {{ transform-origin: -20px 40px; animation: bsway 7s ease-in-out infinite; }}
  @keyframes bsway {{ 50% {{ transform: rotate(1.4deg); }} }}
  @keyframes crow {{ from {{ transform: translateX(1300px); }} to {{ transform: translateX(-100px); }} }}
  .flap {{ transform-box: fill-box; transform-origin: center; animation: flap .7s ease-in-out infinite; }} @keyframes flap {{ 50% {{ transform: scaleY(-.6); }} }}
  .flash {{ animation: flash 13s linear infinite; }} @keyframes flash {{ 0%,91%,100% {{ opacity: 0; }} 92% {{ opacity: .14; }} 93% {{ opacity: 0; }} 94.5% {{ opacity: .08; }} 96% {{ opacity: 0; }} }}
  .gleam {{ animation: gleam 5s ease-in-out infinite; }} @keyframes gleam {{ 0% {{ transform: translateX(-120px); }} 60%,100% {{ transform: translateX(660px); }} }}
  .flick {{ animation: flick 4s steps(1) infinite; }} @keyframes flick {{ 0%,100% {{ opacity: 1; }} 71% {{ opacity: .82; }} 72% {{ opacity: 1; }} 88% {{ opacity: .9; }} }}
  .rise {{ animation: rise 1.6s cubic-bezier(.22,1,.36,1) both; }} .rise.d1 {{ animation-delay: .3s; }} .rise.d2 {{ animation-delay: .6s; }}
  @keyframes rise {{ from {{ opacity: 0; transform: translateY(14px); }} }}
  {RM}
</style>
<clipPath id="card"><rect width="{W}" height="{H}" rx="18"/></clipPath>
<linearGradient id="sky" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#030205"/><stop offset=".55" stop-color="#0E0509"/><stop offset=".8" stop-color="#2A0810"/><stop offset="1" stop-color="#12040A"/></linearGradient>
<radialGradient id="moon" cx=".42" cy=".38" r=".7"><stop offset="0" stop-color="#FF6B7E"/><stop offset=".45" stop-color="#C21F3A"/><stop offset="1" stop-color="#5A0614"/></radialGradient>
<radialGradient id="glow"><stop offset="0" stop-color="#C21F3A" stop-opacity=".55"/><stop offset="1" stop-color="#C21F3A" stop-opacity="0"/></radialGradient>
<linearGradient id="title" x1="0" y1="0" x2="0" y2="1"><stop offset="0" stop-color="#F4EEF2"/><stop offset=".55" stop-color="#D9C9D0"/><stop offset="1" stop-color="#C21F3A"/></linearGradient>
<linearGradient id="gl" x1="0" x2="1"><stop offset="0" stop-color="#fff" stop-opacity="0"/><stop offset=".5" stop-color="#fff" stop-opacity=".9"/><stop offset="1" stop-color="#fff" stop-opacity="0"/></linearGradient>
<filter id="blur8"><feGaussianBlur stdDeviation="8"/></filter>
<filter id="blur20" x="-50%" y="-100%" width="200%" height="300%"><feGaussianBlur stdDeviation="20"/></filter>
<filter id="tglow" x="-10%" y="-30%" width="120%" height="160%"><feGaussianBlur in="SourceAlpha" stdDeviation="6" result="b"/><feFlood flood-color="#C21F3A" flood-opacity=".6"/><feComposite in2="b" operator="in"/><feMerge><feMergeNode/><feMergeNode in="SourceGraphic"/></feMerge></filter>
<filter id="grain"><feTurbulence type="fractalNoise" baseFrequency=".85" numOctaves="2" stitchTiles="stitch"/><feColorMatrix values="0 0 0 0 1 0 0 0 0 1 0 0 0 0 1 0 0 0 .6 0"/></filter>
<mask id="gleamMask"><rect x="80" y="326" width="566" height="4" fill="#fff"/></mask>
</defs>
<g clip-path="url(#card)">
  <rect width="{W}" height="{H}" fill="url(#sky)"/>
  <g>{stars(70,W,300)}</g>
  <circle class="moonglow" cx="850" cy="215" r="250" fill="url(#glow)"/>
  <circle cx="850" cy="215" r="128" fill="url(#moon)"/>
  <g fill="#000" opacity=".16"><circle cx="810" cy="180" r="22"/><circle cx="890" cy="250" r="30"/><circle cx="880" cy="160" r="12"/><circle cx="800" cy="260" r="14"/></g>
  <g class="cloud"><ellipse cx="700" cy="190" rx="260" ry="10" fill="#0A0307" opacity=".85" filter="url(#blur8)"/><ellipse cx="820" cy="212" rx="160" ry="6" fill="#0A0307" opacity=".7" filter="url(#blur8)"/></g>
  <g class="cloud c2"><ellipse cx="600" cy="120" rx="220" ry="9" fill="#12050A" opacity=".8" filter="url(#blur8)"/></g>
  <rect class="flash" width="{W}" height="{H}" fill="#FF8FA3"/>
  <g transform="translate(0 {H-60})">{crows}</g>
  <!-- far mountains -->
  <path d="M0 360 L140 330 L250 300 L330 248 L372 236 L410 250 L500 300 L620 330 L760 342 L900 322 L1040 336 L1200 318 V500 H0Z" fill="#1F0810"/>
  <path d="M330 248 L372 236 L410 250 L392 256 L378 250 L364 258 L350 252Z" fill="#E9DDE3" opacity=".22"/>
  <!-- torii -->
  <g fill="#0B0307" transform="translate(610 334)">
    <path d="M-34 -40 C-10 -44 10 -44 34 -40 L36 -45 C10 -50 -10 -50 -36 -45Z"/><rect x="-28" y="-36" width="56" height="3"/>
    <rect x="-22" y="-40" width="4" height="40"/><rect x="18" y="-40" width="4" height="40"/><rect x="-2" y="-36" width="4" height="4"/>
  </g>
  <path d="M0 400 C120 380 260 372 380 386 C520 400 600 372 720 380 L1200 390 V500 H0Z" fill="#0B0306"/>
  <g class="fog"><ellipse cx="400" cy="400" rx="520" ry="26" fill="#3A1420" opacity=".35" filter="url(#blur20)"/></g>
  <!-- cliff + samurai -->
  <path d="M700 500 L716 430 C740 410 770 398 800 394 L1200 382 V500Z" fill="#040103"/>
  <path d="M716 430 C740 410 770 398 800 394 L1200 382" fill="none" stroke="#C21F3A" stroke-opacity=".25"/>
  <g transform="translate(900 394) scale(1.08)">{samurai}</g>
  <g class="fog f2"><ellipse cx="900" cy="470" rx="600" ry="30" fill="#2A0C16" opacity=".45" filter="url(#blur20)"/></g>
  <!-- title -->
  <g class="rise"><path d="{name}" fill="url(#title)" filter="url(#tglow)" class="flick"/></g>
  <!-- sakura branch top-left -->
  {branch}
  <g class="blos">{blos}</g>
  <g>{petals(46,W,H,seed=11)}</g>
  <g>{snow(90,W,H)}</g>
  <rect width="{W}" height="{H}" filter="url(#grain)" opacity=".05"/>
</g>
<rect x=".5" y=".5" width="{W-1}" height="{H-1}" rx="18" fill="none" stroke="#C21F3A" stroke-opacity=".25"/>
</svg>'''
open(OUT+'hero.svg','w').write(svg); print('hero', len(svg))
