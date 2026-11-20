"""Create original conceptual SVGs for PP anodizing tank construction guides."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

STYLE = '''<style>
text{font-family:Arial,sans-serif;fill:#17324a}.title{font-size:23px;font-weight:bold}.label{font-size:15px}.small{font-size:12px}.tank{fill:#f5f8fa;stroke:#264a62;stroke-width:5}.liquid{fill:#d7eef5}.pp{fill:#81b6c9;stroke:#285970;stroke-width:3}.steel{fill:#aeb9c2;stroke:#455865;stroke-width:3}.liner{fill:#4f9bb2;stroke:#1e5668;stroke-width:3}.warn{fill:#fff0e6;stroke:#af6333;stroke-width:2}.joint{fill:#eaa85a;stroke:#76541b;stroke-width:2}.arrow{stroke:#3d657b;stroke-width:2;marker-end:url(#arrow)}
</style><defs><marker id="arrow" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0 0 L10 4 L0 8z" fill="#3d657b"/></marker></defs>'''

DESIGNS = [
 ('01-shop-welded-rectangular','Shop welded rectangular PP tank','Flat PP-H sheet panels cut, prepared, welded and reinforced in a controlled workshop.','shop'),
 ('02-site-assembled-panels','Site assembled welded panels','Oversize panels or subassemblies joined at the installation site by qualified thermoplastic welders.','site'),
 ('03-pp-liner-in-structural-shell','PP liner in a structural shell','A supported PP wetted liner inside a separate steel or concrete load-bearing shell.','liner'),
 ('04-double-wall-containment','Double wall PP containment','A primary process vessel surrounded by a secondary containment wall or bund.','double'),
 ('05-ribbed-self-supporting-tank','Ribbed self supporting PP tank','A welded PP tank with calculated external PP ribs or structural framing to control flat-wall deflection.','ribs'),
 ('06-circular-tank','Circular welded PP vessel','A cylindrical welded vessel option, generally more relevant to storage or compact processes than long anodizing work.','round'),
 ('07-molded-or-stock-tank','Molded or stock PP vessel','A standard or molded vessel used only where dimensions, geometry, temperature, and duty fit the anodizing process.','stock'),
]

def tank_svg(title, flavor):
    title_txt=f'<text class="title" x="35" y="40">{title}</text>'
    tank='''<path class="tank" d="M190 170 L190 455 L790 455 L790 170"/><path class="liquid" d="M198 258 L782 258 L782 447 L198 447z"/><line x1="198" y1="258" x2="782" y2="258" stroke="#347c93" stroke-width="3"/>'''
    interior='''<rect class="pp" x="250" y="180" width="18" height="240"/><rect class="pp" x="712" y="180" width="18" height="240"/><rect x="463" y="208" width="74" height="200" fill="#bdcbd4" stroke="#496779" stroke-width="3"/><line x1="500" y1="178" x2="500" y2="208" stroke="#496779" stroke-width="4"/><rect class="pp" x="225" y="153" width="550" height="22"/>'''
    if flavor=='round':
        tank='''<ellipse class="tank" cx="490" cy="186" rx="320" ry="58"/><path class="tank" d="M170 186 L170 432 C170 464 810 464 810 432 L810 186"/><path class="liquid" d="M180 258 L800 258 L800 431 C800 450 180 450 180 431z"/><ellipse cx="490" cy="258" rx="310" ry="36" fill="#d7eef5" stroke="#347c93" stroke-width="3"/>'''
        interior='''<rect class="pp" x="250" y="194" width="18" height="225"/><rect class="pp" x="712" y="194" width="18" height="225"/><rect x="463" y="210" width="74" height="205" fill="#bdcbd4" stroke="#496779" stroke-width="3"/><line x1="500" y1="182" x2="500" y2="210" stroke="#496779" stroke-width="4"/><rect class="pp" x="225" y="153" width="550" height="22"/>'''
    extra=''
    notes={'shop':'Shop fabrication supports controlled fit-up, weld procedure, and inspection before delivery.',
           'site':'Plan panel access, seam sequence, weather control, weld access, and site inspection.',
           'liner':'The outer shell carries load; the PP liner must be supported against liquid pressure and movement.',
           'double':'Interspace requires a defined leak detection, drainage, and inspection plan.',
           'ribs':'Rib size and spacing are calculated; do not copy a visual pattern as a structural design.',
           'round':'Round geometry changes rack layout and current distribution; verify long-part handling.',
           'stock':'Stock-vessel material and ratings must match chemical, temperature, immersion, and dimensions.'}[flavor]
    if flavor=='shop':
        extra='''<rect class="pp" x="155" y="198" width="30" height="220"/><rect class="pp" x="795" y="198" width="30" height="220"/><text class="small" x="80" y="510">Exterior welded stiffening ribs, sized by design</text>'''
    elif flavor=='site':
        extra='''<line x1="390" y1="171" x2="390" y2="452" stroke="#e18c3d" stroke-width="5" stroke-dasharray="8 5"/><line x1="590" y1="171" x2="590" y2="452" stroke="#e18c3d" stroke-width="5" stroke-dasharray="8 5"/><text class="small" x="370" y="490">Field seams require controlled fit-up and qualified welding</text>'''
    elif flavor=='liner':
        extra='''<path class="steel" d="M145 130 L145 492 L835 492 L835 130" fill="none"/><path class="liner" d="M190 170 L190 455 L790 455 L790 170" fill="none"/><text class="small" x="160" y="520">Independent shell supports liner; detail anchors and thermal movement</text>'''
    elif flavor=='double':
        extra='''<path d="M155 145 L155 490 L825 490 L825 145" fill="none" stroke="#4f9bb2" stroke-width="7"/><path d="M170 145 L170 490 M810 145 L810 490" fill="none" stroke="#4f9bb2" stroke-width="4" stroke-dasharray="8 6"/><circle cx="174" cy="466" r="9" fill="#d88033"/><text class="small" x="175" y="520">Leak detection point and accessible interspace</text>'''
    elif flavor=='ribs':
        extra='''<rect class="pp" x="153" y="190" width="30" height="28"/><rect class="pp" x="153" y="260" width="30" height="28"/><rect class="pp" x="153" y="330" width="30" height="28"/><rect class="pp" x="153" y="400" width="30" height="28"/><rect class="pp" x="797" y="190" width="30" height="28"/><rect class="pp" x="797" y="260" width="30" height="28"/><rect class="pp" x="797" y="330" width="30" height="28"/><rect class="pp" x="797" y="400" width="30" height="28"/><text class="small" x="280" y="510">Rib reinforcement shown schematically</text>'''
    elif flavor=='round':
        extra='''<text class="small" x="225" y="510">Plan and rack layout differ from rectangular line tank</text>'''
    elif flavor=='stock':
        extra='''<rect class="warn" x="635" y="90" width="250" height="48" rx="7"/><text class="small" x="650" y="120">Verify duty and rating</text><line class="arrow" x1="730" y1="140" x2="755" y2="180"/>'''
    labels='''<text class="label" x="235" y="234">PP cathode</text><text class="label" x="436" y="305">Work / rack</text><text class="label" x="628" y="246">Bath level</text>'''
    bottom=f'<text class="small" x="50" y="570">{notes}</text><text class="small" x="50" y="598">Conceptual view only - not to scale or for fabrication.</text>'
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="630" viewBox="0 0 1000 630">{STYLE}{title_txt}{tank}{interior}{extra}{labels}{bottom}</svg>'

WELDS=[
 ('01-extrusion-welding','Extrusion welding','A prepared joint is filled with compatible molten PP extrudate while hot gas preheats the joint.','extrusion'),
 ('02-hot-gas-welding','Hot gas welding','A heated gas stream softens prepared edges and a compatible filler rod forms the weld bead.','hotgas'),
 ('03-heated-tool-butt-welding','Heated tool butt welding','Prepared panel edges are heated on a controlled tool, brought together under the qualified procedure, and held through cooling.','butt'),
]

def weld_svg(title, flavor):
    if flavor=='extrusion':
        picture='''<rect class="pp" x="320" y="140" width="130" height="300"/><rect class="pp" x="450" y="310" width="300" height="130"/><path class="joint" d="M440 295 Q485 260 525 300 Q505 332 455 330z"/><path class="arrow" d="M655 170 L510 282" fill="none"/><text class="label" x="660" y="160">Extrudate bead</text><text class="label" x="235" y="475">Prepared joint and compatible feedstock</text>'''
    elif flavor=='hotgas':
        picture='''<rect class="pp" x="300" y="145" width="145" height="300"/><rect class="pp" x="445" y="310" width="320" height="135"/><path class="joint" d="M438 295 L468 274 L496 300 L470 330 L445 325z"/><path d="M205 290 Q260 265 320 290" fill="none" stroke="#e77838" stroke-width="8"/><path class="arrow" d="M315 285 L418 300" fill="none"/><text class="label" x="155" y="250">Hot gas</text><text class="label" x="520" y="280">Filler rod / bead</text>'''
    else:
        picture='''<rect class="pp" x="235" y="160" width="240" height="260"/><rect class="pp" x="525" y="160" width="240" height="260"/><rect class="joint" x="480" y="250" width="40" height="80"/><path class="arrow" d="M420 220 L475 220" fill="none"/><path class="arrow" d="M580 220 L525 220" fill="none"/><text class="label" x="420" y="470">Heated tool removed before join-up</text>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="560" viewBox="0 0 1000 560">{STYLE}<text class="title" x="35" y="40">{title}</text>{picture}<text class="small" x="50" y="525">Joint illustration only. Actual weld prep, parameters, and inspection follow qualified procedures and current codes.</text></svg>'

for folder,title,_,flavor in DESIGNS:
    (ROOT/'pp-tank'/'construction-methods'/folder/'construction.svg').write_text(tank_svg(title,flavor),encoding='utf-8')
for folder,title,_,flavor in WELDS:
    (ROOT/'pp-tank'/'welding-methods'/folder/'weld-concept.svg').write_text(weld_svg(title,flavor),encoding='utf-8')
