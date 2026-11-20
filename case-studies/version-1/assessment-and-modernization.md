# Technical assessment and modernization method

## 1. Image based observations

The source is a single 800 by 600 pixel image with limited detail. It appears to show:

- A long rectangular open-top tank or tank bay.
- Repeated vertical features on the interior side wall. These could be stiffeners, rails, support elements, or shadows; the image does not identify them.
- Three dark vertical elements near the far end. They may be process components, pipes, supports, electrodes, or image shadows. Do not assume they are cathodes.
- A broad flat-looking bottom with a visible transverse change in plane or an internal step near the foreground.
- A linear assembly at the left rim and overhead structure; its support, power, or exhaust function is unknown.

The photo does not show enough detail to determine PP versus another liner, whether the tank is leaking, whether the wall is bowed, how the tank is supported, whether any hood is functioning, or what chemical is present. Color is not proof of material or condition.

## 2. Establish the process and requirements

Before design, confirm whether the tank is sulfuric-acid anodizing, hard anodizing, another anodizing chemistry, or a different surface-treatment bath. Record the exact bath formula and concentration range, operating and upset temperature, liquid density, current/voltage envelope, work area per load, part geometry, desired coating and tests, shift pattern, and throughput target. Also identify which customer specification or quality scheme applies. Do not apply sulfuric-acid cathode advice to a different electrolyte without review.

Agree measurable modernization goals with production, quality, maintenance, finance, and EHS. Useful baselines include:

- kWh per square metre or kilogram treated;
- water use and wastewater volume per production unit;
- acid and chemical additions per production unit;
- batch cycle time and throughput;
- thickness, sealing, appearance, corrosion/wear test results, rework, and scrap;
- bath temperature variation under a representative maximum load;
- current and voltage profiles and electrical contact losses;
- mist/airflow results and tank/leak inspection findings.

## 3. Survey the vessel and structure

Have the tank fabricator or competent vessel engineer inspect the tank empty and cleaned under the site's approved chemical isolation and entry procedures. Identify construction material and grade, liner system, sheet thickness from records or approved measurement, weld type/condition, reinforcement, floor/base support, anchors, foundation, frame corrosion, prior repairs, and every nozzle or penetration. Measure wall deformation at repeatable points and compare against design acceptance limits supplied by the tank designer.

Create a photo and measurement baseline. Inspect for cracking, crazing, blistering, delamination, whitening, softened areas, seepage, corrosion behind a liner, unsupported spans, stress around nozzles, and damage from hoists or impact. These are inspection targets, not defects diagnosed from this photograph. Do not pressure test the tank unless it was designed for pressure; use the tank designer's fill/leak-test plan.

## 4. Survey the electrochemical and thermal system

### Rectifier and buswork

Record rectifier make/model, topology, age, rated and actual input/output, control range, current ripple/measurement capability, power factor and power-quality issues, service history, cooling, and spare-part support. Capture real voltage/current traces during representative light and maximum production loads. Measure voltage drop and temperature at the rectifier-to-bus, bus-to-header, rack, and work contacts using approved safe test methods.

Modernization options include a refreshed SCR rectifier or a high-frequency IGBT rectifier, with programmable constant-current/constant-voltage control, recipe storage, ramps/holds if qualified, true current/voltage measurement, alarms, and batch data export. Compare systems using efficiency and power-quality data at the plant's actual load profile. Do not assume the newest topology or a pulse waveform automatically improves coating quality or total cost. QUALANOD's 2026 specifications emphasize adequate current capacity, regulation, accurate measurement, and real current-density control; waveform-based supplies require compatible measurement.

Where the QUALANOD scheme applies, consult its latest issued specification and the plant's applicable customer/quality requirements for current regulation, measurement accuracy, calibration, bus/contact and joint-temperature criteria. The previous January 2026 specification is superseded; this report does not carry forward its numerical criteria as current acceptance limits.

### Bath cooling and agitation

Measure bath temperature at multiple locations during a representative loaded cycle, not only at one tank-wall sensor. Confirm cooling capacity at the maximum installed electrical load and the actual ambient condition. Use the heat-load calculation required by the currently applicable QUALANOD specification and have the cooling designer verify units, process duty, ambient and system factors.

Map agitation and temperature uniformity across the work. Compare engineered circulation/eductors and, where permitted, air agitation against the current quality specification, coating uniformity, mist generation, worker exposure and measured energy. Do not copy diffuser spacing or airflow from a different tank.

### Cathode and rack layout

Identify and trace each dark vertical element and the left rim assembly before changing them. Map polarity and continuity with the approved electrical safety procedure. Establish active anode/work area, cathode area and position, rack clearances, current paths, loading density, edge effects, and hoist clearances.

If sulfuric-acid anodizing is confirmed and the process specification permits it, compare a removable aluminum cathode assembly with the existing arrangement. The supplied AAC bulletin covers candidate aluminum alloys, area ratios, placement, and electrical connections; the detailed repository guide recommends top-supported insulated mounts and avoids improvised wall penetrations. Maintain the required work-to-cathode spacing and validate thickness distribution on representative loads. If the bath or governing spec is different, obtain a process-specific design.

## 5. Select a modernization package

