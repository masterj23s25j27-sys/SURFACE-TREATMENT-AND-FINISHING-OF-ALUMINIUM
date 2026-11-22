# Version 4 Cathode Placement and Jig Design Study

Version 4 converts the stated tank dimensions and two rectifier nameplates into a pair of concept packages: **Cathode Placement Design** and **Zig Design**. “Zig” is interpreted as the anodizing jig or work rack. The starting cathode concept is a removable, opposed long-side arrangement; the starting jig concept is a modular top-hung rack matched to a verified product family. The diagrams compare plausible alternatives from the repository's prior methods. They are not fabrication or operating instructions.

## Design packages

- [Cathode Placement Design](Cathode%20Placement%20Design/README.md) — tank volume check, placement alternatives, support architecture, DC polarity concept, selection matrix, and engineering release inputs.
- [Zig Design](Zig%20Design/README.md) — jig/rack alternatives, tank movement envelope, contact interface, load-family selection, and validation sequence.

## Design basis supplied for Version 4

| Parameter | Stated value | Calculated or design note |
|---|---:|---|
| Tank length | 17.5 ft (5.334 m) | Confirm clear internal length after liner and fittings. |
| Tank width | 2.5 ft (0.762 m) | Confirm usable rack and cathode envelope. |
| Normal liquid depth | 2.5 ft (0.762 m) | Assumed operating depth for gross volume estimate. |
| Vessel depth | 3 ft (0.914 m) | At 2.5 ft liquid depth, nominal freeboard is 6 in. |
| Nominal target capacity | 3,000 L | Rectangular volume at stated length, width and liquid depth is about **3,098 L**, before internal displacement. 3,000 L corresponds to about **29.05 in** liquid depth if the dimensions are internal and unobstructed. |
| Rectifier option A | 24 V / 2,000 A | Nameplate product is 48 kW DC. Verify duty, process recipe, supply, cooling, protection and measured operating point. |
| Rectifier option B | 30 V / 1,000 A | Nameplate product is 30 kW DC. This is a separate option; do not assume the units can be combined. |

The user-provided dimensions and ratings are not verified site measurements. Displacement, tank wall thickness, liquid density, actual bath level, duty cycle, rectifier topology and process current remain unknown. The current ratings alone cannot determine cathode area or jig contacts.

## Concept drawings

### Cathode placement

![Cathode layout alternatives](Cathode%20Placement%20Design/cathode-placement-options.svg)

![Tank dimension and volume check](Cathode%20Placement%20Design/tank-dimensions.svg)

![Support and functional DC polarity concept](Cathode%20Placement%20Design/support-and-power-concept.svg)

### Jig and work rack

![Jig/rack alternatives](Zig%20Design/jig-options.svg)

![Rack travel and clearance envelope](Zig%20Design/rack-envelope.svg)

![Workpiece contact and lifting interface concept](Zig%20Design/contact-detail.svg)

All drawings are original SVG concept diagrams and are schematic, not scale drawings. The folders contain the complete design notes and validation steps.

## How Version 4 uses previous records

| Repository record | Use in this study | Limits retained |
|---|---|---|
| [Version 1 photo assessment and site survey](../version-1/README.md) | Carries forward the measured-data checklist for tank, cathodes, rack, hoist, cooling and electrical records. | The photo does not verify material, chemistry, dimensions, cathode identity or tank condition. |
| [Version 2 setup concept and report](../version-2/REPORT.md) | Supplies the broad equipment context for tank, rack, cooling, ventilation and containment. | The clip has not been verified frame by frame and is not used as dimensional evidence. |
| [Version 3 modernization report](../version-3/REPORT.md) | Applies the staged measurement, integrity, pilot, and discipline approval gates. | Its concepts do not establish installed equipment or local authorization. |
| [Cathode fixing engineering report](../../reports/Cathode_Plate_Fixing_Engineering_Report.docx) | Informs removable top support, material alternatives, work polarity convention and process-specific spacing considerations. | Sulfuric-acid anodizing assumptions must be confirmed before applying the recommendations. |
| [Cathode support methods](../../cathode-plate/methods/README.md) | Informs support comparison and preference for avoiding improvised wetted-wall penetrations. | Tank rim and structural loads need site-specific calculations. |

## Decision gates before detailed design

1. Confirm bath identity, composition, temperature, work alloy, quality specification and process owner.
2. Survey internal tank dimensions, material, condition, support structure, actual liquid level, containment and operating access.
3. Measure representative part/rack dimensions, exposed area, mass, product family, hoist interface and load pattern.
4. Record rectifier make/model, continuous rating, output behavior, polarity, actual current/voltage traces, protections and cooling.
5. Approve cathode area/position and jig contacts through process review and representative-load trials; set acceptance limits for coating quality and contact performance.
6. Obtain tank fabricator/structural, electrical, process, lifting and EHS review before procurement, fabrication, wiring or operation.

## Status

Version 4 is a feasibility study. No tank structural member, cathode plate thickness/count, bus section, cable, jig contact count/force, rectifier setpoint, interlock setting or lifting limit is specified. Those details require site survey and qualified engineering approval.
