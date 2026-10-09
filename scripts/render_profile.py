"""Render the profile's original artwork. Requires Pillow; no network requests."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import math
import os

ASSETS = Path(__file__).resolve().parents[1] / 'assets'
ASSETS.mkdir(exist_ok=True)
REGULAR = os.environ.get('PROFILE_FONT', '/System/Library/Fonts/Supplemental/Arial.ttf')
BOLD = os.environ.get('PROFILE_BOLD_FONT', '/System/Library/Fonts/Supplemental/Arial Bold.ttf')
BG = '#0b1220'
MINT = '#77e6c0'
BLUE = '#79b8ff'
VIOLET = '#bdabff'

def font(size, bold=False):
    return ImageFont.truetype(BOLD if bold else REGULAR, size)

def hero(phase):
    im = Image.new('RGB', (1280, 440), BG)
    d = ImageDraw.Draw(im)
    for x in range(0, 1280, 40):
        for y in range(0, 440, 40):
            d.ellipse((x, y, x+1, y+1), fill='#1e2c3e')
    d.rounded_rectangle((26, 26, 1253, 413), radius=24, outline='#28384e', width=2)
    d.rounded_rectangle((64, 58, 119, 113), radius=12, fill=MINT)
    d.text((75, 73), 'ZT', font=font(26, True), fill=BG)
    d.text((138, 73), 'JELLY / BUILDER & RESEARCHER', font=font(19, True), fill=MINT)
    d.text((61, 143), 'Zhechen Tu', font=font(76, True), fill='#f5f8ff')
    d.text((64, 244), 'AI systems. Real-world impact.', font=font(34), fill='#d8e4f5')
    d.text((64, 304), 'Clinical AI  /  Agents  /  Distributed inference', font=font(23), fill='#a5b7ce')
    d.text((64, 365), 'UW–MADISON  ·  COMPUTER SCIENCE ’27', font=font(17, True), fill='#8fa6c1')
    nodes = [(825, 110), (1010, 70), (1174, 170), (1070, 310), (842, 319), (985, 214)]
    edges = [(0,1),(1,2),(2,3),(3,4),(4,0),(0,5),(1,5),(2,5),(3,5),(4,5)]
    for j,(a,b) in enumerate(edges):
        ax,ay=nodes[a]; bx,by=nodes[b]
        d.line((ax,ay,bx,by), fill='#2e435d', width=2)
        t=(phase+j*.137)%1
        px,py=ax+(bx-ax)*t,ay+(by-ay)*t
        color=[MINT,BLUE,VIOLET][j%3]
        d.ellipse((px-4,py-4,px+4,py+4), fill=color)
    for i,(x,y) in enumerate(nodes):
        color=[MINT,BLUE,VIOLET][i%3]
        r=28 if i==5 else 18
        halo=r+8+int(3*math.sin(phase*math.tau+i))
        d.ellipse((x-halo,y-halo,x+halo,y+halo),outline='#2e435d',width=1)
        d.ellipse((x-r,y-r,x+r,y+r),fill='#142337',outline=color,width=2)
        d.ellipse((x-4,y-4,x+4,y+4),fill=color)
    d.text((862, 374),'IDEAS → SYSTEMS → EVIDENCE',font=font(16,True),fill='#8fa6c1')
    return im

frames=[hero(i/72) for i in range(72)]
frames[0].save(ASSETS/'hero.png')
# One shared palette prevents color flicker and keeps the animation compact.
palette=frames[0].quantize(colors=96)
indexed=[frame.quantize(palette=palette,dither=Image.Dither.NONE) for frame in frames]
indexed[0].save(ASSETS/'hero.gif',save_all=True,append_images=indexed[1:],duration=90,loop=0,optimize=True)

def svg(name, title, eyebrow, color, art):
    (ASSETS/name).write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="640" height="200" viewBox="0 0 640 200" role="img" aria-label="{title}">
<rect width="640" height="200" rx="16" fill="{BG}"/>
<rect x="1" y="1" width="638" height="198" rx="16" fill="none" stroke="#28384e"/>
<path d="M28 34h36" stroke="{color}" stroke-width="4"/>
<text x="28" y="66" fill="{color}" font-family="Arial,sans-serif" font-size="13" font-weight="700" letter-spacing="2">{eyebrow}</text>
<text x="28" y="115" fill="#f5f8ff" font-family="Arial,sans-serif" font-size="34" font-weight="700">{title}</text>
{art}</svg>''')

svg('buzzer.svg','Buzzer','REAL-TIME / FULL STACK',BLUE,'''
<g fill="#142337" stroke="#79b8ff" stroke-width="2">
<rect x="467" y="40" width="135" height="86" rx="10"/>
<rect x="456" y="100" width="42" height="72" rx="7"/><rect x="555" y="100" width="42" height="72" rx="7"/></g>
<path d="M520 142h23m-12-10v20" stroke="#79b8ff" stroke-width="2"/>
<text x="28" y="157" fill="#a5b7ce" font-family="Arial,sans-serif" font-size="18">One room. Every player connected.</text>''')
svg('agent.svg','Local Azure Agent','AGENTS / RETRIEVAL / EVALUATION',MINT,'''
<g fill="#142337" stroke="#77e6c0" stroke-width="2">
<rect x="473" y="48" width="98" height="36" rx="8"/>
<rect x="473" y="116" width="98" height="36" rx="8"/></g>
<path d="M521 85v28m-5-6 5 6 5-6M573 65h24v70h-24" fill="none" stroke="#77e6c0" stroke-width="2"/>
<text x="28" y="157" fill="#a5b7ce" font-family="Arial,sans-serif" font-size="18">Retrieve. Act. Cite the evidence.</text>''')
svg('finance.svg','Financial Asset QA','APPLIED AI / RAG',VIOLET,'''
<path d="M466 143h134M475 150V50" stroke="#344963" stroke-width="2"/>
<path d="m481 128 22-17 20 7 23-43 22 9 26-32" fill="none" stroke="#bdabff" stroke-width="4"/>
<circle cx="594" cy="52" r="6" fill="#bdabff"/>
<text x="28" y="157" fill="#a5b7ce" font-family="Arial,sans-serif" font-size="18">Live data meets grounded answers.</text>''')
svg('terruto.svg','Terruto','GAME SYSTEMS / PIXEL ART','#ffbe7a','''
<g fill="#ffbe7a"><path d="M521 45h16v16h16v16h16v16h16v16h-16v16h-16v16h-16v16h-16v-16h-16v-16h-16v-16h-16V93h16V77h16V61h16z"/>
<rect x="517" y="89" width="24" height="24" fill="#0b1220"/></g>
<text x="28" y="157" fill="#a5b7ce" font-family="Arial,sans-serif" font-size="18">Naruto adventures, built for Terraria.</text>''')

for name,label,color,width in [('website','↗  PERSONAL WEBSITE',MINT,240),('linkedin','↗  LINKEDIN',BLUE,166),('email','↗  LET’S TALK',VIOLET,180)]:
    (ASSETS/f'{name}.svg').write_text(f'''<svg xmlns="http://www.w3.org/2000/svg" width="{width}" height="44" role="img" aria-label="{label}"><rect x="1" y="1" width="{width-2}" height="42" rx="8" fill="{BG}" stroke="#344963"/><text x="{width/2}" y="28" text-anchor="middle" fill="{color}" font-family="Arial,sans-serif" font-size="14" font-weight="700" letter-spacing="1">{label}</text></svg>''')
print(f'Rendered {len(list(ASSETS.iterdir()))} assets in {ASSETS}')

(ASSETS/'heteromesh.svg').write_text('''<svg xmlns="http://www.w3.org/2000/svg" width="1280" height="250" viewBox="0 0 1280 250" role="img" aria-label="HeteroMesh: target topology connecting Windows, macOS, and iPhone">
<rect width="1280" height="250" rx="20" fill="#0b1220"/>
<rect x="1" y="1" width="1278" height="248" rx="20" fill="none" stroke="#28384e"/>
<text x="42" y="55" fill="#77e6c0" font-family="Arial,sans-serif" font-size="18" font-weight="700" letter-spacing="3">CURRENT EXPLORATION / DISTRIBUTED AI</text>
<text x="40" y="134" fill="#f5f8ff" font-family="Arial,sans-serif" font-size="66" font-weight="700">HeteroMesh</text>
<text x="42" y="193" fill="#a5b7ce" font-family="Arial,sans-serif" font-size="26">Many devices. One inference pipeline.</text>
<path d="M796 111h58m136 0h58" stroke="#344963" stroke-width="3"/>
<g fill="#142337" stroke-width="2"><rect x="654" y="62" width="140" height="98" rx="12" stroke="#79b8ff"/><rect x="852" y="62" width="140" height="98" rx="12" stroke="#77e6c0"/><rect x="1050" y="62" width="140" height="98" rx="12" stroke="#bdabff"/></g>
<g fill="#d8e4f5" font-family="Arial,sans-serif" font-size="24" text-anchor="middle"><text x="724" y="119">Windows</text><text x="922" y="119">macOS</text><text x="1120" y="119">iPhone</text></g>
<circle cx="824" cy="111" r="5" fill="#79b8ff"/><circle cx="1020" cy="111" r="5" fill="#77e6c0"/>
<text x="922" y="205" text-anchor="middle" fill="#8fa6c1" font-family="Arial,sans-serif" font-size="18" letter-spacing="2">TARGET TOPOLOGY · IN DEVELOPMENT</text>
</svg>''')