| Package | Scope | Relative disruption | Choose when |
| --- | --- | --- | --- |
| A - Instrument and stabilize | Calibrated current/voltage/temp measurement, bath analysis log, joint inspection, baseline coating tests, leak/level alarms where designed. | Low to moderate | Tank is sound, but process performance is not well measured. |
| B - Cathode/rack retrofit | Reconfigure verified cathodes, bus/header joints, rack geometry, shields, and contact maintenance. | Moderate | Current distribution or thickness variation is a measured bottleneck. |
| C - Thermal and flow retrofit | Resize/repair heat exchange and agitation, add temperature mapping and flow monitoring. | Moderate to high | Loaded temperature gradients or burning/variation are demonstrated. |
| D - Digital rectifier and recipe controls | Upgrade the power supply/control, record actual current/voltage/time/temperature, standardize recipes, and add interlocks. | Moderate to high | Existing supply lacks repeatability, capacity, measurement, serviceability, or batch traceability. |
| E - Environmental and utility package | Assess LEV and mist control, add tank lids when idle, manage drag-out, optimize rinse staging, meter water/energy, and improve stream segregation/recovery. | Low to high | Exposure, resource use, effluent, or permit performance needs improvement. |
| F - Re-line or replace | Engineer a PP tank, PP/FRP dual laminate, or other process-compatible vessel with designed support, containment, and penetrations. | High | Vessel integrity is unacceptable, material is incompatible, or capacity cannot meet the process. |

The package order is not a substitute for risk ranking. Unsafe tank, electrical, ventilation, or containment conditions are addressed before production optimization.

## 6. Environmental and worker-protection upgrades

The image shows an open tank but does not prove whether extraction is present. Have a ventilation engineer assess contaminant generation, hood position, capture at the liquid surface and work opening, duct/filter/scrubber needs, airflow indication, discharge, and commissioning. A visible fan or duct is not proof of effective capture. Keep production access and hoist movement in the LEV design.

For water and chemical use, first measure and segregate rinse streams. Consider longer controlled drain time over the process tank, cascade/counter-current rinse where product quality allows, metered rinse flow, and recovery/reuse where water chemistry suits the process. The EPA Ireland BAT guidance describes drag-out recovery, rinse options, energy monitoring, and wastewater stream segregation. Reuse is conditional on chemistry and customer quality requirements; do not close-loop every rinse automatically.

For wastewater, characterize each relevant stream before choosing treatment. The existing repository has guides for conventional precipitation, sludge dewatering, and acid recovery. Keep a bund/secondary containment and leak response appropriate to the chemical inventory and applicable local rules.

## 7. Implementation and validation sequence

1. **Survey:** complete `site-survey-checklist.md`, gather drawings/logs, map visible components, and sample current process performance.
2. **Define targets:** approve measurable quality, throughput, energy, water, safety, and effluent targets with owners.
3. **Concept design:** compare keep/repair, reline, and replace; size cooling, agitation, electrical, containment, and LEV from actual data.
4. **Design review:** tank fabricator, anodizing/process engineer, electrical engineer, ventilation engineer, and EHS/environmental owner review discipline-specific drawings and procedures.
5. **Shutdown and work:** use plant-authorized chemical handling, isolation/lockout, access, lifting, cleaning, waste, and contractor-control procedures.
6. **Mechanical/electrical commissioning:** inspect welds/supports/containment; validate sensors and interlocks; perform designer-approved leak checks; verify polarity and electrical safety.
7. **Process qualification:** run agreed representative loads, map temperature/current distribution, verify coating thickness and required quality tests, compare energy/water per production unit, and document any recipe changes.
8. **Handover:** save drawings, calibration records, control recipes, training, maintenance intervals, inspection baseline, alarms, spare parts, and responsibility matrix.

## 8. Decision gate

The image supports a reason to survey a long open tank with unusual-looking side and far-end components. It does not support a decision to keep or scrap the tank. Keep the vessel only if its materials, structure, containment, and support system pass a qualified inspection and the modified process can meet the agreed targets. Replace or reline if the condition assessment or calculations cannot demonstrate safe, compatible service.

## References

- [QUALANOD current specifications](https://www.qualanod.net/specifications.html) - the organization lists its July 2026 specification as current as of 20 November 2026; check for later updates before design or qualification.
- [EPA Ireland BAT Guidance for surface treatment of metals and plastics](https://www.epa.ie/publications/licensing--permitting/industrial/ied/BAT-Guidance-Note-for-Metals-%26-Plastics-Sector.pdf).
- [HSE PM86 thermoplastic tank integrity guidance](https://www.hse.gov.uk/pubns/guidance/pm86.pdf).
- [HSE G406 local exhaust ventilation guidance](https://www.hse.gov.uk/pubns/guidance/g406.pdf).
- [AAC Technical Bulletin #1-00 on aluminum cathodes](https://cdn.ymaws.com/anodizing.site-ym.com/resource/resmgr/Docs/Technical_Bulletin_1-00_Sulf.pdf).
- Example of programmable rectifier controls: [Precision Process rectifier control](https://www.precisionprocess.com/equipment/software-and-controls/rectifier-control). This is an example of a product category, not an endorsement or required brand.
