# Concept 2 — digital power, process control, and traceability

## Concept

Build a measured, recipe-controlled operating envelope around the existing or replacement rectifier. Capture approved load/recipe identity, actual current and voltage over time, bath temperature, cooling status, alarms, and product quality result. Add flow, conductivity, tank level/leak and ETP tags only where they support a documented operating response.

## Improvement options

1. Calibrate/repair existing meters, sensors and rectifier controls.
2. Add independent logged current/voltage and multipoint temperature checks for representative loads.
3. Add PLC/SCADA recipe selection, interlocks, alarm history and batch data export.
4. Replace the rectifier only after checking capacity, efficiency at actual loading, power quality, service support and measured coating needs.
5. Explore analytics/predictive maintenance only after timestamped, quality-linked sensor data are trustworthy.

## Constraints

Digital records do not prove coating quality or regulatory compliance by themselves. Retain required manual/lab checks, qualified instrument calibration, validated alarm limits, access control, backups and a safe fallback when a sensor or network fails. Unvalidated analytics must not alter recipes or safety-critical interlocks.

## Acceptance measures

Compare load-to-load variation, temperature uniformity, coating test results, rectifier/contact losses, alarms/downtime, and energy per unit treated before and after commissioning. Use current QUALANOD requirements only when applicable to the plant's process and license/customer scope.

## Related image

See the measurement, PLC/data and sensor relationships in [`integrated-line-concept.svg`](../../visuals/integrated-line-concept.svg).
