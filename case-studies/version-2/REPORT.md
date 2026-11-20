# Version 2 engineering report — tank setup and modernization options

**Subject:** User-supplied tank/process video; planning guide for anodizing tank review  
**Video file:** `source-video.mp4` (44.96 s; metadata-derived; see [`VIDEO-REVIEW.md`](VIDEO-REVIEW.md))  
**Assessment status:** Desktop file and metadata checked. Clip frames not visually decoded. All proposed layouts are conceptual.  
**Purpose:** Establish a safe, evidence-led route from media review to site survey, concept selection, detailed engineering, and qualification.

## 1. Executive assessment

The supplied MP4 is present and readable as a file. Its container reports a video stream of approximately 44.956 seconds and an audio stream of approximately 44.949 seconds. The current command environment had no available `ffmpeg`, `ffprobe`, VLC CLI, or usable video-decoding library, and the user requested continuation without Windows UI control. No frame-level visual observations can therefore be responsibly attributed to the clip in this revision.

This report provides a coordinated tank-system review framework and a conceptual setup drawing. For context only, the separate Version 1 still-photo assessment describes a long, open rectangular tank-like vessel and several unidentified features. Those observations are not proof that the video depicts the same vessel or that the process is anodizing. Confirm the process, equipment, and sequence directly at the installation before applying anodizing-specific recommendations.

**Immediate decision:** do not order cathodes, modify the tank wall, select a treatment train, or fabricate a replacement from this video alone. Complete the video observation log and site survey, confirm chemistry and applicable specifications, then obtain discipline-reviewed drawings and calculations.

## 2. Evidence register

| Item | Status | What can be concluded |
|---|---|---|
| User-provided MP4 file | Verified as present; 9,414,298 bytes | The source file is included unchanged in this case-study folder. |
| MP4 stream metadata | Parsed from the file container | Approximately 44.96 seconds of video and audio. Metadata does not reveal what the camera shows. |
| Video scene, equipment, operating sequence, labels, dimensions | Not visually verified | Do not identify any component or infer its purpose until frames are reviewed. |
| Prior still photo in Version 1 | Separately documented in `../version-1/` | Can guide a survey if it is the same installation, but identity and continuity with this clip are unconfirmed. |
| `setup-concept.svg` | Original engineering concept | Shows functions and interfaces to consider; it is not an image extracted from the video or an approved design. |

## 3. System boundary and information to collect

Treat the installation as a connected process rather than just a tank. Map process tank, work rack/hoist, cathodes and current headers, rectifier and buswork, cooling/heat exchange, bath circulation or agitation, extraction/LEV, adjacent rinse stages, drains, spill containment, and wastewater treatment. Record which items are actually present, their tags and connections, and what happens during normal production, loading, idle, cleaning, and upset conditions.

Before sizing or altering equipment, obtain:

- **Process:** bath identity and analysis limits; concentration; contamination limits; normal and maximum temperatures; work alloy, exposed area, rack envelope, coating targets, load size, throughput, and applicable customer or quality scheme.
- **Tank:** internal dimensions, working/freeboard levels, verified polymer/liner grade, thickness and fabrication records, wall deflection, supports, base/foundation, nozzles, repair history, and secondary containment.
- **Electrical:** rectifier nameplate and measured duty, current/voltage history, polarity map, bus/header/rack materials and joints, contact losses, cathode active area/position, work spacing, and safe isolation points.
- **Thermal/hydraulic:** cooling duty and flow, mapped temperatures under representative maximum load, pump/eductor or air system, flow distribution, filtration, deposits, and maintenance history.
- **Environment:** tank extraction and commissioned airflow evidence, rinse flows, drag-out losses, segregated wastewater streams, laboratory chemistry, effluent limits, sludge classification/disposal route, energy and water use, and incident/maintenance records.
- **Operations:** hoist paths, guarding, access, lifting loads, cleaning method, operator tasks, production downtime constraints, emergency response, and responsibilities for inspection and maintenance.

Use the [Version 1 site survey checklist](../version-1/site-survey-checklist.md) as a starting form and add a frame-by-frame log from `VIDEO-REVIEW.md`.

## 4. Tank and support design options

### 4.1 Preferred route to evaluate

For a new rectangular process bath, evaluate a shop-fabricated welded thermoplastic tank with a calculated external support frame. PP is a common starting material for compatible anodizing service, but no resin, thickness, panel span, or weld method is approved without confirming exact chemistry, additives, temperature, liquid density, design life, and site conditions. If the assembly cannot be transported, consider engineered site-assembled panels with qualified field welds. For a retrofit, a PP liner in a structural shell may be suitable if thermal movement, support, inspection access, and leak detection are resolved.

### 4.2 Alternatives

