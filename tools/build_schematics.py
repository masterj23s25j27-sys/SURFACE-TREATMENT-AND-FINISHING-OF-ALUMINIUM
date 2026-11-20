"""Generate original conceptual SVGs used in this repository's construction guides."""
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
METHODS = [
    ('01-top-suspended', 'Top suspended rim support', 'Tank rim saddles carry a removable header; plates hang into the bath.', 'rim'),
    ('02-independent-frame', 'Independent external frame', 'A separate structure carries the header and cathodes without loading the PP rim.', 'external'),
    ('03-integrated-bus-supports', 'Tank integrated bus supports', 'Purpose designed reinforced seats carry insulated bus bars at the tank rim.', 'integrated'),
    ('04-polymer-cleats', 'Polymer cleats and slots', 'Acid compatible polymer guides retain plate edges; a top retainer prevents lift.', 'cleats'),
    ('05-cross-tank-frame', 'Cross tank suspended frame', 'A removable bridge frame supports suspended cathodes and clears rack handling.', 'bridge'),
    ('06-wall-penetrating', 'Engineered wall penetration', 'A sealed reinforced penetration is shown for comparison; avoid as a retrofit default.', 'penetration'),
]

def svg(title, desc, flavor):
    common='''<style>text{font-family:Arial,sans-serif;fill:#17324a}.label{font-size:15px}.small{font-size:12px}.title{font-size:22px;font-weight:bold}.tank{fill:#f5f8fa;stroke:#263f54;stroke-width:4}.liquid{fill:#d8edf4;stroke:none}.metal{fill:#d89b32;stroke:#76541b;stroke-width:3}.work{fill:#90a9bc;stroke:#38566e;stroke-width:3}.support{fill:#486b80;stroke:#263f54;stroke-width:3}.ins{fill:#e8dff2;stroke:#765a8e;stroke-width:2}.danger{fill:#f9e0dd;stroke:#a23b30;stroke-width:2}.muted{fill:#617789}.arrow{stroke:#405f76;stroke-width:2;marker-end:url(#a)}</style>
<defs><marker id="a" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#405f76"/></marker></defs>'''
    tank='''<rect class="tank" x="150" y="160" width="680" height="390" rx="5"/><rect class="liquid" x="158" y="250" width="664" height="292"/><line x1="158" y1="250" x2="822" y2="250" stroke="#3888a2" stroke-width="3"/>'''
    supports={
      'rim':'<rect class="ins" x="205" y="137" width="70" height="28"/><rect class="ins" x="705" y="137" width="70" height="28"/>',
      'external':'<rect class="support" x="95" y="120" width="35" height="470"/><rect class="support" x="850" y="120" width="35" height="470"/><rect class="support" x="95" y="120" width="790" height="25"/>',
      'integrated':'<rect class="support" x="180" y="126" width="110" height="35"/><rect class="support" x="690" y="126" width="110" height="35"/><rect class="ins" x="205" y="150" width="70" height="17"/><rect class="ins" x="705" y="150" width="70" height="17"/>',
      'cleats':'<rect class="ins" x="182" y="300" width="34" height="100"/><rect class="ins" x="764" y="300" width="34" height="100"/><rect class="ins" x="182" y="165" width="34" height="45"/><rect class="ins" x="764" y="165" width="34" height="45"/>',
      'bridge':'<rect class="ins" x="205" y="130" width="70" height="25"/><rect class="ins" x="705" y="130" width="70" height="25"/><rect class="support" x="128" y="115" width="724" height="24"/>',
      'penetration':'<rect class="ins" x="132" y="310" width="32" height="90"/>'
    }[flavor]
    header='<rect class="metal" x="215" y="164" width="560" height="25"/><rect class="metal" x="228" y="187" width="25" height="300"/><rect class="metal" x="737" y="187" width="25" height="300"/>'
    work='<line x1="475" y1="184" x2="475" y2="474" stroke="#263f54" stroke-width="5"/><rect class="work" x="420" y="225" width="42" height="210"/><rect class="work" x="489" y="225" width="42" height="210"/>'
    extra=''
    if flavor=='external': extra='<text class="small" x="54" y="610">Independent frame carries assembly load</text>'
    if flavor=='integrated': extra='<text class="small" x="170" y="610">Reinforcement and bus seats specified with tank fabricator</text>'
    if flavor=='cleats': extra='<rect class="ins" x="210" y="190" width="38" height="20"/><rect class="ins" x="738" y="190" width="38" height="20"/><text class="small" x="174" y="610">Guides and top retainers must not obstruct rack travel</text>'
    if flavor=='bridge': extra='<text class="small" x="235" y="610">Check hoist and rack clearance before fixing dimensions</text>'
    if flavor=='penetration': extra='<circle class="danger" cx="153" cy="350" r="18"/><text class="small" x="160" y="610" fill="#a23b30">Requires engineered reinforcement, seal, and electrical isolation</text>'
    labels='''<text class="title" x="45" y="42">'''+title+'''</text><text class="label" x="180" y="105">Header / negative bus</text><text class="label" x="235" y="515">Cathode plates</text><text class="label" x="410" y="485">Work rack and parts</text><text class="label" x="670" y="233">Electrolyte level</text><text class="small muted" x="390" y="572">Conceptual front view - not to scale; dimensions require site engineering</text>'''
    return f'<svg xmlns="http://www.w3.org/2000/svg" width="1000" height="660" viewBox="0 0 1000 660">{common}{supports}{tank}{header}{work}{labels}{extra}</svg>'

