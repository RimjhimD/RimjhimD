import random, math
import os
OUT=os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))),'assets')+os.sep
PETAL='M0 0 C3 -7 11 -7 12 -1 C12 2 10 3 8 2 C9 5 5 7 2 5 C0 4 -1 2 0 0Z'
def flower(x,y,r,rot=0,col='#F2A7BF',core='#8E1B3A',op=1):
    ps=''.join(f'<ellipse cx="0" cy="{-r*0.62:.1f}" rx="{r*0.42:.1f}" ry="{r*0.62:.1f}" transform="rotate({a})"/>' for a in range(0,360,72))
    return f'<g transform="translate({x:.1f} {y:.1f}) rotate({rot})" opacity="{op}"><g fill="{col}">{ps}</g><circle r="{r*0.22:.1f}" fill="{core}"/></g>'
FALL_CSS='''
    .pf { transform-box: fill-box; }
    @keyframes fallA { from { transform: translate(0,-40px); } to { transform: translate(-260px, VAR_H); } }
    @keyframes fallB { from { transform: translate(0,-40px); } to { transform: translate(-140px, VAR_H); } }
    @keyframes fallC { from { transform: translate(0,-40px); } to { transform: translate(-360px, VAR_H); } }
    @keyframes snow  { from { transform: translate(0,-20px); } to { transform: translate(-60px, VAR_H); } }
    @keyframes sway  { 0%,100% { transform: translateX(-10px); } 50% { transform: translateX(12px); } }
    @keyframes tumble{ 0% { transform: rotate(0) scaleX(1); } 50% { transform: rotate(200deg) scaleX(-.4); } 100% { transform: rotate(360deg) scaleX(1); } }
    .tb { transform-box: fill-box; transform-origin: center; }
'''
def fall_css(h): return FALL_CSS.replace('VAR_H', f'{h}px')
def petals(n, W, H, seed=1, xmin=None, xmax=None, cols=('#F2A7BF','#E88AAA','#F7C6D5','#D9708F'), scale=(0.7,1.3)):
    R=random.Random(seed); out=[]
    for i in range(n):
        x=R.uniform(xmin if xmin is not None else 0, xmax if xmax is not None else W+300)
        dur=R.uniform(9,18); delay=-R.uniform(0,dur); kind=R.choice('ABC'); s=R.uniform(*scale)
        out.append(f'<g transform="translate({x:.0f} 0)"><g style="animation: fall{kind} {dur:.1f}s linear {delay:.1f}s infinite"><g style="animation: sway {R.uniform(2.5,5):.1f}s ease-in-out {-R.uniform(0,4):.1f}s infinite"><path class="tb" d="{PETAL}" fill="{R.choice(cols)}" opacity="{R.uniform(.6,.95):.2f}" transform="scale({s:.2f})" style="animation: tumble {R.uniform(3,7):.1f}s linear infinite"/></g></g></g>')
    return ''.join(out)
def snow(n, W, H, seed=2):
    R=random.Random(seed); out=[]
    for i in range(n):
        x=R.uniform(0,W+60); dur=R.uniform(8,20); delay=-R.uniform(0,dur); r=R.uniform(.7,2.3)
        out.append(f'<g transform="translate({x:.0f} 0)"><g style="animation: snow {dur:.1f}s linear {delay:.1f}s infinite"><g style="animation: sway {R.uniform(3,6):.1f}s ease-in-out {-R.uniform(0,5):.1f}s infinite"><circle r="{r:.1f}" fill="#F4EEF2" opacity="{R.uniform(.35,.85):.2f}"/></g></g></g>')
    return ''.join(out)
def stars(n,W,H,seed=3):
    R=random.Random(seed)
    return ''.join(f'<circle class="tw" style="animation-delay:{-R.uniform(0,4):.1f}s;animation-duration:{R.uniform(2.5,5):.1f}s" cx="{R.uniform(0,W):.0f}" cy="{R.uniform(0,H):.0f}" r="{R.uniform(.5,1.4):.1f}" fill="#fff" opacity="{R.uniform(.3,.9):.2f}"/>' for _ in range(n))
RM='@media (prefers-reduced-motion: reduce) { * { animation: none !important; } }'
