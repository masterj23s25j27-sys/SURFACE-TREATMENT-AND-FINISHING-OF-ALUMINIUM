# Version 3 engineering report — international advanced modernization concepts

**Prepared:** 20 November 2026  
**Basis:** Version 1 tank photograph assessment; Version 2 user-provided video file and review record; public regulator, standards-body, and research sources.  
**Purpose:** Compare advanced options and set out an evidence-led modernization pathway for investigation.  
**Status:** Desk study only. No site dimensions, bath analyses, operating measurements, decoded video frames, or discharge permit data were supplied.

## 1. Executive summary

The best-supported upgrade strategy is a **measured, modular hybrid** rather than buying one “advanced” tank or a blanket zero-liquid-discharge plant:

1. establish what process and equipment are actually present; inspect tank integrity and map electrical, thermal, water, air, and waste performance;
2. secure the vessel and process basics, then consider a removable, correctly located cathode system and repeatable rectifier/rack controls if sulfuric-acid anodizing and the measured defect mechanism support them;
3. reduce bath loss and rinse demand first with controlled drain-back, catch/drag-out recovery, counter-current cascade rinsing, and conductivity/flow controls;
4. segregate suitable acid-rich streams for a vendor/lab pilot of electrodialysis or a suitable recovery process; reuse recovered acid/water only after quality qualification;
5. treat residual streams using a chemistry-led conventional or hybrid treatment train, then add membranes/evaporation only if water reuse or permit goals and a concentrate outlet justify the life-cycle cost.

This order reflects published international practice. The U.S. EPA describes counter-current cascades, static drag-out rinse, rinse timers, flow control, sprays/fog, controlled drain time, drip shields, and conductivity monitoring. The European Commission's surface-treatment BREF includes cross-sector BAT on drag-out/rinse reduction and recovery, but the Commission page says the BREF was adopted in 2006 and review has started; it is a reference document, not a new 2026 BAT conclusion. A study at an aluminum-finishing facility in Türkiye reported an industrial electrodialysis application that reused recovered acid and water and reduced effluent sent to treatment by about 90%; that is a case-specific result, not a guaranteed plant outcome. The 2025 study of electrocoagulation/electrooxidation on mixed anodizing wastewater was research optimization, and its electrooxidation condition did not meet the stated sewer discharge standard for sulfate. [Sources 1–5](#references)

**First action:** complete a plant survey and analytical baseline. The video still has not been visually inspected frame by frame, and neither media item proves the tank is anodizing service. No fabrication dimensions, recipes, electrical values, chemical setpoints, or discharge design can be issued from this report.

## 2. What Versions 1 and 2 actually establish

### Version 1 — photo case study

The still appears to show a long, rectangular open-top tank or tank bay, repeated vertical interior wall features, three dark vertical features near one end, a broad bottom, and an overhead/left-rim assembly. Each item's function and material remain unknown. The picture does not establish tank resin, wall condition, bath, polarity, cooling, circulation, LEV performance, containment, or operating sequence. See [`Version 1`](../version-1/assessment-and-modernization.md).

### Version 2 — video case study

The user-provided MP4 is about 44.96 seconds by container metadata. The Version 2 record states that the video was not decoded into frames. No video-specific equipment or sequence is confirmed. See [`Version 2`](../version-2/VIDEO-REVIEW.md).

### Consequence for V3

The tank schematics in V3 are design concepts for discussion. They are not reconstructions of the photograph/video. The team must confirm whether those assets show the same installation and identify each feature with records, safe inspection, and process data.

## 3. International reference practices and technology maturity