for folder,title,desc,flavor in METHODS:
    out=ROOT/'cathode-plate'/'methods'/folder/'construction.svg'
    out.write_text(svg(title,desc,flavor),encoding='utf-8')

def flow_svg(title, stages, subtitle):
    parts=['<svg xmlns="http://www.w3.org/2000/svg" width="1100" height="350" viewBox="0 0 1100 350"><style>text{font-family:Arial,sans-serif;fill:#17324a}.title{font-size:22px;font-weight:bold}.box{fill:#eef5f8;stroke:#35627c;stroke-width:2}.warn{fill:#fff0e5;stroke:#ad6734;stroke-width:2}.label{font-size:14px}.arrow{stroke:#405f76;stroke-width:3;marker-end:url(#a)}</style><defs><marker id="a" markerWidth="10" markerHeight="8" refX="9" refY="4" orient="auto"><path d="M0,0 L10,4 L0,8 z" fill="#405f76"/></marker></defs>']
    parts.append(f'<text class="title" x="35" y="38">{title}</text>')
    n=len(stages); gap=22; w=(1030-(n-1)*gap)/n; y=118; h=92
    for i,(name,detail) in enumerate(stages):
        x=35+i*(w+gap); cl='warn' if 'sludge' in name.lower() or 'concentrate' in name.lower() else 'box'
        parts.append(f'<rect class="{cl}" x="{x}" y="{y}" width="{w}" height="{h}" rx="8"/><text class="label" text-anchor="middle" x="{x+w/2}" y="{y+32}">{name}</text><text class="label" text-anchor="middle" x="{x+w/2}" y="{y+58}">{detail}</text>')
        if i<n-1: parts.append(f'<line class="arrow" x1="{x+w+3}" y1="{y+h/2}" x2="{x+w+gap-4}" y2="{y+h/2}"/>')
    parts.append(f'<text class="label" x="35" y="275">{subtitle}</text><text class="label" x="35" y="310">Conceptual flow only. Confirm with lab data, local discharge limits, and qualified process design.</text></svg>')
    return ''.join(parts)

flows=[
 ('conventional-precipitation','conventional-treatment.svg',[('Segregate flows','acid / alkali'),('Equalize','measure pH, metals'),('Neutralize','precipitate Al'),('Flocculate','condition solids'),('Clarify','settle solids'),('Polish / monitor','permit limits')],'Manage concentrated spent baths separately; never assume neutral pH alone means safe discharge.'),
 ('sludge-dewatering','sludge-dewatering.svg',[('Clarifier underflow','metal hydroxide solids'),('Polymer trial','settling / thickening'),('Thicken','reduce water'),('Filter press','dewater cake'),('Characterize','classify waste')],'Choose dewatering from settleability tests and disposal requirements; manage filtrate return deliberately.'),
 ('acid-recovery','acid-recovery.svg',[('Acid rinse waste','sample and segregate'),('Recovery option','ED / diffusion dialysis'),('Recovered acid','reuse if qualified'),('Rinse water','reuse if qualified'),('Residual stream','treat / dispose')],'Recovery may reduce wastewater volume and chemical demand but depends on contaminant profile, economics, and reuse specification.')
]
for folder,name,stages,sub in flows:
    (ROOT/'wastewater'/folder/name).write_text(flow_svg(name.replace('-',' ').title(),stages,sub),encoding='utf-8')
