# Crosswalk to the requested ACS Perspective

Zhuang et al., [“Materials Databases: Foundations of Modern Digital Materials”](https://doi.org/10.1021/prechem.5c00449), *Precision Chemistry* **4** (2026), 1087–1102. Publisher metadata and the full text were inspected on 2026-11-01.

The Perspective distinguishes bulk computation, surfaces/interfaces, and experimental databases; it connects data infrastructure to GNNs, MLIPs and AI agents. It emphasizes interoperable schemas, provenance, experimental conditions, missing negative results, cross-code consistency, and the gap between idealized surfaces and operating environments. Its numerical tables are useful historical context rather than a substitute for versioned provider evidence.

| Coverage in the paper | MatVerse destination |
|---|---|
| AFLOW, MP, OQMD, NOMAD | [Bulk](catalog/bulk_computed.md) and [resources](resources.md) |
| OCP, Catalysis-Hub, CatApp, single-atom catalysts, DigCat | [Surfaces](catalog/surfaces_catalysis.md) and [resources](resources.md) |
| ICSD, COD, CSD, MPDS | [Crystallography](catalog/experimental_crystallography.md) |
| DigBat, DigHyd, Digital Hydrogen-S, Battery Archive | [Experimental properties](catalog/experimental_properties.md) and [resources](resources.md) |
| OPTIMADE and provenance infrastructure | [Resources](resources.md) |

MatVerse's implementation choices are separate: retain explicit units, preserve release scope, attach primary evidence, leave unknown counts unranked, and separate navigation resources. Provider discrepancies and unavailable primary totals remain visible in the cards. No figures or full tables from the article are reproduced.