| Option | When to investigate | Main engineering checks |
|---|---|---|
| Shop-welded rectangular PP | New rectangular line bath with manageable transport | Design to applicable thermoplastic tank standard; creep, liquid head, welds, rib/frame support, base and nozzle loads. |
| Site-assembled PP panels | Oversize vessel that cannot ship intact | Field welding environment, access, welder qualification, seam inspection, and controlled leak test. |
| PP liner in steel/concrete shell | Structural shell can be retained or built independently | Liner support, expansion/sliding details, anchoring, abrasion, inspection and drainage behind liner. |
| Double-wall tank or separate bund | Higher leak consequence or specified containment | Interspace inspection/leak detection, drainage, capacity, and compatibility of both barriers. |
| Ribbed or externally framed PP tank | Rectangular footprint needing deflection control | Calculated wall spans, rib/frame loads, temperature/creep, local stress, supports, and access. |
| PVDF, CPVC/PVC, or HDPE | Process/material-specific alternative or smaller vessel | Exact chemical/temperature compatibility, mechanical rating, fabrication method, permeation and contamination. |
| Dual-laminate PP/FRP or barrier FRP | Structural and chemical barrier functions need separation | Resin/barrier compatibility, laminate quality, thermal limits, inspection and repair route. |
| Lined steel/concrete | Civil/structural shell is advantageous | Lining system, joints, movement, holidays/defects, repairability and inspection. |
| Stainless steel | Only if process compatibility is established for this bath | Corrosion, contamination, electrical/polarity interactions, weld passivation and contamination risk. Do not assume generic stainless is suitable for sulfuric anodizing. |
| Molded/stock vessel | Duty and dimensions fit a rated commercial product | Manufacturer rating at actual temperature, support requirements, penetrations, and full load/cycle. |

The repository's [`pp-tank/construction-methods/`](../../pp-tank/construction-methods/README.md) and [`pp-tank/alternatives/`](../../pp-tank/alternatives/README.md) contain individual conceptual drawings and decision notes. These alternatives are screening options, not a universal ranking.

### 4.3 Tank construction and quality route

1. Produce a design basis from measured process and site data, including empty/full loads, temperature range, liquid properties, design life, movement, and applicable codes.
2. Select the vessel architecture, containment, support, handling, access, lifting, and inspection approach with the tank designer and owner.
3. Obtain stamped/approved calculations and fabrication drawings covering panels, weld map, ribs/frame, base support, nozzles, penetrations, and tolerances.
4. Specify traceable resin/liner and filler materials, qualified welders/procedures, fit-up, joint preparation, inspection/repair records, and dimensional checks.
5. Use the designer's approved leak/fill test and inspection plan. Do not pressure-test a tank designed for atmospheric service.
6. Record as-built dimensions, material certificates, weld documentation, test results, operating limits, repair method, and periodic inspection intervals.

Do not derive sheet thickness, reinforcement spacing, weld dimensions, or support spacing from a photograph or schematic. Thermoplastic strength and creep depend on temperature and time under load. See HSE PM86 and the applicable current EN 12573/DVS design and welding documents.

## 5. Cathode, rack, and electrical arrangements

First identify the bath and safely map polarity and every visible conductor/component. A black tube, vertical rail, pipe, or dark region in a frame cannot be assumed to be a cathode. Record cathode material, exposed surface, active position, electrical contact, header, cooling/flow obstruction, work clearance, and maintenance method.

If sulfuric-acid anodizing is confirmed and the governing process allows it, compare removable aluminum cathodes with the existing arrangement. The Aluminum Anodizers Council technical bulletin addresses aluminum cathodes, alloy, area ratio, positioning, minimum spacing and connection practices. Verify the current specification and process constraints before using any stated dimensions. Preferred support concepts to compare are top-suspended insulated supports, an independent frame, a cross-tank removable frame, or engineered polymer cleats. Wall penetrations need structural and leak-path review; they are not the default retrofit.

For each option, design for:

- removable inspection and cleaning without damaging the tank liner;
- uniform current distribution for the actual load geometry and active area;
- repeatable, low-resistance electrical contacts accessible for inspection;
- support loads transferred into designed seats/frame rather than unsupported thin liner;
- electrical isolation between unlike conductors and the tank frame where required;
- work rack/hoist clearances, drainage, bath circulation and ventilation;
- safe maintenance and isolation under site electrical procedures.

Measure actual current/voltage and contact losses during representative loads. Where QUALANOD applies, consult its current specification for applicable current density, instrumentation, supply regulation, and contact requirements; do not treat one scheme's numbers as universal acceptance criteria.

