# Public superconductivity source audit

Verified 2026-11-01. Four proposed dataset records and seven resource records; canonical data and UI were not edited.

## Count and provenance decisions

- UCI is a frozen, composition-only derivative of the original NIMS SuperCon. Its two files share 21,263 rows; these are not two independent datasets or 21,263 new crystal structures. Official dataset DOI: [10.24432/C53P47](https://doi.org/10.24432/C53P47). The primary paper DOI was independently checked: [10.1016/j.commatsci.2018.07.052](https://doi.org/10.1016/j.commatsci.2018.07.052).
- WebHTS and SRD 62 are one corpus with two IEEE routes. The public search page is still reachable and says “Last Update to Data Content: 1996.” No end-of-service declaration was found. Its current measurement/material total remains unknown. This is evaluated historical literature data, not an unrestricted CIF release.
- OSD’s publication cohort has 110 materials, 184 CSD crystal structures and 440 measured properties. It includes conductors and nonsuperconducting correlated states. Those three numbers count different entities. Public HTTP pages were reachable; HTTPS retrieval failed. Data licensing and redistribution of CSD coordinates remain unverified.
- Robinson’s primary Figshare collection metadata says version 23, 24 public articles; listing the articles returns the same 24 datasets. They characterize wire/film products over many conditions and do not represent 24 unique bulk compounds or 24 scalar observations. Individual data use CC BY 4.0.
- CERN SMaLi is coded property functions and engineering models, including HTS/LTS critical-current functions. It belongs among resources. Historical Roberts tables and the archived Wikipedia list also remain resources, not independent ranked datasets.
- SCLib was an additional public primary-source lead outside IEEE. Its results retain source/sample/condition and model-review labels, but individual expert verification is pending. It is retained as a resource; project CC BY 4.0 does not override original upstream terms.
- Existing MDR SuperCon, SuperBand, 3DSC_MP/ICSD and JARVIS 3D/2D records were not duplicated. Experimental Tc, calculated phonon-mediated Tc, structure matches and engineered-wire critical-current curves remain distinct label types.

## All thirteen IEEE scientific routes

| Route | Stable public URL | Treatment |
|---|---|---|
| CSC Wiki | [CSC Wiki](https://wiki.ieeecsc.org/) | Community property-reference portal; no independently verified count/export. |
| Archived Wikipedia list | [Archived Wikipedia list](https://webdisk.science.upjs.sk/~martin_gmitra/Theory%20of%20Condensed%20Matter/Supporting%20Materials/11/List_of_superconductors_wikipedia.pdf) | Historical reference list, not an independent experimental dataset. |
| UCI Superconductivty Data | [UCI Superconductivty Data](https://archive.ics.uci.edu/dataset/464/superconductivty+data) | Added: 21,263 composition-only regression instances; SuperCon derivative. |
| NIST SRD 62 metadata | [NIST SRD 62 metadata](https://data.nist.gov/od/id/ECBCC1C130112ED9E04306570681B10723) | Same WebHTS corpus as the next route; official DOI 10.18434/T4KP8J. |
| NIST legacy WebHTS portal | [NIST legacy WebHTS portal](https://srdata.nist.gov/CeramicDataPortal/hit) | Reachable query portal; data content last updated 1996. |
| Roberts survey | [Roberts survey](https://srd.nist.gov/jpcrdreprint/1.555540.pdf) | Published 1976, literature through March 1975; reference tables. |
| Roberts 1978 supplement | [Roberts 1978 supplement](https://books.google.com/books?id=bbHgTVWyFlkC) | NBS TN 983; prefer the official stable DOI https://doi.org/10.6028/NBS.TN.983. |
| Clark OSD | [Clark OSD](http://osd.clarku.edu/public/about) | Added: historical 184 CSD structures / 110 materials / 440 measured properties. |
| Materials Project | [Materials Project](https://next-gen.materialsproject.org) | Already cataloged parent database; not a separate superconductivity acquisition. |
| NIMS MatNavi | [NIMS MatNavi](https://mits.nims.go.jp) | Already cataloged portal; this umbrella route is not another SuperCon release. |
| MDR SuperCon Datasheet | [MDR SuperCon Datasheet](https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2) | Already cataloged SuperCon parent/source; no duplicate addition. |
| Robinson critical-current data | [Robinson critical-current data](https://htsdb.wimbush.eu/about) | Added: 24 wire/film characterization datasets; stable archive DOI 10.6084/m9.figshare.c.2861821. |
| CERN materials | [CERN materials](https://steam.docs.cern.ch/libraries/materials/) | Added as SMaLi coded-property-model resource, not a ranked crystal dataset. |

The original Google Books route included presentation parameters; the stable book-ID link above preserves the source without those parameters. No signed download URLs or authentication values are retained.

## License and access limits

- [UCI](https://archive.ics.uci.edu/dataset/464/superconductivty+data) explicitly licenses its released benchmark CC BY 4.0. This does not imply that the full parent SuperCon collection has identical terms.
- [NIST SRD terms](https://www.nist.gov/open/license) distinguish copyrighted Standard Reference Data from other government employee works; WebHTS is not labeled CC0/public domain here.
- [Robinson documentation](https://htsdb2.wimbush.eu/about) explicitly gives CC BY 4.0 to individual datasets. The collection’s [archival DOI](https://doi.org/10.6084/m9.figshare.c.2861821) is preferred over relying solely on the JavaScript visualizer.
- OSD’s 2022 paper is open access, but no blanket dataset-license statement was established. The dataset row preserves that uncertainty.
- No service termination is inferred from a timeout, JavaScript-only response or failed HTTPS request. No current termination declaration was found for the new WebHTS/OSD/Robinson sources.

## Response provenance

Successful public-response SHA-256 hashes are retained below. Full transient HTML was not retained in the deliverables.

| Source | SHA-256 |
|---|---|
| [https://ieeecsc.org/learning-hub/superconductor-databases-resources](https://ieeecsc.org/learning-hub/superconductor-databases-resources) | `57a116bba316278eac12864702ab2e4fb6aef369527db066a9f0490df1effb6c` |
| [https://archive.ics.uci.edu/dataset/464/superconductivty+data](https://archive.ics.uci.edu/dataset/464/superconductivty+data) | `43f88fa8d46d22c2c8842ca9ec8462097d6da5f6bd1d34c960a7194fd5d6e804` |
| [https://archive.ics.uci.edu/api/dataset?id=464](https://archive.ics.uci.edu/api/dataset?id=464) | `592d1ce297f91b1815335f296299157dc2968051e939d433e0d432ae6e7b9898` |
| [https://data.nist.gov/pdr/lps/ECBCC1C130112ED9E04306570681B10723](https://data.nist.gov/pdr/lps/ECBCC1C130112ED9E04306570681B10723) | `f1376c6c24fd6d835c7b4c2f53c759464c4abd8ac7d3bda4ea6ad31302a14f6d` |
| [https://data.nist.gov/od/id/ECBCC1C130112ED9E04306570681B10723](https://data.nist.gov/od/id/ECBCC1C130112ED9E04306570681B10723) | `6796d611945ddce2c9d88848c7baea6812c7b3c8861f808c7e908ee7a1475d39` |
| [http://osd.clarku.edu/public/about](http://osd.clarku.edu/public/about) | `cb847d6d1d6a0006376122a3df96a081dcca73b045bd750233389869cb150794` |
| [https://api.figshare.com/v2/collections/2861821](https://api.figshare.com/v2/collections/2861821) | `1a561fa27262786de44939497510afb86d9e79b9b6aa123525fe22278f59dd5c` |
| [https://api.figshare.com/v2/collections/2861821/articles?page_size=100](https://api.figshare.com/v2/collections/2861821/articles?page_size=100) | `041c82bca5781395ca4fc8cca466cccc1be67840d52a469473c82e4653b23b1c` |
| [https://api.crossref.org/works/10.1016/j.commatsci.2018.07.052](https://api.crossref.org/works/10.1016/j.commatsci.2018.07.052) | `8902bbac0334b764b2bb62ab3aabc3d32f8355076a3f4002e0746974e14181f4` |
| [https://steam-material-library.docs.cern.ch/](https://steam-material-library.docs.cern.ch/) | `062f6af031d7f3ce344f30aec5ff8b2787ea6139725f9391fc75de4bb3a98d62` |
| [https://jzis.org/materials](https://jzis.org/materials) | `2f265958f118e1b27214f8dab429356546b61b238c197d69865826d14eba4b5c` |
| [https://raw.githubusercontent.com/JackZH26/SCLib_JZIS/main/DATA_SOURCES.md](https://raw.githubusercontent.com/JackZH26/SCLib_JZIS/main/DATA_SOURCES.md) | `18acc55d8b0440a65fa9cecc352bb2f04e3584e372b10a5642aed01b74fdfa8d` |