| Practice/technology | Evidence and geographic reference | Maturity in this context | Application caution |
|---|---|---|---|
| Drag-out minimization, delayed drain, drip shields, rinse optimization | U.S. EPA metal-finishing pollution-prevention guidance and EU surface-treatment BREF | Established industrial practices | Optimize by work geometry and quality; some surfaces stain or react during longer drain. |
| Counter-current cascades, static/eco-rinse, flow/rinse timers, conductivity checks | U.S. EPA guidance; EU and Nordic/Baltic sector guidance | Established | Define conductivity limits from product quality and bath carryover; conductivity is not a direct contaminant assay. |
| Acid/water electrodialysis recovery | Peer-reviewed aluminum-finishing case study in Türkiye with a real industrial stream | Industrial case evidence; vendor/process suitability still needed | Trial actual feed, aluminum and contaminant behavior, membrane fouling, concentrate/reuse quality, cleaning and residual purge. |
| Reverse osmosis / nanofiltration / membrane distillation | Peer-reviewed anodizing wastewater studies; use depends on feed | Commercial unit operations; anodizing-specific integration is case-dependent | Pretreatment, acid compatibility, scaling, concentrate disposal, permeate quality, and energy determine feasibility. |
| Evaporation / crystallization and ZLD | EU BREF describes closed-loop membrane and evaporation techniques and cautions that whole-installation zero discharge is not generally BAT | Industrially available, high capital/energy and residual management | ZLD transfers contaminants into concentrate/salt/sludge; it does not eliminate residuals or permit duties. |
| Electrocoagulation / electrooxidation | 2025 mixed-anodizing wastewater study | Emerging/research-to-pilot for this specific stream | Results are matrix-specific; sulfate removal and discharge limits may remain unsatisfied; electrode passivation and sludge require evaluation. |
| Bipolar electrodialysis for alkali recovery | Recent aluminum-finishing research | Emerging; not assumed proven at this installation | Validate caustic strength, aluminum carryover, membrane life and economics with a pilot. |
| Digital recipe logging, current/voltage/temperature/flow sensing, alarms | Common automation architecture; exact anodizing benefits must be measured | Mature controls; process-specific recipe strategy | Sensors must be calibrated and tied to validated quality rules; online instruments do not replace bath/lab checks. |
| AI predictive maintenance or a process digital twin | Possible extension of a well-instrumented line | Optional emerging layer | Use only after clean, timestamped process and maintenance data exist; do not use model output as a safety interlock or permit substitute. |