Compare the six concepts in [`cathode-plate/methods/`](../../cathode-plate/methods/README.md). The [material comparison](../../cathode-plate/material-alternatives/README.md) should be reviewed against exact bath chemistry; material choice cannot be made from appearance alone.

## 6. Cooling, movement, controls, and extraction

### Cooling and agitation

Size heat removal at the actual maximum load and ambient condition, including measured bath losses and equipment factors. QUALANOD publishes an indicative anodizing heat-load relation, `K (kcal/h) = 0.86 × I (A) × [V (V) + 3]`; a competent thermal designer must check applicability, units, operating profile and design margins. Map multiple bath temperatures during loaded cycles. Evaluate a pump/eductor arrangement or appropriately designed low-pressure air agitation against uniformity, mist generation, energy use and coating results. No diffuser pattern or air pressure can be specified from unreviewed media.

### Controls and electrical modernization

Possible upgrades include calibrated digital current, voltage and temperature measurement; rectifier service or replacement with programmable control; recipe records and alarms; cooling flow/temperature monitoring; bath-level indication; and batch data logging. Choose based on measured variability, quality losses, serviceability and total cost. A newer rectifier waveform is not by itself evidence of better coating quality. Validate controls and interlocks before production.

### Local exhaust ventilation

An open tank does not establish whether adequate extraction is present. A ventilation engineer should evaluate hood geometry, capture across the full opening and hoist path, airflow indication, duct/scrubber if needed, exposure and discharge requirements, and commissioning measurements. Follow applicable exposure limits, local regulations, and HSE or equivalent guidance. Do not use a visible hood or fan as proof of capture performance.

## 7. Wastewater and resource-efficiency alternatives

Segregate and characterize streams before selecting treatment. Anodizing rinse, acidic drag-out, alkaline etch, cleaning, dye, sealing, and mixed floor-wash streams may need different management; confirm the actual line first. Collect representative samples and measure flow, pH, acidity/alkalinity, dissolved and total metals, suspended solids, fluoride or other process-specific constituents, and any permit-required parameters. Use an accredited/competent laboratory and permit owner to set the final sampling plan.

| Method | Role | Limits / decision points |
|---|---|---|
| Stream segregation and equalization | Reduce shock loads and prevent incompatible streams from being mixed | Requires drain mapping, operator discipline, tank capacity and overflow control. |
| pH adjustment and metal precipitation | Conventional treatment for compatible metal-bearing streams | Bench/jar testing, pH control, coagulant/flocculant selection, settling, metals analysis, sludge dewatering and disposal are required. Exact chemistry varies. |
| Clarification/filtration | Remove precipitated solids after reaction | Solids loading, filterability, maintenance, backwash and residual-metal limits. |
| Sludge thickening/dewatering | Reduce sludge volume before approved disposal/recovery | Classify sludge, test leachability where required, and confirm licensed route; dewatering does not make waste non-hazardous. |
| Drag-out recovery and cascade rinsing | Reduce water and chemical loss at source | Validate rinse quality, product contamination, recovery tank capacity, and operator/workpiece constraints. |
| Acid recovery / diffusion dialysis / electrodialysis | Potential recovery of compatible acid or metals from selected streams | Requires process-specific pilot/vendor study, feed pretreatment, scaling/fouling and concentrate management. Never assume mixed waste can be recovered. |
| RO or other membrane reuse | Potential rinse-water reuse or concentration | Requires feed suitability, pretreatment, membrane compatibility, concentrate disposal, water-quality validation and lifecycle review. |
| Off-site treatment | Manage variable/small or complex streams through a permitted contractor | Characterization, transport rules, acceptance criteria, manifests and total cost. |

Use the guides for [`conventional precipitation`](../../wastewater/conventional-precipitation/README.md), [`sludge dewatering`](../../wastewater/sludge-dewatering/README.md), and [`acid recovery`](../../wastewater/acid-recovery/README.md) as concept comparisons. The selected treatment train must meet local discharge/pretreatment permit limits and operating capacity. Determine sludge classification and disposal requirements locally. Do not discharge based on pH alone.

Resource improvements to evaluate include controlled drain-back over the process tank, metered rinse flow, counter-current/cascade rinsing, rinse reuse where product quality permits, tank covers during idle periods, heat and current efficiency review, leak detection, and normalized energy/water/chemical tracking per area or mass of product. Qualify each change with quality and environmental owners.

## 8. Modernization packages and selection logic

