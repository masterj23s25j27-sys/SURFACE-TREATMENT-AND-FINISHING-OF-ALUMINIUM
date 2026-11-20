# PP tank construction for sulfuric acid anodizing

This guide expands the supplied cathode-support question into a practical comparison of tank architectures and thermoplastic welding methods. The source document discusses fixing cathode plates to a polypropylene tank; it does not provide tank dimensions, operating conditions, or fabrication drawings. Therefore this guide explains the main build routes and gives conceptual visuals without inventing wall thicknesses or weld settings.

## Recommended starting point

For a new rectangular anodizing process tank, the usual starting concept is a **shop-fabricated, welded PP sheet tank** with a calculated external support system. Use qualified thermoplastic welders, an engineered weld map, suitable reinforcement, and a water-fill/leak inspection plan. If the tank is too large to ship, fabricate transportable subassemblies and complete qualified site welds. Keep cathode support loads at reinforced top seats or on an independent frame; do not casually drill the wetted PP wall.

The build concept is not a design approval. Tank wall, base, ribs, frame, anchors, and supports require calculations using the actual tank dimensions, liquid head, temperature, resin grade, creep/design life, weld factors, and service environment. Rectangular welded thermoplastic tanks are covered by EN 12573 design standards; DVS 2205 covers thermoplastic vessel calculations, and DVS 2207 contains welding procedures. Obtain and apply the current editions appropriate to the installation jurisdiction.

## Construction architecture options

| Option | Best fit | Main concern |
| --- | --- | --- |
| [Shop welded rectangular tank](construction-methods/01-shop-welded-rectangular/README.md) | Most anodizing line baths; custom rectangular footprint and rack handling. | Sidewall deflection, bottom support, weld quality, and temperature effects need calculation. |
| [Site assembled panels](construction-methods/02-site-assembled-panels/README.md) | Oversize tanks that cannot be transported intact. | Site conditions, weld access, qualified welding, and inspection of every field seam. |
| [PP liner in a structural shell](construction-methods/03-pp-liner-in-structural-shell/README.md) | Retrofit or heavy-duty containment where steel/concrete carries structural load. | Liner support, thermal movement, anchoring, and inspection access. |
| [Double-wall containment](construction-methods/04-double-wall-containment/README.md) | Higher consequence leakage cases or where secondary containment is required. | Leak detection and interspace drainage/inspection must be designed. |
| [Ribbed self-supporting tank](construction-methods/05-ribbed-self-supporting-tank/README.md) | Welded rectangular vessel with calculated polymer ribs or external framing. | Ribs and frames cannot be sized by rule of thumb. |
| [Circular welded vessel](construction-methods/06-circular-tank/README.md) | Storage, compact processes, or a process layout designed around a round vessel. | Usually poor fit for long extrusion racks; layout and current distribution change. |
| [Molded or stock tank](construction-methods/07-molded-or-stock-tank/README.md) | Small or standard-size applications when product ratings meet the actual duty. | Stock geometry, material rating, and dimensions may not match long anodizing loads. |

## Welding methods

| Method | Common role | Guide |
| --- | --- | --- |
| Extrusion welding | Structural panel seams, corners, reinforcement, nozzles, and attachments depending on joint design. | [Guide and diagram](welding-methods/01-extrusion-welding/README.md) |
| Hot-gas welding | Local seams and details with compatible filler and prepared joint geometry. | [Guide and diagram](welding-methods/02-hot-gas-welding/README.md) |
| Heated-tool butt welding | Controlled edge-to-edge panel joining, including shop panel assembly. | [Guide and diagram](welding-methods/03-heated-tool-butt-welding/README.md) |

These are process categories, not interchangeable instructions. Material grade, thickness, joint geometry, equipment, welder qualification, and code determine the approved procedure. A production tank may use more than one process. The weld method alone does not make an under-designed tank safe.

## Cathode and anodizing integration

Provide supports for the cathode header, work rack, hoist, heaters/cooling coils, ventilation hood, overflow, drains, and any baffles in the design drawing. The supplied Aluminum Anodizers Council bulletin describes aluminum cathode installation, placement, minimum work-to-cathode distance, and attachment practices for sulfuric-acid anodizing. Keep electrical joints above the bath and locate supports so they do not create leak paths. Review the existing [cathode fixing report](../reports/Cathode_Plate_Fixing_Engineering_Report.docx) and [support-method gallery](../cathode-plate/methods/README.md).

## Information required before tank design

Provide the tank fabricator with: internal length, width, and depth; normal and maximum liquid levels; bath chemistry and concentration range; operating and upset temperature; specific gravity/density; loading and duty cycle; largest workpiece and rack envelope; rectifier current and cathode layout; required freeboard; fill/drain/overflow/nozzle details; heating/cooling/filtration; ventilation requirements; floor bearing capacity and seismic context; indoor/outdoor and UV conditions; containment and leak detection requirements; design life; and applicable permits/customer standards.

Do not copy a wall thickness, rib spacing, support span, weld size, or heater clearance from a sketch or another tank. PP properties change with temperature and time under load. Obtain design calculations and approved fabrication drawings.

## Inspection and handover

Require material identification and traceability; approved drawings and weld map; welder/procedure qualifications; inspection records; dimensional checks; leak/hydrostatic testing at a level and duration selected by the designer; documentation of nozzles and penetrations; repair records; and a written inspection/maintenance plan. Do not pressure-test a tank unless specifically designed for pressure.

## References

- [HSE PM86: Thermoplastic tank integrity management](https://www.hse.gov.uk/pubns/guidance/pm86.pdf) - purchaser/manufacturer information exchange, integrity management, and conditions of service.
- [BSI: BS EN 12573-3](https://knowledge.bsigroup.com/products/welded-static-non-pressurized-thermoplastic-tanks-design-and-calculation-for-single-skin-rectangular-tanks) - design and calculation for single-skin rectangular welded thermoplastic tanks.
- [Swedish Institute for Standards: EN 12573-1](https://www.sis.se/en/produkter/fluid-systems-and-components-for-general-use/fluid-storage-devices/stationary-containers-and-tanks/ssen125731/) - general principles for welded static non-pressurized thermoplastic tanks, including workshop and site fabrications.
- [DVS 2207-11](https://www.dvs-regelwerk.de/en/guidelines-nodes/guideline-dvs-2207-11-05-2020) - heated-element welding of PP pipes, fittings, and panels.
- [Niplast chemical storage tanks](https://www.niplast.com/wp-content/uploads/2021/03/CHEMICAL-STORAGE-TANKS.pdf) - manufacturer description of thermoplastic tanks and butt-fusion fabrication.
- [Fusion Australia fabricated chemical tanks](https://fusionaus.com/services/industrial-plastic-fabrication/fabricated-plastic-chemical-storage-tanks/) - manufacturer description of CNC cutting, butt welding, extrusion welding, and testing.

## Boundary

“All possible methods” cannot be exhaustive because tank size, process, jurisdiction, and supplier designs vary. This repository covers the common architecture choices and welding processes that are relevant to an industrial PP anodizing tank. It is a research and planning guide, not a build-to-print package.
