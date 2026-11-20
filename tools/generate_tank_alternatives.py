"""Generate original conceptual visuals for anodizing-tank material alternatives."""
from pathlib import Path
from textwrap import wrap
from html import escape

ROOT=Path(__file__).resolve().parents[1]
OPTIONS=[
('01-pvdf-tank','PVDF fabricated tank','PVDF','PVDF sheet','PVDF has higher chemical/temperature capability in some duties, with higher material and fabrication cost. Verify actual bath and process specification.','#9471ad',''),
('02-cpvc-pvc-tank','CPVC or PVC fabricated tank','CPVC / PVC','Welded thermoplastic sheet','Consider only within the exact resin grade, temperature, concentration, and service rating supplied by the tank maker.','#6389b0',''),
('03-hdpe-tank','HDPE fabricated tank','HDPE','Welded thermoplastic sheet','Often considered for cold/ambient duty; confirm compatibility and temperature limits for the exact anodizing bath.','#458c79',''),
('04-dual-laminate-pp-frp','PP and FRP dual laminate tank','PP wetted liner + FRP structure','Liner protects; FRP carries calculated load','Useful where a reinforced composite shell is desired. Liner, shell, bond/interface, seams, and penetrations must be designed as one system.','#4d91a5','dual'),
('05-frp-chemical-barrier','FRP tank with designed resin barrier','FRP corrosion barrier','Resin system / veil selected for service','FRP is not a generic acid-proof material. Resin, barrier thickness, cure, fabrication, and chemical duty require specialist approval.','#b28b57',''),
('06-lined-steel-or-concrete','Structural steel or concrete shell with liner','PP / PVC / rubber lining','Outer shell supports','A liner isolates the process liquid from the structure. Detail backing, thermal movement, seams, penetrations, leak detection, and inspection access.','#687985','lined'),
('07-stainless-steel-tank','Stainless steel process tank','316L or specified stainless','Bare metal only if approved','Specialty alternative requiring corrosion, contamination, temperature, and process approval. Do not presume stainless steel is compatible with sulfuric anodizing service.','#8b969e','')
]

def make_svg(title, material, build, caution, color, mode):
    shell=f'<path d="M220 160 L220 430 L780 430 L780 160" fill="none" stroke="{color}" stroke-width="22" stroke-linejoin="round"/>'
    if mode=='dual':
        shell='<path d="M220 160 L220 430 L780 430 L780 160" fill="none" stroke="#658a91" stroke-width="28" stroke-linejoin="round"/><path d="M233 169 L233 416 L767 416 L767 169" fill="none" stroke="#4d91a5" stroke-width="8" stroke-linejoin="round"/>'
    elif mode=='lined':
        shell='<path d="M195 135 L195 455 L805 455 L805 135" fill="none" stroke="#687985" stroke-width="36" stroke-linejoin="round"/><path d="M224 157 L224 427 L776 427 L776 157" fill="none" stroke="#4d91a5" stroke-width="8" stroke-linejoin="round"/>'
    fill_color=color if mode=='' else '#4d91a5'
    caution_lines=''.join(f'<tspan x="74" dy="0">{escape(line)}</tspan>' if i==0 else f'<tspan x="74" dy="16">{escape(line)}</tspan>' for i,line in enumerate(wrap(caution,width=112)))
    content=f'''<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="640" viewBox="0 0 1000 640">
<style>text{{font-family:Arial,sans-serif;fill:#17324a}}.title{{font-size:24px;font-weight:bold}}.label{{font-size:16px}}.small{{font-size:13px}}.bath{{fill:#d8edf4;opacity:.95}}.work{{fill:#aebec8;stroke:#536b7b;stroke-width:3}}.bus{{fill:#d99a34;stroke:#755019;stroke-width:3}}</style>
<text class="title" x="40" y="45">{title}</text>
<path d="M220 160 L220 430 L780 430 L780 160" fill="#f7fafb" stroke="#254b62" stroke-width="4"/>
<path class="bath" d="M228 250 L772 250 L772 422 L228 422z"/><line x1="228" y1="250" x2="772" y2="250" stroke="#347c93" stroke-width="3"/>
{shell}
<rect class="bus" x="280" y="144" width="440" height="17"/><rect class="bus" x="290" y="160" width="16" height="235"/><rect class="bus" x="694" y="160" width="16" height="235"/>
<rect class="work" x="465" y="196" width="70" height="192"/><line x1="500" y1="161" x2="500" y2="196" stroke="#536b7b" stroke-width="4"/>
<text class="label" x="260" y="220">Cathode</text><text class="label" x="460" y="417">Work rack</text><text class="label" x="610" y="239">Electrolyte level</text>
<text class="label" x="60" y="490">Candidate material: {material}</text><text class="label" x="60" y="520">Construction: {build}</text>
<rect x="60" y="540" width="880" height="58" rx="5" fill="#fff2e8" stroke="#ac673b" stroke-width="1.5"/><text class="small" x="74" y="558">{caution_lines}</text>
<text class="small" x="60" y="625">Conceptual comparison visual - not to scale, not a fabrication drawing, and not proof of chemical compatibility.</text>
</svg>'''
    return content

for folder,title,material,build,caution,color,mode in OPTIONS:
    d=ROOT/'pp-tank'/'alternatives'/folder
    (d/'alternative.svg').write_text(make_svg(title,material,build,caution,color,mode),encoding='utf-8')
