# Aluminum Anodizing Cathode and Wastewater Field Guide

This repository organizes practical engineering information for sulfuric-acid aluminum anodizing cathodes and aluminum-finishing wastewater. It includes a technical report, original construction schematics, method-by-method notes, material alternatives, and wastewater treatment concepts.

## Start here

1. Read [the cathode fixing engineering report](reports/Cathode_Plate_Fixing_Engineering_Report.docx).
2. Compare support options in [`cathode-plate/methods/`](cathode-plate/methods/).
3. Compare cathode materials in [`cathode-plate/material-alternatives/`](cathode-plate/material-alternatives/).
4. Compare [PP tank build options and welding approaches](pp-tank/README.md).
5. Review wastewater options in [`wastewater/`](wastewater/).
6. See [video and media notes](media/videos/README.md) for external visual references.

## Repository map

| Folder | What it contains |
| --- | --- |
| `reports/` | Engineering report with recommendation, alternatives, sizing example, and a pre-fabrication checklist. |
| `cathode-plate/methods/` | Six support and fixing arrangements. Each method folder has a short guide and an original SVG schematic. |
| `cathode-plate/material-alternatives/` | Notes comparing aluminum, lead, stainless steel, and graphite cathode options. |
| `pp-tank/` | Seven tank architectures and three PP welding process guides, each with original conceptual SVG visuals and a README. |
| `wastewater/` | Conceptual process flow references for conventional precipitation, sludge dewatering, and acid recovery. |
| `media/videos/` | Curated links and notes. No third-party video files are redistributed. |

## Recommended starting design

For a conventional sulfuric-acid anodizing tank, begin with a removable, top-supported cathode assembly. Attach the cathode plates to a header bar, support the assembly at the tank rim or on an independent frame, keep electrical joints above the solution, and avoid drilling through the wetted PP wall unless the tank fabricator has designed and sealed the penetration. Confirm tank capacity, chemistry compatibility, electrical design, dimensions, and the governing process specification before fabrication.

The Aluminum Anodizers Council bulletin supplied with the project identifies aluminum cathodes as a lower-resistance alternative to lead in sulfuric-acid anodizing. It specifies alloy and placement considerations, gives a 250 mm (10 in.) minimum anode-to-cathode spacing, and describes attachment and maintenance. See the [public bulletin](https://cdn.ymaws.com/anodizing.site-ym.com/resource/resmgr/Docs/Technical_Bulletin_1-00_Sulf.pdf). The bulletin is copyrighted; this repository links to it and paraphrases key design points rather than redistributing the supplied PDF.

## Important scope and safety note

These files are preliminary study aids, not approved fabrication drawings, operating procedures, or environmental permits. The schematics are conceptual and not to scale. A qualified tank fabricator and plant electrical/process engineer must check loads, PP creep and temperature limits, chemical compatibility, current distribution, lifting points, electrical isolation, and process approval. Wastewater selection depends on measured flow and chemistry, applicable discharge limits, sludge classification, and site-specific trials. Follow the facility's chemical handling, lockout, ventilation, PPE, and waste rules.

“All methods” here means the main practical configurations identified for comparison, not every possible proprietary or site-specific design. A wall-penetrating support is included as a comparison option but is not the default recommendation.

## Visuals and video

All diagrams in this repository are original vector schematics authored for this guide. They show relative arrangement only and contain no fabrication dimensions. See `media/videos/README.md` for the limited external video references found; those clips are educational context, not instructions for industrial tank construction.

## Sources

- Aluminum Anodizers Council, [Technical Bulletin #1-00: Sulfuric Acid Anodizing with Aluminum Cathodes](https://cdn.ymaws.com/anodizing.site-ym.com/resource/resmgr/Docs/Technical_Bulletin_1-00_Sulf.pdf).
- Larry Chesterfield, [Anode: Cathode, Materials, and Surface Area Ratios for Aluminum Anodizing](https://finishingandcoating.com/index.php/anodizingcat/1867-anode-cathode-materials-and-surface-area-ratios-for-aluminum-anodizing), Finishing & Coating.
- [Properly Installing Anodizing Cathodes](https://finishingandcoating.com/index.php/anodizingcat/1465-properly-installing-anodizing-cathodes), Finishing & Coating.
- [Custom Plating & Anodizing Process Tanks](https://www.protank.com/custom-plating-anodizing-tanks), Protank.
- Saunders, Sezgin, and Kutz, [Treatment of Aluminum-Finishing Wastewaters and Sludges](https://p2infohouse.org/ref/27/26524.pdf).
- Finnish Water Utilities Association, [Finnish Industrial Wastewater Guide](https://www.vvy.fi/site/assets/files/1110/finnish_industrial_wastewater_guide.pdf).
- Türk, Zoungrana, and Çakmakci, [Chemical precipitation and membrane distillation process for the treatment of acidic anodic oxidation wastewaters](https://doi.org/10.1016/j.jece.2022.108036).
- Yuzer et al., [Application of electrodialysis to recover nitric acid from aluminum finishing industry waste](https://www.deswater.com/DWT_articles/vol_172_papers/172_2019_199.pdf).

## Contributions

When adding a method, include a clear description, advantages, limitations, required verification, and an original or properly licensed visual. Cite external technical claims and distinguish measured results from rules of thumb. Do not add third-party copyrighted PDFs, images, or videos without permission.
