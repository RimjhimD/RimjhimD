from common import *
import textpath as T
def meme_text(txt,y,maxw=264,size=34):
    while T.width('meme',txt,size,1)>maxw: size-=1
    d=T.path('meme',txt,size,150,y,'middle',ls=1)
    return f'<path d="{d}" fill="#fff" stroke="#000" stroke-width="{max(3,size/8):.1f}" stroke-linejoin="round" paint-order="stroke"/>'
def cat(cx,base,eye='#F5D547'):
    return f'''
<g class="tail"><path d="M{cx+40} {base-12} C{cx+95} {base-10} {cx+104} {base-60} {cx+86} {base-96} C{cx+78} {base-112} {cx+90} {base-126} {cx+104} {base-120}" stroke="#050305" stroke-width="13" fill="none" stroke-linecap="round"/></g>
<path d="M{cx} {base-150} C{cx-42} {base-150} {cx-56} {base-80} {cx-50} {base-34} C{cx-46} {base-6} {cx-26} {base} {cx} {base} C{cx+26} {base} {cx+46} {base-6} {cx+50} {base-34} C{cx+56} {base-80} {cx+42} {base-150} {cx} {base-150}Z" fill="#050305" stroke="#C21F3A" stroke-opacity=".5" stroke-width="1.5"/>
<ellipse cx="{cx-22}" cy="{base-4}" rx="15" ry="8" fill="#050305"/><ellipse cx="{cx+22}" cy="{base-4}" rx="15" ry="8" fill="#050305"/>
<g class="head">
  <path class="earL" d="M{cx-44} {base-172} L{cx-40} {base-226} L{cx-8} {base-196}Z" fill="#050305" stroke="#C21F3A" stroke-opacity=".5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M{cx-38} {base-180} L{cx-36} {base-212} L{cx-16} {base-194}Z" fill="#3A1520"/>
  <path class="earR" d="M{cx+44} {base-172} L{cx+40} {base-226} L{cx+8} {base-196}Z" fill="#050305" stroke="#C21F3A" stroke-opacity=".5" stroke-width="1.5" stroke-linejoin="round"/>
  <path d="M{cx+38} {base-180} L{cx+36} {base-212} L{cx+16} {base-194}Z" fill="#3A1520"/>
  <ellipse cx="{cx}" cy="{base-170}" rx="50" ry="42" fill="#050305" stroke="#C21F3A" stroke-opacity=".5" stroke-width="1.5"/>
  <g class="eyes">
    <ellipse cx="{cx-20}" cy="{base-176}" rx="12" ry="14" fill="{eye}"/><ellipse cx="{cx+20}" cy="{base-176}" rx="12" ry="14" fill="{eye}"/>
    <ellipse class="pupil" cx="{cx-20}" cy="{base-176}" rx="3" ry="11" fill="#050305"/><ellipse class="pupil" cx="{cx+20}" cy="{base-176}" rx="3" ry="11" fill="#050305"/>
    <circle cx="{cx-16}" cy="{base-182}" r="2.5" fill="#fff"/><circle cx="{cx+24}" cy="{base-182}" r="2.5" fill="#fff"/>
  </g>
  <path d="M{cx-4} {base-158} H{cx+4} L{cx} {base-153}Z" fill="#E88AAA"/>
  <path d="M{cx-8} {base-148} Q{cx-4} {base-144} {cx} {base-150} Q{cx+4} {base-144} {cx+8} {base-148}" stroke="#6A5A62" stroke-width="1.5" fill="none"/>
  <g stroke="#6A5A62" stroke-width="1.2"><path d="M{cx-24} {base-156} L{cx-62} {base-162} M{cx-24} {base-152} L{cx-62} {base-150}"/><path d="M{cx+24} {base-156} L{cx+62} {base-162} M{cx+24} {base-152} L{cx+62} {base-150}"/></g>
</g>'''
CAT_CSS='''
  .tail { transform-origin: 190px 348px; animation: tail 2.8s ease-in-out infinite; } @keyframes tail { 50% { transform: rotate(-14deg); } }
  .eyes { transform-box: fill-box; transform-origin: center; animation: blink 4.5s infinite; } @keyframes blink { 0%,92%,100% { transform: scaleY(1); } 95% { transform: scaleY(.08); } }
  .earL { transform-box: fill-box; transform-origin: 50% 100%; animation: ear 6s infinite; } @keyframes ear { 0%,80%,100% { transform: rotate(0); } 83% { transform: rotate(-12deg); } 86% { transform: rotate(0); } }
  .head { transform-origin: 150px 200px; animation: tilt 9s ease-in-out infinite; } @keyframes tilt { 0%,40%,100% { transform: rotate(0); } 50%,80% { transform: rotate(-7deg); } }
'''
# ---------- meme cat ----------
W,H=300,420
M=[("I'M FINE","(I AM NOT FINE)"),("404","MOTIVATION NOT FOUND"),("IT WORKS","ON MY MACHINE"),("SLEEP?","NEVER HEARD OF HER"),("ME AFTER","ONE BUG FIX")]
SL=4.5; TOT=SL*len(M); caps=''
for i,(a,b) in enumerate(M):
    s0=i/len(M)*100; e=(i+1)/len(M)*100
    caps+=f'<style>@keyframes m{i} {{ 0%,100% {{ opacity: 0; }} {s0:.1f}% {{ opacity: 0; }} {s0+1:.1f}% {{ opacity: 1; }} {e-1:.1f}% {{ opacity: 1; }} {e:.1f}% {{ opacity: 0; }} }}</style><g opacity="0" style="animation: m{i} {TOT}s steps(1) infinite">{meme_text(a,62,size=40)}{meme_text(b,398,size=30)}</g>'
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Black cat meme with rotating captions: I'm fine, 404 motivation not found, it works on my machine, sleep never heard of her">
<title>cat.exe</title>
<defs><style>{CAT_CSS}{fall_css(H+40)} {RM}</style>
<clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath>
<radialGradient id="win" cx=".5" cy=".4" r=".6"><stop offset="0" stop-color="#3A1624"/><stop offset="1" stop-color="#0C0609"/></radialGradient></defs>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="#0C0609"/>
  <path d="M62 300 V150 A88 88 0 0 1 238 150 V300Z" fill="url(#win)"/>
  <circle cx="196" cy="140" r="24" fill="#C21F3A" opacity=".75"/>
  <path d="M150 64 V300 M62 230 H238" stroke="#050305" stroke-width="4" opacity="0"/>
  <path d="M150 68 V300" stroke="#1E0E14" stroke-width="6"/>
  <circle cx="150" cy="112" r="16" fill="none" stroke="#1E0E14" stroke-width="5"/>
  <path d="M62 300 V150 A88 88 0 0 1 238 150 V300" fill="none" stroke="#1E0E14" stroke-width="10"/>
  <g>{petals(7,W,H,seed=31,scale=(.6,.9))}</g>
  <rect y="348" width="{W}" height="72" fill="#070406"/>
  {cat(150,350)}
  {caps}
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="#C21F3A" stroke-opacity=".35" stroke-width="2"/>
</svg>'''
open(OUT+'cat-meme.svg','w').write(svg); print('meme',len(svg))
# ---------- rain cat ----------
W,H=300,420
import random
R=random.Random(5); drops=''
for i in range(16):
    x=R.uniform(90,220); d=R.uniform(.7,1.1)
    drops+=f'<line x1="{x:.0f}" y1="92" x2="{x-3:.0f}" y2="104" stroke="#8FB3D9" stroke-width="2" stroke-linecap="round" style="animation: drop {d:.2f}s linear {-R.uniform(0,1):.2f}s infinite"/>'
line1=T.path('italic','no thoughts.',30,150,356,'middle'); line2=T.path('italic','just loaf.',30,150,390,'middle')
svg=f'''<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" viewBox="0 0 {W} {H}" role="img" aria-label="Sad black cat loafing in a box under its own small rain cloud: no thoughts, just loaf">
<title>no thoughts, just loaf</title>
<defs><style>
  .cloud {{ animation: bob 3s ease-in-out infinite; }} @keyframes bob {{ 50% {{ transform: translateY(-5px); }} }}
  @keyframes drop {{ from {{ transform: translateY(0); opacity: .9; }} to {{ transform: translateY(120px); opacity: 0; }} }}
  .eyesz {{ transform-box: fill-box; transform-origin: center; animation: sleepy 5s ease-in-out infinite; }} @keyframes sleepy {{ 0%,100% {{ transform: scaleY(1); }} 50% {{ transform: scaleY(.35); }} }}
  .z {{ animation: z 3.6s ease-out infinite; opacity: 0; }} .z.b {{ animation-delay: 1.2s; }} .z.c {{ animation-delay: 2.4s; }}
  @keyframes z {{ 0% {{ opacity: 0; transform: translate(0,0); }} 20% {{ opacity: 1; }} 100% {{ opacity: 0; transform: translate(26px,-40px); }} }}
  .bolt {{ animation: bolt 7s steps(1) infinite; opacity: 0; }} @keyframes bolt {{ 0%,88%,92%,100% {{ opacity: 0; }} 89%,91% {{ opacity: 1; }} }}
  {RM}