The EU JRC page says the Surface Treatment of Metals and Plastics BREF is under review while its downloadable core BREF was adopted in August 2006. Consult current national rules and subsequent BAT conclusions; do not label an old reference as the latest legally binding standard. QUALANOD lists an edition dated 1 July 2026 as current on its specifications page and says the January edition was superseded; the full specification is available upon written request. Confirm the actual edition and license/customer scope before using acceptance values. [Sources 1 and 6](#references)

## 4. Integrated V3 concept — design functions

The [integrated line diagram](visuals/integrated-line-concept.svg) shows process functions, not a site-specific P&ID. The modern arrangement to assess includes:

1. **Vessel and structure:** compatible wetted barrier, calculated frame/base, secondary containment, leak indication where justified, safe access and drain routing. A PP welded tank, PP liner/structural shell, dual-laminate vessel, or engineered replacement remain alternatives. Use the V1/V2 survey and [repository tank comparisons](../../pp-tank/README.md).
2. **Cathode and work circuit:** removable cathodes on a designed top support/header or independent frame; insulated mounts as required; work rack/hoist clearances; documented polarity; measurable low-loss joints; removable parts for inspection. Select material/position only after bath confirmation. Consult the [existing cathode concepts](../../cathode-plate/methods/README.md) and current applicable anodizing specification.
3. **Power and process recipe:** service/replace rectifier only if data justify it; measure actual current, voltage, bath temperature and process time; store approved recipes and alarm limits; record batch/load identity and quality results. Specify control tolerances from the applicable quality scheme and process trials.
4. **Thermal and flow:** size cooling at maximum actual load; balance circulation/eductors and avoid dead zones; map temperature and flow with production-like loads. Anodizing heat-load calculations must be checked by a process/thermal engineer; do not size from nominal tank voltage alone.
5. **Air and operator safety:** evaluate capture hood around the real tank/hoist envelope; prove extraction performance with competent measurements; review mist handling, duct/material compatibility, scrubber if required, make-up air, access and exposure controls.
6. **Rinsing and recovery:** drip back over the source tank, provide catch/drag-out recovery where chemistry allows, then use staged counter-current rinses with controlled flow and conductivity/quality verification. Return a recovered stream only to a bath whose impurity and concentration specification it can meet.
7. **Wastewater treatment:** segregate streams by chemistry and recoverable value. Treat a characterized residual stream with a validated precipitation/clarification/filtration route or a compatible advanced/polishing stage. Log flow, pH, conductivity and process events; verify regulated analytes by the required laboratory method.

## 5. Tank and cathode upgrade paths

### Path A — retain and instrument

Choose only if a competent inspection finds sound liner, welds, supports and base and the existing vessel is chemically compatible for the validated service. Establish baseline wall deflection, leak/containment status, temperature profile, rectifier profile, current-contact losses, cathode position and coating-quality variation. Add sensors and safe inspection points without drilling or loading an unverified tank wall.

### Path B — engineered retrofit

For a sound tank with a measured cathode/current-distribution or handling problem, review removable cathodes on top seats/crossbeam or an independent support frame; revise bus joints, rack contact and alignment; add replaceable guides/cleats if tank designer approves. Avoid unengineered wall penetrations. Confirm no new interference with cooling, flow, LEV, hoist, cover, or work clearances.

### Path C — replace or reline

If inspection cannot demonstrate integrity, compatibility or design life, compare a new shop-built welded thermoplastic tank with external support, site-assembled panels, liner-in-shell, dual-containment, and dual-laminate options. Obtain design calculations and approved fabrication drawings for liquid head, polymer creep, temperature, welds, supports, nozzle loads, foundation and containment. Do not derive sheet thickness or weld settings from an image.

### Cathode decision gate

First confirm electrolyte and process/customer specification. If sulfuric-acid anodizing permits it, compare a removable aluminum cathode solution to the known existing setup using actual work geometry, active area, bath spacing, polarity and rectifier capacity. The AAC bulletin previously referenced by the project is a useful source for sulfuric anodizing, but its provisions must be checked against current scheme requirements and the actual process. Do not assume the dark objects in either media file are cathodes.

## 6. International water and chemical recovery concepts

### 6.1 Source reduction before treatment

The EPA's metal-finishing guidance recommends optimizing rinse tanks, counter-current cascade, drag-out rinses, air agitation where suitable, flow restrictors and timers, sprays/fog, drip shields, controlled drain time, and monitoring conductivity. It also warns that longer drain time or air knives are not suitable for every workpiece/process. Implement in this order:

1. map each tank and wastewater source, including spills, floor wash and batch dump;
2. slow or sequence rack withdrawal and capture drips over the source tank where product surface permits;
3. use drainboard/catch/eco-rinse to collect a concentrated return stream;
4. stage counter-current rinses, supply clean water to final rinse, transfer overflow upstream, and meter by demand;
5. use conductivity/flow sensors for trend/alarm/control only after they are correlated with final-product quality and lab analysis;
6. check energy, ventilation and product-quality tradeoffs if fog/spray or air agitation are considered.

### 6.2 Electrodialysis and acid recovery

A 2022 peer-reviewed study reports electrodialysis optimized for dilute sulfuric-acid rinse wastewater at an aluminum anodizing facility. The authors report industrial-scale reuse-quality acid/water and approximately 90% lower effluent volume sent to the plant's wastewater treatment system. This establishes a strong pilot candidate, not a guaranteed performance or a requirement. Feed composition, aluminum loading, dyes/sealants/additives, organics, sulfate, throughput, membrane cleaning, reject/concentrate, and acid makeup compatibility need testing. Recovery should be a closed-loop quality decision, not merely a pH/acid concentration target.

### 6.3 Membranes and thermal concentration

Nanofiltration/reverse osmosis can be considered for selected rinse streams after pretreatment; membrane distillation/crystallization or evaporators may concentrate residuals where heat integration and residual handling support them. Anodizing-specific literature exists, but these are not plug-and-play on mixed, high-salt or hot acidic waste. Evaluate: feed limits, pretreatment, membrane materials, cleaning chemistry, scale/fouling, recovery ratio, energy and heat source, permeate conductivity/contaminants, concentrate composition, residual salt/sludge outlet, and total lifecycle costs.

### 6.4 Near-zero liquid discharge

Use ZLD as a site-level objective only if permits, water scarcity, reuse demand, economics and residuals management support it. The EU BREF notes that zero discharge can be achieved in specific cases but is not generally BAT for an entire facility. A realistic design may combine segregated streams, source reduction, reuse/recovery, membrane concentration and evaporation/crystallization of a smaller purge. Document the final destination and cost for every solid, brine and off-spec concentrate. “No liquid outfall” is not “no waste” or “no environmental impact.”

See [Concept 3](concepts/03-rinse-and-acid-recovery/README.md) and [Concept 5](concepts/05-selective-zld/README.md).

## 7. Wastewater treatment alternatives

### Conventional robust train

For residual metal-bearing wastewater: separate concentrated acids/alkalis and incompatible streams; equalize appropriately; adjust pH in controlled reaction stages based on jar tests; precipitate metals; coagulate/flocculate if validated; clarify or use lamella/DAF where suitable; polish through filtration; manage dewatered sludge under local classification and licensed disposition. Verify effluent using permit parameters and accredited laboratory procedures. This remains a sensible baseline when influent is variable and robust operation matters.

### Advanced and hybrid trains

- **Electrocoagulation (EC):** candidate pilot for certain mixed anodizing streams. A 2025 study reported high aluminum/COD removal and sulfate removal under its tested conditions. Do not copy its optimized current/pH/time values; its reported dataset is not design data for this plant.
- **Electrooxidation (EO):** possible polishing for particular oxidizable organics; the 2025 study reported sulfate remained above its sewer standard, so EO alone should not be presented as a complete anodizing effluent solution.
- **Membrane polishing:** UF/NF/RO may support reuse after pretreatment; reject stream still needs a permitted route.
- **Selective ion exchange/electrodialysis:** consider where ions/acid are sufficiently valuable and the matrix is well-characterized; regenerate/manage brine correctly.
- **Sludge recovery:** test hydroxide sludge composition and consistency before exploring reuse/recovery; classification, contaminants, product specifications, offtake and regulatory acceptance govern viability.
- **Online monitoring and automation:** interlock/alert on flow, pH, conductivity, level, tank leakage and treatment status as appropriate. Maintain grab/lab sampling and operator rounds; control systems need fail-safe design.

The decision tree in [the wastewater concept image](visuals/water-and-waste-options.svg) begins with source segregation and leads to recovery or treatment according to actual chemistry. No stream is discharged solely because pH is acceptable.

## 8. Digital and operational advances

### Mature control layer

Use a PLC/SCADA or equivalent industrial control architecture only to the extent needed: barcode/recipe identification; batch time, current, voltage and temperature records; rectifier and cooling alarms; rinse flow/quality trends; tank level/leak alarms; ETP batch/continuous feed records; maintenance and calibration schedules; and secure export to a plant historian or quality system. Add validated setpoints and operator override rules. Document sensor accuracy, calibration, audit history, access control, backup, and response when a sensor fails.

### Predictive analytics (optional)

After sufficient trustworthy data exist, an analytics model may flag drift, predict cooling/rectifier maintenance, estimate rinse water demand, or correlate process parameters with quality outcomes. Keep the human/process engineer in the loop. Validate on held-out production batches, monitor model drift, and prevent unvalidated AI outputs from automatically changing recipes, safety interlocks, or discharge decisions.

## 9. Comparison and recommended sequence

See the full [method comparison matrix](METHOD-COMPARISON.md). For most existing lines, the preferred feasibility sequence is:

1. **Safety/integrity gate:** inspect tank, supports, bund, electrics, LEV, and permits; remediate any unsafe condition first.
2. **Measurement baseline:** collect one representative production campaign for current/voltage, temperature map, flow/water, product quality, bath chemistry, wastewater and sludge.
3. **Low-disruption improvement:** optimize extraction/handling, drain-back, rinse layout and flow controls, measurement/calibration, preventative maintenance.
4. **Targeted tank/cathode/rectifier change:** only if measured quality or equipment limits show a bottleneck and process chemistry confirms the design basis.
5. **Recovery pilot:** run bench/pilot ED or membrane tests on segregated streams. Compare recovered-material quality, treatment-load reduction, energy, reagent, membranes, waste residuals and payback.
6. **Residual ETP design:** validate conventional and advanced alternatives by jar/pilot testing, discharge analysis and residuals route.
7. **ZLD decision:** assess last, with full water/energy balance and written brine/solid outlet. Do not make it the default retrofit.
8. **Qualification and handover:** demonstrate coating quality, process repeatability, water/energy per unit, validated effluent compliance, operator competence and inspection/maintenance.

## 10. Measurements and decision gates

Do not choose between technologies without this dataset:

- tank material and dimensions, wall movement/deflection, weld/repair records, foundation, containment, compatible temperature/chemical limits;
- bath identity, concentrations, impurities, work alloys, active area/load, target quality and current/voltage/time trends;
- cathode material/area/position/spacing and safe verified polarity map;
- cooling duty/flow, multipoint tank temperatures, circulation/flow distribution, power and water use;
- LEV capture test and applicable exposure measurements;
- flow and chemistry by wastewater stream, pH/acidity, aluminum/other metals, sulfate, COD/TOC if relevant, solids, contaminants, permit limits and sludge classification;
- local water cost/scarcity, energy tariff, reuse demand, disposal/haul cost, chemical and membrane costs, outage allowance and payback threshold.

**Gate 1:** process and vessel identity confirmed. **Gate 2:** inspection acceptable or repair/replacement plan approved. **Gate 3:** pilot proves product and effluent quality. **Gate 4:** life-cycle cost and residual route accepted. **Gate 5:** independent discipline reviews and required permits complete before build/operation.

## 11. Safety and engineering boundaries

Acids, caustics, electrical rectifiers, hot baths, mist, lifting loads and wet floors create serious hazards. Tank entry, chemical removal, cleaning, electrical work and fabrication require site-approved risk assessment, isolation/lockout, ventilation, PPE, contractor control and competent personnel. Tank design/fabrication and environmental treatment design require qualified professionals and local approval. This report is a planning aid; no unsupervised construction or operating procedure is provided.

## References

1. European Commission Joint Research Centre, [Surface Treatment of Metals and Plastics BREF](https://bureau-industrial-transformation.jrc.ec.europa.eu/reference/surface-treatment-metals-and-plastics) — status is “review started”; the listed core BREF was adopted August 2006. It is a cross-sector reference and not itself proof of local current permit compliance.
2. U.S. EPA, [Pollution Prevention: Metal Finishing Shops Shine with P2](https://www.epa.gov/system/files/documents/2022-02/p2-metal-finishing.pdf) (November 2021) — counter-current cascade rinsing, drag-out rinse, conductivity, flow control, sprays/fog, drip protection and drag-out practices.
3. Yuzer et al., [Optimal performance of electrodialysis process for the recovery of acid wastes in wastewater: aluminum finishing industry](https://doi.org/10.1016/j.cej.2022.134755), *Chemical Engineering Journal* (2022) — industrial aluminum-finishing case plus bench/pilot study.
4. Türk et al., [A Multivariate Approach for the Treatment of Mixed Anodizing Coating Wastewater by Electrochemical Processes](https://doi.org/10.1002/wer.70166), *Water Environment Research* (first published 27 August 2025) — EC/EO optimization and limitations for the tested mixed wastewater.
5. Ali et al., [Treatment of Wastewater Solutions From Anodizing Industry by Membrane Distillation and Membrane Crystallization](https://doi.org/10.3390/app9020287), *Applied Sciences* (2019); Ali et al., [Industrial Wastewater Treatment by Nanofiltration—A Case Study on the Anodizing Industry](https://doi.org/10.3390/membranes10010085), *Membranes* (2020) — research/case evidence; site-specific validation still required.
6. QUALANOD, [Current specifications page](https://www.qualanod.net/specifications.html) — lists edition 1 July 2026 as current and states that it supersedes January 2026; full specification is available by written request.
7. HSE, [PM86: Thermoplastic tank integrity management](https://www.hse.gov.uk/pubns/guidance/pm86.pdf) — tank design basis, inspection, anchoring and integrity-management guidance.
8. EPA, [Guidance Manual for Electroplating and Metal Finishing Pretreatment Standards](https://www.epa.gov/system/files/documents/2021-07/owm0022.pdf) — rinse reduction, process management and treatment options; older but useful technical background.

## Change control

Record future revisions with date, reviewer, source data, changes and approvals. Keep Version 1 and Version 2 as earlier evidence records; do not overwrite their original media or rewrite their uncertainty statements when adding verified observations later.