| Package | Scope | Select when measured evidence shows |
|---|---|---|
| 1 — Inspect and instrument | Tank survey, calibrated temperature/current/voltage/flow readings, leak/containment review, baseline product and effluent testing | The current system's condition or performance is poorly understood. |
| 2 — Cathode/rack correction | Reposition/renew verified cathodes, supports, bus/header joints and rack contacts | Current distribution, contact loss, thickness uniformity or handling is a demonstrated constraint. |
| 3 — Thermal/hydraulic correction | Cooling, circulation/eductors, filtration and multi-point temperature monitoring | Loaded bath mapping or coating results show thermal/flow non-uniformity. |
| 4 — Controls/rectifier | Service or upgrade rectifier, instrument/control loop, batch records and alarms | Capacity, repeatability, measurement, efficiency, parts or traceability are inadequate. |
| 5 — Air/water/waste | LEV assessment, rinse/drag-out optimization, stream segregation, ETP upgrades or recovery trial | Measured exposures, water use, effluent results, sludge volume, or permit conditions justify change. |
| 6 — Reline/replace | Engineered repair, liner, new supported vessel and secondary containment | Inspection finds unacceptable integrity/material compatibility, or existing capacity cannot meet validated needs. |

These packages can be combined or sequenced based on risk. Address an immediate integrity, exposure, electrical, containment or permit problem before production optimization.

## 9. Implementation, commissioning, and handover

1. Complete video review and the site-survey data set; preserve originals and identify evidence by source and date.
2. Confirm bath/process, governing quality requirements, regulatory limits, production envelope, and measurable success targets.
3. Compare keep/repair, reline, and replacement. Develop alternative concepts for tank, cathode, cooling, controls, extraction and wastewater.
4. Obtain discipline-reviewed drawings, calculations, materials, fabrication procedures, risk assessments and outage plan.
5. Execute shutdown, cleaning, isolation/lockout, lifting, contractor control and waste handling under approved plant procedures.
6. Inspect fabrication, tank support and containment; check instrumentation, polarity, bonding/isolation, alarms, guarding and ventilation. Perform only designer-approved leak tests.
7. Commission with documented acceptance criteria; map current, temperature, flow and exhaust performance; run representative loads; test coating quality; characterize treatment effluent/sludge; compare energy and water baselines.
8. Handover as-built drawings, certificates, welding/inspection/test records, operating limits, controls/recipes, calibration, maintenance plan, training and emergency response.

## 10. Open questions and release gates

Before converting this report into a detailed design, answer:

1. Does the clip show the same installation as Version 1's photo? What does each visible part do, and at what timestamp?
2. What exact process bath is this, and which alloy, load area, coating quality, current density, and temperature range are required?
3. What are verified tank construction material, dimensions, wall condition, supports, and leak/containment status?
4. What are the measured rectifier envelope, bus/contact losses, cathode arrangement, and work clearance?
5. What cooling/agitation and extraction are installed, and what commissioned measurements exist?
6. What are wastewater flows/analyses, local discharge limits, sludge classification and current treatment performance?
7. What are the site's safety, quality, environmental, budget, outage, and design-life requirements?

Do not release a tank/cathode fabrication drawing or wastewater process specification until the relevant data and approvals are recorded.

## References

- [QUALANOD current specifications](https://www.qualanod.net/specifications.html) — as of 20 November 2026, the organization lists its 1 July 2026 edition as current; confirm the latest issue and scheme scope before design.
- HSE, [PM86: The assessment of chemical tank integrity](https://www.hse.gov.uk/pubns/guidance/pm86.pdf).
- HSE, [G406: Local exhaust ventilation](https://www.hse.gov.uk/pubns/guidance/g406.pdf).
- Aluminum Anodizers Council, [Technical Bulletin #1-00: Sulfuric Acid Anodizing with Aluminum Cathodes](https://cdn.ymaws.com/anodizing.site-ym.com/resource/resmgr/Docs/Technical_Bulletin_1-00_Sulf.pdf) — repository users should consult the source, since the bulletin is copyrighted.
- [EPA Ireland BAT guidance for metal and plastics surface treatment](https://www.epa.ie/publications/licensing--permitting/industrial/ied/BAT-Guidance-Note-for-Metals-%26-Plastics-Sector.pdf) — jurisdiction-specific BAT reference, not a substitute for local permits.
- BSI, [BS EN 12573-3: design and calculation for single-skin rectangular welded thermoplastic tanks](https://knowledge.bsigroup.com/products/welded-static-non-pressurized-thermoplastic-tanks-design-and-calculation-for-single-skin-rectangular-tanks).
- DVS, [DVS 2207-11: heated-element welding of PP](https://www.dvs-regelwerk.de/en/guidelines-nodes/guideline-dvs-2207-11-05-2020).

## Limits

This is a preliminary desk-study report. It does not establish the video's visual contents, identify an actual tank's condition, certify chemical compatibility, set fabrication dimensions or weld parameters, design electrical equipment or ventilation, select wastewater setpoints, or authorize operation. Confirm local rules and obtain competent engineering approvals.