</style><clipPath id="c"><rect width="{W}" height="{H}" rx="14"/></clipPath></defs>
<g clip-path="url(#c)">
  <rect width="{W}" height="{H}" fill="#0C0609"/>
  <g transform="translate(0 20)"><g>{drops}</g>
  <g class="cloud" fill="#2E2833"><circle cx="120" cy="72" r="26"/><circle cx="155" cy="58" r="34"/><circle cx="192" cy="74" r="24"/><rect x="96" y="70" width="118" height="26" rx="13"/>
    <path class="bolt" d="M160 96 L150 116 H160 L152 136 L172 110 H162 L170 96Z" fill="#F5D547"/></g>
  <g transform="translate(0 -22)"><!-- loaf -->
  <path d="M86 210 C86 168 214 168 214 210Z" fill="#050305" stroke="#C21F3A" stroke-opacity=".45"/>
  <path d="M96 186 L100 150 L124 172Z M204 186 L200 150 L176 172Z" fill="#050305" stroke="#C21F3A" stroke-opacity=".45" stroke-linejoin="round"/>
  <path d="M104 178 L106 160 L118 172Z M196 178 L194 160 L182 172Z" fill="#3A1520"/>
  <g class="eyesz"><path d="M124 190 Q132 196 140 190 M160 190 Q168 196 176 190" stroke="#F5D547" stroke-width="3" fill="none" stroke-linecap="round"/></g>
  <path d="M147 200 H153 L150 204Z" fill="#E88AAA"/>
  <path d="M138 214 C140 206 132 204 132 212" stroke="#8FB3D9" stroke-width="0" fill="none"/>
  <circle cx="186" cy="200" r="3" fill="#8FB3D9" opacity=".8"><animate attributeName="cy" values="198;214;214" keyTimes="0;.8;1" dur="3s" repeatCount="indefinite"/><animate attributeName="opacity" values="0;.9;0" keyTimes="0;.2;1" dur="3s" repeatCount="indefinite"/></circle>
  </g>
  <!-- box -->
  <path d="M70 206 H230 L220 290 H80Z" fill="#3B2418"/><path d="M70 206 H230 L240 196 H60Z" fill="#4E3020"/>
  <path d="M70 206 L50 232 L82 236Z M230 206 L250 232 L218 236Z" fill="#2E1B12"/>
  <path d="M120 250 h60" stroke="#2A170F" stroke-width="3"/><path d="M128 262 h44" stroke="#2A170F" stroke-width="2"/>
  <g fill="#C9B7BF" font-family="Georgia, serif" font-style="italic"><text class="z" x="214" y="170" font-size="14">z</text><text class="z b" x="220" y="160" font-size="18">z</text><text class="z c" x="228" y="150" font-size="22">z</text></g>
  </g>
  <path d="{line1}" fill="#EFE6EA"/><path d="{line2}" fill="#C21F3A"/>
</g>
<rect x="1" y="1" width="{W-2}" height="{H-2}" rx="14" fill="none" stroke="#C21F3A" stroke-opacity=".35" stroke-width="2"/>
</svg>'''
open(OUT+'cat-rain.svg','w').write(svg); print('rain',len(svg))
