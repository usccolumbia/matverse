# MatVerse source links

Link inventory checked 2026-11-01. This file combines every official route and evidence URL in the maintained catalog, navigation-resource sources, the two requested source collections, and supporting perspective references.

Collection-listed links are discovery leads. Their presence here does not mean every destination is still accessible, every resource supplies crystal coordinates, or every count/license has been verified. Crystal-related additions enter the ranked catalog only with their own evidence; adjacent molecular, polymer, engineering and handbook resources remain labeled in the collection inventories.

## Source collections supplied by the user

### [blaiszik/awesome-matchem-datasets](<https://github.com/blaiszik/awesome-matchem-datasets>)

Inspected revision: `d3b1d551eb6abcfd2ea62bcd75ac18c9471900c8`.

Inspection boundary and caveats:

- Complete pinned raw README audited, including dataset tables, TODO, resources, other links and full changelog.
- All external HTTP(S) Markdown and bare URLs extracted; repeated links retained when label or section differs. Pure internal anchors and non-URL placeholders omitted.
- Tracking parameters dropped; only public content selector query keys retained. No credentials or access-bearing query parameters exported.
- Scope tags are triage, not primary scientific validation. Collection counts and licences are not treated as authoritative dataset evidence.
- Molecular, polymer, protein, reaction, CFD and engineering links remain in extraction as adjacent resources rather than becoming crystal datasets.
- Existing canonical catalog has 115 datasets and 27 resources at comparison time. Exact-URL mismatches can be aliases or derivatives, so missing candidates require identity review.
- Important missing names for verification: 2D Alloy Database, Experimental 2D Materials Database (X2DB), Quantum-Chemical Bonding Database (LOBSTER), ARROWS³ Synthesis Dataset, ZeoSyn, MatSyn25, Carbon Data, AQCat25, OCx24, A-Lab, CAMEO, Perovskite Database Project, MatText, TextEdge, LLM4Mat
- Raw table exact-URL unmatched candidates: OMat24 (Meta), OMC25, Vector-QM24, C2DB, CoRE MOF 2019, QMOF Database, ODAC23, MOFX-DB, Carbon Data, Quantum‑Chemical Bonding DB (LOBSTER), Matbench Discovery, AQCat25, van der Waals Bilayer Database (BiDB), Van der Waals 2D Heterostructure Database (HetDB), Quantum Point Defects Database (QPOD), 2D Alloy Database, MAD (Massive Atomic Diversity), NIST ICSD (subset), CSD (Cambridge), opXRD, MDR SuperCon, OCx24, CoRE MOF 2024, Experimental 2D Materials Database (X2DB), ARROWS³ Synthesis Dataset, A-Lab (Autonomous Inorganic Synthesis), CAMEO (Closed-Loop Autonomous Exploration), MatText, TextEdge, LAMBench-TrainingSet-v1, LLM4Mat, Mat-Instructions, Open Materials Guide (OMG), MatSyn25, L2M3 - Large Language Model MOF Miner, ZeoSyn
- Eight proposed primary-verified additions are in research/collection_blaiszik_additions.json; canonical data was not modified.
- ARROWS Zenodo 8331001 resolves to software njszym/ARROWS v0.0.1 (other-open licence), not by itself a verified 241-experiment dataset; the 241 count was not copied.
- LOBSTER original 2023 Zenodo release has 1520 compounds. Newer NOMAD DOI10.17172/nomad.mc38-9gm1 resolves via DataCite, but collection claim 13800 was not independently verified.
- Carbon-data headline counts 22.9 million atomic environments; provider arithmetic yields 114660 MD snapshots. Labels are from C-GAP-17, not new DFT.
- OCx24 pinned raw CSV has 5412 tests and 672 sample IDs, while clean/processed subsets differ. Collection 572-sample summary was not reused.
- AQCat25 has gated file access and CC BY-NC-SA 4.0 terms; public card access is not unrestricted file access.
- X2DB contains metadata records and explicitly no measurement datasets.
- Existing canonical matches with alternate URLs (for example C2DB, OMat24, CoRE MOF, MAD and OpenLAM) are not new datasets merely because an exact-URL comparison misses them.
- Validated exported URL queries for access-bearing keys and rejected private Figshare /s/ paths; no such URLs remain.

274 labeled link occurrences; 218 distinct URLs. Section and scope labels preserve the collection context.

| Linked source | Original section | Scope |
|---|---|---|
| [BOOM: Benchmarks for Out-Of-distribution Molecules](<https://github.com/FLASK-LLNL/BOOM>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [MSR-ACC/TAE25](<https://doi.org/10.5281/zenodo.15387279>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [OMat24 (Meta)](<https://huggingface.co/datasets/fairchem/OMAT24>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [OMol25 (Meta)](<https://huggingface.co/facebook/OMol25>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [OMC25](<https://huggingface.co/facebook/OMC25>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Materials Project (LBL)](<https://materialsproject.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Open Catalyst 2020 (OC20)](<https://opencatalystproject.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [AFLOW](<https://aflow.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [OQMD](<https://oqmd.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [JARVIS-DFT (NIST)](<https://jarvis.nist.gov>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Carolina Materials DB](<http://www.carolinamatdb.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [NOMAD](<https://nomad-lab.eu/prod/v1/gui/search/entries/search/entries>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [MatPES](<https://matpes.ai>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Vector-QM24](<https://doi.org/10.5281/zenodo.11164951>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [AIMNet2 Dataset](<https://doi.org/10.1184/R1/27629937.v1>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [RDB7](<https://zenodo.org/records/13328872>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [RDB19-Rad](<https://zenodo.org/records/11493786>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [QCML](<https://zenodo.org/records/14859804>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [QM9](<http://quantum-machine.org/datasets/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [QM7/QM7b](<http://quantum-machine.org/datasets/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [QMugs](<https://www.openqdc.io/datasets/qmugs>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [C2DB](<https://c2db.fysik.dtu.dk>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [ANI-1x / 1ccx](<https://qcawebapps.molssi.org/ml_datasets/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [CoRE MOF 2019](<https://pubs.acs.org/doi/10.1021/acs.jced.9b00835>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [QMOF Database](<https://figshare.com/articles/dataset/QMOF_Database/13147324>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Catalysis-Hub](<https://www.catalysis-hub.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [ODAC23](<https://fair-chem.github.io/dac/datasets/odac.html>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [MOFX-DB](<https://doi.org/10.1021/acs.jced.2c00583>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [LeMat-Bulk](<https://huggingface.co/datasets/LeMaterial/LeMat-Bulk>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [LeMat-Traj](<https://huggingface.co/datasets/LeMaterial/LeMat-Traj>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [NeurIPS Open Polymer Prediction 2025](<https://www.kaggle.com/competitions/neurips-open-polymer-prediction-2025/data>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Carbon Data](<https://github.com/jla-gardner/carbon-data>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [MSR-ACC/TAE25](<https://zenodo.org/records/15387280>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [DFT Solvation Energy Dataset](<https://www.doi.org/10.18126/jos5-wj65>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [MD Simulated Monomer Properties](<https://doi.org/10.18126/8p6m-e135>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Multimodal Spectroscopic Dataset](<https://github.com/rxn4chemistry/multimodal-spectroscopic-dataset>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [PubChemQCR](<https://huggingface.co/datasets/divelab/PubChemQCR>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [MP-ALOE](<https://figshare.com/articles/dataset/MP-ALOE_An_r2SCAN_dataset_for_universal_machine_learning_interatomic_potentials/29452190>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [Alexandria DB](<https://alexandria.icams.rub.de>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Quantum‑Chemical Bonding DB (LOBSTER)](<https://doi.org/10.17172/nomad.mc38-9gm1>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [MultixcQM9 (OpenQDC)](<https://www.openqdc.io/datasets>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [SPICE (OpenQDC)](<https://www.openqdc.io/datasets>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Matbench v0.1](<https://matbench.materialsproject.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Matbench Discovery](<https://matbench-discovery.materialsproject.org/data>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Materials Cloud Archives](<https://archive.materialscloud.org>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [MS25](<https://zenodo.org/records/10901820>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [RadonPy Polymer Properties Data](<https://github.com/RadonPy/RadonPy/blob/648c9a492808339c9bb7ad2c1137e5a7b07614ca/data/PI1070.csv>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [SHNITSEL Data](<https://doi.org/10.5281/zenodo.15482819>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Frustrated Lewis Pairs Database](<https://jingyun-ye.github.io/FLPDB/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [AQCat25](<https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [OMol25 Electronic Structures](<https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25_elec.md>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Unrestricted CCSD(T) Dataset For Organic Molecule Reactions](<https://figshare.com/articles/dataset/Unrestricted_CCSD_T_Dataset_For_Organic_Molecule_Reactions/30267877?file=58465231>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [MC-PDFT-OPESf](<https://github.com/Ferg-Lab/PDFT_OPESf>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [Quantum Cluster Database](<https://muellergroup.jhu.edu/qcd/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [The Cambridge Cluster Database](<https://www-wales.ch.cam.ac.uk/CCD.html>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Battery Electrolyte Solvation/Ionization](<https://doi.org/10.5281/zenodo.15252439>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [van der Waals Bilayer Database (BiDB)](<https://bidb.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Van der Waals 2D Heterostructure Database (HetDB)](<https://hetdb.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [Quantum Point Defects Database (QPOD)](<https://qpod.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [2D Alloy Database](<https://cmrdb.fysik.dtu.dk/2dalloys/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [OC25 (Open Catalyst 2025)](<https://huggingface.co/facebook/OC25>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [OPoly26 (Open Polymers 2026)](<https://huggingface.co/datasets/colabfit/OPoly26-train>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [MAD (Massive Atomic Diversity)](<https://archive.materialscloud.org/records/xdsbt-a3r17>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | crystal_related |
| [qcMol](<https://structpred.life.tsinghua.edu.cn/qcmol/>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | adjacent |
| [Transition1x](<https://doi.org/10.6084/m9.figshare.19614657>) | Awesome Materials & Chemistry Datasets / Datasets / Computational Datasets | uncertain |
| [Crystallography Open Database (COD)](<https://www.crystallography.net/cod>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [NIST ICSD (subset)](<https://icsd.products.fiz-karlsruhe.de>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [CSD (Cambridge)](<https://www.ccdc.cam.ac.uk>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [opXRD](<https://doi.org/10.5281/zenodo.14254270>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [MDR SuperCon](<https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [ChEMBL](<https://www.ebi.ac.uk/chembl/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [MoleculeNet](<http://moleculenet.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [ESOL](<http://moleculenet.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [FreeSolv](<https://github.com/MobleyLab/FreeSolv>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Lipophilicity](<https://www.ebi.ac.uk/chembl/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | uncertain |
| [PCBA](<https://pubchem.ncbi.nlm.nih.gov/bioassay>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [HIV](<https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | uncertain |
| [BACE](<http://moleculenet.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [BBBP](<http://moleculenet.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Tox21](<https://tripod.nih.gov/tox21/challenge/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [ToxCast](<https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [SIDER](<http://sideeffects.embl.de/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [ClinTox](<http://moleculenet.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [PDBbind](<http://www.pdbbind.org.cn/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [BindingDB](<https://www.bindingdb.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [ProtBENCH](<https://github.com/hevalatas/ProtBENCH>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [PDBench](<https://github.com/wells-wood-research/PDBench>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [PDB-Struct](<https://github.com/WANG-CR/PDB-Struct>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [HTEM-DB](<https://htem.nrel.gov>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [OCx24](<https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/applications/ocx/data>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [Polymer Genome](<https://khazana.gatech.edu/dataset/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [CoRE MOF 2024](<https://www.ccdc.cam.ac.uk/support-and-resources/downloads/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [SAIR](<https://pub.sandboxaq.com/data/ic50-dataset>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Anion Solvation DB](<https://doi.org/10.5281/zenodo.13987781>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [BigSolDB](<https://doi.org/10.5281/zenodo.6809668>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [StarryData2](<https://github.com/starrydata/starrydata_datasets>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [CRIPT Polymer Data](<https://www.criptapp.org>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Catechol Benchmark](<https://www.kaggle.com/datasets/aichemy/catechol-benchmark>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Leeds Solubility Data](<https://doi.org/10.5281/zenodo.3686213>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [BigSolDB 2.0](<https://doi.org/10.5281/zenodo.15094979>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [OpenExp](<https://osf.io/e68v4/files/3dv4k>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | uncertain |
| [Battery Imaging Library (BIL)](<https://www.batteryimaginglibrary.com>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Experimental 2D Materials Database (X2DB)](<https://x2db.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [NMRexp](<https://zenodo.org/records/17296666>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [OpenBind (first release)](<https://openbind.uk>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [SAFE Database (LANL)](<https://safe.lanl.gov>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | uncertain |
| [ARROWS³ Synthesis Dataset](<https://doi.org/10.5281/zenodo.8331001>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [NIST AM-Bench](<https://www.nist.gov/ambench/am-bench-2025-measurements-and-challenge-problems>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Ti-6Al-4V LPBF Process–Structure–Property](<https://zenodo.org/records/6587905>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [AlSi10Mg LPBF Process–Structure–Property](<https://zenodo.org/records/10008435>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [UHCSDB (Ultra-High Carbon Steel Micrographs)](<http://uhcsdb.materials.cmu.edu>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Aurora Robotic Battery Platform](<https://zenodo.org/records/15481956>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [A-Lab (Autonomous Inorganic Synthesis)](<https://www.nature.com/articles/s41586-023-06734-w>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [AlphaFlow](<https://github.com/AbolhasaniLab/AlphaFlow>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Swiss Cat+ CO₂ Hydrogenation HTE](<https://zenodo.org/doi/10.5281/zenodo.8314734>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [CAMEO (Closed-Loop Autonomous Exploration)](<https://data.nist.gov/od/ds/mds2-2480/CAMEO_NComm-master.zip>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | crystal_related |
| [Olympus SDL Benchmarks](<https://github.com/aspuru-guzik-group/olympus>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Perovskite Database Project](<https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Dreher–Doyle Buchwald–Hartwig HTE](<https://github.com/rxn4chemistry/rxn_yields>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Pfizer Suzuki–Miyaura HTE](<https://github.com/rxn4chemistry/rxn_yields>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [Pfizer HiTEA](<https://github.com/emmaking-smith/HiTEA>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [AstraZeneca ELN Buchwald–Hartwig](<https://github.com/nsf-c-cas>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | uncertain |
| [Minerva HTE](<https://github.com/schwallergroup/minerva>) | Awesome Materials & Chemistry Datasets / Datasets / Experimental Datasets | adjacent |
| [ChemPile](<https://huggingface.co/collections/jablonkagroup/chempile-6824e88c60d3286ba9b0dae1>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [SmolInstruct](<https://huggingface.co/datasets/osunlp/SMolInstruct>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [CAMEL](<https://huggingface.co/datasets/camel-ai/chemistry>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ChemNLP](<https://github.com/OpenBioML/chemnlp>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ChemQA](<https://github.com/ChemFoundationModels/ChemLLMBench>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ChemLLMBench](<https://github.com/ChemFoundationModels/ChemLLMBench>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ChemistryQA](<https://github.com/microsoft/chemistry-qa>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [MaScQA](<https://github.com/abhijeetgangan/MaSTeA>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [SciCode](<https://scicode-bench.github.io>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [ChemData 700K](<https://huggingface.co/datasets/AI4Chem/ChemData700K>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MatSci-Instruct (HoneyBee)](<https://zenodo.org/record/10119842>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [MoleculeQA](<https://huggingface.co/datasets/hcaoaf/MoleculeQA>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [BioInstruct 25K](<https://huggingface.co/datasets/bio-nlp-umass/bioinstruct>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [Lab-Bench](<https://huggingface.co/datasets/futurehouse/lab-bench>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [ChemBench 4K](<https://huggingface.co/datasets/AI4Chem/ChemBench4K>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [GPQA Diamond](<https://github.com/idavidrein/gpqa>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MaCBench](<https://macbench.lamalab.org>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ChemBench](<https://chembench.lamalab.org>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MatText](<https://huggingface.co/datasets/n0w0f/MatText>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [SciAssess](<https://github.com/sci-assess/SciAssess>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [ZINC20-ML](<https://files.docking.org/zinc20-ML/>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [PMC Open Access Subset](<https://huggingface.co/datasets/pmc/open_access>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [MatScholar Task-Schema QA (MatSci-NLP)](<https://github.com/BangLab-UdeM-Mila/NLP4MatSci-ACL23>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [Mol-Instructions](<https://huggingface.co/collections/zjunlp/mol-instructions-662e0b9435ab6df9593e8ea0>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [USPTO-LLM](<https://zenodo.org/records/14396156>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [ChemRxivQuest](<https://arxiv.org/abs/2505.05232>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [USPTO-Lowe](<https://figshare.com/articles/dataset/5104873>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MolTextNet](<https://huggingface.co/datasets/liuganghuggingface/moltextnet>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MolOpt-Instructions](<https://huggingface.co/datasets/blazerye/MolOpt-Instructions>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [TextEdge](<https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [LAMBench-TrainingSet-v1](<https://aissquare.com/datasets/detail?pageType=datasets&name=LAMBench-TrainingSet-v1&id=308>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [LLM4Mat](<https://drive.google.com/drive/folders/1HpGhuNHG4EQCQMZaKPwEQNH9stJKw-ht>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [LLM-EO](<https://github.com/deepprinciple/llmeo>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [Flavor Analysis and Recognition Transformer](<https://github.com/fart-lab/fart/tree/main/dataset>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [SCQA (Solar Cell QA)](<https://huggingface.co/collections/CambridgeMolecularEngineering/solar-cell-qa-datasets-67b398f1b9c0f0dd7600a159>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ScienceQA](<https://scienceqa.github.io/>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [SciBench](<https://scibench-ucla.github.io>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MegaScience](<https://huggingface.co/MegaScience>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [Mat-Instructions](<https://github.com/AI4MOL/Mat-Instruction>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [Open Materials Guide (OMG)](<https://huggingface.co/datasets/iknow-lab/open-materials-guide-2024>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [ChemDFM](<https://github.com/OpenDFM/ChemDFM>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [ChemTable](<https://github.com/lqzxt/ChemTable>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [ChemCoTBench](<https://huggingface.co/datasets/OpenMol/ChemCoTDataset>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [SciCUEval](<https://arxiv.org/abs/2505.15094>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [MatSciBench](<https://arxiv.org/abs/2510.12171>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | adjacent |
| [MolecularIQ](<https://github.com/ml-jku/moleculariq>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | uncertain |
| [MatSyn25](<https://huggingface.co/datasets/MatSynAI/MatSyn25>) | Awesome Materials & Chemistry Datasets / Datasets / LLM Training Datasets | crystal_related |
| [PubChem](<https://pubchem.ncbi.nlm.nih.gov>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | adjacent |
| [Open Reaction Database (ORD)](<https://open-reaction-database.org>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [PatCID (IBM)](<https://github.com/DS4SD/PatCID>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [MatScholar](<https://matscholar.com>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [Matbench (metadata/text tasks)](<https://matbench.materialsproject.org/>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | crystal_related |
| [OpenQDC Hub](<https://github.com/valence-labs/openQDC>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | adjacent |
| [L2M3 - Large Language Model MOF Miner](<https://figshare.com/articles/dataset/L2M3_Database/27187917>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | crystal_related |
| [RetroRules 2026](<https://retrorules.org>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [Text-Mined Solid-State Synthesis (CederGroup)](<https://github.com/CederGroupHub/text-mined-synthesis_public>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | crystal_related |
| [Text-Mined Solution-Based Synthesis (CederGroup)](<https://github.com/CederGroupHub/text-mined-solution-synthesis_public>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | crystal_related |
| [Solid-State Synthesis w/ Impurity Phases](<https://doi.org/10.6084/m9.figshare.30423274>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | crystal_related |
| [ZeoSyn](<https://github.com/eltonpan/zeosyn_dataset>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | crystal_related |
| [PaRoutes](<https://github.com/MolecularAI/PaRoutes>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [USPTO-50k (Schneider)](<https://figshare.com/articles/dataset/USPTO-50K_raw_/25459573>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | adjacent |
| [Syntheseus](<https://github.com/microsoft/syntheseus>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [mech-USPTO-31k](<https://doi.org/10.6084/m9.figshare.24797220>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | adjacent |
| [PMechDB (Polar Mechanism DB)](<https://deeprxn.ics.uci.edu/pmechdb/download>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [RMechDB (Radical Mechanism DB)](<https://deeprxn.ics.uci.edu/rmechdb>) | Awesome Materials & Chemistry Datasets / Datasets / Literature-mined & Text Datasets | uncertain |
| [PDEBench](<https://github.com/pdebench/PDEBench>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [BLASTNet](<https://blastnet.github.io>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [Johns Hopkins Turbulence DB (JHTDB)](<https://turbulence.pha.jhu.edu>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [Airfoil CFD 2k](<https://data.openei.org/submissions/5970>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [PDEArena (collection)](<https://huggingface.co/pdearena>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [WeatherBench 2](<https://github.com/pangeo-data/WeatherBench>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [UT Austin Channel-DNS Suite](<https://turbulence.oden.utexas.edu>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [Compressible TPC DNS DB](<https://data.mendeley.com/datasets/wt8t5kxzbs>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [Curated RANS ↔ DNS Dataset](<https://doi.org/10.34740/kaggle/dsv/2637500>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [NASA Common Research Model (CRM)](<https://commonresearchmodel.larc.nasa.gov>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [Darcy-Flow (FNO)](<https://github.com/neuraloperator/neuraloperator>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [HiFi-TURB LES/DNS](<https://cordis.europa.eu/project/id/814837>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [NASA High Lift Prediction Workshop (HLPW)](<https://hiliftpw.larc.nasa.gov/>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [High-Speed TBL DNS DB](<https://arc.aiaa.org/doi/10.2514/1.J063456>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [ML Turbulence (Kaggle)](<https://www.kaggle.com/datasets/ryleymcconkey/ml-turbulence-dataset>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [AgentFEM Material Loading Memory](<https://huggingface.co/datasets/HaomingLuo/AgentFEM-Material-Loading-Memory>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [AgentFEM Controlled Transient Heat](<https://huggingface.co/datasets/HaomingLuo/AgentFEM-Controlled-Transient-Heat>) | Awesome Materials & Chemistry Datasets / Datasets / 🌊 Computational Fluid Dynamics, PDE & Engineering Datasets | adjacent |
| [PoLyInfo](<https://polymer.nims.go.jp/en/>) | Awesome Materials & Chemistry Datasets / Datasets / Proprietary Datasets (for reference) | adjacent |
| [The Materials Data Facility](<https://www.materialsdatafacility.org>) | Awesome Materials & Chemistry Datasets / Datasets / Dataset Resources | crystal_related |
| [Foundry-ML](<https://materialsdatafacility.org/portal>) | Awesome Materials & Chemistry Datasets / Datasets / Dataset Resources | crystal_related |
| [https://www.openqdc.io/datasets](<https://www.openqdc.io/datasets>) | Awesome Materials & Chemistry Datasets / TODO | uncertain |
| [Data](<https://github.com/Shorku/rhnet/tree/main/data>) | Awesome Materials & Chemistry Datasets / TODO | adjacent |
| [Materials Cloud Datasets](<https://www.materialscloud.org/discover/menu>) | Awesome Materials & Chemistry Datasets / TODO | uncertain |
| [Atomly](<https://atomly.net/#/>) | Awesome Materials & Chemistry Datasets / TODO | crystal_related |
| [https://zenodo.org/records/8091844](<https://zenodo.org/records/8091844>) | Awesome Materials & Chemistry Datasets / TODO | crystal_related |
| [https://zenodo.org/records/8092187](<https://zenodo.org/records/8092187>) | Awesome Materials & Chemistry Datasets / TODO | crystal_related |
| [http://quantum-machine.org/datasets/](<http://quantum-machine.org/datasets/>) | Awesome Materials & Chemistry Datasets / TODO | uncertain |
| [ChemRxivQuest](<https://arxiv.org/abs/2505.05232>) | Awesome Materials & Chemistry Datasets / TODO | adjacent |
| [Awesome Materials Informatics](<https://github.com/tilde-lab/awesome-materials-informatics>) | Awesome Materials & Chemistry Datasets / TODO / Other Links | crystal_related |
| [OC25 (Open Catalyst 2025) — source](<https://huggingface.co/facebook/OC25>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [OPoly26 (Open Polymers 2026) — source](<https://huggingface.co/datasets/colabfit/OPoly26-train>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | adjacent |
| [OPoly26 (Open Polymers 2026) — source](<https://huggingface.co/facebook/OMol25>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | adjacent |
| [MAD (Massive Atomic Diversity) — source](<https://archive.materialscloud.org/records/xdsbt-a3r17>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [qcMol — source](<https://structpred.life.tsinghua.edu.cn/qcmol/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | adjacent |
| [BiDB (van der Waals Bilayer Database) — source](<https://bidb.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [BiDB (van der Waals Bilayer Database) — source](<https://2dhub.org/bidb/bidb.html>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [HetDB (van der Waals 2D Heterostructure Database) — source](<https://hetdb.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [HetDB (van der Waals 2D Heterostructure Database) — source](<https://2dhub.org/hetdb/hetdb.html>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [QPOD (Quantum Point Defects Database) — source](<https://qpod.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [2D Alloy Database — source](<https://cmrdb.fysik.dtu.dk/2dalloys/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [2D Alloy Database — source](<https://2dhub.org/2dalloys/2dalloys.html>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧮 Computational Datasets (8 datasets) | crystal_related |
| [NMRexp — source](<https://zenodo.org/records/17296666>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧪 Experimental Datasets (4 datasets) | adjacent |
| [OpenBind (first release) — source](<https://openbind.uk>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧪 Experimental Datasets (4 datasets) | crystal_related |
| [SAFE Database (LANL) — source](<https://safe.lanl.gov>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧪 Experimental Datasets (4 datasets) | uncertain |
| [X2DB (Experimental 2D Materials Database) — source](<https://x2db.fysik.dtu.dk/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧪 Experimental Datasets (4 datasets) | crystal_related |
| [X2DB (Experimental 2D Materials Database) — source](<https://2dhub.org/x2db/x2db.html>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧪 Experimental Datasets (4 datasets) | crystal_related |
| [RetroRules 2026 — source](<https://retrorules.org>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 📖 Literature-mined & Text Datasets (1 dataset) | adjacent |
| [MolecularIQ — source](<https://github.com/ml-jku/moleculariq>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 📚 LLM Training & Benchmark Datasets (4 datasets) | uncertain |
| [MolecularIQ — source](<https://huggingface.co/spaces/ml-jku/molecularIQ_leaderboard>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 📚 LLM Training & Benchmark Datasets (4 datasets) | uncertain |
| [MatSyn25 (Material Synthesis 2025) — source](<https://huggingface.co/datasets/MatSynAI/MatSyn25>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 📚 LLM Training & Benchmark Datasets (4 datasets) | crystal_related |
| [Text-Mined Solid-State Synthesis (CederGroup / Kononova) — source](<https://github.com/CederGroupHub/text-mined-synthesis_public>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | crystal_related |
| [Text-Mined Solid-State Synthesis (CederGroup / Kononova) — source](<https://doi.org/10.6084/m9.figshare.9722159>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | crystal_related |
| [Text-Mined Solution-Based Synthesis (CederGroup / Wang) — source](<https://github.com/CederGroupHub/text-mined-solution-synthesis_public>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | uncertain |
| [Solid-State Synthesis with Impurity Phases (CederGroup, 2025) — source](<https://doi.org/10.6084/m9.figshare.30423274>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | crystal_related |
| [ZeoSyn — source](<https://github.com/eltonpan/zeosyn_dataset>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | crystal_related |
| [ARROWS³ — source](<https://doi.org/10.5281/zenodo.8331001>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | crystal_related |
| [ARROWS³ — source](<https://github.com/njszym/ARROWS>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🧫 Materials Synthesis Recipes & Precursor Data (5 datasets) | crystal_related |
| [NIST AM-Bench — source](<https://www.nist.gov/ambench/am-bench-2025-measurements-and-challenge-problems>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🏭 Processing → Structure → Property (Causality) (4 datasets) | adjacent |
| [NIST AM-Bench — source](<https://data.nist.gov>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🏭 Processing → Structure → Property (Causality) (4 datasets) | adjacent |
| [Ti-6Al-4V LPBF Process–Structure–Property — source](<https://zenodo.org/records/6587905>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🏭 Processing → Structure → Property (Causality) (4 datasets) | adjacent |
| [AlSi10Mg LPBF Process–Structure–Property — source](<https://zenodo.org/records/10008435>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🏭 Processing → Structure → Property (Causality) (4 datasets) | adjacent |
| [UHCSDB (Ultra-High Carbon Steel Micrograph DB) — source](<http://uhcsdb.materials.cmu.edu>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🏭 Processing → Structure → Property (Causality) (4 datasets) | adjacent |
| [UHCSDB (Ultra-High Carbon Steel Micrograph DB) — source](<https://materialsdata.nist.gov/handle/11256/940>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🏭 Processing → Structure → Property (Causality) (4 datasets) | adjacent |
| [Aurora Autonomous Robotic Battery Platform (Empa) — source](<https://zenodo.org/records/15481956>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | adjacent |
| [A-Lab (Autonomous Inorganic Synthesis, LBNL) — source](<https://www.nature.com/articles/s41586-023-06734-w>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | crystal_related |
| [A-Lab (Autonomous Inorganic Synthesis, LBNL) — source](<https://github.com/CederGroupHub/s4>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | crystal_related |
| [AlphaFlow (NC State) — source](<https://github.com/AbolhasaniLab/AlphaFlow>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | adjacent |
| [Swiss Cat+ CO₂ Hydrogenation HTE — source](<https://zenodo.org/doi/10.5281/zenodo.8314734>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | adjacent |
| [CAMEO (NIST) — source](<https://data.nist.gov/od/ds/mds2-2480/CAMEO_NComm-master.zip>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | crystal_related |
| [Olympus — source](<https://github.com/aspuru-guzik-group/olympus>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | adjacent |
| [Perovskite Database Project (NOMAD) — source](<https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / 🤖 Self-Driving Lab / Autonomous Experimentation & HTE (7 datasets) | adjacent |
| [Dreher–Doyle Buchwald–Hartwig HTE — source](<https://github.com/rxn4chemistry/rxn_yields>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [Pfizer HiTEA — source](<https://github.com/emmaking-smith/HiTEA>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [AstraZeneca ELN Buchwald–Hartwig — source](<https://github.com/nsf-c-cas>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [Minerva HTE — source](<https://github.com/schwallergroup/minerva>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [PaRoutes — source](<https://zenodo.org/records/6275421>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [PaRoutes — source](<https://github.com/MolecularAI/PaRoutes>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [USPTO-50k (Schneider) — source](<https://figshare.com/articles/dataset/USPTO-50K_raw_/25459573>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [USPTO-50k (Schneider) — source](<http://tdcommons.ai/generation_tasks/retrosyn/>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [Syntheseus (Microsoft) — source](<https://github.com/microsoft/syntheseus>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [PMechDB (Polar Mechanism Database) — source](<https://deeprxn.ics.uci.edu/pmechdb/download>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [RMechDB (Radical Mechanism Database) — source](<https://deeprxn.ics.uci.edu/rmechdb>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | uncertain |
| [mech-USPTO-31k — source](<https://doi.org/10.6084/m9.figshare.24797220>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [mech-USPTO-31k — source](<https://github.com/snu-micc/MechFinder>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [Transition1x — source](<https://doi.org/10.6084/m9.figshare.19614657>) | Awesome Materials & Chemistry Datasets / Changelog / June 2026 / ⚗️ Reaction & Synthesis Planning (12 datasets) | adjacent |
| [repository commit history](<https://github.com/your-repo/commits>) | Awesome Materials & Chemistry Datasets / Changelog / Earlier Updates | uncertain |

### [JARVIS-Tools Notebooks](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks>)

Inspected revision: `e9a794b94e1aadfe86460fd9b884fa345dc3b001`.

Inspection boundary and caveats:

- Extraction boundary: requested repository metadata and README at commit e9a794b94e1aadfe86460fd9b884fa345dc3b001, plus the README of the explicitly linked atomgptlab successor at 9d9496e2ad53795b6dcdd8cd55827647bceb1e5b.
- The requested repository is archived/read-only and says it is no longer maintained. Links in both README documents are inventoried; notebook contents and repository trees were not recursively scraped.
- Notebook/tutorial links are teaching and navigation resources, not additive datasets; linked upstream material families already exist in the canonical catalog.
- Section-based relevance labels are conservative navigational classifications; uncertain notebook links require inspection before dataset promotion.

229 labeled link occurrences; 104 distinct URLs. Section and scope labels preserve the collection context.

| Linked source | Original section | Scope |
|---|---|---|
| [alt text](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/actions/workflows/test-notebooks.yml/badge.svg>) | Requested repository README | crystal_related |
| [https://github.com/atomgptlab/jarvis-tools-notebooks](<https://github.com/atomgptlab/jarvis-tools-notebooks>) | Requested repository README | crystal_related |
| [NIST-JARVIS](<https://jarvis.nist.gov/>) | Requested repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [JARVIS-Tools](<https://jarvis-tools.readthedocs.io/en/master/tutorials.html>) | Requested repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [SlideShare](<https://www.slideshare.net/KAMALCHOUDHARY4>) | Requested repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [https://github.com/knc6/slides](<https://github.com/knc6/slides>) | Requested repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [https://www.youtube.com/@dr_k_choudhary](<https://www.youtube.com/@dr_k_choudhary>) | Requested repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [Introduction to high-performance computing](<https://tacc-reproducible-intro-hpc.readthedocs.io/en/latest/intro_to_hpc/overview.html>) | Requested repository README / Basics | adjacent |
| [Python beginners notebook](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/python_beginners_notebook.ipynb>) | Requested repository README / Basics | adjacent |
| [Silicon atomic structure and analysis example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Silicon_atomic_structure_and_analysis_example.ipynb>) | Requested repository README / Basics | crystal_related |
| [Analyzing_data_in_the_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Analyzing_data_in_the_JARVIS_Leaderboard](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_Leaderboard.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Basic quantum espresso run](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Basic_Example.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_Optoelectronics_Computational_screening_of_high_performance_optoelectronic_materials_using_OptB88vdW_and_TB_mBJ_formalisms](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Optoelectronics_Computational_screening_of_high_performance_optoelectronic_materials_using_OptB88vdW_and_TB_mBJ_formalisms.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_TopologicalSpillage_High_throughput_Discovery_of_Topologically_Non_trivial_Materials_using_Spin_orbit_Spillage](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_TopologicalSpillage_High_throughput_Discovery_of_Topologically_Non_trivial_Materials_using_Spin_orbit_Spillage.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_Solar_Accelerated_Discovery_of_Efficient_Solar_Cell_Materials_Using_Quantum_and_Machine_Learning_Methods](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Solar_Accelerated_Discovery_of_Efficient_Solar_Cell_Materials_Using_Quantum_and_Machine_Learning_Methods.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Si_bandstructure&densityof_states](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Si_bandstructure%26densityof_states.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_Wannier90Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Wannier90Example.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [BoltztrapExample](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/BoltztrapExample.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Making 2D heterostructures](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Making_2D_heterostructures.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_DFT_FormationEnergiesAccuracyCheck](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_FormationEnergiesAccuracyCheck.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Downloading raw analysis data and input/output files](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Download_raw_data_for_webpages.ipynb>) | Requested repository README / Electronic structure | adjacent |
| [JARVIS_DFT_2D_High_throughput_Identification_and_Characterization_of_Two_dimensional_Materials_using_Density_functional_theory](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_2D_High_throughput_Identification_and_Characterization_of_Two_dimensional_Materials_using_Density_functional_theory.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_CONVERG_Convergence_and_machine_learning_predictions_of_Monkhorst_Pack_k_points_and_plane_wave_cut_off_in_high_throughput_DFT_calculations](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_CONVERG_Convergence_and_machine_learning_predictions_of_Monkhorst_Pack_k_points_and_plane_wave_cut_off_in_high_throughput_DFT_calculations.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_DFPT_High_throughput_Density_Functional_Perturbation_Theory_and_Machine_Learning_Predictions_of_Infrared,_Piezoelectric_and_Dielectric_Responses](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFPT_High_throughput_Density_Functional_Perturbation_Theory_and_Machine_Learning_Predictions_of_Infrared%2C_Piezoelectric_and_Dielectric_Responses.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_TE_Data_driven_discovery_of_3D_and_2D_thermoelectric_materials](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_TE_Data_driven_discovery_of_3D_and_2D_thermoelectric_materials.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_ELAST_Elastic_properties_of_bulk_and_low_dimensional_materials_using_van_der_Waals_density_functional](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ELAST_Elastic_properties_of_bulk_and_low_dimensional_materials_using_van_der_Waals_density_functional.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Get JARVIS-DFT final structures in ASE or Pymatgen format](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Get_JARVIS_DFT_final_structures_in_ASE_or_Pymatgen_format.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_QuantumEspressoColab_Designing_High_Tc_Superconductors_with_BCS_inspired_Screening,_Density_Functional_Theory_and_Deep_learning](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Designing_High_Tc_Superconductors_with_BCS_inspired_Screening%2C_Density_Functional_Theory_and_Deep_learning.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_WTBH_Database_of_Wannier_tight_binding_Hamiltonians_using_high_throughput_density_functional_theory](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_WTBH_Database_of_Wannier_tight_binding_Hamiltonians_using_high_throughput_density_functional_theory.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Comapre_MP_JV](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Comapre_MP_JV.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [ParsingWebpages(JARVIS_DFT)](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT>) | Requested repository README / Electronic structure | adjacent |
| [https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb>) | Requested repository README / Electronic structure | adjacent |
| [ConvexHull](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ConvexHull.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [DimensionalityAndExfoliationEnergy](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/DimensionalityAndExfoliationEnergy.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Element_filter_for_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Element_filter_for_JARVIS_DFT_dataset.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [Run GPAW on Google-colab and calculate interface energy with jarvis-tools](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/GPAW_Colab.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [ParsingWebpages(JARVIS_DFT)](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT>) | Requested repository README / Electronic structure | adjacent |
| [https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb>) | Requested repository README / Electronic structure | adjacent |
| [WTBH_MagneticMats.ipynb](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/WTBH_MagneticMats.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [QMCPACK_Basic_Example](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/QMCPACK_Basic_Example.ipynb>) | Requested repository README / Electronic structure | crystal_related |
| [JARVIS_LAMMPS](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_LAMMPS.ipynb>) | Requested repository README / Force-field | crystal_related |
| [MLFF SNAP training](<https://colab.research.google.com/github/FitSNAP/FitSNAP/blob/master/tutorial.ipynb>) | Requested repository README / Force-field | navigation |
| [ALIGNN-FF for energy and forces](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | Requested repository README / Force-field | crystal_related |
| [ALLEGRO training for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_ALLEGRO.ipynb>) | Requested repository README / Force-field | crystal_related |
| [Analyzing_MOF_datasets](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_MOF_datasets.ipynb>) | Requested repository README / Force-field | crystal_related |
| [ML Sklearn Steel Fatigue](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ML_Sklearn.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | adjacent |
| [ML_Chem_Formula_Descriptors](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_Magpie_AIMS.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Basic_Machine_learning_training_example_with_CFID_descriptors](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Machine_learning_training_example_with_CFID_descriptors.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_ML_TrainingGPU](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TrainingGPU.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_CFID_LightGBM_GPUvsCPU](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_LightGBM_GPUvsCPU.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_ML_TensorFlowExample](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TensorFlowExample.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | adjacent |
| [JARVIS_Leaderboard_MatMiner](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/MatMiner_on_JARVIS_DFT.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [CIF To Graph_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/cif2graph.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_ALIGNN_Basic_Training_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Training_ALIGNN_model_example.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN-FF pretrained model/calculator usage](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Structure_Relaxation_Phonons_Interface.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_Leaderboard_contribution_ALIGNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_Leaderboard_MLFF/ALIGNN-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_Leaderboard_KGCNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/kgcnn_jarvis_leaderboard.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN Superconductor training](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Sc.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Train ALLEGRO-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_ALLEGRO.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Train NEQUIP-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_NEQUIP.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Train CHGNet-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_CHGNet.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [MatGL-FF_Mlearn for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Matgl_mlearn.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [SNAP-FF_Mlearn for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/snap_mlearn.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Pretrained CHGNet Prediction](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chgnet_prediction.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Pretrained OpenCatalystProject Model](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ocp_load_pretrained_models.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN-Pretrained property-predictor models](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/GetTotalEnergy.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN-PhononDos](<https://colab.research.google.com/github/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_PhononDOS.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Inverse design of superconductors with CDVAE](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/cdvae_example.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_STEM_2D](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_STEM_2D.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomVision_Leaderboard_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionImageClassification.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomVision_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionExample.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [ChemNLP example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ChemNLP_Example.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [ChemNLP HuggingFace example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ChemNLP_TitleToAbstract.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomGPT training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomGPT forward model training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_forward_example.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomGPT HuggingFace inference example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example_huggingface.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Open catalyst project load model](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ocp_load_pretrained_models.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Vacancy formation ML](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/vacancy_ml.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Interface Materials Design/InterMat example](<https://colab.research.google.com/gist/knc6/0d9aa89f671687c6e925eea2be9b824a/intermat_gettingstarted.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | navigation |
| [ALIGNN-FF Melt Quench](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Fast_Melt_Quench.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Basic external tutorial on linear models](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/training_linear_models>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [Analyzing data in JARVIS-Leaderboard](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_Leaderboard.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [CHIPS-FF: Evaluation of universal machine learning force-fields](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chipsff_example.ipynb>) | Requested repository README / Artificial intelligence/Machine learning | crystal_related |
| [With new qiskit package version: Quantum computation and Qiskit based electronic bandstructure](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_latest_qiskit.ipynb>) | Requested repository README / Quantum computation | adjacent |
| [With old qiskit package version: Quantum computation and Qiskit based electronic bandstructure](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_.ipynb>) | Requested repository README / Quantum computation | adjacent |
| [XRD Matching](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/XRD_Matching.ipynb>) | Requested repository README / Experiment related tutorials | crystal_related |
| [https://nanohub.org/FAIR_workshop_2024](<https://nanohub.org/FAIR_workshop_2024>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [Basic quantum espresso run](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Basic_Example.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [Analyzing_data_in_the_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [JARVIS_Leaderboard_contribution_ALIGNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [ALIGNN-FF for energy and forces](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [AtomGPT training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [AtomGPT HuggingFace inference example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example_huggingface.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [AtomVision_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionExample.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [JARVIS_LAMMPS](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_LAMMPS.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [Quantum computation and Qiskit based electronic bandstructure](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_latest_qiskit.ipynb>) | Requested repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | adjacent |
| [https://github.com/usnistgov/aims2024_workshop](<https://github.com/usnistgov/aims2024_workshop>) | Requested repository README / AIMS2024 tutorial and presentation slides | navigation |
| [More info](<https://jarvis.nist.gov/events/school>) | Requested repository README / JARVIS-School | crystal_related |
| [More info](<https://march.aps.org/events/tutorial-graph-neural-networks>) | Requested repository README / APS2023 tutorial | navigation |
| [More info](<https://jarvis.nist.gov/events/aims>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [The joint automated repository for various integrated simulations (JARVIS) for data-driven materials design](<https://www.nature.com/articles/s41524-020-00440-1>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [various other publications](<https://jarvis-tools.readthedocs.io/en/master/publications.html>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [Contribution instructions](<https://github.com/usnistgov/jarvis/blob/master/Contribution.rst>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [Github issues](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues)(preferred](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues)(preferred>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [https://www.nist.gov/mgi](<https://www.nist.gov/mgi>) | Requested repository README / AIMS2022 tutorial | navigation |
| [Code of conduct](<https://github.com/usnistgov/jarvis/blob/master/CODE_OF_CONDUCT.md>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [NIST License](<https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst>) | Requested repository README / AIMS2022 tutorial | crystal_related |
| [alt text](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/actions/workflows/test-notebooks.yml/badge.svg>) | Successor repository README | crystal_related |
| [NIST-JARVIS](<https://jarvis.nist.gov/>) | Successor repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [JARVIS-Tools](<https://jarvis-tools.readthedocs.io/en/master/tutorials.html>) | Successor repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [SlideShare](<https://www.slideshare.net/KAMALCHOUDHARY4>) | Successor repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [https://github.com/knc6/slides](<https://github.com/knc6/slides>) | Successor repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [https://www.youtube.com/@dr_k_choudhary](<https://www.youtube.com/@dr_k_choudhary>) | Successor repository README / JARVIS-Tools Notebooks (Introduction) | crystal_related |
| [NIST-AIMS workshop](<http://jarvis.nist.gov/events/aims>) | Successor repository README / Mini-course collection | crystal_related |
| [Analyzing_data_in_the_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | Successor repository README / JARVIS-DFT: | crystal_related |
| [Basic quantum espresso run](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Basic_Example.ipynb>) | Successor repository README / JARVIS-DFT: | crystal_related |
| [Basic_ALIGNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb>) | Successor repository README / ALIGNN: | crystal_related |
| [AtomGPT_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example.ipynb>) | Successor repository README / AtomGPT: | crystal_related |
| [DiffractGPT_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/DiffractGPT_example.ipynb>) | Successor repository README / AtomGPT: | crystal_related |
| [MicroscopyGPT_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/MicroscopyGPT.ipynb>) | Successor repository README / AtomGPT: | crystal_related |
| [open in colab](<https://colab.research.google.com/github/usnistgov/aims_workshop/blob/main/tutorials/intro-gnn-potentials.ipynb>) | Successor repository README / Machine Learning Force Fields: | navigation |
| [CHIPS_FF_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chipsff_example.ipynb>) | Successor repository README / CHIPS-FF: | crystal_related |
| [Scaling ALIGNN/SlaKoNet](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/scaling_analysis.ipynb>) | Successor repository README / Scaling test: | crystal_related |
| [Introduction to high-performance computing](<https://tacc-reproducible-intro-hpc.readthedocs.io/en/latest/intro_to_hpc/overview.html>) | Successor repository README / Basics | adjacent |
| [Python beginners notebook](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/python_beginners_notebook.ipynb>) | Successor repository README / Basics | adjacent |
| [Silicon atomic structure and analysis example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Silicon_atomic_structure_and_analysis_example.ipynb>) | Successor repository README / Basics | crystal_related |
| [Analyzing_data_in_the_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Analyzing_data_in_the_JARVIS_Leaderboard](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_Leaderboard.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Basic quantum espresso run](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Basic_Example.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_Optoelectronics_Computational_screening_of_high_performance_optoelectronic_materials_using_OptB88vdW_and_TB_mBJ_formalisms](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Optoelectronics_Computational_screening_of_high_performance_optoelectronic_materials_using_OptB88vdW_and_TB_mBJ_formalisms.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_TopologicalSpillage_High_throughput_Discovery_of_Topologically_Non_trivial_Materials_using_Spin_orbit_Spillage](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_TopologicalSpillage_High_throughput_Discovery_of_Topologically_Non_trivial_Materials_using_Spin_orbit_Spillage.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_Solar_Accelerated_Discovery_of_Efficient_Solar_Cell_Materials_Using_Quantum_and_Machine_Learning_Methods](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Solar_Accelerated_Discovery_of_Efficient_Solar_Cell_Materials_Using_Quantum_and_Machine_Learning_Methods.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Si_bandstructure&densityof_states](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Si_bandstructure%26densityof_states.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_Wannier90Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Wannier90Example.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [BoltztrapExample](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/BoltztrapExample.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Making 2D heterostructures](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Making_2D_heterostructures.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_DFT_FormationEnergiesAccuracyCheck](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_FormationEnergiesAccuracyCheck.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Downloading raw analysis data and input/output files](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Download_raw_data_for_webpages.ipynb>) | Successor repository README / Electronic structure | adjacent |
| [JARVIS_DFT_2D_High_throughput_Identification_and_Characterization_of_Two_dimensional_Materials_using_Density_functional_theory](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_2D_High_throughput_Identification_and_Characterization_of_Two_dimensional_Materials_using_Density_functional_theory.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_CONVERG_Convergence_and_machine_learning_predictions_of_Monkhorst_Pack_k_points_and_plane_wave_cut_off_in_high_throughput_DFT_calculations](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_CONVERG_Convergence_and_machine_learning_predictions_of_Monkhorst_Pack_k_points_and_plane_wave_cut_off_in_high_throughput_DFT_calculations.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_DFPT_High_throughput_Density_Functional_Perturbation_Theory_and_Machine_Learning_Predictions_of_Infrared,_Piezoelectric_and_Dielectric_Responses](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFPT_High_throughput_Density_Functional_Perturbation_Theory_and_Machine_Learning_Predictions_of_Infrared%2C_Piezoelectric_and_Dielectric_Responses.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_TE_Data_driven_discovery_of_3D_and_2D_thermoelectric_materials](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_TE_Data_driven_discovery_of_3D_and_2D_thermoelectric_materials.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_ELAST_Elastic_properties_of_bulk_and_low_dimensional_materials_using_van_der_Waals_density_functional](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ELAST_Elastic_properties_of_bulk_and_low_dimensional_materials_using_van_der_Waals_density_functional.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Get JARVIS-DFT final structures in ASE or Pymatgen format](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Get_JARVIS_DFT_final_structures_in_ASE_or_Pymatgen_format.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_QuantumEspressoColab_Designing_High_Tc_Superconductors_with_BCS_inspired_Screening,_Density_Functional_Theory_and_Deep_learning](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Designing_High_Tc_Superconductors_with_BCS_inspired_Screening%2C_Density_Functional_Theory_and_Deep_learning.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_WTBH_Database_of_Wannier_tight_binding_Hamiltonians_using_high_throughput_density_functional_theory](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_WTBH_Database_of_Wannier_tight_binding_Hamiltonians_using_high_throughput_density_functional_theory.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Comapre_MP_JV](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Comapre_MP_JV.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [ParsingWebpages(JARVIS_DFT)](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT>) | Successor repository README / Electronic structure | adjacent |
| [https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb>) | Successor repository README / Electronic structure | adjacent |
| [ConvexHull](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ConvexHull.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [DimensionalityAndExfoliationEnergy](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/DimensionalityAndExfoliationEnergy.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Element_filter_for_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Element_filter_for_JARVIS_DFT_dataset.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [Run GPAW on Google-colab and calculate interface energy with jarvis-tools](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/GPAW_Colab.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [ParsingWebpages(JARVIS_DFT)](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT>) | Successor repository README / Electronic structure | adjacent |
| [https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb>) | Successor repository README / Electronic structure | adjacent |
| [WTBH_MagneticMats.ipynb](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/WTBH_MagneticMats.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [QMCPACK_Basic_Example](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/QMCPACK_Basic_Example.ipynb>) | Successor repository README / Electronic structure | crystal_related |
| [JARVIS_LAMMPS](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_LAMMPS.ipynb>) | Successor repository README / Force-field | crystal_related |
| [MLFF SNAP training](<https://colab.research.google.com/github/FitSNAP/FitSNAP/blob/master/tutorial.ipynb>) | Successor repository README / Force-field | navigation |
| [ALIGNN-FF for energy and forces](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | Successor repository README / Force-field | crystal_related |
| [ALLEGRO training for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_ALLEGRO.ipynb>) | Successor repository README / Force-field | crystal_related |
| [Analyzing_MOF_datasets](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_MOF_datasets.ipynb>) | Successor repository README / Force-field | crystal_related |
| [ML Sklearn Steel Fatigue](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ML_Sklearn.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | adjacent |
| [ML_Chem_Formula_Descriptors](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_Magpie_AIMS.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Basic_Machine_learning_training_example_with_CFID_descriptors](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Machine_learning_training_example_with_CFID_descriptors.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_ML_TrainingGPU](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TrainingGPU.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_CFID_LightGBM_GPUvsCPU](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_LightGBM_GPUvsCPU.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_ML_TensorFlowExample](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TensorFlowExample.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | adjacent |
| [JARVIS_Leaderboard_MatMiner](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/MatMiner_on_JARVIS_DFT.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [CIF To Graph_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/cif2graph.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_ALIGNN_Basic_Training_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Training_ALIGNN_model_example.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN-FF pretrained model/calculator usage](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Structure_Relaxation_Phonons_Interface.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_Leaderboard_contribution_ALIGNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_Leaderboard_MLFF/ALIGNN-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_Leaderboard_KGCNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/kgcnn_jarvis_leaderboard.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN Superconductor training](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Sc.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Train ALLEGRO-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_ALLEGRO.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Train NEQUIP-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_NEQUIP.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Train CHGNet-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_CHGNet.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [MatGL-FF_Mlearn for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Matgl_mlearn.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [SNAP-FF_Mlearn for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/snap_mlearn.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Pretrained CHGNet Prediction](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chgnet_prediction.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Pretrained OpenCatalystProject Model](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ocp_load_pretrained_models.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN-Pretrained property-predictor models](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/GetTotalEnergy.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [ALIGNN-PhononDos](<https://colab.research.google.com/github/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_PhononDOS.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Inverse design of superconductors with CDVAE](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/cdvae_example.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [JARVIS_STEM_2D](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_STEM_2D.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomVision_Leaderboard_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionImageClassification.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomVision_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionExample.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [ChemNLP example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ChemNLP_Example.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [ChemNLP HuggingFace example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ChemNLP_TitleToAbstract.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomGPT training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomGPT forward model training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_forward_example.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [AtomGPT HuggingFace inference example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example_huggingface.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Open catalyst project load model](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ocp_load_pretrained_models.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Vacancy formation ML](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/vacancy_ml.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Interface Materials Design/InterMat example](<https://colab.research.google.com/gist/knc6/0d9aa89f671687c6e925eea2be9b824a/intermat_gettingstarted.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | navigation |
| [ALIGNN-FF Melt Quench](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Fast_Melt_Quench.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Basic external tutorial on linear models](<https://github.com/atomgptlab/jarvis-tools-notebooks/blob/master/training_linear_models>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [Analyzing data in JARVIS-Leaderboard](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_Leaderboard.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [CHIPS-FF: Evaluation of universal machine learning force-fields](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chipsff_example.ipynb>) | Successor repository README / Artificial intelligence/Machine learning | crystal_related |
| [With new qiskit package version: Quantum computation and Qiskit based electronic bandstructure](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_latest_qiskit.ipynb>) | Successor repository README / Quantum computation | adjacent |
| [With old qiskit package version: Quantum computation and Qiskit based electronic bandstructure](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_.ipynb>) | Successor repository README / Quantum computation | adjacent |
| [XRD Matching](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/XRD_Matching.ipynb>) | Successor repository README / Experiment related tutorials | crystal_related |
| [https://nanohub.org/FAIR_workshop_2024](<https://nanohub.org/FAIR_workshop_2024>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [Basic quantum espresso run](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Basic_Example.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [Analyzing_data_in_the_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [JARVIS_Leaderboard_contribution_ALIGNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [ALIGNN-FF for energy and forces](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [AtomGPT training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [AtomGPT HuggingFace inference example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example_huggingface.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [AtomVision_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionExample.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [JARVIS_LAMMPS](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_LAMMPS.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | crystal_related |
| [Quantum computation and Qiskit based electronic bandstructure](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_latest_qiskit.ipynb>) | Successor repository README / NanoHub FAIR workflow workshop/JARVIS-School @ Purdue university | adjacent |
| [https://github.com/usnistgov/aims2024_workshop](<https://github.com/usnistgov/aims2024_workshop>) | Successor repository README / AIMS2024 tutorial and presentation slides | navigation |
| [More info](<https://jarvis.nist.gov/events/school>) | Successor repository README / JARVIS-School | crystal_related |
| [More info](<https://march.aps.org/events/tutorial-graph-neural-networks>) | Successor repository README / APS2023 tutorial | navigation |
| [More info](<https://jarvis.nist.gov/events/aims>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [The joint automated repository for various integrated simulations (JARVIS) for data-driven materials design](<https://www.nature.com/articles/s41524-020-00440-1>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [various other publications](<https://jarvis-tools.readthedocs.io/en/master/publications.html>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [Contribution instructions](<https://github.com/usnistgov/jarvis/blob/master/Contribution.rst>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [Github issues](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues)(preferred](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues)(preferred>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [https://www.nist.gov/mgi](<https://www.nist.gov/mgi>) | Successor repository README / AIMS2022 tutorial | navigation |
| [Code of conduct](<https://github.com/usnistgov/jarvis/blob/master/CODE_OF_CONDUCT.md>) | Successor repository README / AIMS2022 tutorial | crystal_related |
| [NIST License](<https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst>) | Successor repository README / AIMS2022 tutorial | crystal_related |

### [Machine Learning Materials Datasets / MAST-ML education](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>)

Inspected revision: `Figshare version5; metadata SHA-256 a89916385075278bdd94780ad0b3eef244e5fdaf184a324001403aa1cf2485b3`.

Inspection boundary and caveats:

- Extraction boundary: Figshare article metadata v5, its attached README.txt, and metadata-listed file download URLs. CSVs were read only to verify row counts; their cell text was not used to expand links.
- All links means the HTTP/S references in those inspected documents, not all MAST-ML repositories or papers.
- Counts independently parsed after one header row: diffusion408; perovskite1929; metallic glass585. These are educational packaging counts, not new unique crystal structures.
- Metallic-glass data are adjacent, not crystalline structure data. Dataset README bibliography fields are preserved as source links, not treated as independently verified citation metadata.

9 labeled link occurrences; 9 distinct URLs. Section and scope labels preserve the collection context.

| Linked source | Original section | Scope |
|---|---|---|
| [README.txt](<https://ndownloader.figshare.com/files/13008500>) | Figshare v5 attached files | navigation |
| [Dilute_Solute_Diffusion_with_features.csv](<https://ndownloader.figshare.com/files/13007075>) | Figshare v5 attached files | crystal_related |
| [Perovskite_Stability_with_features.csv](<https://ndownloader.figshare.com/files/12978425>) | Figshare v5 attached files | crystal_related |
| [Metallic_Glass_Forming_with_features.csv](<https://ndownloader.figshare.com/files/12978419>) | Figshare v5 attached files | adjacent |
| [https://www.nature.com/articles/sdata201654](<https://www.nature.com/articles/sdata201654>) | Attached README | navigation |
| [https://www.sciencedirect.com/science/article/pii/S0927025617301738](<https://www.sciencedirect.com/science/article/pii/S0927025617301738>) | Attached README | navigation |
| [https://www.sciencedirect.com/science/article/pii/S092702561830274X](<https://www.sciencedirect.com/science/article/pii/S092702561830274X>) | Attached README | navigation |
| [https://www.sciencedirect.com/science/article/pii/S0022309300000648](<https://www.sciencedirect.com/science/article/pii/S0022309300000648>) | Attached README | navigation |
| [MAST-ML toolkit](<https://github.com/uw-cmg/MAST-ML>) | Figshare description | navigation |

### [nanoHUB Machine Learning Lab Module](<https://nanohub.org/tools/intromllab>)

Inspected revision: `Version1.7 / revision36 / published2022-09-13 / DOI10.21981/CPNK-XE48`.

Inspection boundary and caveats:

- Extraction boundary: public About page, directly linked Supporting Docs list, and public license page. No launch/login or authenticated tool environment was entered.
- Public description and supporting-document filenames are accessible. Running the tool explicitly requires login; launch access is unverified. No login,403 or other access control was bypassed.
- Supporting documents comprise five teaching slide decks and four teacher/reading/quiz documents; their contents were not opened or mined for further links.
- Public tool license is GNU GPL version3-or-later; this software license is not automatically a license for every example dataset.
- No unique materials count is asserted; visible usage/user counters are not dataset sizes.

41 labeled link occurrences; 27 distinct URLs. Section and scope labels preserve the collection context.

| Linked source | Original section | Scope |
|---|---|---|
| [Machine Learning Lab Module](<https://nanohub.org/resources/intromllab>) | Resource About page | navigation |
| [cite this](<https://nanohub.org/resources/intromllab/about#citethis>) | Resource About page | navigation |
| [license](<https://nanohub.org/resources/license?tool=intromllab_r36&tmpl=component>) | Resource About page | navigation |
| [download](<https://nanohub.org/resources/sourcecode?tool=intromllab_r36>) | Resource About page | navigation |
| [View All Supporting Documents](<https://nanohub.org/resources/intromllab/supportingdocs>) | Resource About page | navigation |
| [1893 users (currently updating)](<https://nanohub.org/resources/intromllab/usage>) | Resource About page | navigation |
| [0 Citation(s)](<https://nanohub.org/resources/intromllab/citations>) | Resource About page | navigation |
| [3 questions](<https://nanohub.org/resources/intromllab/questions>) | Resource About page | navigation |
| [Ask a question](<https://nanohub.org/resources/intromllab/questions?action=new>) | Resource About page | navigation |
| [0 review(s)](<https://nanohub.org/resources/intromllab/reviews>) | Resource About page | navigation |
| [Review this](<https://nanohub.org/resources/intromllab/reviews?action=addreview#commentform>) | Resource About page | navigation |
| [About : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/about>) | Resource About page | navigation |
| [Wishlist : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/wishlist>) | Resource About page | navigation |
| [Versions : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/versions>) | Resource About page | navigation |
| [10.21981/CPNK-XE48](<https://doi.org/10.21981/CPNK-XE48>) | Resource About page | navigation |
| [BibTex](<https://nanohub.org/resources/32730/citation?citationFormat=bibtex&no_html=1&rev=36>) | Resource About page | navigation |
| [EndNote](<https://nanohub.org/resources/32730/citation?citationFormat=endnote&no_html=1&rev=36>) | Resource About page | navigation |
| [Machine Learning Lab Module](<https://nanohub.org/resources/intromllab>) | Supporting Docs list | navigation |
| [cite this](<https://nanohub.org/resources/intromllab/about#citethis>) | Supporting Docs list | navigation |
| [license](<https://nanohub.org/resources/license?tool=intromllab_r36&tmpl=component>) | Supporting Docs list | navigation |
| [download](<https://nanohub.org/resources/sourcecode?tool=intromllab_r36>) | Supporting Docs list | navigation |
| [View All Supporting Documents](<https://nanohub.org/resources/intromllab/supportingdocs>) | Supporting Docs list | navigation |
| [1893 users (currently updating)](<https://nanohub.org/resources/intromllab/usage>) | Supporting Docs list | navigation |
| [0 Citation(s)](<https://nanohub.org/resources/intromllab/citations>) | Supporting Docs list | navigation |
| [3 questions](<https://nanohub.org/resources/intromllab/questions>) | Supporting Docs list | navigation |
| [Ask a question](<https://nanohub.org/resources/intromllab/questions?action=new>) | Supporting Docs list | navigation |
| [0 review(s)](<https://nanohub.org/resources/intromllab/reviews>) | Supporting Docs list | navigation |
| [Review this](<https://nanohub.org/resources/intromllab/reviews?action=addreview#commentform>) | Supporting Docs list | navigation |
| [About : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/about>) | Supporting Docs list | navigation |
| [Wishlist : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/wishlist>) | Supporting Docs list | navigation |
| [Versions : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/versions>) | Supporting Docs list | navigation |
| [Module_1_-_Machine_Learning_Basics_in_Materials_Science.pptx](<https://nanohub.org/resources/34383/download/Module_1_-_Machine_Learning_Basics_in_Materials_Science.pptx>) | Supporting Docs list | adjacent |
| [Module_2_-_Data_Cleaning_and_Featurizing.pptx](<https://nanohub.org/resources/34384/download/Module_2_-_Data_Cleaning_and_Featurizing.pptx>) | Supporting Docs list | adjacent |
| [Module_3_-_Model_Assessment_Optimization_Predictions.pptx](<https://nanohub.org/resources/34385/download/Module_3_-_Model_Assessment_Optimization_Predictions.pptx>) | Supporting Docs list | adjacent |
| [Module_4_-_Machine_Learning_Tools_for_Materials_Science.pptx](<https://nanohub.org/resources/34386/download/Module_4_-_Machine_Learning_Tools_for_Materials_Science.pptx>) | Supporting Docs list | adjacent |
| [Module_5_-_Machine_Learning_Tools_for_Materials_Science.pptx](<https://nanohub.org/resources/34387/download/Module_5_-_Machine_Learning_Tools_for_Materials_Science.pptx>) | Supporting Docs list | adjacent |
| [Teachers_Guide.docx](<https://nanohub.org/resources/34391/download/Teachers_Guide.docx>) | Supporting Docs list | adjacent |
| [Reading_List.docx](<https://nanohub.org/resources/34388/download/Reading_List.docx>) | Supporting Docs list | adjacent |
| [Quiz_Questions.docx](<https://nanohub.org/resources/34389/download/Quiz_Questions.docx>) | Supporting Docs list | adjacent |
| [Quiz_Questions_-_Answers.docx](<https://nanohub.org/resources/34390/download/Quiz_Questions_-_Answers.docx>) | Supporting Docs list | adjacent |
| [GNU GPL v3 text](<https://www.gnu.org/licenses/gpl-3.0.en.html>) | Public tool license | navigation |

### [REMI: REsource for Materials Informatics](<https://pages.nist.gov/remi/>)

Inspected revision: `596b04435fb577175264a70c4434f5539b809510`.

Inspection boundary and caveats:

- Extraction boundary: REMI repository README, homepage index.html and its _data/resources.csv instructional-resource list, directly linked data/index.md and learn/index.md lists, and the two data-library directories/descriptions linked by data/index.md.
- All links means links in those inspected documents and the direct file lists; linked notebooks, papers, external database sites and other REMI directories were not recursively crawled.
- Direct urllib request to the site returned403; public web-tool reading and the owning public GitHub source remained accessible. Source repository is archived; no protection was bypassed.
- The homepage table has 106 listed rows, which are educational resources, not a materials total.
- Directly linked experimental libraries contain921 Fe–Co–Ni and278 Fe–Ga–Pd aligned composition/diffraction/property rows, independently verified from the released files. No atomic-coordinate structures or release-specific data license were found.

146 labeled link occurrences; 145 distinct URLs. Section and scope labels preserve the collection context.

| Linked source | Original section | Scope |
|---|---|---|
| [Automatminer Basic Tutorial](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/automatminer-nb/automatminer_basic.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Data Retrieval Basics](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/data_retrieval_basics.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Plot and compare experimental and computational bandgaps](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/expt_vs_comp_bandgap.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Interacting with Jarvis via MDF Search](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/jarvis.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Uranium-oxygen bond length analysis using MPDS](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/mpds.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Visualization using FigRecipes](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/figrecipes-nb/figrecipes_basics.ipynb>) | Homepage instructional resource table / Matminer | navigation |
| [Advanced Visualization using FigRecipes](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/figrecipes-nb/figrecipes_advanced.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Matminer introduction - Predicting bulk modulus](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/bulk_modulus.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Train a Model to Predict Formation Energy using the OQMD](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/formation_e.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Recreating Ling IMMI (2017) - Random Forest with Uncertainty](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/rf-with-uncertainty.ipynb>) | Homepage instructional resource table / Matminer | navigation |
| [Using sklearn Pipeline with matminer](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/sklearn_pipeline.ipynb>) | Homepage instructional resource table / Matminer | adjacent |
| [Using the Crystal Structure Representation of Ward et al. to predict formation enthalpy,using the FLLA dataset.](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/voronoi-ward-prb-2017.ipynb>) | Homepage instructional resource table / Matminer | crystal_related |
| [Analyzing data in the JARVIS DFT dataset](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [BoltzTrap Example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/BoltztrapExample.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [JARVIS DFT Formation Energies Accuracy Check](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_FormationEnergiesAccuracyCheck.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [GPU can accelerate model training with respect to CPU using JARVIS-ML CFID dataset](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_LightGBM_GPUvsCPU.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [JARVIS ML TensorFlow Example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TensorFlowExample.ipynb>) | Homepage instructional resource table / Jarvis | adjacent |
| [JARVIS ML Training GPU](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TrainingGPU.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [JARVIS Wannier 90 Example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Wannier90Example.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [Si band structure & density of states](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Si_bandstructure%26densityof_states.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [Simple Machine learning training example with CFID descriptors](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Machine_learning_training_example_with_CFID_descriptors.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [Simple Silicon atomic structure and analysis example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Silicon_atomic_structure_and_analysis_example.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [Python for novice](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/python_beginners_notebook.ipynb>) | Homepage instructional resource table / Jarvis | crystal_related |
| [Introduction](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/1-Introduction.ipynb>) | Homepage instructional resource table / MDF Forge | navigation |
| [Core Query Builder Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/2-Core_Query_Builder_Functions.ipynb>) | Homepage instructional resource table / MDF Forge | crystal_related |
| [General Helper Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/4-General_Helper_Functions.ipynb>) | Homepage instructional resource table / MDF Forge | crystal_related |
| [Field Specific Helper Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/5-Field-Specific_Helper_Functions.ipynb>) | Homepage instructional resource table / MDF Forge | crystal_related |
| [Data Retrieval Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/6-Data_Retrieval_Functions.ipynb>) | Homepage instructional resource table / MDF Forge | navigation |
| [Band Excitation data processing](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/BE_Processing.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [Band Excitation & Contact Kelvin Probe Force Microscopy (cKPFM) data processing](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/BE_Processing_cKPFM.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [Band Excitation Relaxation Spectroscopy Data Processing](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/BE_Relaxation%20Processing.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [G-Mode KPFM with Fast Free Force Recovery (F3R)](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/GKPFM_base_notebook.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [Static force spectroscopy simulation over a viscoelastic material](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/AFM_simulations/Force_Spectroscopy/Static_Force_Spectroscopy.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [Introduction to dynamic AFM simulations](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/AFM_simulations/IntroductionToSimulations/IntroToAFMSimulations.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [Dynamic atomic force microscopy simulations over a viscoelastic material](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/AFM_simulations/Multifrequency_Viscoelasticity/Simulation_SoftMatter.ipynb>) | Homepage instructional resource table / pycroscopy | adjacent |
| [AFLOW machine learning](<https://colab.research.google.com/drive/1oJa2Qk5HpBPXEoArtJxfz605859MDNCz>) | Homepage instructional resource table / AFLOW | crystal_related |
| [Density of States](<https://plotly.com/python/v3/ipython-notebooks/density-of-states/>) | Homepage instructional resource table / Plotly | crystal_related |
| [EELS analysis](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/EELS/EELS_analysis.ipynb>) | Homepage instructional resource table / hyperspy | crystal_related |
| [SEM EDS 4D visualization](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/EDS/SEM_EDS_4D_visualisation.ipynb>) | Homepage instructional resource table / hyperspy | navigation |
| [TEM EDS nanoparticles](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/EDS/TEM_EDS_nanoparticles.ipynb>) | Homepage instructional resource table / hyperspy | crystal_related |
| [Holography](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/Holography/Holography.ipynb>) | Homepage instructional resource table / hyperspy | navigation |
| [Getting Started](<https://github.com/hyperspy/hyperspy-demos/blob/master/1_Getting_Started.ipynb>) | Homepage instructional resource table / hyperspy | navigation |
| [SVD and BSS](<https://github.com/hyperspy/hyperspy-demos/blob/master/2_SVD_and_BSS.ipynb>) | Homepage instructional resource table / hyperspy | crystal_related |
| [Fitting tutorial](<https://github.com/hyperspy/hyperspy-demos/blob/master/Fitting_tutorial.ipynb>) | Homepage instructional resource table / hyperspy | navigation |
| [Online Robust PCA](<https://github.com/hyperspy/hyperspy-demos/blob/master/Online_Robust_PCA.ipynb>) | Homepage instructional resource table / hyperspy | navigation |
| [Working with image data](<https://github.com/hyperspy/hyperspy-demos/blob/master/image_data/working_with_imagedata.ipynb>) | Homepage instructional resource table / hyperspy | crystal_related |
| [Working with image data](<https://github.com/hyperspy/hyperspy-demos/tree/master/image_data>) | Homepage instructional resource table / hyperspy | navigation |
| [How to extract or plot the NiO band structure from a VASP calculation using pymagen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Bandstructure%20of%20NiO.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [core functionality of pymatgen,including the core objects representing Elements,Species,Lattices,and Structures](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Basic%20functionality.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [calculate reaction energies using the Materials API and pymatgen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Calculating%20Reaction%20Energies%20with%20the%20Materials%20API.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [how to plot an XRD plot for the two polymorphs of CsCl ($Pm\overline{3}m$ and $Fm\overline{3}m$)](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Calculating%20XRD%20patterns.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [how to obtain an explaination of the different corrections being applied in the Materials Project](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Explanation%20of%20Corrections.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Getting crystal structures from online sources](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Getting%20crystal%20structures%20from%20online%20sources.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [matgen's functionality in terms of creating and editing molecules,as well as its integration with OpenBabel](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Molecule.ipynb>) | Homepage instructional resource table / matgenb | adjacent |
| [ordering of a disordered structure using pymatgen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Ordering%20Disordered%20Structures.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Plotting and Analyzing a Phase Diagram using the Materials API](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Plotting%20and%20Analyzing%20a%20Phase%20Diagram%20using%20the%20Materials%20API.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Plotting the electronic structure of Fe](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Plotting%20the%20electronic%20structure%20of%20Fe.ipynb>) | Homepage instructional resource table / matgenb | navigation |
| [Units](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Units.ipynb>) | Homepage instructional resource table / matgenb | navigation |
| [Data-driven First Principles Methods for the Study and Design of Alkali Superionic Conductors Part 1 - Structure Generation](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-08-Data-driven%20First%20Principles%20Methods%20for%20the%20Study%20and%20Design%20of%20Alkali%20Superionic%20Conductors%20Part%201%20-%20Structure%20Generation.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Data-driven First Principles Methods for the Study and Design of Alkali Superionic Conductors Part 2 - Phase and Electrochemical Stability](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-08-Data-driven%20First%20Principles%20Methods%20for%20the%20Study%20and%20Design%20of%20Alkali%20Superionic%20Conductors%20Part%202%20-%20Phase%20and%20Electrochemical%20Stability.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Data-driven First Principles Methods for the Study and Design of Alkali Superionic Conductors Part 3 - Diffusivity and Ionic Conductivity](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-08-Data-driven%20First%20Principles%20Methods%20for%20the%20Study%20and%20Design%20of%20Alkali%20Superionic%20Conductors%20Part%203%20-%20Diffusivity%20and%20Ionic%20Conductivity.ipynb>) | Homepage instructional resource table / matgenb | navigation |
| [how to use the output from VASP DFPT calculation and the phonopy interface to plot the phonon bandstructure and density of states](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-25-Plotting%20phonon%20bandstructure%20and%20dos.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [how you can obtain various data from the Materials Project using pymatgen's interface to the Materials API](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-03-02-Getting%20data%20from%20Materials%20Project.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Slab generation and Wulff shape](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-04-03-Slab%20generation%20and%20Wulff%20shape.ipynb>) | Homepage instructional resource table / matgenb | navigation |
| [Inputs and Analysis of VASP runs](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-04-14-Inputs%20and%20Analysis%20of%20VASP%20runs.ipynb>) | Homepage instructional resource table / matgenb | navigation |
| [Running Jupyter Notebook on clusters](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-05-11-Running%20Jupyter%20Notebook%20on%20clusters.ipynb>) | Homepage instructional resource table / matgenb | adjacent |
| [Analyze and plot band structures](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-09-03-Analyze%20and%20plot%20band%20structures.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Plotting a Pourbaix Diagram](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-12-15-Plotting%20a%20Pourbaix%20Diagram.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [ChemEnv - How to automatically identify coordination environments in a structure](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-01-01-ChemEnv%20-%20How%20to%20automatically%20identify%20coordination%20environments%20in%20a%20structure.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Computing the Reaction Diagram between Two Compounds](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-03-09-Computing%20the%20Reaction%20Diagram%20between%20Two%20Compounds.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Plotting COHP from LOBSTER](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-03-14-Plotting%20COHP%20from%20LOBSTER.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Adsorption on solid surfaces](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-07-24-Adsorption%20on%20solid%20surfaces.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Structure Prediction using Pymatgen and the Materials API](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-09-25-Structure%20Prediction%20using%20Pymatgen%20and%20the%20Materials%20API.ipynb>) | Homepage instructional resource table / matgenb | navigation |
| [Dopant suggestions using Pymatgen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-11-6-Dopant%20suggestions%20using%20Pymatgen.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [How to use Boltztra2 interface](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2019-01-04-How%20to%20use%20Boltztra2%20interface.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [How to plot and evaluate output files from Lobster](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2019-01-11-How%20to%20plot%20and%20evaluate%20output%20files%20from%20Lobster.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [Interface Reactions](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2019-03-11-Interface%20Reactions.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [How to plot a Fermi surface](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2020-07-15-How%20to%20plot%20a%20Fermi%20surface.ipynb>) | Homepage instructional resource table / matgenb | crystal_related |
| [How to plot a Fermi surface](<https://github.com/materialsvirtuallab/matgenb/tree/master/notebooks>) | Homepage instructional resource table / matgenb | navigation |
| [Experimental design with Citrination](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/ExperimentalDesign.ipynb>) | Homepage instructional resource table / Citrine | crystal_related |
| [Import Instron](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/ImportInstron.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Citrination t-SNE API](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/TsneDemo.ipynb>) | Homepage instructional resource table / Citrine | crystal_related |
| [Citrination t-SNE API](<https://github.com/CitrineInformatics/learn-citrination/tree/master/citrination_api_examples>) | Homepage instructional resource table / Citrine | navigation |
| [Importing data from VASP calculations into Citrination](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/1_ImportVASP.ipynb>) | Homepage instructional resource table / Citrine | crystal_related |
| [Working with PIFs](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/2_WorkingWithPIFs.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Introduction to Queries](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/3_IntroQueries.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Machine Learning on Citrination](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/4_MLonCitrination.ipynb>) | Homepage instructional resource table / Citrine | crystal_related |
| [Advanced PIF Tutorial](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/AdvancedPif.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Advanced Queries](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/AdvancedQueries.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Advanced Queries](<https://github.com/CitrineInformatics/learn-citrination/tree/master/citrination_api_examples/tutorial_sequence>) | Homepage instructional resource table / Citrine | navigation |
| [Citrination Demo on Shape Memory Alloys](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_ui_examples/JournalPaperToModel.ipynb>) | Homepage instructional resource table / Citrine | crystal_related |
| [Citrination Demo on Shape Memory Alloys](<https://github.com/CitrineInformatics/learn-citrination/tree/master/citrination_ui_examples>) | Homepage instructional resource table / Citrine | navigation |
| [Compare Band Gaps From Citrination and Materials Project](<https://github.com/CitrineInformatics/learn-citrination/blob/master/matminer_examples/BandGapComparisonCitrinationVsMP.ipynb>) | Homepage instructional resource table / Citrine | crystal_related |
| [Citrine Data Retrieval Example](<https://github.com/CitrineInformatics/learn-citrination/blob/master/matminer_examples/DataRetrievalWithMatMiner.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Synthetic Data Demo](<https://github.com/CitrineInformatics/learn-citrination/blob/master/synthetic_data_examples/SyntheticDataDemo.ipynb>) | Homepage instructional resource table / Citrine | navigation |
| [Synthetic Data Demo](<https://github.com/CitrineInformatics/learn-citrination/tree/master/synthetic_data_examples>) | Homepage instructional resource table / Citrine | navigation |
| [NANO106 - Symmetry Computations on m3¯¯¯m (Oh) Point Group](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_4_point_group_symmetry/Symmetry%20Computations%20on%20m-3m%20%28O_h%29%20Point%20Group.ipynb>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [NANO106 - Symmetry Computations on mmm(D2h) Point Group](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_4_point_group_symmetry/Symmetry%20Computations%20on%20mmm%20%28D_2h%29%20Point%20Group.ipynb>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [NANO106 - Symmetry Computations on mmm(D2h) Point Group](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/tree/master/lectures/lecture_4_point_group_symmetry/>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [Using pymatgen to mine the Materials Project](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_5_the_230_space_groups/Datamining%20the%20Materials%20Project%20for%20Space%20Group%20statistics.ipynb>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [plot representation quadrics for some rank 2 tensors](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_10_principal_directions_and_representation_quadrics/Representation_quadrics.ipynb>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [plot an XRD plot for the two polymorphs of CsCl (Pm3¯¯¯m and Fm3¯¯¯m) by computing the structure factors](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_13_xrd/XRD%20CsCl.ipynb>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [plot an XRD plot for the two polymorphs of CsCl (Pm3¯¯¯m and Fm3¯¯¯m) by computing the structure factors](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/tree/master/lectures/lecture_13_xrd/>) | Homepage instructional resource table / MaterialsVirtualLab | adjacent |
| [Bayesian Optimization and Regression Analysis for Ferromagnetic Materials](<https://github.com/will-colea/BO_Magnetics>) | Homepage instructional resource table /  | navigation |
| [issue](<https://github.com/usnistgov/remi/issues>) | Repository README / remi | navigation |
| [Fe-Co-Ni](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni>) | Open Access Data list / Combinatorial Library Data | crystal_related |
| [Wang, A., et al. arXiv preprint arXiv:2204.05838 (2022).](<https://arxiv.org/abs/2204.05838>) | Open Access Data list / Combinatorial Library Data | uncertain |
| [Yoo, Y. K. et al. Intermetallics 14, 241–247 (2006).](<https://www.sciencedirect.com/science/article/pii/S096697950500186X>) | Open Access Data list / Combinatorial Library Data | uncertain |
| [Fe-Ga-Pd](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd>) | Open Access Data list / Combinatorial Library Data | crystal_related |
| [Kusne, A. G., et al. Nature communications 11.1 (2020): 1-11.](<https://www.nature.com/articles/s41467-020-19597-w>) | Open Access Data list / Combinatorial Library Data | uncertain |
| [Long, C. J., et al. Review of Scientific Instruments 78.7 (2007): 072217.](<https://aip.scitation.org/doi/full/10.1063/1.2755487>) | Open Access Data list / Combinatorial Library Data | uncertain |
| [Materials Resource Registery](<https://materials.registry.nist.gov/>) | Open Access Data list / General | navigation |
| [Materials Data Facility](<https://www.materialsdatafacility.org/>) | Open Access Data list / General | crystal_related |
| [AFLOW: Automatic FLOW for Materials Discovery](<http://www.aflow.org/>) | Open Access Data list / Computation-based | crystal_related |
| [JARVIS: Joint Automated Repository for Various Integrated Simulations](<https://jarvis.nist.gov/>) | Open Access Data list / Computation-based | crystal_related |
| [OQMD: Open Quantum Materials Database](<http://oqmd.org/>) | Open Access Data list / Computation-based | crystal_related |
| [Materials Project](<https://materialsproject.org/>) | Open Access Data list / Computation-based | crystal_related |
| [Software Carpentry: Python](<https://swcarpentry.github.io/python-novice-inflammation/>) | Learning Resources list / Programming Languages: | adjacent |
| [Software Carpentry: Plotting and Programming in Python](<http://swcarpentry.github.io/python-novice-gapminder/>) | Learning Resources list / Programming Languages: | adjacent |
| [Software Carpentry: Programming with R](<http://swcarpentry.github.io/r-novice-inflammation/>) | Learning Resources list / Programming Languages: | adjacent |
| [Software Carpentry: R for Reproducible Scientific Analysis](<http://swcarpentry.github.io/r-novice-gapminder/>) | Learning Resources list / Programming Languages: | adjacent |
| [List of Tutorials](<https://julialang.org/learning/tutorials/>) | Learning Resources list / Programming Languages: | navigation |
| [Scikit-Learn](<https://scikit-learn.org/stable/>) | Learning Resources list / Software Libraries: | adjacent |
| [Scikit-Image](<https://scikit-image.org/>) | Learning Resources list / Software Libraries: | navigation |
| [Jupyter Notebooks](<https://datacarpentry.org/python-ecology-lesson/jupyter_notebooks/>) | Learning Resources list / Notebook Tools: | adjacent |
| [Pluto Notebooks](<https://juliahub.com/docs/Pluto/OJqMt/0.7.4/>) | Learning Resources list / Notebook Tools: | adjacent |
| [Materials Data Facility](<https://www.materialsdatafacility.org/>) | Learning Resources list / Data Publishing: | crystal_related |
| [Materials Data Curation System](<https://mdcs.nist.gov/>) | Learning Resources list / Data Publishing: | crystal_related |
| [Git](<http://swcarpentry.github.io/git-novice/>) | Learning Resources list / Code handling: | navigation |
| [Introduction to Statistical Learning](<http://www-bcf.usc.edu/~gareth/ISL/>) | Learning Resources list / Machine Learning: | navigation |
| [Elements of Statistical Learning](<http://statweb.stanford.edu/~tibs/ElemStatLearn/>) | Learning Resources list / Machine Learning: | navigation |
| [Machine Learning in Materials Science: Recent Progress And Emerging Applications 2016](<https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=915933>) | Learning Resources list / Machine Learning: | navigation |
| [Machine Learning for Materials Research Bootcamp and Workshop](<https://www.nanocenter.umd.edu/events/mlmr-2021/>) | Learning Resources list / Machine Learning: | navigation |
| [Practical Deep Learning for Coders](<https://www.fast.ai/>) | Learning Resources list / Machine Learning: | navigation |
| [OpenDataScience Open Machine Learning Course](<https://mlcourse.ai/>) | Learning Resources list / Machine Learning: | navigation |
| [DataCamp](<https://www.datacamp.com>) | Learning Resources list / Machine Learning: | navigation |
| [Open Access Data](<https://pages.nist.gov/remi/data/>) | Site navigation | navigation |
| [Learning Resources](<https://pages.nist.gov/remi/learn/>) | Site navigation | navigation |
| [Homepage resource table CSV](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/_data/resources.csv>) | Site source | navigation |
| [FeCoNi_benchmark_dataset_220501a.mat](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni/FeCoNi_benchmark_dataset_220501a.mat>) | Open Access Data / Fe-Co-Ni | crystal_related |
| [data description.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni/data%20description.txt>) | Open Access Data / Fe-Co-Ni | navigation |
| [FeGaPd_CMP.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_CMP.txt>) | Open Access Data / Fe-Ga-Pd | crystal_related |
| [FeGaPd_DFT_regions.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_DFT_regions.txt>) | Open Access Data / Fe-Ga-Pd | crystal_related |
| [FeGaPd_Mag.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_Mag.txt>) | Open Access Data / Fe-Ga-Pd | crystal_related |
| [FeGaPd_XRD.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_XRD.txt>) | Open Access Data / Fe-Ga-Pd | crystal_related |
| [data description.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/data%20description.txt>) | Open Access Data / Fe-Ga-Pd | navigation |

### [sedaoturak/data-resources-for-materials-science](<https://github.com/sedaoturak/data-resources-for-materials-science>)

Inspected revision: `0df2e06e7caa6a49f807c20a068ce98050a14d13`.

Inspection boundary and caveats:

- GitHub recursive tree for the default branch contains exactly one tracked file, README.md; no additional in-repository source lists exist.
- Extracted 90 link occurrences and 87 distinct public URLs across Markdown sections; repeated links retain separate section provenance.
- All raw HTTP(S) URL tokens in the README were accounted for by Markdown-link extraction.
- README SHA-256: ce849ca3f98268ab0529c7081e10060c89757a673f2e2185babf388d489e2065. GitHub blob SHA: 63e7676bdd45169a66e8cba38d6acf9008ccf67d.
- Collection descriptions and historic counts are discovery leads, not independently verified dataset metadata.
- Scope labels preserve isolated-molecule, polymer, amorphous, microscopy, processing and navigation links without automatically ranking them as crystal datasets.
- Canonical comparison performed against data/datasets.json (115 rows) and data/resources.json (27 resources), snapshot during this audit.
- Verified additions are provided in research/collection_sedaoturak_additions.json. Work-function data have a CC BY-NC restriction; perovskite devices carry CC BY 4.0; TQC underlying ICSD-coordinate rights are not assumed.

90 labeled link occurrences; 87 distinct URLs. Section and scope labels preserve the collection context.

| Linked source | Original section | Scope |
|---|---|---|
| [NIST Materials Genome Initiative (MGI)](<https://www.nist.gov/mgi>) | Databases in Materials Science | navigation |
| [NIST Materials Data Curation System (Part of MGI)](<https://phasedata.nist.gov/>) | Databases in Materials Science | crystal_related |
| [NIST Materials Data Repository (Part of MGI)](<https://materialsdata.nist.gov/>) | Databases in Materials Science | navigation |
| [MDR NIMS Materials Data Repository](<https://mdr.nims.go.jp/>) | Databases in Materials Science | navigation |
| [The NIMS Materials Database (MatNavi)](<https://mits.nims.go.jp/en/>) | Databases in Materials Science | navigation |
| [The Novel Materials Discovery (NOMAD) Laboratory](<https://nomad-lab.eu/index.php?page=repo-arch>) | Databases in Materials Science | navigation |
| [notebooks](<https://nomad-lab.eu/aitoolkit>) | Databases in Materials Science | navigation |
| [The Materials Data Facility (MDF)](<https://materialsdatafacility.org/>) | Databases in Materials Science | navigation |
| [The Joint Automated Repository for Various Integrated Simulations (JARVIS)](<https://jarvis.nist.gov/>) | Databases in Materials Science | crystal_related |
| [Materials Project](<https://materialsproject.org/>) | Databases in Materials Science | crystal_related |
| [Pauling File](<https://paulingfile.com/>) | Databases in Materials Science | crystal_related |
| [MPDS](<https://mpds.io>) | Databases in Materials Science | crystal_related |
| [NIST Alloy Data](<https://trc.nist.gov/metals_data/>) | Databases in Materials Science | uncertain |
| [NIST Structural Ceramics Database (SCD) Database](<https://srdata.nist.gov/CeramicDataPortal/scd>) | Databases in Materials Science | uncertain |
| [Polymer Property Predictor and Database](<https://pppdb.uchicago.edu/>) | Databases in Materials Science | adjacent |
| [NIST Standard Reference Data (SRD)](<https://www.nist.gov/srd/srd-catalog>) | Databases in Materials Science | navigation |
| [NIST Self-Diffusion Data](<https://www.ctcms.nist.gov/~gkl/selfdiffusion.html>) | Databases in Materials Science | uncertain |
| [Open Quantum Materials Database (OQMD)](<http://oqmd.org/>) | Databases in Materials Science | crystal_related |
| [Automatic Flow for Materials Discovery (AFLOW)](<http://www.aflowlib.org/>) | Databases in Materials Science | crystal_related |
| [NRELMatDB](<https://materials.nrel.gov/>) | Databases in Materials Science | crystal_related |
| [High Throughput Experimental Materials Database (HTEM DB)](<https://htem.nrel.gov/>) | Databases in Materials Science | crystal_related |
| [Matmatch](<https://matmatch.com/>) | Databases in Materials Science | navigation |
| [MatWeb](<http://www.matweb.com/>) | Databases in Materials Science | navigation |
| [Materials Cloud](<https://www.materialscloud.org/>) | Databases in Materials Science | navigation |
| [Knowledgebase of Interatomic Models (OpenKIM)](<https://openkim.org/>) | Databases in Materials Science | navigation |
| [Materials Commons](<https://materialscommons.org/>) | Databases in Materials Science | navigation |
| [Crystallography Open Database (COD)](<http://www.crystallography.net/cod/>) | Databases in Materials Science | crystal_related |
| [Organic Materials Database (OMDB)](<https://omdb.mathub.io/>) | Databases in Materials Science | crystal_related |
| [Open Reaction Database (ORD)](<https://open-reaction-database.org>) | Databases in Materials Science | adjacent |
| [Polymer Genome](<https://www.polymergenome.org/>) | Databases in Materials Science | adjacent |
| [DoITPoMS Micrograph Library](<https://www.doitpoms.ac.uk/miclib/index.php>) | Databases in Materials Science | adjacent |
| [Python for Glass Genomics (PyGGi)](<https://pyggi.iitd.ac.in/>) | Databases in Materials Science | adjacent |
| [The Engineering Toolbox](<https://www.engineeringtoolbox.com/material-properties-t_24.html>) | Databases in Materials Science | navigation |
| [nanoHUB](<https://nanohub.org/publications/datasets>) | Databases in Materials Science | navigation |
| [NanoMine](<https://github.com/Duke-MatSci/nanomine>) | Databases in Materials Science | adjacent |
| [Topological Quantum Chemistry](<https://www.topologicalquantumchemistry.com/#/>) | Databases in Materials Science | crystal_related |
| [SciGlass](<https://github.com/epam/SciGlass>) | Databases in Materials Science | adjacent |
| [ORNL_AISD-Ex](<https://www.osti.gov/biblio/1907919>) | Databases in Materials Science | adjacent |
| [The Perovskite Database Project](<https://www.perovskitedatabase.com/>) | Databases in Materials Science | crystal_related |
| [Polymer Scholar](<https://polymerscholar.org/>) | Databases in Materials Science | adjacent |
| [Computational Materials Repository (CMR)](<https://cmr.fysik.dtu.dk/index.html>) | Databases in Materials Science | navigation |
| [Fatigue Database of AM Alloys2022](<https://figshare.com/articles/dataset/Fatigue_Database_of_Additively_Manufactured_Alloys/22337629>) | Databases in Materials Science | adjacent |
| [DigiMOF](<https://figshare.com/collections/DigiMOF_A_Database_of_Metal_Organic_Framework_Synthesis_Information_Generated_via_Text_Mining/6652495>) | Databases in Materials Science | crystal_related |
| [OpenDAC](<https://open-dac.github.io/>) | Databases in Materials Science | crystal_related |
| [Catalysis-Hub.org](<https://www.catalysis-hub.org/>) | Databases in Materials Science | crystal_related |
| [Springer Materials](<https://materials.springer.com/>) | Databases in Materials Science | navigation |
| [BEAST DB](<https://beastdb.nrel.gov/>) | Databases in Materials Science | crystal_related |
| [COD_HEM](<https://codhem.cecas.clemson.edu/login>) | Databases in Materials Science | uncertain |
| [COD_HEM associated paper](<https://www.sciencedirect.com/science/article/abs/pii/S0927025624008097>) | Databases in Materials Science | uncertain |
| [Alexandria Databases](<https://alexandria.icams.rub.de>) | Databases in Materials Science | crystal_related |
| [Stress-Strain Properties Database](<https://github.com/gh-PankajKumar/chemdataextractorv2.3-stresseng>) | Databases in Materials Science | adjacent |
| [ICEM Database](<https://www.innomat.se/icem>) | Databases in Materials Science | adjacent |
| [Figshare](<https://figshare.com/>) | Datasets in Materials Science | navigation |
| [Zenodo](<https://zenodo.org/>) | Datasets in Materials Science | navigation |
| [NIST Materials Resource Registry](<https://materials.registry.nist.gov/explore/keyword/>) | Datasets in Materials Science | navigation |
| [Mendeley Data](<https://data.mendeley.com/>) | Datasets in Materials Science | navigation |
| [Materials Cloud](<https://www.materialscloud.org/>) | Datasets in Materials Science | navigation |
| [Materials Commons](<https://materialscommons.org/>) | Datasets in Materials Science | navigation |
| [OPoly26](<https://huggingface.co/facebook/OMol25#open-polymers-2026-opoly26-dataset>) | Datasets in Materials Science | adjacent |
| [OMol25 (The Open Molecules 2025)](<https://huggingface.co/facebook/OMol25>) | Datasets in Materials Science | adjacent |
| [OC25 (The Open Catalyst 2025)](<https://huggingface.co/facebook/OC25>) | Datasets in Materials Science | crystal_related |
| [OMat24](<https://fair-chem.github.io/inorganic_materials/datasets/omat24.html>) | Datasets in Materials Science | crystal_related |
| [OCx24](<https://fair-chem.github.io/catalysts/datasets/ocx24.html>) | Datasets in Materials Science | crystal_related |
| [ODAC23](<https://fair-chem.github.io/dac/datasets/odac.html>) | Datasets in Materials Science | crystal_related |
| [AQCat25](<https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset>) | Datasets in Materials Science | crystal_related |
| [QCML](<https://zenodo.org/records/14859804>) | Datasets in Materials Science | adjacent |
| [QM9Star](<https://doi.org/10.6084/m9.figshare.27002905>) | Datasets in Materials Science | adjacent |
| [Work function and cleavage energy dataset](<https://zenodo.org/records/10703249>) | Datasets in Materials Science | crystal_related |
| [MatPES](<https://matpes.ai/>) | Datasets in Materials Science | crystal_related |
| [MAD-1.5](<https://archive.materialscloud.org/records/18tke-tt476>) | Datasets in Materials Science | crystal_related |
| [MSR-ACC/TAE25](<https://zenodo.org/records/17629321>) | Datasets in Materials Science | adjacent |
| [MatSyn25](<https://huggingface.co/datasets/MatSynAI/MatSyn25>) | Datasets in Materials Science | crystal_related |
| [AM26](<https://github.com/vldgroup/AM26>) | Datasets in Materials Science | adjacent |
| [MOFs_CO2N2O2_ML](<https://github.com/hasancangulbalkan/MOFs_CO2N2O2_ML>) | Datasets in Materials Science | crystal_related |
| [STEM Bank 26](<https://huggingface.co/buckets/ghollyer/STEM-Bank-26>) | Datasets in Materials Science | adjacent |
| [sysTEm](<https://github.com/tankylz/sysTEm_dataset>) | Datasets in Materials Science | adjacent |
| [Ductile Cast Iron Project](<https://www.ductilecastironproject.com/>) | Datasets in Materials Science | adjacent |
| [nanoHUB](<https://nanohub.org/publications/datasets>) | Datasets in Materials Science | navigation |
| [CHiMAD NIST (TDDFT)](<https://acdc.alcf.anl.gov/mdf/detail/kononov_firstprinciples_simulation_graphene_v1.1/>) | Datasets in Materials Science | crystal_related |
| [Mechanical-MNIST](<https://github.com/elejeune11/Mechanical-MNIST>) | Datasets in Materials Science | adjacent |
| [Elastomeric Foam Materials](<https://acdc.alcf.anl.gov/mdf/detail/foam_db_v1.1/>) | Datasets in Materials Science | adjacent |
| [Polyinfo](<https://polymer.nims.go.jp/>) | Datasets in Materials Science | adjacent |
| [GNoME](<https://github.com/google-deepmind/materials_discovery?tab=readme-ov-file#dataset>) | Datasets in Materials Science | crystal_related |
| [MP_ALOE](<https://figshare.com/articles/dataset/MP-ALOE_An_r2SCAN_dataset_for_universal_machine_learning_interatomic_potentials/29452190>) | Datasets in Materials Science | crystal_related |
| [Peregrine](<https://doi.ccs.ornl.gov/dataset/96b7da99-07e1-562d-88d5-d7e079acfef7>) | Datasets in Materials Science | adjacent |
| [BOS-TMC Dataset](<https://zenodo.org/records/19410245>) | Datasets in Materials Science | adjacent |
| [Machine Learning Materials Datasets](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>) | Toy Datasets for Machine Learning Applications in Materials Science | adjacent |
| [JARVIS Materials Design – Tools, Notebooks](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks>) | Toy Datasets for Machine Learning Applications in Materials Science | navigation |
| [Machine Learning Lab Module](<https://nanohub.org/tools/intromllab>) | Toy Datasets for Machine Learning Applications in Materials Science | navigation |
| [REMI: REsource for Materials Informatics](<https://pages.nist.gov/remi/>) | Toy Datasets for Machine Learning Applications in Materials Science | navigation |

## Ranked catalog: official routes and evidence

### Aggregated and deduplicated crystal collections

#### MateriaViva Open

Release: Provider page snapshot, checked 2026-11-01.

- Homepage: [MateriaViva Open](<https://huggingface.co/datasets/AI4QC/MateriaViva-Open>)
- Evidence (2026-11-01): [MateriaViva Open — primary documentation](<https://huggingface.co/datasets/AI4QC/MateriaViva-Open>)

#### LeMat-Bulk

Release: Main card/config metadata snapshot (2025 release).

- Homepage: [LeMat-Bulk](<https://huggingface.co/datasets/LeMaterial/LeMat-Bulk>)
- Evidence (2026-11-01): [LeMat-Bulk — primary documentation](<https://huggingface.co/datasets/LeMaterial/LeMat-Bulk>)

#### LeMat-BulkUnique

Release: December 2024 card snapshot.

- Homepage: [LeMat-BulkUnique](<https://huggingface.co/datasets/LeMaterial/LeMat-BulkUnique>)
- Evidence (2026-11-01): [LeMat-BulkUnique — primary documentation](<https://huggingface.co/datasets/LeMaterial/LeMat-BulkUnique>)

### Computed bulk inorganic crystals

#### Alexandria

Release: 2025-07-02 PBE release, described in 2026 paper.

- Homepage: [Alexandria](<https://alexandria.icams.rub.de/>)
- Data: [Alexandria](<https://alexandria.icams.rub.de/datasets.html>)
- Paper: [Alexandria](<https://doi.org/10.1088/2515-7639/ae6620>)
- Evidence (2026-11-01): [Alexandria — primary documentation](<https://doi.org/10.1088/2515-7639/ae6620>)

#### AFLOW

Release: Provider page snapshot, checked 2026-11-01.

- Homepage: [AFLOW](<https://aflow.org/>)
- Data: [AFLOW](<https://aflow.org/API/aflowlib_stats/>)
- Code: [AFLOW](<https://github.com/aflow-org/aflow>)
- Evidence (2026-11-01): [AFLOW — primary documentation](<https://aflow.org/API/aflowlib_stats/>)
- Evidence (2026-11-01): [AFLOW documentation and data disclaimer](<https://aflow.org/documentation/>)

#### OQMD

Release: Provider page snapshot, checked 2026-11-01.

- Homepage: [OQMD](<https://oqmd.org/>)
- Data: [OQMD](<https://oqmd.org/download/>)
- Evidence (2026-11-01): [OQMD — primary documentation](<https://oqmd.org/>)

#### GNoME released stable-materials set

Release: Public stable-materials set; June 2024 overlap update.

- Homepage: [GNoME released stable-materials set](<https://github.com/google-deepmind/materials_discovery>)
- Data: [GNoME released stable-materials set](<https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md>)
- Paper: [GNoME released stable-materials set](<https://doi.org/10.1038/s41586-023-06735-9>)
- Evidence (2026-11-01): [GNoME released stable-materials set — primary documentation](<https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md>)

#### Carolina Materials Database

Release: Provider page snapshot, checked 2026-11-01.

- Homepage: [Carolina Materials Database](<http://www.carolinamatdb.org/>)
- Evidence (2026-11-01): [Carolina Materials Database — primary documentation](<http://www.carolinamatdb.org/>)

#### Materials Project

Release: Homepage v2026.04.13 snapshot.

- Homepage: [Materials Project](<https://materialsproject.org/>)
- Data: [Materials Project](<https://docs.materialsproject.org/downloading-data>)
- Paper: [Materials Project](<https://doi.org/10.1063/1.4812323>)
- Evidence (2026-11-01): [Materials Project — primary documentation](<https://doi.org/10.17188/1693272>)
- Evidence (2026-11-01): [Materials Project database versions](<https://docs.materialsproject.org/changes/database-versions>)

#### JARVIS-DFT 3D

Release: dft_3d / 2022-12-12 downloader release.

- Homepage: [JARVIS-DFT 3D](<https://jarvis.nist.gov/>)
- Data: [JARVIS-DFT 3D](<https://doi.org/10.6084/m9.figshare.6815699>)
- Code: [JARVIS-DFT 3D](<https://github.com/usnistgov/jarvis>)
- Evidence (2026-11-01): [JARVIS-DFT 3D — primary documentation](<https://github.com/usnistgov/jarvis/blob/master/jarvis/db/figshare.py>)
- Evidence (2026-11-01): [JARVIS-DFT 3D Figshare metadata](<https://api.figshare.com/v2/articles/6815699>)

#### Materials Cloud 3D (MC3D)

Release: PBEsol-v2 (2025 paper).

- Homepage: [Materials Cloud 3D (MC3D)](<https://www.materialscloud.org/discover/mc3d>)
- Data: [Materials Cloud 3D (MC3D)](<https://archive.materialscloud.org/records/szjaf-cfv74>)
- Paper: [Materials Cloud 3D (MC3D)](<https://arxiv.org/abs/2508.19223>)
- Evidence (2026-11-01): [Materials Cloud 3D (MC3D) — primary documentation](<https://arxiv.org/abs/2508.19223>)

#### NLR MatDB (formerly NRELMatDB)

Release: Official portal snapshot checked 2026-11-01.

- Homepage: [NLR MatDB (formerly NRELMatDB)](<https://materials.nlr.gov/>)
- Data: [NLR MatDB (formerly NRELMatDB)](<https://materials.nlr.gov/>)
- Paper: [NLR MatDB (formerly NRELMatDB)](<https://doi.org/10.1103/PhysRevB.85.115104>)
- Code: [NLR MatDB (formerly NRELMatDB)](<https://github.com/pylada/pylada-light>)
- Evidence (2026-11-01): [NLR MatDB official portal](<https://materials.nlr.gov/>)
- Evidence (2026-11-01): [NLR MatDB help](<https://materials.nlr.gov/help>)

### Experimental crystallography and reference collections

#### Cambridge Structural Database (CSD)

Release: CCDC publication-year statistics, 2026-01-01.

- Homepage: [Cambridge Structural Database (CSD)](<https://www.ccdc.cam.ac.uk/solutions/software/csd/>)
- Data: [Cambridge Structural Database (CSD)](<https://www.ccdc.cam.ac.uk/structures/>)
- Evidence (2026-11-01): [CCDC CSD Publication Year Statistics, 1 January 2026](<https://www.ccdc.cam.ac.uk/media/CSD-Publication-Year-Statistics-2026.pdf>)
- Evidence (2026-11-01): [CCDC: Access Structures downloads](<https://support.ccdc.cam.ac.uk/support/solutions/articles/103000306361/>)
- Evidence (2026-11-01): [CCDC/FIZ Access Structures](<https://www.ccdc.cam.ac.uk/structures/>)

#### Crystallography Open Database (COD)

Release: Live homepage, accessed 2026-11-01.

- Homepage: [Crystallography Open Database (COD)](<https://www.crystallography.net/cod/>)
- Data: [Crystallography Open Database (COD)](<https://www.crystallography.net/cod/archives/>)
- Evidence (2026-11-01): [COD official mirror](<https://cod.psdi.ac.uk/>)

#### Materials Platform for Data Science (MPDS / PAULING FILE)

Release: Live provider counters, accessed 2026-11-01.

- Homepage: [Materials Platform for Data Science (MPDS / PAULING FILE)](<https://mpds.io/>)
- Data: [Materials Platform for Data Science (MPDS / PAULING FILE)](<https://mpds.io/#start>)
- Code: [Materials Platform for Data Science (MPDS / PAULING FILE)](<https://mpds.io/developer/>)
- Evidence (2026-11-01): [MPDS provider home](<https://mpds.io/>)
- Evidence (2026-11-01): [MPDS introduction](<https://mpds.io/tutorial/>)

#### NIMS AtomWork-Adv

Release: 2026-03-31 NIMS statistics.

- Homepage: [NIMS AtomWork-Adv](<https://atomwork-adv.nims.go.jp/>)
- Data: [NIMS AtomWork-Adv](<https://atomwork-adv.nims.go.jp/en/service.html>)
- Evidence (2026-11-01): [MEXT/NIMS materials data infrastructure presentation](<https://www.mext.go.jp/content/20260522-mxt_jyohoka01-000050160_3.pdf>)
- Evidence (2026-11-01): [AtomWork-Adv provider service terms](<https://atomwork-adv.nims.go.jp/service.html?lan=jp>)
- Evidence (2026-11-01): [A comprehensive data network for data-driven study of battery materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC11573338/>)

#### Pearson's Crystal Data

Release: Release 2023/24.

- Homepage: [Pearson's Crystal Data](<https://crystalimpact.com/pcd/>)
- Data: [Pearson's Crystal Data](<https://asm.mpds.io/>)
- Evidence (2026-11-01): [Pearson's Crystal Data publisher page](<https://crystalimpact.com/pcd/>)

#### Inorganic Crystal Structure Database (ICSD)

Release: 2026-10-30 announcement.

- Homepage: [Inorganic Crystal Structure Database (ICSD)](<https://icsd.products.fiz-karlsruhe.de/en>)
- Data: [Inorganic Crystal Structure Database (ICSD)](<https://icsd.fiz-karlsruhe.de/>)
- Evidence (2026-11-01): [ICSD home](<https://icsd.products.fiz-karlsruhe.de/en>)
- Evidence (2026-11-01): [About ICSD](<https://icsd.products.fiz-karlsruhe.de/en/about/about-icsd>)
- Evidence (2026-11-01): [ICSD products](<https://icsd.products.fiz-karlsruhe.de/en/products/icsd-products>)

#### NIMS AtomWork

Release: Historical NIMS data table reproduced in 2020 government materials.

- Homepage: [NIMS AtomWork](<https://mits.nims.go.jp/en/>)
- Data: [NIMS AtomWork](<https://crystdb.nims.go.jp/>)
- Evidence (2026-11-01): [MEXT materials data reference, NIMS-provided table](<https://www.mext.go.jp/content/20200602-mxt_nanozai-000007507_6_2.pdf>)
- Evidence (2026-11-01): [NIMS MatNavi](<https://mits.nims.go.jp/en/>)

#### MAGNDATA

Release: Live landing page, accessed 2026-11-01.

- Homepage: [MAGNDATA](<https://cryst.ehu.es/magndata/>)
- Data: [MAGNDATA](<https://cryst.ehu.es/magndata/magndata_download.html>)
- Evidence (2026-11-01): [MAGNDATA landing page](<https://cryst.ehu.es/magndata/>)
- Evidence (2026-11-01): [MAGNDATA bulk download instructions](<https://test2.cryst.ehu.eus/magndata/magndata_download.html>)

#### American Mineralogist Crystal Structure Database (AMCSD)

Release: Current RRUFF documentation.

- Homepage: [American Mineralogist Crystal Structure Database (AMCSD)](<https://www.rruff.net/>)
- Data: [American Mineralogist Crystal Structure Database (AMCSD)](<https://www.rruff.net/about/download-data/>)
- Evidence (2026-11-01): [RRUFF FAQ: AMCSD](<https://www.rruff.net/help/faq/>)
- Evidence (2026-11-01): [RRUFF: ZIP download](<https://www.rruff.net/help/zip-download/>)

### Bulk and mixed-domain MLIP configurations

#### LeMat-Traj

Release: Main metadata/API snapshot, verified 2026-11-01.

- Homepage: [LeMat-Traj](<https://huggingface.co/datasets/LeMaterial/LeMat-Traj>)
- Evidence (2026-11-01): [LeMat-Traj — primary documentation](<https://huggingface.co/datasets/LeMaterial/LeMat-Traj>)
- Evidence (2026-11-01): [LeMat-Traj dataset server metadata](<https://datasets-server.huggingface.co/info?dataset=LeMaterial%2FLeMat-Traj>)

#### Open Materials 2024 (OMat24)

Release: 2024-10-18 train + corrected 2024-12-20 validation.

- Homepage: [Open Materials 2024 (OMat24)](<https://huggingface.co/datasets/facebook/OMAT24>)
- Data: [Open Materials 2024 (OMat24)](<https://huggingface.co/datasets/facebook/OMAT24>)
- Paper: [Open Materials 2024 (OMat24)](<https://doi.org/10.1038/s43588-026-00996-w>)
- Code: [Open Materials 2024 (OMat24)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [Open Materials 2024 (OMat24) — primary documentation](<https://huggingface.co/datasets/facebook/OMAT24>)

#### ELEMENTA public core release

Release: First public release; card checked 2026-11-01.

- Homepage: [ELEMENTA public core release](<https://huggingface.co/datasets/kairosmaterial/ELEMENTA>)
- Evidence (2026-11-01): [ELEMENTA public core release — primary documentation](<https://huggingface.co/datasets/kairosmaterial/ELEMENTA>)

#### sAlex25

Release: sAlex25; 2026 expansion paper.

- Homepage: [sAlex25](<https://alexandria.icams.rub.de/datasets.html>)
- Data: [sAlex25](<https://alexandria.icams.rub.de/datasets.html>)
- Paper: [sAlex25](<https://doi.org/10.1088/2515-7639/ae6620>)
- Evidence (2026-11-01): [sAlex25 — primary documentation](<https://doi.org/10.1088/2515-7639/ae6620>)

#### sAlex (OMat24 distribution)

Release: 2024-10-18 sAlex train/validation.

- Homepage: [sAlex (OMat24 distribution)](<https://huggingface.co/datasets/facebook/OMAT24>)
- Evidence (2026-11-01): [sAlex (OMat24 distribution) — primary documentation](<https://huggingface.co/datasets/facebook/OMAT24>)

#### ELEMENTA Spin

Release: Provider page snapshot, checked 2026-11-01.

- Homepage: [ELEMENTA Spin](<https://huggingface.co/datasets/kairosmaterial/ELEMENTA>)
- Evidence (2026-11-01): [ELEMENTA Spin — primary documentation](<https://huggingface.co/datasets/kairosmaterial/ELEMENTA>)

#### Materials Project Trajectory (MPtrj)

Release: MP 2022.9-derived MPtrj / 2023 release.

- Homepage: [Materials Project Trajectory (MPtrj)](<https://github.com/CederGroupHub/chgnet>)
- Data: [Materials Project Trajectory (MPtrj)](<https://doi.org/10.6084/m9.figshare.23713842>)
- Paper: [Materials Project Trajectory (MPtrj)](<https://doi.org/10.1038/s42256-023-00716-3>)
- Evidence (2026-11-01): [Materials Project Trajectory (MPtrj) — primary documentation](<https://api.figshare.com/v2/articles/23713842>)

#### MP-ALOE

Release: 2025 published dataset.

- Homepage: [MP-ALOE](<https://doi.org/10.1038/s41524-025-01834-9>)
- Paper: [MP-ALOE](<https://arxiv.org/abs/2507.05559>)
- Data: [MP-ALOE](<https://doi.org/10.1038/s41524-025-01834-9>)
- Evidence (2026-11-01): [MP-ALOE — primary documentation](<https://doi.org/10.1038/s41524-025-01834-9>)

#### MatPES

Release: 2025.1 size reference; 2025.2 available since 2026-04-15.

- Homepage: [MatPES](<https://matpes.ai/>)
- Data: [MatPES](<https://huggingface.co/datasets/materialyze/matpes>)
- Paper: [MatPES](<https://arxiv.org/abs/2503.04070>)
- Code: [MatPES](<https://github.com/materialyzeai/matpes>)
- Evidence (2026-11-01): [MatPES — primary documentation](<https://github.com/materialyzeai/matpes>)

#### ALIGNN-FF training dataset

Release: 2023 ALIGNN-FF dataset.

- Homepage: [ALIGNN-FF training dataset](<https://github.com/usnistgov/alignn>)
- Data: [ALIGNN-FF training dataset](<https://github.com/usnistgov/jarvis/blob/master/jarvis/db/figshare.py>)
- Paper: [ALIGNN-FF training dataset](<https://doi.org/10.1039/D2DD00096B>)
- Evidence (2026-11-01): [ALIGNN-FF training dataset — primary documentation](<https://doi.org/10.1039/D2DD00096B>)

#### Massive Atomic Diversity (MAD-1.5)

Release: MAD-1.5, arXiv v2.

- Homepage: [Massive Atomic Diversity (MAD-1.5)](<https://arxiv.org/html/2603.02089v2>)
- Evidence (2026-11-01): [Massive Atomic Diversity (MAD-1.5) — primary documentation](<https://arxiv.org/html/2603.02089v2>)

#### MPF.2021.2.8

Release: 2021-02-08 source / original MPF release.

- Homepage: [MPF.2021.2.8](<https://github.com/materialsvirtuallab/m3gnet>)
- Data: [MPF.2021.2.8](<https://doi.org/10.6084/m9.figshare.19470599>)
- Paper: [MPF.2021.2.8](<https://doi.org/10.1038/s41524-024-01227-4>)
- Evidence (2026-11-01): [MPF.2021.2.8 — primary documentation](<https://www.nature.com/articles/s41524-024-01227-4>)

#### Carbon-data synthetic atomistic trajectories

Release: Provider README, checked 2026-11-01.

- Homepage: [Carbon-data synthetic atomistic trajectories](<https://github.com/jla-gardner/carbon-data>)
- Data: [Carbon-data synthetic atomistic trajectories](<https://github.com/jla-gardner/carbon-data/tree/main/results>)
- Paper: [Carbon-data synthetic atomistic trajectories](<https://arxiv.org/abs/2211.16443>)
- Evidence (2026-11-01): [Carbon-data author README](<https://raw.githubusercontent.com/jla-gardner/carbon-data/main/README.md>)

#### Massive Atomic Diversity (MAD-1.6)

Release: MAD-1.6 archive, October 2026.

- Homepage: [Massive Atomic Diversity (MAD-1.6)](<https://archive.materialscloud.org/records/ffd5a-1hc37>)
- Evidence (2026-11-01): [Massive Atomic Diversity (MAD-1.6) — primary documentation](<https://archive.materialscloud.org/records/ffd5a-1hc37>)
- Evidence (2026-11-01): [MAD-1.6 Materials Cloud metadata](<https://archive.materialscloud.org/api/records/ffd5a-1hc37>)

#### OpenLAM TrainingSet

Release: OpenLAM-TrainingSet-v1 (2025); later model variants use revised collections.

- Homepage: [OpenLAM TrainingSet](<https://www.aissquare.com/datasets/detail?pageType=datasets&name=OpenLAM-TrainingSet-v1&id=308>)
- Evidence (2026-11-01): [OpenLAM TrainingSet — primary documentation](<https://www.aissquare.com/datasets/detail?pageType=datasets&name=OpenLAM-TrainingSet-v1&id=308>)

### Two-dimensional and layered materials

#### Computational 2D Materials Database (C2DB)

Release: 2024-05-01 release listed on official 2DHub page.

- Homepage: [Computational 2D Materials Database (C2DB)](<https://2dhub.org/c2db/c2db.html>)
- Paper: [Computational 2D Materials Database (C2DB)](<https://doi.org/10.1088/2053-1583/ac1059>)
- Evidence (2026-11-01): [C2DB official release history](<https://2dhub.org/c2db/c2db.html>)

#### van der Waals Bilayer Database (BiDB)

Release: 2024 publication dataset.

- Homepage: [van der Waals Bilayer Database (BiDB)](<https://2dhub.org/bidb/bidb.html>)
- Data: [van der Waals Bilayer Database (BiDB)](<https://2dhub.org/bidb/bidb.html>)
- Paper: [van der Waals Bilayer Database (BiDB)](<https://doi.org/10.1038/s41467-024-45003-w>)
- Evidence (2026-11-01): [BiDB official page](<https://2dhub.org/bidb/bidb.html>)

#### 2DMatPedia

Release: Figshare v3, 2019.

- Homepage: [2DMatPedia](<http://www.2dmatpedia.org/>)
- Data: [2DMatPedia](<https://figshare.com/articles/dataset/7699910/3>)
- Paper: [2DMatPedia](<https://doi.org/10.1038/s41597-019-0097-3>)
- Evidence (2026-11-01): [2DMatPedia official Figshare metadata](<https://api.figshare.com/v2/articles/7699910>)
- Evidence (2026-11-01): [2DMatPedia official JSONL data](<https://ndownloader.figshare.com/files/14399918>)
- Evidence (2026-11-01): [2DMatPedia author paper](<https://arxiv.org/abs/1901.09487>)
- Evidence (2026-11-01): [2DMatPedia, an open computational database of two-dimensional materials from top-down and bottom-up approaches — Scientific Data descriptor](<https://doi.org/10.1038/s41597-019-0097-3>)

#### Materials Cloud Two-Dimensional Structure Database (MC2D)

Release: Materials Cloud 2022.84 v1 / 2023 paper.

- Homepage: [Materials Cloud Two-Dimensional Structure Database (MC2D)](<https://mc2d.materialscloud.org/>)
- Data: [Materials Cloud Two-Dimensional Structure Database (MC2D)](<https://archive.materialscloud.org/records/17gf6-84915>)
- Paper: [Materials Cloud Two-Dimensional Structure Database (MC2D)](<https://doi.org/10.1021/acsnano.2c11510>)
- Evidence (2026-11-01): [MC2D archived release](<https://archive.materialscloud.org/records/17gf6-84915>)
- Evidence (2026-11-01): [MC2D record metadata](<https://archive.materialscloud.org/api/records/17gf6-84915>)

#### Quantum Point Defects Database (QPOD)

Release: 2022-07-11 release table.

- Homepage: [Quantum Point Defects Database (QPOD)](<https://2dhub.org/qpod/qpod.html>)
- Paper: [Quantum Point Defects Database (QPOD)](<https://doi.org/10.1038/s41524-022-00730-w>)
- Evidence (2026-11-01): [QPOD official page](<https://2dhub.org/qpod/qpod.html>)

#### JARVIS-DFT 2D snapshot

Release: d2-12-12-2022.json / Figshare v8.

- Homepage: [JARVIS-DFT 2D snapshot](<https://pages.nist.gov/jarvis/databases/>)
- Data: [JARVIS-DFT 2D snapshot](<https://figshare.com/articles/dataset/6815705>)
- Paper: [JARVIS-DFT 2D snapshot](<https://doi.org/10.1038/s41524-020-00440-1>)
- Code: [JARVIS-DFT 2D snapshot](<https://github.com/usnistgov/jarvis>)
- Evidence (2026-11-01): [JARVIS-DFT 2D Figshare release](<https://api.figshare.com/v2/articles/6815705>)
- Evidence (2026-11-01): [Official JARVIS 2D payload](<https://ndownloader.figshare.com/files/38521268>)
- Evidence (2026-11-01): [JARVIS data registry](<https://pages.nist.gov/jarvis/databases/>)

#### 2D-Alloy Database

Release: 2DHub provider documentation updated 2026-09-30.

- Homepage: [2D-Alloy Database](<https://2dhub.org/2dalloys/2dalloys.html>)
- Data: [2D-Alloy Database](<https://2dhub.org/_downloads/93db2a0b33028278cf5e22b17a3994f7/2dalloys.db>)
- Paper: [2D-Alloy Database](<https://doi.org/10.1021/jacs.4c13863>)
- Evidence (2026-11-01): [2DHub: 2D-Alloy Database](<https://2dhub.org/2dalloys/2dalloys.html>)

#### van der Waals 2D Heterostructure Database (HetDB)

Release: 2025 publication dataset.

- Homepage: [van der Waals 2D Heterostructure Database (HetDB)](<https://2dhub.org/hetdb/hetdb.html>)
- Paper: [van der Waals 2D Heterostructure Database (HetDB)](<https://doi.org/10.1103/cl8c-8f1f>)
- Evidence (2026-11-01): [HetDB official page](<https://2dhub.org/hetdb/hetdb.html>)

### MOFs, COFs and zeolites

#### Open Direct Air Capture 2025 (ODAC25)

Release: 2025 release.

- Data: [Open Direct Air Capture 2025 (ODAC25)](<https://huggingface.co/facebook/ODAC25>)
- Paper: [Open Direct Air Capture 2025 (ODAC25)](<https://arxiv.org/abs/2508.03162>)
- Code: [Open Direct Air Capture 2025 (ODAC25)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [ODAC25 official dataset documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac25.md>)
- Evidence (2026-11-01): [ODAC25 official access page](<https://huggingface.co/facebook/ODAC25/tree/main>)

#### Open Direct Air Capture 2023 (ODAC23)

Release: 2023 corpus / 2024 ACS Central Science descriptor.

- Homepage: [Open Direct Air Capture 2023 (ODAC23)](<https://open-dac.github.io/>)
- Data: [Open Direct Air Capture 2023 (ODAC23)](<https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac23.md>)
- Paper: [Open Direct Air Capture 2023 (ODAC23)](<https://doi.org/10.1021/acscentsci.3c01629>)
- Code: [Open Direct Air Capture 2023 (ODAC23)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [ODAC23 author paper Table 1](<https://arxiv.org/html/2311.00341v2>)
- Evidence (2026-11-01): [ODAC23 official download documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac23.md>)

#### Deem hypothetical zeolites / PCOD SLC-good

Release: v2.1 SLC-good download subset.

- Homepage: [Deem hypothetical zeolites / PCOD SLC-good](<https://mwdeem.org/PCOD/index.html>)
- Data: [Deem hypothetical zeolites / PCOD SLC-good](<https://mwdeem.org/PCOD/index.html>)
- Paper: [Deem hypothetical zeolites / PCOD SLC-good](<https://doi.org/10.1039/C0CP02255A>)
- Evidence (2026-11-01): [Deem PCOD author download page](<https://mwdeem.org/PCOD/index.html>)

#### Boyd-Woo hypothetical MOFs for wet flue-gas capture

Release: Materials Cloud 2018.0016 v3, deposited 2019.

- Data: [Boyd-Woo hypothetical MOFs for wet flue-gas capture](<https://archive.materialscloud.org/records/nsp7v-2dk91>)
- Paper: [Boyd-Woo hypothetical MOFs for wet flue-gas capture](<https://doi.org/10.1038/s41586-019-1798-7>)
- Evidence (2026-11-01): [Boyd-Woo Materials Cloud archive](<https://archive.materialscloud.org/records/nsp7v-2dk91>)
- Evidence (2026-11-01): [Boyd-Woo file rights](<https://archive.materialscloud.org/api/records/nsp7v-2dk91>)

#### ab initio REPEAT Charge MOF Database (ARC-MOF)

Release: Zenodo v7 (2025); structure archive ARCMOF_20241004.

- Data: [ab initio REPEAT Charge MOF Database (ARC-MOF)](<https://zenodo.org/records/16802743>)
- Paper: [ab initio REPEAT Charge MOF Database (ARC-MOF)](<https://doi.org/10.1021/acs.chemmater.2c02485>)
- Code: [ab initio REPEAT Charge MOF Database (ARC-MOF)](<https://github.com/uowoolab>)
- Evidence (2026-11-01): [ARC-MOF v7](<https://zenodo.org/records/16802743>)
- Evidence (2026-11-01): [ARC-MOF rights metadata](<https://zenodo.org/api/records/16802743>)

#### ReDD-COFFEE

Release: Materials Cloud 2023.13 v1.

- Data: [ReDD-COFFEE](<https://archive.materialscloud.org/records/y5gs8-pyj90>)
- Paper: [ReDD-COFFEE](<https://doi.org/10.1039/D3TA00470H>)
- Evidence (2026-11-01): [ReDD-COFFEE v1](<https://archive.materialscloud.org/record/2023.13>)
- Evidence (2026-11-01): [ReDD-COFFEE deposited file rights](<https://archive.materialscloud.org/records/y5gs8-pyj90>)

#### Wilmer hypothetical MOF database (hMOF)

Release: Original 2011/2012 publication corpus.

- Homepage: [Wilmer hypothetical MOF database (hMOF)](<http://hmofs.northwestern.edu/>)
- Paper: [Wilmer hypothetical MOF database (hMOF)](<https://doi.org/10.1038/nchem.1192>)
- Evidence (2026-11-01): [Wilmer et al., Nature Chemistry](<https://www.nature.com/articles/nchem.1192>)
- Evidence (2026-11-01): [Author-hosted original paper](<https://chemgroups.northwestern.edu/hupp/Publications/316.pdf>)

#### MOSAEC MOF Database (MOSAEC-DB)

Release: 1.0.0-release, January 2025.

- Data: [MOSAEC MOF Database (MOSAEC-DB)](<https://zenodo.org/records/15808197>)
- Paper: [MOSAEC MOF Database (MOSAEC-DB)](<https://doi.org/10.1039/D4SC07438F>)
- Code: [MOSAEC MOF Database (MOSAEC-DB)](<https://github.com/uowoolab/MOSAEC-DB>)
- Evidence (2026-11-01): [MOSAEC-DB author deposit](<https://zenodo.org/records/15808197>)

#### Mercado hypothetical 2D and 3D COFs

Release: Materials Cloud 2018.0003 v3.

- Data: [Mercado hypothetical 2D and 3D COFs](<https://archive.materialscloud.org/records/cjhyq-nr115>)
- Paper: [Mercado hypothetical 2D and 3D COFs](<https://doi.org/10.1021/acs.chemmater.8b01425>)
- Evidence (2026-11-01): [Hypothetical COF Materials Cloud archive](<https://archive.materialscloud.org/records/cjhyq-nr115>)
- Evidence (2026-11-01): [Hypothetical COF rights](<https://archive.materialscloud.org/api/records/cjhyq-nr115>)

#### CoRE MOF Database

Release: CoRE MOF 2025 v1.0.

- Homepage: [CoRE MOF Database](<https://chung-research-group.github.io/CoRE%20MOF%20Database.dc.html>)
- Data: [CoRE MOF Database](<https://zenodo.org/records/15621349>)
- Paper: [CoRE MOF Database](<https://doi.org/10.1016/j.matt.2025.102140>)
- Code: [CoRE MOF Database](<https://github.com/mtap-research/CoRE-MOF-Tools>)
- Evidence (2026-11-01): [CoRE MOF 2025 v1.0](<https://zenodo.org/records/15621349>)
- Evidence (2026-11-01): [CoRE MOF 2024 release history](<https://zenodo.org/records/15055758>)
- Evidence (2026-11-01): [CoRE MOF 2025 deposit metadata](<https://zenodo.org/api/records/15621349>)

#### Zeo-1

Release: Materials Cloud 2021.171; Scientific Data 2022.

- Data: [Zeo-1](<https://archive.materialscloud.org/records/3xmh2-vv758>)
- Paper: [Zeo-1](<https://doi.org/10.1038/s41597-022-01160-5>)
- Evidence (2026-11-01): [Zeo-1 Scientific Data descriptor](<https://www.nature.com/articles/s41597-022-01160-5.pdf>)
- Evidence (2026-11-01): [Zeo-1 archived rights](<https://archive.materialscloud.org/api/records/3xmh2-vv758>)

#### Quantum MOF Database (QMOF)

Release: Figshare v18 / current author documentation.

- Homepage: [Quantum MOF Database (QMOF)](<https://github.com/Andrew-S-Rosen/QMOF>)
- Data: [Quantum MOF Database (QMOF)](<https://figshare.com/articles/dataset/13147324/18>)
- Paper: [Quantum MOF Database (QMOF)](<https://doi.org/10.1038/s41524-022-00796-6>)
- Code: [Quantum MOF Database (QMOF)](<https://github.com/Andrew-S-Rosen/QMOF>)
- Evidence (2026-11-01): [QMOF author repository](<https://github.com/Andrew-S-Rosen/QMOF>)
- Evidence (2026-11-01): [QMOF official Figshare metadata](<https://api.figshare.com/v2/articles/13147324>)

#### Computation-Ready Experimental COF Database (CoRE COF)

Release: DT1242-v7.0; Git commit edbb24a, 2024-03-13.

- Homepage: [Computation-Ready Experimental COF Database (CoRE COF)](<https://github.com/core-cof/CoRE-COF-Database>)
- Data: [Computation-Ready Experimental COF Database (CoRE COF)](<https://github.com/core-cof/CoRE-COF-Database/blob/master/CoRE-COFs_DT1242-v7.0.zip>)
- Paper: [Computation-Ready Experimental COF Database (CoRE COF)](<https://doi.org/10.1016/j.ces.2017.05.004>)
- Evidence (2026-11-01): [CoRE COF author repository](<https://github.com/core-cof/CoRE-COF-Database>)
- Evidence (2026-11-01): [CoRE COF v7 archive](<https://raw.githubusercontent.com/core-cof/CoRE-COF-Database/master/CoRE-COFs_DT1242-v7.0.zip>)

#### CURATED covalent organic frameworks

Release: July 2022 extension; Materials Cloud archive updated 2023-11-02.

- Homepage: [CURATED covalent organic frameworks](<https://materialscloud-org.github.io/mc-frontend/discover/curated-cofs>)
- Data: [CURATED covalent organic frameworks](<https://archive.materialscloud.org/records/1xf71-nf390>)
- Paper: [CURATED covalent organic frameworks](<https://doi.org/10.1021/acscentsci.9b00619>)
- Code: [CURATED covalent organic frameworks](<https://github.com/danieleongari/CURATED-COFs>)
- Evidence (2026-11-01): [CURATED COFs archive release history](<https://archive.materialscloud.org/records/1xf71-nf390>)
- Evidence (2026-11-01): [CURATED COFs file license](<https://archive.materialscloud.org/api/records/1xf71-nf390>)

#### IZA Database of Zeolite Structures

Release: Framework type codes updated 2026-07-30.

- Homepage: [IZA Database of Zeolite Structures](<https://www.iza-structure.org/databases/>)
- Data: [IZA Database of Zeolite Structures](<https://www.iza-structure.org/IZA-SC/ftc_table.php>)
- Evidence (2026-11-01): [IZA Framework Type Codes](<https://europe.iza-structure.org/IZA-SC_FTC.php>)
- Evidence (2026-11-01): [IZA official database](<https://www.iza-structure.org/databases/>)

### Molecular crystals and ice

#### Open Molecular Crystals 2025 (OMC25)

Release: Public 250802 train and validation release; Scientific Data 2026.

- Data: [Open Molecular Crystals 2025 (OMC25)](<https://huggingface.co/datasets/facebook/OMC25>)
- Paper: [Open Molecular Crystals 2025 (OMC25)](<https://doi.org/10.1038/s41597-026-06628-2>)
- Code: [Open Molecular Crystals 2025 (OMC25)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [OMC25 official dataset card](<https://huggingface.co/datasets/facebook/OMC25/blob/main/README.md>)
- Evidence (2026-11-01): [OMC25 Scientific Data descriptor](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12979844/>)
- Evidence (2026-11-01): [OMC25 official access documentation](<https://facebookresearch.github.io/fairchem/omc25/>)
- Evidence (2026-11-01): [Open Molecular Crystals 2025 (OMC25) dataset and models — Scientific Data descriptor](<https://doi.org/10.1038/s41597-026-06628-2>)

#### X23 diffusion Monte Carlo benchmark

Release: 2024 DMC reference study.

- Paper: [X23 diffusion Monte Carlo benchmark](<https://doi.org/10.1103/PhysRevLett.133.046401>)
- Evidence (2026-11-01): [Author abstract of 2024 X23 DMC paper](<https://pubmed.ncbi.nlm.nih.gov/39121404/>)

#### DMC-ICE13

Release: 2022 JCP reference dataset.

- Paper: [DMC-ICE13](<https://doi.org/10.1063/5.0102645>)
- Data: [DMC-ICE13](<https://discovery.ucl.ac.uk/id/eprint/10162009/1/2207.01353v1.pdf>)
- Evidence (2026-11-01): [DMC-ICE13 author paper](<https://arxiv.org/abs/2207.01353>)
- Evidence (2026-11-01): [DMC-ICE13 author supporting information](<https://discovery.ucl.ac.uk/id/eprint/10162009/1/2207.01353v1.pdf>)

### Surfaces, interfaces and catalysis

#### Open Catalyst 2020 (OC20)

Release: Corrected S2EF training files, February 2021.

- Homepage: [Open Catalyst 2020 (OC20)](<https://opencatalystproject.org/>)
- Data: [Open Catalyst 2020 (OC20)](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20.md>)
- Paper: [Open Catalyst 2020 (OC20)](<https://doi.org/10.1021/acscatal.0c04525>)
- Code: [Open Catalyst 2020 (OC20)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [OC20 author paper v5](<https://arxiv.org/abs/2010.09990>)
- Evidence (2026-11-01): [OC20 official task downloads and changelog](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20.md>)

#### AQCat25 heterogeneous-catalysis dataset

Release: Provider dataset card, checked 2026-11-01.

- Homepage: [AQCat25 heterogeneous-catalysis dataset](<https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset>)
- Data: [AQCat25 heterogeneous-catalysis dataset](<https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset>)
- Paper: [AQCat25 heterogeneous-catalysis dataset](<https://arxiv.org/abs/2510.22938>)
- Evidence (2026-11-01): [AQCat25 provider data card](<https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset>)

#### Open Catalyst 2022 (OC22)

Release: Author paper v3, March 2023.

- Data: [Open Catalyst 2022 (OC22)](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md>)
- Paper: [Open Catalyst 2022 (OC22)](<https://doi.org/10.1021/acscatal.2c05426>)
- Code: [Open Catalyst 2022 (OC22)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [OC22 final author paper](<https://arxiv.org/abs/2206.08917v3>)
- Evidence (2026-11-01): [OC22 official data documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md>)

#### Open Catalyst 2025 (OC25)

Release: 2025 author paper and official release.

- Data: [Open Catalyst 2025 (OC25)](<https://huggingface.co/facebook/OC25>)
- Paper: [Open Catalyst 2025 (OC25)](<https://arxiv.org/abs/2509.17862>)
- Code: [Open Catalyst 2025 (OC25)](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [OC25 primary dataset paper](<https://arxiv.org/html/2509.17862v1>)
- Evidence (2026-11-01): [OC25 official data documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc25.md>)

#### Work function and cleavage energy surface database

Release: Zenodo v2.1, February 2024.

- Homepage: [Work function and cleavage energy surface database](<https://zenodo.org/records/10703249>)
- Data: [Work function and cleavage energy surface database](<https://doi.org/10.5281/zenodo.10703249>)
- Paper: [Work function and cleavage energy surface database](<https://doi.org/10.1002/adfm.202401764>)
- Evidence (2026-11-01): [Work Function and Cleavage Energy Database](<https://zenodo.org/records/10703249>)
- Evidence (2026-11-01): [Zenodo release metadata](<https://zenodo.org/api/records/10703249>)

#### BEAST DB

Release: 2024 publication corpus.

- Homepage: [BEAST DB](<https://beastdb.nrel.gov/>)
- Paper: [BEAST DB](<https://doi.org/10.1021/acs.jpcc.4c06826>)
- Code: [BEAST DB](<https://github.com/Nick-Singstock/BEAST_DB_Manager>)
- Evidence (2026-11-01): [BEAST DB primary author paper](<https://arxiv.org/abs/2405.20239>)

#### Computational Single-Atom Catalyst Database (NCEPU)

Release: 2025 JPCC publication corpus.

- Data: [Computational Single-Atom Catalyst Database (NCEPU)](<https://catalysis-ncepu-hvkydg736ykqeq26d5gxrn.streamlit.app/>)
- Paper: [Computational Single-Atom Catalyst Database (NCEPU)](<https://doi.org/10.1021/acs.jpcc.5c00491>)
- Code: [Computational Single-Atom Catalyst Database (NCEPU)](<https://github.com/Weijie-Yang/AML>)
- Evidence (2026-11-01): [Computational Single-Atom Catalyst Database primary article](<https://pubs.acs.org/doi/10.1021/acs.jpcc.5c00491>)

### Computed properties and prediction benchmarks

#### WBM / Matbench Discovery stability test set

Release: Matbench Discovery filtered WBM release.

- Homepage: [WBM / Matbench Discovery stability test set](<https://matbench-discovery.materialsproject.org/>)
- Data: [WBM / Matbench Discovery stability test set](<https://figshare.com/articles/dataset/22715158>)
- Paper: [WBM / Matbench Discovery stability test set](<https://doi.org/10.1038/s41524-020-00481-6>)
- Code: [WBM / Matbench Discovery stability test set](<https://github.com/janosh/matbench-discovery>)
- Evidence (2026-11-01): [WBM benchmark test-set documentation](<https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/wbm/readme.md>)
- Evidence (2026-11-01): [Matbench Discovery data-file release metadata](<https://api.figshare.com/v2/articles/22715158>)

#### Matbench mp_e_form

Release: Matbench v0.1.

- Homepage: [Matbench mp_e_form](<https://matbench.materialsproject.org/>)
- Data: [Matbench mp_e_form](<https://github.com/materialsproject/matbench/tree/main/matbench>)
- Paper: [Matbench mp_e_form](<https://doi.org/10.1038/s41524-020-00406-3>)
- Code: [Matbench mp_e_form](<https://github.com/materialsproject/matbench>)
- Evidence (2026-11-01): [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>)
- Evidence (2026-11-01): [Official Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### Matbench mp_gap / mp_is_metal (shared source cohort)

Release: Matbench v0.1.

- Homepage: [Matbench mp_gap / mp_is_metal (shared source cohort)](<https://matbench.materialsproject.org/>)
- Data: [Matbench mp_gap / mp_is_metal (shared source cohort)](<https://github.com/materialsproject/matbench/tree/main/matbench>)
- Paper: [Matbench mp_gap / mp_is_metal (shared source cohort)](<https://doi.org/10.1038/s41524-020-00406-3>)
- Code: [Matbench mp_gap / mp_is_metal (shared source cohort)](<https://github.com/materialsproject/matbench>)
- Evidence (2026-11-01): [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>)
- Evidence (2026-11-01): [Official Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### Topological Quantum Chemistry all-band materials catalog

Release: Science 2022 / arXiv 2105.09954v2 publication cohort.

- Homepage: [Topological Quantum Chemistry all-band materials catalog](<https://www.topologicalquantumchemistry.com/>)
- Data: [Topological Quantum Chemistry all-band materials catalog](<https://www.topologicalquantumchemistry.fr/>)
- Paper: [Topological Quantum Chemistry all-band materials catalog](<https://doi.org/10.1126/science.abg9094>)
- Evidence (2026-11-01): [All Topological Bands of All Nonmagnetic Stoichiometric Materials](<https://arxiv.org/abs/2105.09954>)
- Evidence (2026-11-01): [All Topological Bands, full author manuscript](<https://arxiv.org/html/2105.09954v2>)

#### LeMat-Rho

Release: 2026-10-19 card revision.

- Homepage: [LeMat-Rho](<https://huggingface.co/datasets/LeMaterial/LeMat-Rho>)
- Evidence (2026-11-01): [LeMat-Rho — primary documentation](<https://huggingface.co/datasets/LeMaterial/LeMat-Rho>)

#### Materials Project / Ricci electronic transport database

Release: Publication release.

- Homepage: [Materials Project / Ricci electronic transport database](<https://materialsproject.org/>)
- Data: [Materials Project / Ricci electronic transport database](<https://doi.org/10.5061/dryad.gn001>)
- Paper: [Materials Project / Ricci electronic transport database](<https://doi.org/10.1038/sdata.2017.85>)
- Code: [Materials Project / Ricci electronic transport database](<https://github.com/materialsproject/pymatgen>)
- Evidence (2026-11-01): [An ab initio electronic transport database for inorganic materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC5496472/>)
- Evidence (2026-11-01): [Dryad electronic-transport dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.gn001>)

#### Materials Project Phonon database v1.1

Release: v1.1, 2026-06-08.

- Homepage: [Materials Project Phonon database v1.1](<https://materialsproject.org/>)
- Data: [Materials Project Phonon database v1.1](<https://doi.org/10.5281/zenodo.20196565>)
- Evidence (2026-11-01): [Materials Project Phonon database v1.1 - (26,413 compounds)](<https://zenodo.org/records/20196565>)

#### Phonix anharmonic phonon database

Release: v2026.03.28.

- Homepage: [Phonix anharmonic phonon database](<https://phonix-db.org/>)
- Data: [Phonix anharmonic phonon database](<https://phonix-db.org/ver2026.03.28/index.html>)
- Paper: [Phonix anharmonic phonon database](<https://www.nature.com/articles/s41524-026-02033-w>)
- Code: [Phonix anharmonic phonon database](<https://github.com/phonix-db/auto-kappa>)
- Evidence (2026-11-01): [Phonix v2026.03.28 release statistics](<https://phonix-db.org/ver2026.03.28/index.html>)
- Evidence (2026-11-01): [Phonix official database documentation](<https://phonix-db.org/>)

#### OMDB-GAP1

Release: v1.1.

- Homepage: [OMDB-GAP1](<https://omdb.mathub.io/>)
- Data: [OMDB-GAP1](<https://omdb.mathub.io/dataset/>)
- Paper: [OMDB-GAP1](<https://doi.org/10.1002/qute.201900023>)
- Evidence (2026-11-01): [Organic Materials Database dataset downloads](<https://omdb.mathub.io/dataset/>)

#### Matbench log_gvrh / log_kvrh (shared source cohort)

Release: Matbench v0.1.

- Homepage: [Matbench log_gvrh / log_kvrh (shared source cohort)](<https://matbench.materialsproject.org/>)
- Data: [Matbench log_gvrh / log_kvrh (shared source cohort)](<https://github.com/materialsproject/matbench/tree/main/matbench>)
- Paper: [Matbench log_gvrh / log_kvrh (shared source cohort)](<https://doi.org/10.1038/s41524-020-00406-3>)
- Code: [Matbench log_gvrh / log_kvrh (shared source cohort)](<https://github.com/materialsproject/matbench>)
- Evidence (2026-11-01): [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>)
- Evidence (2026-11-01): [Official Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### SNUMAT hybrid-functional band-gap dataset

Release: Publication finite-gap release (Figshare v7 update 2021).

- Homepage: [SNUMAT hybrid-functional band-gap dataset](<http://www.snumat.com/>)
- Data: [SNUMAT hybrid-functional band-gap dataset](<https://figshare.com/articles/dataset/hybrid_bandgap_200821_v1_zip/12839240>)
- Paper: [SNUMAT hybrid-functional band-gap dataset](<https://doi.org/10.1038/s41597-020-00723-8>)
- Code: [SNUMAT hybrid-functional band-gap dataset](<https://github.com/MDIL-SNU/AMP2>)
- Evidence (2026-11-01): [A band-gap database for semiconducting inorganic materials calculated with hybrid functional](<https://www.nature.com/articles/s41597-020-00723-8>)
- Evidence (2026-11-01): [SNUMAT Figshare publication-release metadata](<https://api.figshare.com/v2/articles/12839240>)

#### PhononDB / MDR harmonic phonon calculation database

Release: Kyoto v2018-04-07 parent; migrated MDR collection checked 2026-11-01.

- Homepage: [PhononDB / MDR harmonic phonon calculation database](<https://github.com/atztogo/phonondb>)
- Data: [PhononDB / MDR harmonic phonon calculation database](<https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en>)
- Code: [PhononDB / MDR harmonic phonon calculation database](<https://github.com/phonopy/phonopy>)
- Evidence (2026-11-01): [MDR phonon calculation database](<https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en>)
- Evidence (2026-11-01): [Phonondb author repository](<https://github.com/atztogo/phonondb>)

#### PhononDB lattice thermal conductivity (MDR)

Release: Author release index snapshot 2026-11-01.

- Homepage: [PhononDB lattice thermal conductivity (MDR)](<https://github.com/atztogo/phonondb>)
- Data: [PhononDB lattice thermal conductivity (MDR)](<https://github.com/atztogo/phonondb/tree/main/mdr/phonondb_LTC>)
- Code: [PhononDB lattice thermal conductivity (MDR)](<https://github.com/phonopy/phono3py>)
- Evidence (2026-11-01): [Phonondb lattice thermal conductivity data on MDR at NIMS](<https://raw.githubusercontent.com/atztogo/phonondb/main/mdr/phonondb_LTC/README.md>)

#### Matbench dielectric

Release: Matbench v0.1.

- Homepage: [Matbench dielectric](<https://matbench.materialsproject.org/>)
- Data: [Matbench dielectric](<https://github.com/materialsproject/matbench/tree/main/matbench>)
- Paper: [Matbench dielectric](<https://doi.org/10.1038/s41524-020-00406-3>)
- Code: [Matbench dielectric](<https://github.com/materialsproject/matbench>)
- Evidence (2026-11-01): [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>)
- Evidence (2026-11-01): [Official Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### AFLOW AEL–AGL thermomechanical cohort (2017)

Release: 2017 publication cohort; current count not asserted.

- Homepage: [AFLOW AEL–AGL thermomechanical cohort (2017)](<https://aflow.org/>)
- Data: [AFLOW AEL–AGL thermomechanical cohort (2017)](<https://aflow.org/documentation/>)
- Paper: [AFLOW AEL–AGL thermomechanical cohort (2017)](<https://doi.org/10.1103/PhysRevMaterials.1.015401>)
- Evidence (2026-11-01): [Combining the AFLOW GIBBS and elastic libraries to efficiently and robustly screen thermomechanical properties of solids](<https://doi.org/10.1103/PhysRevMaterials.1.015401>)
- Evidence (2026-11-01): [AFLOW REST/AFLUX documentation](<https://aflow.org/documentation/>)

#### SuperBand electronic-band / superconductivity dataset

Release: Scientific Data 2025 band-data release.

- Homepage: [SuperBand electronic-band / superconductivity dataset](<https://www.superband.work/>)
- Data: [SuperBand electronic-band / superconductivity dataset](<https://doi.org/10.57760/sciencedb.16728>)
- Paper: [SuperBand electronic-band / superconductivity dataset](<https://doi.org/10.1038/s41597-025-05015-7>)
- Code: [SuperBand electronic-band / superconductivity dataset](<https://github.com/ljcj007/SuperBand>)
- Evidence (2026-11-01): [SuperBand: an Electronic-band and Fermi surface structure database of superconductors](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12056090/>)
- Evidence (2026-11-01): [SuperBand official repository](<https://github.com/ljcj007/SuperBand>)
- Evidence (2026-11-01): [SuperBand: an Electronic-band and Fermi surface structure database of superconductors — Scientific Data descriptor](<https://doi.org/10.1038/s41597-025-05015-7>)

#### MAST-ML perovskite stability educational slice

Release: Figshare7017254 v5, 2018-09-11.

- Homepage: [MAST-ML perovskite stability educational slice](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>)
- Data: [MAST-ML perovskite stability educational slice](<https://ndownloader.figshare.com/files/12978425>)
- Paper: [MAST-ML perovskite stability educational slice](<https://doi.org/10.1016/j.commatsci.2018.04.033>)
- Evidence (2026-11-01): [MAST-ML educational release metadata](<https://api.figshare.com/v2/articles/7017254>)
- Evidence (2026-11-01): [Educational dataset README](<https://ndownloader.figshare.com/files/13008500>)
- Evidence (2026-11-01): [Official perovskite educational CSV](<https://ndownloader.figshare.com/files/12978425>)

#### Materials Project / Petretto DFPT phonons (2018)

Release: Publication release.

- Homepage: [Materials Project / Petretto DFPT phonons (2018)](<https://materialsproject.org/>)
- Data: [Materials Project / Petretto DFPT phonons (2018)](<https://doi.org/10.6084/m9.figshare.c.3938023>)
- Paper: [Materials Project / Petretto DFPT phonons (2018)](<https://doi.org/10.1038/sdata.2018.65>)
- Evidence (2026-11-01): [High-throughput density-functional perturbation theory phonons for inorganic materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC5928854/>)

#### Quantum-Chemical Bonding Database for Solid-State Materials (2023)

Release: Published 2023 Zenodo parts 1 and 2.

- Homepage: [Quantum-Chemical Bonding Database for Solid-State Materials (2023)](<https://zenodo.org/records/8091844>)
- Data: [Quantum-Chemical Bonding Database for Solid-State Materials (2023)](<https://zenodo.org/records/8091844>)
- Paper: [Quantum-Chemical Bonding Database for Solid-State Materials (2023)](<https://www.nature.com/articles/s41597-023-02477-5>)
- Code: [Quantum-Chemical Bonding Database for Solid-State Materials (2023)](<https://github.com/naik-aakash/lobster-database-paper-analysis-scripts>)
- Evidence (2026-11-01): [LOBSTER database Part 1 author deposit](<https://zenodo.org/api/records/8091844>)
- Evidence (2026-11-01): [LOBSTER database Part 2 author deposit](<https://zenodo.org/api/records/8092187>)

#### Matbench phonons

Release: Matbench v0.1.

- Homepage: [Matbench phonons](<https://matbench.materialsproject.org/>)
- Data: [Matbench phonons](<https://github.com/materialsproject/matbench/tree/main/matbench>)
- Paper: [Matbench phonons](<https://doi.org/10.1038/s41524-020-00406-3>)
- Code: [Matbench phonons](<https://github.com/materialsproject/matbench>)
- Evidence (2026-11-01): [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>)
- Evidence (2026-11-01): [Official Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### Materials Project elastic tensor release (2015)

Release: Publication release.

- Homepage: [Materials Project elastic tensor release (2015)](<https://materialsproject.org/>)
- Data: [Materials Project elastic tensor release (2015)](<https://doi.org/10.5061/dryad.h505v>)
- Paper: [Materials Project elastic tensor release (2015)](<https://doi.org/10.1038/sdata.2015.9>)
- Code: [Materials Project elastic tensor release (2015)](<https://github.com/materialsproject/pymatgen>)
- Evidence (2026-11-01): [Charting the complete elastic properties of inorganic crystalline compounds](<https://pmc.ncbi.nlm.nih.gov/articles/PMC4432655/>)
- Evidence (2026-11-01): [Dryad elastic-tensor dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.h505v>)

#### JARVIS superconductivity 3D DFT cohort

Release: JARVIS-Tools named supercon_3d release.

- Homepage: [JARVIS superconductivity 3D DFT cohort](<https://jarvis.nist.gov/supercon>)
- Data: [JARVIS superconductivity 3D DFT cohort](<https://figshare.com/ndownloader/files/38307921>)
- Paper: [JARVIS superconductivity 3D DFT cohort](<https://doi.org/10.1038/s41524-022-00933-1>)
- Code: [JARVIS superconductivity 3D DFT cohort](<https://github.com/usnistgov/jarvis>)
- Evidence (2026-11-01): [JARVIS-Tools database inventory](<https://pages.nist.gov/jarvis/databases/>)
- Evidence (2026-11-01): [Official JARVIS dataset loader](<https://raw.githubusercontent.com/usnistgov/jarvis/master/jarvis/db/figshare.py>)
- Evidence (2026-11-01): [JARVIS-SuperconDB Figshare metadata](<https://api.figshare.com/v2/articles/21370572>)

#### Materials Project dielectric tensor release (2017)

Release: Publication release.

- Homepage: [Materials Project dielectric tensor release (2017)](<https://materialsproject.org/>)
- Data: [Materials Project dielectric tensor release (2017)](<https://doi.org/10.5061/dryad.ph81h>)
- Paper: [Materials Project dielectric tensor release (2017)](<https://doi.org/10.1038/sdata.2016.134>)
- Code: [Materials Project dielectric tensor release (2017)](<https://github.com/materialsproject/pymatgen>)
- Evidence (2026-11-01): [High-throughput screening of inorganic compounds for the discovery of novel dielectric and optical materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC5315501/>)
- Evidence (2026-11-01): [Dryad dielectric-tensor dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.ph81h>)

#### Materials Project piezoelectric tensor release (2015)

Release: Publication release.

- Homepage: [Materials Project piezoelectric tensor release (2015)](<https://materialsproject.org/>)
- Data: [Materials Project piezoelectric tensor release (2015)](<https://doi.org/10.5061/dryad.n63m4>)
- Paper: [Materials Project piezoelectric tensor release (2015)](<https://doi.org/10.1038/sdata.2015.53>)
- Code: [Materials Project piezoelectric tensor release (2015)](<https://github.com/materialsproject/pymatgen>)
- Evidence (2026-11-01): [A database to enable discovery and design of piezoelectric materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC4587372/>)
- Evidence (2026-11-01): [Dryad piezoelectric-tensor dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.n63m4>)

#### Matbench jdft2d

Release: Matbench v0.1.

- Homepage: [Matbench jdft2d](<https://matbench.materialsproject.org/>)
- Data: [Matbench jdft2d](<https://github.com/materialsproject/matbench/tree/main/matbench>)
- Paper: [Matbench jdft2d](<https://doi.org/10.1038/s41524-020-00406-3>)
- Code: [Matbench jdft2d](<https://github.com/materialsproject/matbench>)
- Evidence (2026-11-01): [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>)
- Evidence (2026-11-01): [Official Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### MAST-ML dilute-solute diffusion educational slice

Release: Figshare7017254 v5, 2018-09-11.

- Homepage: [MAST-ML dilute-solute diffusion educational slice](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>)
- Data: [MAST-ML dilute-solute diffusion educational slice](<https://ndownloader.figshare.com/files/13007075>)
- Paper: [MAST-ML dilute-solute diffusion educational slice](<https://doi.org/10.1038/sdata.2016.54>)
- Evidence (2026-11-01): [MAST-ML educational release metadata](<https://api.figshare.com/v2/articles/7017254>)
- Evidence (2026-11-01): [Educational dataset README](<https://ndownloader.figshare.com/files/13008500>)
- Evidence (2026-11-01): [Official diffusion educational CSV](<https://ndownloader.figshare.com/files/13007075>)

#### JARVIS superconductivity 2D DFT cohort

Release: JARVIS-Tools named supercon_2d release.

- Homepage: [JARVIS superconductivity 2D DFT cohort](<https://jarvis.nist.gov/supercon>)
- Data: [JARVIS superconductivity 2D DFT cohort](<https://figshare.com/ndownloader/files/38950433>)
- Paper: [JARVIS superconductivity 2D DFT cohort](<https://doi.org/10.1021/acs.nanolett.2c04420>)
- Code: [JARVIS superconductivity 2D DFT cohort](<https://github.com/usnistgov/jarvis>)
- Evidence (2026-11-01): [JARVIS-Tools database inventory](<https://pages.nist.gov/jarvis/databases/>)
- Evidence (2026-11-01): [Official JARVIS dataset loader](<https://raw.githubusercontent.com/usnistgov/jarvis/master/jarvis/db/figshare.py>)
- Evidence (2026-11-01): [JARVIS-SuperconDB Figshare metadata](<https://api.figshare.com/v2/articles/21370572>)

#### Phono3py 103-compound finite-displacement dataset (PBEsol)

Release: PBEsol finite-displacement release.

- Homepage: [Phono3py 103-compound finite-displacement dataset (PBEsol)](<https://github.com/atztogo/phonondb>)
- Data: [Phono3py 103-compound finite-displacement dataset (PBEsol)](<https://github.com/atztogo/phonondb/tree/main/mdr/phono3py_103compounds_fd>)
- Paper: [Phono3py 103-compound finite-displacement dataset (PBEsol)](<https://doi.org/10.7566/JPSJ.92.012001>)
- Code: [Phono3py 103-compound finite-displacement dataset (PBEsol)](<https://github.com/phonopy/phono3py>)
- Evidence (2026-11-01): [Lattice thermal conductivity calculation datasets for 103 binary compounds by finite displacement method](<https://mdr.nims.go.jp/collections/e85f8f40-d810-42ae-91c4-0a07b9641219?locale=en>)
- Evidence (2026-11-01): [Phonondb author repository](<https://github.com/atztogo/phonondb>)

### Crystal generation and discovery benchmarks

#### OpenLAM Crystal Philately challenge collection

Release: January 2025 first-round challenge-report snapshot.

- Homepage: [OpenLAM Crystal Philately challenge collection](<https://github.com/deepmodeling/openlam>)
- Data: [OpenLAM Crystal Philately challenge collection](<https://github.com/deepmodeling/openlam#query-crystal-structures-from-openlam-database>)
- Paper: [OpenLAM Crystal Philately challenge collection](<https://arxiv.org/abs/2501.16358>)
- Code: [OpenLAM Crystal Philately challenge collection](<https://github.com/deepmodeling/openlam>)
- Evidence (2026-11-01): [The OpenLAM Challenges](<https://arxiv.org/abs/2501.16358>)
- Evidence (2026-11-01): [OpenLAM official repository](<https://github.com/deepmodeling/openlam>)

#### Alex-MP reference dataset (MatterGen public release)

Release: Public MatterGen Alex-MP reference release.

- Homepage: [Alex-MP reference dataset (MatterGen public release)](<https://github.com/microsoft/mattergen>)
- Data: [Alex-MP reference dataset (MatterGen public release)](<https://github.com/microsoft/mattergen/tree/main/data-release/alex-mp>)
- Paper: [Alex-MP reference dataset (MatterGen public release)](<https://doi.org/10.1038/s41586-025-08628-5>)
- Code: [Alex-MP reference dataset (MatterGen public release)](<https://github.com/microsoft/mattergen>)
- Evidence (2026-11-01): [MatterGen official README](<https://raw.githubusercontent.com/microsoft/mattergen/main/README.md>)

#### Alex-MP-20 (MatterGen)

Release: MatterGen publication training corpus.

- Homepage: [Alex-MP-20 (MatterGen)](<https://github.com/microsoft/mattergen>)
- Data: [Alex-MP-20 (MatterGen)](<https://github.com/microsoft/mattergen/tree/main/data-release/alex-mp>)
- Paper: [Alex-MP-20 (MatterGen)](<https://doi.org/10.1038/s41586-025-08628-5>)
- Code: [Alex-MP-20 (MatterGen)](<https://github.com/microsoft/mattergen>)
- Evidence (2026-11-01): [Microsoft MatterGen data summary card](<https://huggingface.co/microsoft/mattergen/blob/main/data_summary_card.md>)
- Evidence (2026-11-01): [MatterGen Alex-MP data-release README](<https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/alex-mp/README.md>)

#### MP-20 (CDVAE benchmark)

Release: CDVAE ICLR 2022 release.

- Homepage: [MP-20 (CDVAE benchmark)](<https://github.com/txie-93/cdvae/tree/main/data/mp_20>)
- Data: [MP-20 (CDVAE benchmark)](<https://github.com/txie-93/cdvae/tree/main/data/mp_20>)
- Paper: [MP-20 (CDVAE benchmark)](<https://arxiv.org/abs/2110.06197>)
- Code: [MP-20 (CDVAE benchmark)](<https://github.com/txie-93/cdvae>)
- Evidence (2026-11-01): [CDVAE MP-20 dataset documentation](<https://raw.githubusercontent.com/txie-93/cdvae/main/data/mp_20/README.md>)

#### Perov-5 / Matbench perovskites

Release: Castelli corpus / CDVAE and Matbench benchmark derivatives.

- Homepage: [Perov-5 / Matbench perovskites](<https://github.com/txie-93/cdvae/tree/main/data/perov_5>)
- Data: [Perov-5 / Matbench perovskites](<https://github.com/txie-93/cdvae/tree/main/data/perov_5>)
- Paper: [Perov-5 / Matbench perovskites](<https://doi.org/10.1039/C2EE22341D>)
- Code: [Perov-5 / Matbench perovskites](<https://github.com/txie-93/cdvae>)
- Evidence (2026-11-01): [CDVAE Perov-5 dataset documentation](<https://raw.githubusercontent.com/txie-93/cdvae/main/data/perov_5/README.md>)
- Evidence (2026-11-01): [Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>)

#### Carbon-24 (CDVAE benchmark)

Release: CDVAE ICLR 2022 release, from Pickard 2020 AIRSS archive.

- Homepage: [Carbon-24 (CDVAE benchmark)](<https://github.com/txie-93/cdvae/tree/main/data/carbon_24>)
- Data: [Carbon-24 (CDVAE benchmark)](<https://github.com/txie-93/cdvae/tree/main/data/carbon_24>)
- Paper: [Carbon-24 (CDVAE benchmark)](<https://arxiv.org/abs/2110.06197>)
- Code: [Carbon-24 (CDVAE benchmark)](<https://github.com/txie-93/cdvae>)
- Evidence (2026-11-01): [CDVAE Carbon-24 dataset documentation](<https://raw.githubusercontent.com/txie-93/cdvae/main/data/carbon_24/README.md>)

### Experimental properties and literature extraction

#### ChemDataExtractor battery materials database (2020)

Release: Figshare v2, 2020-07-13.

- Homepage: [ChemDataExtractor battery materials database (2020)](<https://github.com/ShuHuang/batterydatabase>)
- Data: [ChemDataExtractor battery materials database (2020)](<https://doi.org/10.6084/m9.figshare.11888115.v2>)
- Paper: [ChemDataExtractor battery materials database (2020)](<https://www.nature.com/articles/s41597-020-00602-2>)
- Code: [ChemDataExtractor battery materials database (2020)](<https://github.com/ShuHuang/batterydatabase>)
- Evidence (2026-11-01): [Battery materials Scientific Data descriptor](<https://www.nature.com/articles/s41597-020-00602-2>)
- Evidence (2026-11-01): [Battery database v2 metadata](<https://api.figshare.com/v2/articles/11888115/versions/2>)

#### Material Synthesis 2025 (MatSyn25)

Release: 2025-10-01 author preprint and public data card.

- Homepage: [Material Synthesis 2025 (MatSyn25)](<https://huggingface.co/datasets/MatSynAI/MatSyn25>)
- Data: [Material Synthesis 2025 (MatSyn25)](<https://huggingface.co/datasets/MatSynAI/MatSyn25>)
- Paper: [Material Synthesis 2025 (MatSyn25)](<https://arxiv.org/abs/2510.00776>)
- Code: [Material Synthesis 2025 (MatSyn25)](<https://github.com/MatSynAI/MatSyn25>)
- Evidence (2026-11-01): [MatSyn25 author preprint](<https://arxiv.org/abs/2510.00776>)
- Evidence (2026-11-01): [MatSyn25 provider data card](<https://huggingface.co/datasets/MatSynAI/MatSyn25/raw/main/README.md>)

#### High Throughput Experimental Materials Database (HTEM)

Release: 2018 Scientific Data descriptor.

- Homepage: [High Throughput Experimental Materials Database (HTEM)](<https://htem.nrel.gov/>)
- Paper: [High Throughput Experimental Materials Database (HTEM)](<https://www.nature.com/articles/sdata201853>)
- Evidence (2026-11-01): [HTEM Scientific Data descriptor](<https://www.nature.com/articles/sdata201853>)

#### Starrydata2 experimental materials datasets

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata2 experimental materials datasets](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata2 experimental materials datasets](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Paper: [Starrydata2 experimental materials datasets](<https://doi.org/10.1080/27660400.2025.2590811>)
- Code: [Starrydata2 experimental materials datasets](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata2 experimental materials datasets](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_papers.csv.gz>)
- Samples: [Starrydata2 experimental materials datasets](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_samples.csv.gz>)
- Curves: [Starrydata2 experimental materials datasets](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata live release manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata dataset release repository](<https://github.com/starrydata/starrydata_datasets>)

#### 3DSC_ICSD

Release: 2023 published release.

- Homepage: [3DSC_ICSD](<https://github.com/aimat-lab/3DSC>)
- Paper: [3DSC_ICSD](<https://www.nature.com/articles/s41597-023-02721-y>)
- Code: [3DSC_ICSD](<https://github.com/aimat-lab/3DSC>)
- Data: [3DSC_ICSD](<https://doi.org/10.6084/m9.figshare.24499924>)
- Evidence (2026-11-01): [3DSC Scientific Data descriptor](<https://www.nature.com/articles/s41597-023-02721-y>)
- Evidence (2026-11-01): [3DSC_ICSD (only Tc and ICSD IDs) repository metadata](<https://api.figshare.com/v2/articles/24499924>)

#### LeMat-Synth synthesis-procedure corpus

Release: v1.0.

- Homepage: [LeMat-Synth synthesis-procedure corpus](<https://lematerial.org/lemat-synth/overview/>)
- Data: [LeMat-Synth synthesis-procedure corpus](<https://huggingface.co/datasets/LeMaterial/LeMat-Synth>)
- Paper: [LeMat-Synth synthesis-procedure corpus](<https://arxiv.org/abs/2510.26824>)
- Code: [LeMat-Synth synthesis-procedure corpus](<https://github.com/LeMaterial/lematerial-llm-synthesis>)
- Evidence (2026-11-01): [LeMat-Synth: a multi-modal toolbox to curate broad synthesis procedure databases from scientific literature](<https://arxiv.org/abs/2510.26824>)
- Evidence (2026-11-01): [LeMat-Synth official overview](<https://lematerial.org/lemat-synth/overview/>)

#### Solid-state synthesis recipes with impurity phases

Release: 2025 published Figshare release.

- Homepage: [Solid-state synthesis recipes with impurity phases](<https://github.com/slee-lab/solid-state-recipes-with-impurity>)
- Data: [Solid-state synthesis recipes with impurity phases](<https://doi.org/10.6084/m9.figshare.30423274>)
- Paper: [Solid-state synthesis recipes with impurity phases](<https://www.nature.com/articles/s41597-025-06222-y>)
- Code: [Solid-state synthesis recipes with impurity phases](<https://github.com/slee-lab/solid-state-recipes-with-impurity>)
- Evidence (2026-11-01): [Impurity-aware synthesis Scientific Data descriptor](<https://www.nature.com/articles/s41597-025-06222-y>)
- Evidence (2026-11-01): [Impurity synthesis Figshare metadata](<https://api.figshare.com/v2/articles/30423274>)

#### ChemDataExtractor/Snowball Curie–Néel dataset (2025)

Release: Figshare v2; 2025 descriptor.

- Homepage: [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](<https://github.com/C-R-Kelly/Curie-Neel-temperature-dataset>)
- Data: [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](<https://doi.org/10.6084/m9.figshare.29559686.v2>)
- Paper: [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](<https://www.nature.com/articles/s41597-025-06244-6>)
- Code: [ChemDataExtractor/Snowball Curie–Néel dataset (2025)](<https://github.com/C-R-Kelly/Curie-Neel-temperature-dataset>)
- Evidence (2026-11-01): [2025 magnetic temperature Scientific Data descriptor](<https://www.nature.com/articles/s41597-025-06244-6>)
- Evidence (2026-11-01): [Curie–Néel v2 repository metadata](<https://api.figshare.com/v2/articles/29559686/versions/2>)

#### Starrydata — Thermoelectric Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Thermoelectric Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_papers.csv.gz>)
- Samples: [Starrydata — Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_samples.csv.gz>)
- Curves: [Starrydata — Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata ThermoelectricMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Perovskite Database Project (solar cells)

Release: 2021 publication historical corpus; current hosting migrated to NOMAD by 2026.

- Homepage: [Perovskite Database Project (solar cells)](<https://www.perovskitedatabase.com/>)
- Data: [Perovskite Database Project (solar cells)](<https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database>)
- Paper: [Perovskite Database Project (solar cells)](<https://doi.org/10.1038/s41560-021-00941-3>)
- Code: [Perovskite Database Project (solar cells)](<https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database>)
- Evidence (2026-11-01): [An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles](<https://www.nature.com/articles/s41560-021-00941-3>)
- Evidence (2026-11-01): [Perovskite Database official project page](<https://www.perovskitedatabase.com/>)
- Evidence (2026-11-01): [Perovskite Database license](<https://www.perovskitedatabase.com/how-to-cite/>)

#### ChemDataExtractor Curie and Néel database (2018)

Release: 2018 published release.

- Homepage: [ChemDataExtractor Curie and Néel database (2018)](<https://github.com/cjcourt/magdb>)
- Data: [ChemDataExtractor Curie and Néel database (2018)](<https://doi.org/10.6084/m9.figshare.c.3954418>)
- Paper: [ChemDataExtractor Curie and Néel database (2018)](<https://www.nature.com/articles/sdata2018111>)
- Code: [ChemDataExtractor Curie and Néel database (2018)](<https://github.com/cjcourt/magdb>)
- Evidence (2026-11-01): [Magnetic transition Scientific Data descriptor](<https://www.nature.com/articles/sdata2018111>)

#### Text-mined solution-based inorganic synthesis procedures

Release: Figshare v4, 2022-02-04.

- Homepage: [Text-mined solution-based inorganic synthesis procedures](<https://github.com/CederGroupHub/text-mined-solution-synthesis_public>)
- Data: [Text-mined solution-based inorganic synthesis procedures](<https://doi.org/10.6084/m9.figshare.16583387.v4>)
- Paper: [Text-mined solution-based inorganic synthesis procedures](<https://www.nature.com/articles/s41597-022-01317-2>)
- Code: [Text-mined solution-based inorganic synthesis procedures](<https://github.com/CederGroupHub/text-mined-solution-synthesis_public>)
- Evidence (2026-11-01): [Solution-synthesis Scientific Data descriptor](<https://www.nature.com/articles/s41597-022-01317-2>)
- Evidence (2026-11-01): [Solution-synthesis v4 metadata](<https://api.figshare.com/v2/articles/16583387/versions/4>)

#### Digital Hydrogen Platform (DigHyd)

Release: September 2026 author descriptor.

- Homepage: [Digital Hydrogen Platform (DigHyd)](<https://www.dighyd.org>)
- Data: [Digital Hydrogen Platform (DigHyd)](<https://www.dighyd.org>)
- Paper: [Digital Hydrogen Platform (DigHyd)](<https://link.springer.com/article/10.1007/s00339-026-09903-6>)
- Evidence (2026-11-01): [DigHyd author descriptor](<https://link.springer.com/article/10.1007/s00339-026-09903-6>)

#### ZeoSyn zeolite synthesis dataset

Release: 2024 author release.

- Homepage: [ZeoSyn zeolite synthesis dataset](<https://github.com/eltonpan/zeosyn_dataset>)
- Data: [ZeoSyn zeolite synthesis dataset](<https://github.com/eltonpan/zeosyn_dataset/blob/master/dataset/ZEOSYN.xlsx>)
- Paper: [ZeoSyn zeolite synthesis dataset](<https://doi.org/10.1021/acscentsci.3c01615>)
- Code: [ZeoSyn zeolite synthesis dataset](<https://github.com/eltonpan/zeosyn_dataset>)
- Evidence (2026-11-01): [ZeoSyn author README](<https://raw.githubusercontent.com/eltonpan/zeosyn_dataset/master/README.md>)
- Evidence (2026-11-01): [ZeoSyn repository licence](<https://raw.githubusercontent.com/eltonpan/zeosyn_dataset/master/LICENSE>)

#### ChemDataExtractor thermoelectric materials database

Release: 2022 published release.

- Homepage: [ChemDataExtractor thermoelectric materials database](<https://github.com/odysie/thermoelectricsdb>)
- Data: [ChemDataExtractor thermoelectric materials database](<https://doi.org/10.6084/m9.figshare.19658787>)
- Paper: [ChemDataExtractor thermoelectric materials database](<https://www.nature.com/articles/s41597-022-01752-1>)
- Code: [ChemDataExtractor thermoelectric materials database](<https://github.com/odysie/thermoelectricsdb>)
- Evidence (2026-11-01): [Thermoelectric Scientific Data descriptor](<https://www.nature.com/articles/s41597-022-01752-1.pdf>)
- Evidence (2026-11-01): [Thermoelectric database Figshare metadata](<https://api.figshare.com/v2/articles/19658787>)

#### Text-mined inorganic solid-state synthesis recipes

Release: Figshare v3, 2019-09-27.

- Homepage: [Text-mined inorganic solid-state synthesis recipes](<https://github.com/CederGroupHub/text-mined-synthesis_public>)
- Data: [Text-mined inorganic solid-state synthesis recipes](<https://doi.org/10.6084/m9.figshare.9722159.v3>)
- Paper: [Text-mined inorganic solid-state synthesis recipes](<https://www.nature.com/articles/s41597-019-0224-1>)
- Code: [Text-mined inorganic solid-state synthesis recipes](<https://github.com/CederGroupHub/text-mined-synthesis_public>)
- Evidence (2026-11-01): [Solid-state synthesis Scientific Data descriptor](<https://www.nature.com/articles/s41597-019-0224-1>)
- Evidence (2026-11-01): [Solid-state synthesis v3 metadata](<https://api.figshare.com/v2/articles/9722159/versions/3>)

#### Starrydata — Magnetic Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Magnetic Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Magnetic Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Magnetic Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Magnetic Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_papers.csv.gz>)
- Samples: [Starrydata — Magnetic Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_samples.csv.gz>)
- Curves: [Starrydata — Magnetic Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata MagneticMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — Battery Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Battery Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Battery Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_papers.csv.gz>)
- Samples: [Starrydata — Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_samples.csv.gz>)
- Curves: [Starrydata — Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata BatteryMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — Dielectric Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Dielectric Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Dielectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Dielectric Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Dielectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_papers.csv.gz>)
- Samples: [Starrydata — Dielectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_samples.csv.gz>)
- Curves: [Starrydata — Dielectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata DielectricMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### 3DSC_MP

Release: 2023 published release.

- Homepage: [3DSC_MP](<https://github.com/aimat-lab/3DSC>)
- Paper: [3DSC_MP](<https://www.nature.com/articles/s41597-023-02721-y>)
- Code: [3DSC_MP](<https://github.com/aimat-lab/3DSC>)
- Data: [3DSC_MP](<https://doi.org/10.6084/m9.figshare.24499930>)
- Evidence (2026-11-01): [3DSC Scientific Data descriptor](<https://www.nature.com/articles/s41597-023-02721-y>)
- Evidence (2026-11-01): [3DSC_MP repository metadata](<https://api.figshare.com/v2/articles/24499930>)

#### Open Catalyst Experiments 2024 (OCx24) experimental data

Release: ExpDataDump_241113.csv at fairchem 61266df4188e.

- Homepage: [Open Catalyst Experiments 2024 (OCx24) experimental data](<https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/applications/ocx/data>)
- Data: [Open Catalyst Experiments 2024 (OCx24) experimental data](<https://raw.githubusercontent.com/facebookresearch/fairchem/61266df4188eeca70fc56baebfba8abd74a0c695/src/fairchem/applications/ocx/data/experimental_data/ExpDataDump_241113.csv>)
- Code: [Open Catalyst Experiments 2024 (OCx24) experimental data](<https://github.com/facebookresearch/fairchem>)
- Evidence (2026-11-01): [OCx24 pinned raw experimental CSV](<https://raw.githubusercontent.com/facebookresearch/fairchem/61266df4188eeca70fc56baebfba8abd74a0c695/src/fairchem/applications/ocx/data/experimental_data/ExpDataDump_241113.csv>)
- Evidence (2026-11-01): [OCx24 author data documentation](<https://raw.githubusercontent.com/facebookresearch/fairchem/main/src/fairchem/applications/ocx/data/README.md>)

#### Starrydata — Condensed Matter

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Condensed Matter](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Condensed Matter](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Condensed Matter](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Condensed Matter](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_papers.csv.gz>)
- Samples: [Starrydata — Condensed Matter](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_samples.csv.gz>)
- Curves: [Starrydata — Condensed Matter](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata CondensedMatter project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### DigBat / Dynamic Database of Solid-State Electrolytes

Release: June 2026 experimental subset.

- Homepage: [DigBat / Dynamic Database of Solid-State Electrolytes](<https://www.digbat.org>)
- Data: [DigBat / Dynamic Database of Solid-State Electrolytes](<https://www.digbat.org>)
- Paper: [DigBat / Dynamic Database of Solid-State Electrolytes](<https://doi.org/10.1016/j.nanoms.2026.07.001>)
- Evidence (2026-11-01): [Tohoku University DigBat provider announcement](<https://www.tohoku.ac.jp/en/press/digbat_an_ai_ready_digital_platform_for_solid_state_battery_research.html>)
- Evidence (2026-11-01): [DigBat author paper](<https://www.sciencedirect.com/science/article/pii/S2589965126001236>)

#### Starrydata — Resistor

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Resistor](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Resistor](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Resistor](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Resistor](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_papers.csv.gz>)
- Samples: [Starrydata — Resistor](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_samples.csv.gz>)
- Curves: [Starrydata — Resistor](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata Resistor project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — General DB

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — General DB](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — General DB](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — General DB](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — General DB](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_papers.csv.gz>)
- Samples: [Starrydata — General DB](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_samples.csv.gz>)
- Curves: [Starrydata — General DB](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata GeneralDB project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — High Thermal Conductivity Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — High Thermal Conductivity Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — High Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — High Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — High Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_papers.csv.gz>)
- Samples: [Starrydata — High Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_samples.csv.gz>)
- Curves: [Starrydata — High Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata HighThermalConductivityMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — Low Thermal Conductivity Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Low Thermal Conductivity Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Low Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Low Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Low Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_papers.csv.gz>)
- Samples: [Starrydata — Low Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_samples.csv.gz>)
- Curves: [Starrydata — Low Thermal Conductivity Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata LowThermalConductivityMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — Organic Thermoelectric Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Organic Thermoelectric Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Organic Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Organic Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Organic Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_papers.csv.gz>)
- Samples: [Starrydata — Organic Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_samples.csv.gz>)
- Curves: [Starrydata — Organic Thermoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata OrganicThermoelectricMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — Hypermaterial

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Hypermaterial](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Hypermaterial](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Hypermaterial](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Hypermaterial](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_papers.csv.gz>)
- Samples: [Starrydata — Hypermaterial](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_samples.csv.gz>)
- Curves: [Starrydata — Hypermaterial](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata Hypermaterial project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### HYPOD-X: quasicrystals and approximants

Release: Figshare v3, 2024 release.

- Homepage: [HYPOD-X: quasicrystals and approximants](<https://www.nature.com/articles/s41597-024-04043-z>)
- Paper: [HYPOD-X: quasicrystals and approximants](<https://www.nature.com/articles/s41597-024-04043-z>)
- Data: [HYPOD-X: quasicrystals and approximants](<https://doi.org/10.6084/m9.figshare.25650705.v3>)
- Evidence (2026-11-01): [HYPOD-X Scientific Data descriptor](<https://www.nature.com/articles/s41597-024-04043-z>)
- Evidence (2026-11-01): [HYPOD-X v3 Figshare metadata](<https://api.figshare.com/v2/articles/25650705/versions/3>)

#### Starrydata — Solid State Battery Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Solid State Battery Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Solid State Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Solid State Battery Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Solid State Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_papers.csv.gz>)
- Samples: [Starrydata — Solid State Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_samples.csv.gz>)
- Curves: [Starrydata — Solid State Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata SolidStateBatteryMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Starrydata — Piezoelectric Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Piezoelectric Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Piezoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Piezoelectric Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Piezoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_papers.csv.gz>)
- Samples: [Starrydata — Piezoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_samples.csv.gz>)
- Curves: [Starrydata — Piezoelectric Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata PiezoelectricMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### Experimental 2D Materials Database (X2DB)

Release: Provider live table, checked 2026-11-01.

- Homepage: [Experimental 2D Materials Database (X2DB)](<https://x2db.fysik.dtu.dk/>)
- Data: [Experimental 2D Materials Database (X2DB)](<https://x2db.fysik.dtu.dk/>)
- Paper: [Experimental 2D Materials Database (X2DB)](<https://doi.org/10.1021/acsnano.6c01514>)
- Evidence (2026-11-01): [X2DB live provider table](<https://x2db.fysik.dtu.dk/>)
- Evidence (2026-11-01): [2DHub: X2DB documentation](<https://2dhub.org/x2db/x2db.html>)

#### Starrydata — Air Battery Materials

Release: DB snapshot 2026-11-01 02:00:01 UTC+0900 (JST).

- Homepage: [Starrydata — Air Battery Materials](<https://starrydata.github.io/starrydata_datasets/>)
- Data: [Starrydata — Air Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>)
- Code: [Starrydata — Air Battery Materials](<https://github.com/starrydata/starrydata_datasets>)
- Papers: [Starrydata — Air Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_papers.csv.gz>)
- Samples: [Starrydata — Air Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_samples.csv.gz>)
- Curves: [Starrydata — Air Battery Materials](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_curves.csv.gz>)
- Evidence (2026-11-01): [Starrydata AirBatteryMaterials project manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>)
- Evidence (2026-11-01): [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>)
- Evidence (2026-11-01): [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>)

#### MDR SuperCon Datasheet

Release: Ver.240322.

- Homepage: [MDR SuperCon Datasheet](<https://doi.org/10.48505/nims.3739>)
- Data: [MDR SuperCon Datasheet](<https://doi.org/10.48505/nims.4487>)
- Evidence (2026-11-01): [MDR SuperCon Datasheet Ver.240322](<https://mdr.nims.go.jp/datasets/650c4826-f0ca-42e8-8dd9-94025a5307ce?locale=ja>)

### Diffraction, spectroscopy and characterization

#### ICDD Powder Diffraction File PDF-5+

Release: PDF-5+ 2026.

- Homepage: [ICDD Powder Diffraction File PDF-5+](<https://www.icdd.com/>)
- Data: [ICDD Powder Diffraction File PDF-5+](<https://www.icdd.com/pdf-5/>)
- Evidence (2026-11-01): [ICDD 2026 product booklet](<https://www.icdd.com/assets/files/2026-Product-Booklet.pdf>)
- Evidence (2026-11-01): [ICDD licensing process](<https://www.icdd.com/licensing-process/>)

#### opXRD: Open Experimental Powder X-ray Diffraction Database

Release: 2025 paper; downloadable archive v11 (2025-04-28).

- Homepage: [opXRD: Open Experimental Powder X-ray Diffraction Database](<https://xrd.aimat.science/>)
- Data: [opXRD: Open Experimental Powder X-ray Diffraction Database](<https://zenodo.org/records/15298026>)
- Paper: [opXRD: Open Experimental Powder X-ray Diffraction Database](<https://doi.org/10.1002/aidi.202500044>)
- Code: [opXRD: Open Experimental Powder X-ray Diffraction Database](<https://github.com/aimat-lab/opXRD>)
- Evidence (2026-11-01): [opXRD author preprint v2](<https://arxiv.org/html/2503.05577v2>)
- Evidence (2026-11-01): [opXRD archive v11](<https://zenodo.org/records/15298026>)
- Evidence (2026-11-01): [opXRD Zenodo metadata](<https://zenodo.org/api/records/15298026>)

#### MDR XAFS DB

Release: Live collection, accessed 2026-11-01.

- Homepage: [MDR XAFS DB](<https://mdr.nims.go.jp/collections/a0f3fbf1-f94a-4be7-8a66-6b91a24f6b54>)
- Data: [MDR XAFS DB](<https://doi.org/10.48505/nims.1447>)
- Paper: [MDR XAFS DB](<https://doi.org/10.1080/27660400.2023.2197518>)
- Evidence (2026-11-01): [MDR XAFS DB collection](<https://mdr.nims.go.jp/collections/a0f3fbf1-f94a-4be7-8a66-6b91a24f6b54>)

#### Raman Open Database (ROD)

Release: Live provider homepage, accessed 2026-11-01.

- Homepage: [Raman Open Database (ROD)](<https://solsa.crystallography.net/rod/>)
- Paper: [Raman Open Database (ROD)](<https://journals.iucr.org/j/issues/2019/03/00/nb5236/>)
- Evidence (2026-11-01): [ROD homepage](<https://solsa.crystallography.net/rod/>)
- Evidence (2026-11-01): [ROD primary descriptor](<https://journals.iucr.org/j/issues/2019/03/00/nb5236/>)

#### REMI Fe-Co-Ni combinatorial library

Release: REMI nist-pages source snapshot2026-11-01.

- Homepage: [REMI Fe-Co-Ni combinatorial library](<https://pages.nist.gov/remi/data/>)
- Data: [REMI Fe-Co-Ni combinatorial library](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni>)
- Paper: [REMI Fe-Co-Ni combinatorial library](<https://arxiv.org/abs/2204.05838>)
- Evidence (2026-11-01): [REMI direct data list](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md>)
- Evidence (2026-11-01): [Library data description](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni/data%20description.txt>)
- Evidence (2026-11-01): [Official release files](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni>)

#### REMI Fe-Ga-Pd combinatorial library

Release: REMI nist-pages source snapshot2026-11-01.

- Homepage: [REMI Fe-Ga-Pd combinatorial library](<https://pages.nist.gov/remi/data/>)
- Data: [REMI Fe-Ga-Pd combinatorial library](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd>)
- Paper: [REMI Fe-Ga-Pd combinatorial library](<https://doi.org/10.1038/s41467-020-19597-w>)
- Evidence (2026-11-01): [REMI direct data list](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md>)
- Evidence (2026-11-01): [Library data description](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/data%20description.txt>)
- Evidence (2026-11-01): [Official release files](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd>)

#### RRUFF mineral spectroscopy and diffraction

Release: Current provider documentation.

- Homepage: [RRUFF mineral spectroscopy and diffraction](<https://www.rruff.net/>)
- Data: [RRUFF mineral spectroscopy and diffraction](<https://www.rruff.net/about/download-data/>)
- Evidence (2026-11-01): [RRUFF home](<https://www.rruff.net/>)
- Evidence (2026-11-01): [RRUFF data downloads](<https://www.rruff.net/about/download-data/>)
- Evidence (2026-11-01): [RRUFF download documentation](<https://www.rruff.net/help/zip-download/>)

## Repository, portal and adjacent-resource evidence

### [NOMAD Repository and Archive](<https://nomad-lab.eu/>)

Role: repository platform.

- [NOMAD Repository and Archive](<https://cloud.nomad-lab.eu/nomad-lab/>) (checked 2026-11-01)

### [Materials Cloud Archive](<https://archive.materialscloud.org/>)

Role: repository platform.

- [Materials Cloud Archive](<https://archive.materialscloud.org/>) (checked 2026-11-01)

### [ColabFit Exchange](<https://materials.colabfit.org/>)

Role: dataset exchange.

- [ColabFit Exchange](<https://materials.colabfit.org/>) (checked 2026-11-01)

### [Materials Data Facility](<https://materialsdatafacility.org/>)

Role: repository platform.

- [Materials Data Facility](<https://materialsdatafacility.org/>) (checked 2026-11-01)

### [OPTIMADE](<https://www.optimade.org/>)

Role: interoperability API.

- [OPTIMADE](<https://www.optimade.org/>) (checked 2026-11-01)

### [LeMaterial Atompack](<https://huggingface.co/datasets/LeMaterial/Atompack>)

Role: format mirror.

- [LeMaterial Atompack](<https://huggingface.co/datasets/LeMaterial/Atompack>) (checked 2026-11-01)

### [MatterSim training data availability](<https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md>)

Role: model and availability reference.

- [MatterSim training data availability](<https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md>) (checked 2026-11-01)

### [SevenNet-Omni domain bridging set](<https://doi.org/10.6084/m9.figshare.30399814>)

Role: domain bridging data.

- [SevenNet-Omni domain bridging set](<https://doi.org/10.6084/m9.figshare.30399814>) (checked 2026-11-01)
- [Optimizing cross-domain transfer for universal machine learning interatomic potentials](<https://www.nature.com/articles/s41467-026-70195-8>) (checked 2026-11-01)

### [Awesome Materials & Chemistry Datasets](<https://github.com/blaiszik/awesome-matchem-datasets>)

Role: github_collection.

- [Awesome Materials & Chemistry Datasets](<https://github.com/blaiszik/awesome-matchem-datasets>) (checked 2026-11-01)

### [matminer dataset collection](<https://github.com/hackingmaterials/matminer>)

Role: github_collection.

- [matminer dataset summary](<https://hackingmaterials.lbl.gov/matminer/dataset_summary.html>) (checked 2026-11-01)
- [matminer repository](<https://github.com/hackingmaterials/matminer>) (checked 2026-11-01)

### [NIMS MatNavi](<https://mits.nims.go.jp/en/>)

Role: database_portal.

- [NIMS MatNavi](<https://mits.nims.go.jp/en/>) (checked 2026-11-01)

### [NIMS MatDaCs](<https://mat-dacs.dxmt.nims.go.jp/en/>)

Role: dataset_discovery_catalog.

- [NIMS MatDaCs: COD](<https://mat-dacs.dxmt.nims.go.jp/en/list/350>) (checked 2026-11-01)
- [NIMS MatDaCs: AtomWork-Adv](<https://mat-dacs.dxmt.nims.go.jp/en/list/316>) (checked 2026-11-01)

### [Materials Data Facility / Foundry](<https://www.materialsdatafacility.org/>)

Role: data_repository.

- [Materials Data Facility](<https://www.materialsdatafacility.org/>) (checked 2026-11-01)
- [MDF publishing/discovering guides](<https://connect.materialsdatafacility.org/how-to>) (checked 2026-11-01)

### [NIST Materials Data Repository](<https://materialsdata.nist.gov/>)

Role: data_repository.

- [NIST Materials Data Repository](<https://materialsdata.nist.gov/>) (checked 2026-11-01)

### [SpringerMaterials](<https://materials.springer.com/>)

Role: commercial_database_portal.

- [SpringerMaterials publisher overview](<https://www.springernature.com/gp/librarians/products/databases-solutions/springermaterials>) (checked 2026-11-01)

### [Scientific Data materials Data Descriptors](<https://www.nature.com/sdata/collections?page=3&type=collection>)

Role: journal_collection.

- [Scientific Data collections](<https://www.nature.com/sdata/collections?page=3&type=collection>) (checked 2026-11-01)
- [Scientific Data data policies](<https://www.nature.com/sdata/policies/data-policies>) (checked 2026-11-01)

### [Battery Archive](<https://batteryarchive.org/>)

Role: adjacent_experimental_data_portal.

- [Battery Archive provider home](<https://batteryarchive.org/>) (checked 2026-11-01)

### [Digital Hydrogen-S](<https://digital-hydrogen.com/storage>)

Role: dataset_portal_pending_primary_verification.

- [Crossref publisher-deposited Digital Hydrogen-S metadata](<https://api.crossref.org/works/10.1016/j.ijhydene.2026.153434>) (checked 2026-11-01)

### [Matbench v0.1 suite](<https://matbench.materialsproject.org/>)

Role: benchmark suite.

- [Benchmarking Materials Property Prediction Methods](<https://arxiv.org/abs/2005.00707>) (checked 2026-11-01)

### [Matbench Discovery data sets](<https://matbench-discovery.materialsproject.org/data/sets>)

Role: dataset registry and benchmark.

- [Matbench Discovery dataset registry](<https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/datasets.yml>) (checked 2026-11-01)

### [LeMat-GenBench](<https://github.com/LeMaterial/lemat-genbench>)

Role: crystal-generation evaluation framework.

- [LeMat-GenBench official README](<https://raw.githubusercontent.com/LeMaterial/lemat-genbench/main/README.md>) (checked 2026-11-01)

### [MatterGen MP-20 reprocessed release](<https://github.com/microsoft/mattergen/tree/main/data-release/mp-20>)

Role: versioned benchmark derivative.

- [MatterGen MP-20 data-release README](<https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/mp-20/README.md>) (checked 2026-11-01)

### [AFLOW AEL/AGL thermomechanical property libraries](<https://aflow.org/documentation/>)

Role: property-library access resource.

- [Official AFLOW REST/AFLUX documentation](<https://aflow.org/documentation/>) (checked 2026-11-01)

### [Catalysis-Hub / CatHub](<https://www.catalysis-hub.org/>)

Role: database_portal.

- [Catalysis-Hub primary data descriptor](<https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/>) (checked 2026-11-01)

### [CatApp](<https://cmr.fysik.dtu.dk/catapp/catapp.html>)

Role: legacy_property_database.

- [CatApp official CMR page](<https://cmr.fysik.dtu.dk/catapp/catapp.html>) (checked 2026-11-01)
- [Catalysis-Hub primary descriptor discussion of CatApp](<https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/>) (checked 2026-11-01)

### [Digital Catalysis Platform (DigCat)](<https://www.digcat.org/>)

Role: database_portal.

- [DigCat provider laboratory page](<https://www.li-lab-cat-design.com/code--database.html>) (checked 2026-11-01)
- [DigCat 2024 author preprint](<https://www.cambridge.org/engage/chemrxiv/article-details/6760cd4381d2151a02fb5356>) (checked 2026-11-01)

### [MOFX-DB](<https://mof.tech.northwestern.edu/>)

Role: database_portal.

- [MOFX-DB primary descriptor](<https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=931567>) (checked 2026-11-01)

### [Data Resources for Materials Science](<https://github.com/sedaoturak/data-resources-for-materials-science>)

Role: dataset collection.

- [Data Resources for Materials Science](<https://github.com/sedaoturak/data-resources-for-materials-science>) (checked 2026-11-01)

### [Machine Learning Materials Datasets / MAST-ML education](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>)

Role: educational dataset collection.

- [Machine Learning Materials Datasets Figshare v5](<https://api.figshare.com/v2/articles/7017254>) (checked 2026-11-01)
- [Attached dataset README](<https://ndownloader.figshare.com/files/13008500>) (checked 2026-11-01)

### [JARVIS-Tools Notebooks](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks>)

Role: tools and notebook collection.

- [Requested notebook README](<https://raw.githubusercontent.com/JARVIS-Materials-Design/jarvis-tools-notebooks/master/README.md>) (checked 2026-11-01)

### [nanoHUB Machine Learning Lab Module](<https://nanohub.org/tools/intromllab>)

Role: interactive educational module.

- [Public module page](<https://nanohub.org/tools/intromllab>) (checked 2026-11-01)
- [Tool license page](<https://nanohub.org/resources/license?tool=intromllab_r36&tmpl=component>) (checked 2026-11-01)

### [REMI: REsource for Materials Informatics](<https://pages.nist.gov/remi/>)

Role: instructional resource and dataset directory.

- [Primary resource CSV](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/_data/resources.csv>) (checked 2026-11-01)
- [Open Access Data list](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md>) (checked 2026-11-01)

## Supporting perspective papers

- [Materials Databases: Foundations of Modern Digital Materials](<https://doi.org/10.1021/prechem.5c00449>)
- [The rise of the digital materials ecosystem](<https://doi.org/10.20517/aiagent.2026.08>)
- [Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models](<https://doi.org/10.1002/anie.202526150>)
- [Roadmap for transforming heterogeneous catalysis with artificial intelligence](<https://doi.org/10.1038/s41929-026-01479-x>)

The [ACS crosswalk](docs/review-crosswalk.md) and [related-paper notes](docs/related-perspectives.md) describe how these references were used and which full texts or previews were available.

## All distinct source URLs

**1057 distinct public URLs** across the sections above. This index deduplicates exact URL strings; redirects, mirrors and release variants may point to overlapping content.

| Source link | Included as |
|---|---|
| [2DHub: 2D-Alloy Database](<https://2dhub.org/2dalloys/2dalloys.html>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [2D-Alloy Database — data](<https://2dhub.org/_downloads/93db2a0b33028278cf5e22b17a3994f7/2dalloys.db>) | Catalog official route |
| [BiDB official page](<https://2dhub.org/bidb/bidb.html>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [C2DB official release history](<https://2dhub.org/c2db/c2db.html>) | Catalog evidence; Catalog official route |
| [HetDB official page](<https://2dhub.org/hetdb/hetdb.html>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [QPOD official page](<https://2dhub.org/qpod/qpod.html>) | Catalog evidence; Catalog official route |
| [2DHub: X2DB documentation](<https://2dhub.org/x2db/x2db.html>) | Catalog evidence; blaiszik/awesome-matchem-datasets |
| [Elastomeric Foam Materials](<https://acdc.alcf.anl.gov/mdf/detail/foam_db_v1.1/>) | sedaoturak/data-resources-for-materials-science |
| [CHiMAD NIST (TDDFT)](<https://acdc.alcf.anl.gov/mdf/detail/kononov_firstprinciples_simulation_graphene_v1.1/>) | sedaoturak/data-resources-for-materials-science |
| [AFLOW](<https://aflow.org>) | blaiszik/awesome-matchem-datasets |
| [AFLOW — homepage](<https://aflow.org/>) | Catalog official route |
| [AFLOW — data](<https://aflow.org/API/aflowlib_stats/>) | Catalog evidence; Catalog official route |
| [AFLOW REST/AFLUX documentation](<https://aflow.org/documentation/>) | Catalog evidence; Catalog official route; Navigation resource; Resource evidence |
| [Long, C. J., et al. Review of Scientific Instruments 78.7 (2007): 072217.](<https://aip.scitation.org/doi/full/10.1063/1.2755487>) | REMI: REsource for Materials Informatics |
| [LAMBench-TrainingSet-v1](<https://aissquare.com/datasets/detail?pageType=datasets&name=LAMBench-TrainingSet-v1&id=308>) | blaiszik/awesome-matchem-datasets |
| [Alexandria DB](<https://alexandria.icams.rub.de>) | blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [Alexandria — homepage](<https://alexandria.icams.rub.de/>) | Catalog official route |
| [sAlex25 — data](<https://alexandria.icams.rub.de/datasets.html>) | Catalog official route |
| [Crossref publisher-deposited Digital Hydrogen-S metadata](<https://api.crossref.org/works/10.1016/j.ijhydene.2026.153434>) | Resource evidence |
| [Battery database v2 metadata](<https://api.figshare.com/v2/articles/11888115/versions/2>) | Catalog evidence |
| [SNUMAT Figshare publication-release metadata](<https://api.figshare.com/v2/articles/12839240>) | Catalog evidence |
| [QMOF official Figshare metadata](<https://api.figshare.com/v2/articles/13147324>) | Catalog evidence |
| [Solution-synthesis v4 metadata](<https://api.figshare.com/v2/articles/16583387/versions/4>) | Catalog evidence |
| [Thermoelectric database Figshare metadata](<https://api.figshare.com/v2/articles/19658787>) | Catalog evidence |
| [JARVIS-SuperconDB Figshare metadata](<https://api.figshare.com/v2/articles/21370572>) | Catalog evidence |
| [Matbench Discovery data-file release metadata](<https://api.figshare.com/v2/articles/22715158>) | Catalog evidence |
| [Materials Project Trajectory (MPtrj) — primary documentation](<https://api.figshare.com/v2/articles/23713842>) | Catalog evidence |
| [3DSC_ICSD (only Tc and ICSD IDs) repository metadata](<https://api.figshare.com/v2/articles/24499924>) | Catalog evidence |
| [3DSC_MP repository metadata](<https://api.figshare.com/v2/articles/24499930>) | Catalog evidence |
| [HYPOD-X v3 Figshare metadata](<https://api.figshare.com/v2/articles/25650705/versions/3>) | Catalog evidence |
| [Curie–Néel v2 repository metadata](<https://api.figshare.com/v2/articles/29559686/versions/2>) | Catalog evidence |
| [Impurity synthesis Figshare metadata](<https://api.figshare.com/v2/articles/30423274>) | Catalog evidence |
| [Starrydata 20261101 archival metadata](<https://api.figshare.com/v2/articles/34875318>) | Catalog evidence |
| [JARVIS-DFT 3D Figshare metadata](<https://api.figshare.com/v2/articles/6815699>) | Catalog evidence |
| [JARVIS-DFT 2D Figshare release](<https://api.figshare.com/v2/articles/6815705>) | Catalog evidence |
| [MAST-ML educational release metadata](<https://api.figshare.com/v2/articles/7017254>) | Catalog evidence; Collection evidence; Resource evidence |
| [2DMatPedia official Figshare metadata](<https://api.figshare.com/v2/articles/7699910>) | Catalog evidence |
| [Solid-state synthesis v3 metadata](<https://api.figshare.com/v2/articles/9722159/versions/3>) | Catalog evidence |
| [JARVIS-Tools Notebooks inspected document](<https://api.github.com/repos/JARVIS-Materials-Design/jarvis-tools-notebooks>) | Collection evidence |
| [JARVIS-Tools Notebooks inspected document](<https://api.github.com/repos/JARVIS-Materials-Design/jarvis-tools-notebooks/commits/master>) | Collection evidence |
| [JARVIS-Tools Notebooks inspected document](<https://api.github.com/repos/atomgptlab/jarvis-tools-notebooks/commits/master>) | Collection evidence |
| [Starrydata latest release asset metadata](<https://api.github.com/repos/starrydata/starrydata_datasets/releases/latest>) | Catalog evidence |
| [REMI owning repository](<https://api.github.com/repos/usnistgov/remi>) | Collection evidence |
| [REMI: REsource for Materials Informatics inspected document](<https://api.github.com/repos/usnistgov/remi/commits/nist-pages>) | Collection evidence |
| [REMI: REsource for Materials Informatics inspected document](<https://api.github.com/repos/usnistgov/remi/contents/data/Combinatorial%20Libraries/Fe-Co-Ni?ref=nist-pages>) | Collection evidence |
| [REMI: REsource for Materials Informatics inspected document](<https://api.github.com/repos/usnistgov/remi/contents/data/Combinatorial%20Libraries/Fe-Ga-Pd?ref=nist-pages>) | Collection evidence |
| [REMI: REsource for Materials Informatics inspected document](<https://api.github.com/repos/usnistgov/remi/readme?ref=nist-pages>) | Collection evidence |
| [High-Speed TBL DNS DB](<https://arc.aiaa.org/doi/10.2514/1.J063456>) | blaiszik/awesome-matchem-datasets |
| [Materials Cloud Archives](<https://archive.materialscloud.org>) | blaiszik/awesome-matchem-datasets |
| [Materials Cloud Archive](<https://archive.materialscloud.org/>) | Navigation resource; Resource evidence |
| [MC2D record metadata](<https://archive.materialscloud.org/api/records/17gf6-84915>) | Catalog evidence |
| [CURATED COFs file license](<https://archive.materialscloud.org/api/records/1xf71-nf390>) | Catalog evidence |
| [Zeo-1 archived rights](<https://archive.materialscloud.org/api/records/3xmh2-vv758>) | Catalog evidence |
| [Hypothetical COF rights](<https://archive.materialscloud.org/api/records/cjhyq-nr115>) | Catalog evidence |
| [MAD-1.6 Materials Cloud metadata](<https://archive.materialscloud.org/api/records/ffd5a-1hc37>) | Catalog evidence |
| [Boyd-Woo file rights](<https://archive.materialscloud.org/api/records/nsp7v-2dk91>) | Catalog evidence |
| [ReDD-COFFEE v1](<https://archive.materialscloud.org/record/2023.13>) | Catalog evidence |
| [MC2D archived release](<https://archive.materialscloud.org/records/17gf6-84915>) | Catalog evidence; Catalog official route |
| [MAD-1.5](<https://archive.materialscloud.org/records/18tke-tt476>) | sedaoturak/data-resources-for-materials-science |
| [CURATED COFs archive release history](<https://archive.materialscloud.org/records/1xf71-nf390>) | Catalog evidence; Catalog official route |
| [Zeo-1 — data](<https://archive.materialscloud.org/records/3xmh2-vv758>) | Catalog official route |
| [Hypothetical COF Materials Cloud archive](<https://archive.materialscloud.org/records/cjhyq-nr115>) | Catalog evidence; Catalog official route |
| [Massive Atomic Diversity (MAD-1.6) — homepage](<https://archive.materialscloud.org/records/ffd5a-1hc37>) | Catalog evidence; Catalog official route |
| [Boyd-Woo Materials Cloud archive](<https://archive.materialscloud.org/records/nsp7v-2dk91>) | Catalog evidence; Catalog official route |
| [Materials Cloud 3D (MC3D) — data](<https://archive.materialscloud.org/records/szjaf-cfv74>) | Catalog official route |
| [MAD (Massive Atomic Diversity)](<https://archive.materialscloud.org/records/xdsbt-a3r17>) | blaiszik/awesome-matchem-datasets |
| [ReDD-COFFEE — data](<https://archive.materialscloud.org/records/y5gs8-pyj90>) | Catalog evidence; Catalog official route |
| [2DMatPedia author paper](<https://arxiv.org/abs/1901.09487>) | Catalog evidence |
| [Benchmarking Materials Property Prediction Methods](<https://arxiv.org/abs/2005.00707>) | Resource evidence |
| [OC20 author paper v5](<https://arxiv.org/abs/2010.09990>) | Catalog evidence |
| [All Topological Bands of All Nonmagnetic Stoichiometric Materials](<https://arxiv.org/abs/2105.09954>) | Catalog evidence |
| [MP-20 (CDVAE benchmark) — paper](<https://arxiv.org/abs/2110.06197>) | Catalog official route |
| [REMI Fe-Co-Ni combinatorial library — paper](<https://arxiv.org/abs/2204.05838>) | Catalog official route; REMI: REsource for Materials Informatics |
| [OC22 final author paper](<https://arxiv.org/abs/2206.08917v3>) | Catalog evidence |
| [DMC-ICE13 author paper](<https://arxiv.org/abs/2207.01353>) | Catalog evidence |
| [Carbon-data synthetic atomistic trajectories — paper](<https://arxiv.org/abs/2211.16443>) | Catalog official route |
| [BEAST DB primary author paper](<https://arxiv.org/abs/2405.20239>) | Catalog evidence |
| [The OpenLAM Challenges](<https://arxiv.org/abs/2501.16358>) | Catalog evidence; Catalog official route |
| [MatPES — paper](<https://arxiv.org/abs/2503.04070>) | Catalog official route |
| [ChemRxivQuest](<https://arxiv.org/abs/2505.05232>) | blaiszik/awesome-matchem-datasets |
| [SciCUEval](<https://arxiv.org/abs/2505.15094>) | blaiszik/awesome-matchem-datasets |
| [MP-ALOE — paper](<https://arxiv.org/abs/2507.05559>) | Catalog official route |
| [Open Direct Air Capture 2025 (ODAC25) — paper](<https://arxiv.org/abs/2508.03162>) | Catalog official route |
| [Materials Cloud 3D (MC3D) — paper](<https://arxiv.org/abs/2508.19223>) | Catalog evidence; Catalog official route |
| [Open Catalyst 2025 (OC25) — paper](<https://arxiv.org/abs/2509.17862>) | Catalog official route |
| [MatSyn25 author preprint](<https://arxiv.org/abs/2510.00776>) | Catalog evidence; Catalog official route |
| [MatSciBench](<https://arxiv.org/abs/2510.12171>) | blaiszik/awesome-matchem-datasets |
| [AQCat25 heterogeneous-catalysis dataset — paper](<https://arxiv.org/abs/2510.22938>) | Catalog official route |
| [LeMat-Synth synthesis-procedure corpus — paper](<https://arxiv.org/abs/2510.26824>) | Catalog evidence; Catalog official route |
| [All Topological Bands, full author manuscript](<https://arxiv.org/html/2105.09954v2>) | Catalog evidence |
| [ODAC23 author paper Table 1](<https://arxiv.org/html/2311.00341v2>) | Catalog evidence |
| [opXRD author preprint v2](<https://arxiv.org/html/2503.05577v2>) | Catalog evidence |
| [OC25 primary dataset paper](<https://arxiv.org/html/2509.17862v1>) | Catalog evidence |
| [Massive Atomic Diversity (MAD-1.5) — homepage](<https://arxiv.org/html/2603.02089v2>) | Catalog evidence; Catalog official route |
| [Pearson's Crystal Data — data](<https://asm.mpds.io/>) | Catalog official route |
| [Atomly](<https://atomly.net/#/>) | blaiszik/awesome-matchem-datasets |
| [NIMS AtomWork-Adv — homepage](<https://atomwork-adv.nims.go.jp/>) | Catalog official route |
| [NIMS AtomWork-Adv — data](<https://atomwork-adv.nims.go.jp/en/service.html>) | Catalog official route |
| [AtomWork-Adv provider service terms](<https://atomwork-adv.nims.go.jp/service.html?lan=jp>) | Catalog evidence |
| [Battery Archive](<https://batteryarchive.org/>) | Navigation resource; Resource evidence |
| [BEAST DB](<https://beastdb.nrel.gov/>) | Catalog official route; sedaoturak/data-resources-for-materials-science |
| [van der Waals Bilayer Database (BiDB)](<https://bidb.fysik.dtu.dk/>) | blaiszik/awesome-matchem-datasets |
| [BLASTNet](<https://blastnet.github.io>) | blaiszik/awesome-matchem-datasets |
| [C2DB](<https://c2db.fysik.dtu.dk>) | blaiszik/awesome-matchem-datasets |
| [Computational Single-Atom Catalyst Database (NCEPU) — data](<https://catalysis-ncepu-hvkydg736ykqeq26d5gxrn.streamlit.app/>) | Catalog official route |
| [ChemBench](<https://chembench.lamalab.org>) | blaiszik/awesome-matchem-datasets |
| [Author-hosted original paper](<https://chemgroups.northwestern.edu/hupp/Publications/316.pdf>) | Catalog evidence |
| [CoRE MOF Database — homepage](<https://chung-research-group.github.io/CoRE%20MOF%20Database.dc.html>) | Catalog official route |
| [NOMAD Repository and Archive](<https://cloud.nomad-lab.eu/nomad-lab/>) | Resource evidence |
| [CatApp](<https://cmr.fysik.dtu.dk/catapp/catapp.html>) | Navigation resource; Resource evidence |
| [Computational Materials Repository (CMR)](<https://cmr.fysik.dtu.dk/index.html>) | sedaoturak/data-resources-for-materials-science |
| [2D Alloy Database](<https://cmrdb.fysik.dtu.dk/2dalloys/>) | blaiszik/awesome-matchem-datasets |
| [COD official mirror](<https://cod.psdi.ac.uk/>) | Catalog evidence |
| [COD_HEM](<https://codhem.cecas.clemson.edu/login>) | sedaoturak/data-resources-for-materials-science |
| [AFLOW machine learning](<https://colab.research.google.com/drive/1oJa2Qk5HpBPXEoArtJxfz605859MDNCz>) | REMI: REsource for Materials Informatics |
| [Interface Materials Design/InterMat example](<https://colab.research.google.com/gist/knc6/0d9aa89f671687c6e925eea2be9b824a/intermat_gettingstarted.ipynb>) | JARVIS-Tools Notebooks |
| [MLFF SNAP training](<https://colab.research.google.com/github/FitSNAP/FitSNAP/blob/master/tutorial.ipynb>) | JARVIS-Tools Notebooks |
| [ALIGNN-PhononDos](<https://colab.research.google.com/github/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_PhononDOS.ipynb>) | JARVIS-Tools Notebooks |
| [ALIGNN-FF pretrained model/calculator usage](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Structure_Relaxation_Phonons_Interface.ipynb>) | JARVIS-Tools Notebooks |
| [Analyzing_MOF_datasets](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_MOF_datasets.ipynb>) | JARVIS-Tools Notebooks |
| [Analyzing_data_in_the_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | JARVIS-Tools Notebooks |
| [Analyzing data in JARVIS-Leaderboard](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_Leaderboard.ipynb>) | JARVIS-Tools Notebooks |
| [AtomVision_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionExample.ipynb>) | JARVIS-Tools Notebooks |
| [AtomVision_Leaderboard_Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/AtomVisionImageClassification.ipynb>) | JARVIS-Tools Notebooks |
| [BoltztrapExample](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/BoltztrapExample.ipynb>) | JARVIS-Tools Notebooks |
| [ChemNLP example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ChemNLP_Example.ipynb>) | JARVIS-Tools Notebooks |
| [ChemNLP HuggingFace example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ChemNLP_TitleToAbstract.ipynb>) | JARVIS-Tools Notebooks |
| [Comapre_MP_JV](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Comapre_MP_JV.ipynb>) | JARVIS-Tools Notebooks |
| [ConvexHull](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ConvexHull.ipynb>) | JARVIS-Tools Notebooks |
| [DiffractGPT_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/DiffractGPT_example.ipynb>) | JARVIS-Tools Notebooks |
| [DimensionalityAndExfoliationEnergy](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/DimensionalityAndExfoliationEnergy.ipynb>) | JARVIS-Tools Notebooks |
| [Downloading raw analysis data and input/output files](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Download_raw_data_for_webpages.ipynb>) | JARVIS-Tools Notebooks |
| [Element_filter_for_JARVIS_DFT_dataset](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Element_filter_for_JARVIS_DFT_dataset.ipynb>) | JARVIS-Tools Notebooks |
| [ALIGNN-FF Melt Quench](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Fast_Melt_Quench.ipynb>) | JARVIS-Tools Notebooks |
| [Run GPAW on Google-colab and calculate interface energy with jarvis-tools](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/GPAW_Colab.ipynb>) | JARVIS-Tools Notebooks |
| [ALIGNN-Pretrained property-predictor models](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/GetTotalEnergy.ipynb>) | JARVIS-Tools Notebooks |
| [Get JARVIS-DFT final structures in ASE or Pymatgen format](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Get_JARVIS_DFT_final_structures_in_ASE_or_Pymatgen_format.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_CONVERG_Convergence_and_machine_learning_predictions_of_Monkhorst_Pack_k_points_and_plane_wave_cut_off_in_high_throughput_DFT_calculations](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_CONVERG_Convergence_and_machine_learning_predictions_of_Monkhorst_Pack_k_points_and_plane_wave_cut_off_in_high_throughput_DFT_calculations.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_DFPT_High_throughput_Density_Functional_Perturbation_Theory_and_Machine_Learning_Predictions_of_Infrared,_Piezoelectric_and_Dielectric_Responses](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFPT_High_throughput_Density_Functional_Perturbation_Theory_and_Machine_Learning_Predictions_of_Infrared%2C_Piezoelectric_and_Dielectric_Responses.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_DFT_2D_High_throughput_Identification_and_Characterization_of_Two_dimensional_Materials_using_Density_functional_theory](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_2D_High_throughput_Identification_and_Characterization_of_Two_dimensional_Materials_using_Density_functional_theory.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_DFT_FormationEnergiesAccuracyCheck](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_FormationEnergiesAccuracyCheck.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_ELAST_Elastic_properties_of_bulk_and_low_dimensional_materials_using_van_der_Waals_density_functional](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ELAST_Elastic_properties_of_bulk_and_low_dimensional_materials_using_van_der_Waals_density_functional.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_LAMMPS](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_LAMMPS.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_CFID_LightGBM_GPUvsCPU](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_LightGBM_GPUvsCPU.ipynb>) | JARVIS-Tools Notebooks |
| [ML_Chem_Formula_Descriptors](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_Magpie_AIMS.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_ML_TensorFlowExample](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TensorFlowExample.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_ML_TrainingGPU](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TrainingGPU.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_Optoelectronics_Computational_screening_of_high_performance_optoelectronic_materials_using_OptB88vdW_and_TB_mBJ_formalisms](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Optoelectronics_Computational_screening_of_high_performance_optoelectronic_materials_using_OptB88vdW_and_TB_mBJ_formalisms.ipynb>) | JARVIS-Tools Notebooks |
| [Basic quantum espresso run](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Basic_Example.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_QuantumEspressoColab_Designing_High_Tc_Superconductors_with_BCS_inspired_Screening,_Density_Functional_Theory_and_Deep_learning](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_QuantumEspressoColab_Designing_High_Tc_Superconductors_with_BCS_inspired_Screening%2C_Density_Functional_Theory_and_Deep_learning.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_STEM_2D](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_STEM_2D.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_Solar_Accelerated_Discovery_of_Efficient_Solar_Cell_Materials_Using_Quantum_and_Machine_Learning_Methods](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Solar_Accelerated_Discovery_of_Efficient_Solar_Cell_Materials_Using_Quantum_and_Machine_Learning_Methods.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_TE_Data_driven_discovery_of_3D_and_2D_thermoelectric_materials](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_TE_Data_driven_discovery_of_3D_and_2D_thermoelectric_materials.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_TopologicalSpillage_High_throughput_Discovery_of_Topologically_Non_trivial_Materials_using_Spin_orbit_Spillage](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_TopologicalSpillage_High_throughput_Discovery_of_Topologically_Non_trivial_Materials_using_Spin_orbit_Spillage.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_WTBH_Database_of_Wannier_tight_binding_Hamiltonians_using_high_throughput_density_functional_theory](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_WTBH_Database_of_Wannier_tight_binding_Hamiltonians_using_high_throughput_density_functional_theory.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_Wannier90Example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Wannier90Example.ipynb>) | JARVIS-Tools Notebooks |
| [ML Sklearn Steel Fatigue](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ML_Sklearn.ipynb>) | JARVIS-Tools Notebooks |
| [Making 2D heterostructures](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Making_2D_heterostructures.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_Leaderboard_MatMiner](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/MatMiner_on_JARVIS_DFT.ipynb>) | JARVIS-Tools Notebooks |
| [MatGL-FF_Mlearn for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Matgl_mlearn.ipynb>) | JARVIS-Tools Notebooks |
| [MicroscopyGPT_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/MicroscopyGPT.ipynb>) | JARVIS-Tools Notebooks |
| [ParsingWebpages(JARVIS_DFT)](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT>) | JARVIS-Tools Notebooks |
| [https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb>) | JARVIS-Tools Notebooks |
| [With old qiskit package version: Quantum computation and Qiskit based electronic bandstructure](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_.ipynb>) | JARVIS-Tools Notebooks |
| [Si_bandstructure&densityof_states](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Si_bandstructure%26densityof_states.ipynb>) | JARVIS-Tools Notebooks |
| [Basic_Machine_learning_training_example_with_CFID_descriptors](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Machine_learning_training_example_with_CFID_descriptors.ipynb>) | JARVIS-Tools Notebooks |
| [Silicon atomic structure and analysis example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Silicon_atomic_structure_and_analysis_example.ipynb>) | JARVIS-Tools Notebooks |
| [ALIGNN-FF for energy and forces](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_ALIGNNFF_Mlearn.ipynb>) | JARVIS-Tools Notebooks |
| [Train CHGNet-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_CHGNet.ipynb>) | JARVIS-Tools Notebooks |
| [ALLEGRO training for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_ALLEGRO.ipynb>) | JARVIS-Tools Notebooks |
| [Train NEQUIP-FF for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Train_MLFF_NEQUIP.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_ALIGNN_Basic_Training_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Training_ALIGNN_model_example.ipynb>) | JARVIS-Tools Notebooks |
| [Basic_ALIGNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/alignn_jarvis_leaderboard.ipynb>) | JARVIS-Tools Notebooks |
| [AtomGPT_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example.ipynb>) | JARVIS-Tools Notebooks |
| [AtomGPT HuggingFace inference example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_example_huggingface.ipynb>) | JARVIS-Tools Notebooks |
| [AtomGPT forward model training example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/atomgpt_forward_example.ipynb>) | JARVIS-Tools Notebooks |
| [Inverse design of superconductors with CDVAE](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/cdvae_example.ipynb>) | JARVIS-Tools Notebooks |
| [Pretrained CHGNet Prediction](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chgnet_prediction.ipynb>) | JARVIS-Tools Notebooks |
| [CHIPS_FF_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/chipsff_example.ipynb>) | JARVIS-Tools Notebooks |
| [CIF To Graph_example](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/cif2graph.ipynb>) | JARVIS-Tools Notebooks |
| [JARVIS_Leaderboard_KGCNN](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/kgcnn_jarvis_leaderboard.ipynb>) | JARVIS-Tools Notebooks |
| [Pretrained OpenCatalystProject Model](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ocp_load_pretrained_models.ipynb>) | JARVIS-Tools Notebooks |
| [Python beginners notebook](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/python_beginners_notebook.ipynb>) | JARVIS-Tools Notebooks |
| [Scaling ALIGNN/SlaKoNet](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/scaling_analysis.ipynb>) | JARVIS-Tools Notebooks |
| [SNAP-FF_Mlearn for Silicon](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/snap_mlearn.ipynb>) | JARVIS-Tools Notebooks |
| [Vacancy formation ML](<https://colab.research.google.com/github/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/vacancy_ml.ipynb>) | JARVIS-Tools Notebooks |
| [open in colab](<https://colab.research.google.com/github/usnistgov/aims_workshop/blob/main/tutorials/intro-gnn-potentials.ipynb>) | JARVIS-Tools Notebooks |
| [NASA Common Research Model (CRM)](<https://commonresearchmodel.larc.nasa.gov>) | blaiszik/awesome-matchem-datasets |
| [MDF publishing/discovering guides](<https://connect.materialsdatafacility.org/how-to>) | Resource evidence |
| [HiFi-TURB LES/DNS](<https://cordis.europa.eu/project/id/814837>) | blaiszik/awesome-matchem-datasets |
| [MAGNDATA — homepage](<https://cryst.ehu.es/magndata/>) | Catalog evidence; Catalog official route |
| [MAGNDATA — data](<https://cryst.ehu.es/magndata/magndata_download.html>) | Catalog official route |
| [Pearson's Crystal Data — homepage](<https://crystalimpact.com/pcd/>) | Catalog evidence; Catalog official route |
| [NIMS AtomWork — data](<https://crystdb.nims.go.jp/>) | Catalog official route |
| [Mendeley Data](<https://data.mendeley.com/>) | sedaoturak/data-resources-for-materials-science |
| [Compressible TPC DNS DB](<https://data.mendeley.com/datasets/wt8t5kxzbs>) | blaiszik/awesome-matchem-datasets |
| [NIST AM-Bench — source](<https://data.nist.gov>) | blaiszik/awesome-matchem-datasets |
| [CAMEO (NIST) — source](<https://data.nist.gov/od/ds/mds2-2480/CAMEO_NComm-master.zip>) | blaiszik/awesome-matchem-datasets |
| [Airfoil CFD 2k](<https://data.openei.org/submissions/5970>) | blaiszik/awesome-matchem-datasets |
| [Jupyter Notebooks](<https://datacarpentry.org/python-ecology-lesson/jupyter_notebooks/>) | REMI: REsource for Materials Informatics |
| [Dryad electronic-transport dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.gn001>) | Catalog evidence |
| [Dryad elastic-tensor dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.h505v>) | Catalog evidence |
| [Dryad piezoelectric-tensor dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.n63m4>) | Catalog evidence |
| [Dryad dielectric-tensor dataset metadata](<https://datadryad.org/dataset/doi:10.5061/dryad.ph81h>) | Catalog evidence |
| [LeMat-Traj dataset server metadata](<https://datasets-server.huggingface.co/info?dataset=LeMaterial%2FLeMat-Traj>) | Catalog evidence |
| [PMechDB (Polar Mechanism DB)](<https://deeprxn.ics.uci.edu/pmechdb/download>) | blaiszik/awesome-matchem-datasets |
| [RMechDB (Radical Mechanism DB)](<https://deeprxn.ics.uci.edu/rmechdb>) | blaiszik/awesome-matchem-datasets |
| [Digital Hydrogen-S](<https://digital-hydrogen.com/storage>) | Navigation resource |
| [DMC-ICE13 — data](<https://discovery.ucl.ac.uk/id/eprint/10162009/1/2207.01353v1.pdf>) | Catalog evidence; Catalog official route |
| [Materials Project database versions](<https://docs.materialsproject.org/changes/database-versions>) | Catalog evidence |
| [Materials Project — data](<https://docs.materialsproject.org/downloading-data>) | Catalog official route |
| [Peregrine](<https://doi.ccs.ornl.gov/dataset/96b7da99-07e1-562d-88d5-d7e079acfef7>) | sedaoturak/data-resources-for-materials-science |
| [Work function and cleavage energy surface database — paper](<https://doi.org/10.1002/adfm.202401764>) | Catalog official route |
| [opXRD: Open Experimental Powder X-ray Diffraction Database — paper](<https://doi.org/10.1002/aidi.202500044>) | Catalog official route |
| [Accelerating Catalyst Materials Discovery With Large Artificial Intelligence Models](<https://doi.org/10.1002/anie.202526150>) | Supporting perspective |
| [OMDB-GAP1 — paper](<https://doi.org/10.1002/qute.201900023>) | Catalog official route |
| [Computation-Ready Experimental COF Database (CoRE COF) — paper](<https://doi.org/10.1016/j.ces.2017.05.004>) | Catalog official route |
| [MAST-ML perovskite stability educational slice — paper](<https://doi.org/10.1016/j.commatsci.2018.04.033>) | Catalog official route |
| [CoRE MOF Database — paper](<https://doi.org/10.1016/j.matt.2025.102140>) | Catalog official route |
| [DigBat / Dynamic Database of Solid-State Electrolytes — paper](<https://doi.org/10.1016/j.nanoms.2026.07.001>) | Catalog official route |
| [ab initio REPEAT Charge MOF Database (ARC-MOF) — paper](<https://doi.org/10.1021/acs.chemmater.2c02485>) | Catalog official route |
| [Mercado hypothetical 2D and 3D COFs — paper](<https://doi.org/10.1021/acs.chemmater.8b01425>) | Catalog official route |
| [MOFX-DB](<https://doi.org/10.1021/acs.jced.2c00583>) | blaiszik/awesome-matchem-datasets |
| [BEAST DB — paper](<https://doi.org/10.1021/acs.jpcc.4c06826>) | Catalog official route |
| [Computational Single-Atom Catalyst Database (NCEPU) — paper](<https://doi.org/10.1021/acs.jpcc.5c00491>) | Catalog official route |
| [JARVIS superconductivity 2D DFT cohort — paper](<https://doi.org/10.1021/acs.nanolett.2c04420>) | Catalog official route |
| [Open Catalyst 2020 (OC20) — paper](<https://doi.org/10.1021/acscatal.0c04525>) | Catalog official route |
| [Open Catalyst 2022 (OC22) — paper](<https://doi.org/10.1021/acscatal.2c05426>) | Catalog official route |
| [ZeoSyn zeolite synthesis dataset — paper](<https://doi.org/10.1021/acscentsci.3c01615>) | Catalog official route |
| [Open Direct Air Capture 2023 (ODAC23) — paper](<https://doi.org/10.1021/acscentsci.3c01629>) | Catalog official route |
| [CURATED covalent organic frameworks — paper](<https://doi.org/10.1021/acscentsci.9b00619>) | Catalog official route |
| [Materials Cloud Two-Dimensional Structure Database (MC2D) — paper](<https://doi.org/10.1021/acsnano.2c11510>) | Catalog official route |
| [Experimental 2D Materials Database (X2DB) — paper](<https://doi.org/10.1021/acsnano.6c01514>) | Catalog official route |
| [2D-Alloy Database — paper](<https://doi.org/10.1021/jacs.4c13863>) | Catalog official route |
| [Materials Databases: Foundations of Modern Digital Materials](<https://doi.org/10.1021/prechem.5c00449>) | Supporting perspective |
| [Wilmer hypothetical MOF database (hMOF) — paper](<https://doi.org/10.1038/nchem.1192>) | Catalog official route |
| [REMI Fe-Ga-Pd combinatorial library — paper](<https://doi.org/10.1038/s41467-020-19597-w>) | Catalog official route |
| [van der Waals Bilayer Database (BiDB) — paper](<https://doi.org/10.1038/s41467-024-45003-w>) | Catalog official route |
| [Matbench jdft2d — paper](<https://doi.org/10.1038/s41524-020-00406-3>) | Catalog official route |
| [JARVIS-DFT 2D snapshot — paper](<https://doi.org/10.1038/s41524-020-00440-1>) | Catalog official route |
| [WBM / Matbench Discovery stability test set — paper](<https://doi.org/10.1038/s41524-020-00481-6>) | Catalog official route |
| [Quantum Point Defects Database (QPOD) — paper](<https://doi.org/10.1038/s41524-022-00730-w>) | Catalog official route |
| [Quantum MOF Database (QMOF) — paper](<https://doi.org/10.1038/s41524-022-00796-6>) | Catalog official route |
| [JARVIS superconductivity 3D DFT cohort — paper](<https://doi.org/10.1038/s41524-022-00933-1>) | Catalog official route |
| [MPF.2021.2.8 — paper](<https://doi.org/10.1038/s41524-024-01227-4>) | Catalog official route |
| [MP-ALOE — data](<https://doi.org/10.1038/s41524-025-01834-9>) | Catalog evidence; Catalog official route |
| [Perovskite Database Project (solar cells) — paper](<https://doi.org/10.1038/s41560-021-00941-3>) | Catalog official route |
| [Boyd-Woo hypothetical MOFs for wet flue-gas capture — paper](<https://doi.org/10.1038/s41586-019-1798-7>) | Catalog official route |
| [GNoME released stable-materials set — paper](<https://doi.org/10.1038/s41586-023-06735-9>) | Catalog official route |
| [Alex-MP-20 (MatterGen) — paper](<https://doi.org/10.1038/s41586-025-08628-5>) | Catalog official route |
| [2DMatPedia — paper](<https://doi.org/10.1038/s41597-019-0097-3>) | Catalog evidence; Catalog official route |
| [SNUMAT hybrid-functional band-gap dataset — paper](<https://doi.org/10.1038/s41597-020-00723-8>) | Catalog official route |
| [Zeo-1 — paper](<https://doi.org/10.1038/s41597-022-01160-5>) | Catalog official route |
| [SuperBand electronic-band / superconductivity dataset — paper](<https://doi.org/10.1038/s41597-025-05015-7>) | Catalog evidence; Catalog official route |
| [Open Molecular Crystals 2025 (OMC25) — paper](<https://doi.org/10.1038/s41597-026-06628-2>) | Catalog evidence; Catalog official route |
| [Roadmap for transforming heterogeneous catalysis with artificial intelligence](<https://doi.org/10.1038/s41929-026-01479-x>) | Supporting perspective |
| [Materials Project Trajectory (MPtrj) — paper](<https://doi.org/10.1038/s42256-023-00716-3>) | Catalog official route |
| [Open Materials 2024 (OMat24) — paper](<https://doi.org/10.1038/s43588-026-00996-w>) | Catalog official route |
| [Materials Project piezoelectric tensor release (2015) — paper](<https://doi.org/10.1038/sdata.2015.53>) | Catalog official route |
| [Materials Project elastic tensor release (2015) — paper](<https://doi.org/10.1038/sdata.2015.9>) | Catalog official route |
| [Materials Project dielectric tensor release (2017) — paper](<https://doi.org/10.1038/sdata.2016.134>) | Catalog official route |
| [MAST-ML dilute-solute diffusion educational slice — paper](<https://doi.org/10.1038/sdata.2016.54>) | Catalog official route |
| [Materials Project / Ricci electronic transport database — paper](<https://doi.org/10.1038/sdata.2017.85>) | Catalog official route |
| [Materials Project / Petretto DFPT phonons (2018) — paper](<https://doi.org/10.1038/sdata.2018.65>) | Catalog official route |
| [Deem hypothetical zeolites / PCOD SLC-good — paper](<https://doi.org/10.1039/C0CP02255A>) | Catalog official route |
| [Perov-5 / Matbench perovskites — paper](<https://doi.org/10.1039/C2EE22341D>) | Catalog official route |
| [ALIGNN-FF training dataset — paper](<https://doi.org/10.1039/D2DD00096B>) | Catalog evidence; Catalog official route |
| [ReDD-COFFEE — paper](<https://doi.org/10.1039/D3TA00470H>) | Catalog official route |
| [MOSAEC MOF Database (MOSAEC-DB) — paper](<https://doi.org/10.1039/D4SC07438F>) | Catalog official route |
| [Materials Project — paper](<https://doi.org/10.1063/1.4812323>) | Catalog official route |
| [DMC-ICE13 — paper](<https://doi.org/10.1063/5.0102645>) | Catalog official route |
| [MDR XAFS DB — paper](<https://doi.org/10.1080/27660400.2023.2197518>) | Catalog official route |
| [Starrydata2 experimental materials datasets — paper](<https://doi.org/10.1080/27660400.2025.2590811>) | Catalog official route |
| [Computational 2D Materials Database (C2DB) — paper](<https://doi.org/10.1088/2053-1583/ac1059>) | Catalog official route |
| [sAlex25 — paper](<https://doi.org/10.1088/2515-7639/ae6620>) | Catalog evidence; Catalog official route |
| [NLR MatDB (formerly NRELMatDB) — paper](<https://doi.org/10.1103/PhysRevB.85.115104>) | Catalog official route |
| [X23 diffusion Monte Carlo benchmark — paper](<https://doi.org/10.1103/PhysRevLett.133.046401>) | Catalog official route |
| [AFLOW AEL–AGL thermomechanical cohort (2017) — paper](<https://doi.org/10.1103/PhysRevMaterials.1.015401>) | Catalog evidence; Catalog official route |
| [van der Waals 2D Heterostructure Database (HetDB) — paper](<https://doi.org/10.1103/cl8c-8f1f>) | Catalog official route |
| [Topological Quantum Chemistry all-band materials catalog — paper](<https://doi.org/10.1126/science.abg9094>) | Catalog official route |
| [AIMNet2 Dataset](<https://doi.org/10.1184/R1/27629937.v1>) | blaiszik/awesome-matchem-datasets |
| [Quantum‑Chemical Bonding DB (LOBSTER)](<https://doi.org/10.17172/nomad.mc38-9gm1>) | blaiszik/awesome-matchem-datasets |
| [Materials Project — primary documentation](<https://doi.org/10.17188/1693272>) | Catalog evidence |
| [MD Simulated Monomer Properties](<https://doi.org/10.18126/8p6m-e135>) | blaiszik/awesome-matchem-datasets |
| [The rise of the digital materials ecosystem](<https://doi.org/10.20517/aiagent.2026.08>) | Supporting perspective |
| [10.21981/CPNK-XE48](<https://doi.org/10.21981/CPNK-XE48>) | nanoHUB Machine Learning Lab Module |
| [Curated RANS ↔ DNS Dataset](<https://doi.org/10.34740/kaggle/dsv/2637500>) | blaiszik/awesome-matchem-datasets |
| [MDR XAFS DB — data](<https://doi.org/10.48505/nims.1447>) | Catalog official route |
| [MDR SuperCon Datasheet — homepage](<https://doi.org/10.48505/nims.3739>) | Catalog official route |
| [MDR SuperCon Datasheet — data](<https://doi.org/10.48505/nims.4487>) | Catalog official route |
| [Materials Project / Ricci electronic transport database — data](<https://doi.org/10.5061/dryad.gn001>) | Catalog official route |
| [Materials Project elastic tensor release (2015) — data](<https://doi.org/10.5061/dryad.h505v>) | Catalog official route |
| [Materials Project piezoelectric tensor release (2015) — data](<https://doi.org/10.5061/dryad.n63m4>) | Catalog official route |
| [Materials Project dielectric tensor release (2017) — data](<https://doi.org/10.5061/dryad.ph81h>) | Catalog official route |
| [Work function and cleavage energy surface database — data](<https://doi.org/10.5281/zenodo.10703249>) | Catalog official route |
| [Vector-QM24](<https://doi.org/10.5281/zenodo.11164951>) | blaiszik/awesome-matchem-datasets |
| [Anion Solvation DB](<https://doi.org/10.5281/zenodo.13987781>) | blaiszik/awesome-matchem-datasets |
| [opXRD](<https://doi.org/10.5281/zenodo.14254270>) | blaiszik/awesome-matchem-datasets |
| [BigSolDB 2.0](<https://doi.org/10.5281/zenodo.15094979>) | blaiszik/awesome-matchem-datasets |
| [Battery Electrolyte Solvation/Ionization](<https://doi.org/10.5281/zenodo.15252439>) | blaiszik/awesome-matchem-datasets |
| [MSR-ACC/TAE25](<https://doi.org/10.5281/zenodo.15387279>) | blaiszik/awesome-matchem-datasets |
| [SHNITSEL Data](<https://doi.org/10.5281/zenodo.15482819>) | blaiszik/awesome-matchem-datasets |
| [Materials Project Phonon database v1.1 — data](<https://doi.org/10.5281/zenodo.20196565>) | Catalog official route |
| [Leeds Solubility Data](<https://doi.org/10.5281/zenodo.3686213>) | blaiszik/awesome-matchem-datasets |
| [BigSolDB](<https://doi.org/10.5281/zenodo.6809668>) | blaiszik/awesome-matchem-datasets |
| [ARROWS³ — source](<https://doi.org/10.5281/zenodo.8331001>) | blaiszik/awesome-matchem-datasets |
| [SuperBand electronic-band / superconductivity dataset — data](<https://doi.org/10.57760/sciencedb.16728>) | Catalog official route |
| [ChemDataExtractor battery materials database (2020) — data](<https://doi.org/10.6084/m9.figshare.11888115.v2>) | Catalog official route |
| [Text-mined solution-based inorganic synthesis procedures — data](<https://doi.org/10.6084/m9.figshare.16583387.v4>) | Catalog official route |
| [MPF.2021.2.8 — data](<https://doi.org/10.6084/m9.figshare.19470599>) | Catalog official route |
| [Transition1x](<https://doi.org/10.6084/m9.figshare.19614657>) | blaiszik/awesome-matchem-datasets |
| [ChemDataExtractor thermoelectric materials database — data](<https://doi.org/10.6084/m9.figshare.19658787>) | Catalog official route |
| [Materials Project Trajectory (MPtrj) — data](<https://doi.org/10.6084/m9.figshare.23713842>) | Catalog official route |
| [3DSC_ICSD — data](<https://doi.org/10.6084/m9.figshare.24499924>) | Catalog official route |
| [3DSC_MP — data](<https://doi.org/10.6084/m9.figshare.24499930>) | Catalog official route |
| [mech-USPTO-31k](<https://doi.org/10.6084/m9.figshare.24797220>) | blaiszik/awesome-matchem-datasets |
| [HYPOD-X: quasicrystals and approximants — data](<https://doi.org/10.6084/m9.figshare.25650705.v3>) | Catalog official route |
| [QM9Star](<https://doi.org/10.6084/m9.figshare.27002905>) | sedaoturak/data-resources-for-materials-science |
| [ChemDataExtractor/Snowball Curie–Néel dataset (2025) — data](<https://doi.org/10.6084/m9.figshare.29559686.v2>) | Catalog official route |
| [SevenNet-Omni domain bridging set](<https://doi.org/10.6084/m9.figshare.30399814>) | Navigation resource; Resource evidence |
| [Solid-State Synthesis w/ Impurity Phases](<https://doi.org/10.6084/m9.figshare.30423274>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [JARVIS-DFT 3D — data](<https://doi.org/10.6084/m9.figshare.6815699>) | Catalog official route |
| [Text-Mined Solid-State Synthesis (CederGroup / Kononova) — source](<https://doi.org/10.6084/m9.figshare.9722159>) | blaiszik/awesome-matchem-datasets |
| [Text-mined inorganic solid-state synthesis recipes — data](<https://doi.org/10.6084/m9.figshare.9722159.v3>) | Catalog official route |
| [Materials Project / Petretto DFPT phonons (2018) — data](<https://doi.org/10.6084/m9.figshare.c.3938023>) | Catalog official route |
| [ChemDataExtractor Curie and Néel database (2018) — data](<https://doi.org/10.6084/m9.figshare.c.3954418>) | Catalog official route |
| [Phono3py 103-compound finite-displacement dataset (PBEsol) — paper](<https://doi.org/10.7566/JPSJ.92.012001>) | Catalog official route |
| [LLM4Mat](<https://drive.google.com/drive/folders/1HpGhuNHG4EQCQMZaKPwEQNH9stJKw-ht>) | blaiszik/awesome-matchem-datasets |
| [TextEdge](<https://drive.google.com/drive/folders/1YCDBzwjwNRIc1FRkB662G3Y5AOWaokUG>) | blaiszik/awesome-matchem-datasets |
| [IZA Framework Type Codes](<https://europe.iza-structure.org/IZA-SC_FTC.php>) | Catalog evidence |
| [OMC25 official access documentation](<https://facebookresearch.github.io/fairchem/omc25/>) | Catalog evidence |
| [OCx24](<https://fair-chem.github.io/catalysts/datasets/ocx24.html>) | sedaoturak/data-resources-for-materials-science |
| [ODAC23](<https://fair-chem.github.io/dac/datasets/odac.html>) | blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [OMat24](<https://fair-chem.github.io/inorganic_materials/datasets/omat24.html>) | sedaoturak/data-resources-for-materials-science |
| [Figshare](<https://figshare.com/>) | sedaoturak/data-resources-for-materials-science |
| [Quantum MOF Database (QMOF) — data](<https://figshare.com/articles/dataset/13147324/18>) | Catalog official route |
| [WBM / Matbench Discovery stability test set — data](<https://figshare.com/articles/dataset/22715158>) | Catalog official route |
| [USPTO-Lowe](<https://figshare.com/articles/dataset/5104873>) | blaiszik/awesome-matchem-datasets |
| [JARVIS-DFT 2D snapshot — data](<https://figshare.com/articles/dataset/6815705>) | Catalog official route |
| [2DMatPedia — data](<https://figshare.com/articles/dataset/7699910/3>) | Catalog official route |
| [Fatigue Database of AM Alloys2022](<https://figshare.com/articles/dataset/Fatigue_Database_of_Additively_Manufactured_Alloys/22337629>) | sedaoturak/data-resources-for-materials-science |
| [L2M3 - Large Language Model MOF Miner](<https://figshare.com/articles/dataset/L2M3_Database/27187917>) | blaiszik/awesome-matchem-datasets |
| [Machine Learning Materials Datasets](<https://figshare.com/articles/dataset/MAST-ML_Education_Datasets/7017254>) | Catalog official route; Navigation resource; Requested collection; sedaoturak/data-resources-for-materials-science |
| [MP-ALOE](<https://figshare.com/articles/dataset/MP-ALOE_An_r2SCAN_dataset_for_universal_machine_learning_interatomic_potentials/29452190>) | blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [QMOF Database](<https://figshare.com/articles/dataset/QMOF_Database/13147324>) | blaiszik/awesome-matchem-datasets |
| [USPTO-50k (Schneider)](<https://figshare.com/articles/dataset/USPTO-50K_raw_/25459573>) | blaiszik/awesome-matchem-datasets |
| [Unrestricted CCSD(T) Dataset For Organic Molecule Reactions](<https://figshare.com/articles/dataset/Unrestricted_CCSD_T_Dataset_For_Organic_Molecule_Reactions/30267877?file=58465231>) | blaiszik/awesome-matchem-datasets |
| [SNUMAT hybrid-functional band-gap dataset — data](<https://figshare.com/articles/dataset/hybrid_bandgap_200821_v1_zip/12839240>) | Catalog official route |
| [DigiMOF](<https://figshare.com/collections/DigiMOF_A_Database_of_Metal_Organic_Framework_Synthesis_Information_Generated_via_Text_Mining/6652495>) | sedaoturak/data-resources-for-materials-science |
| [JARVIS superconductivity 3D DFT cohort — data](<https://figshare.com/ndownloader/files/38307921>) | Catalog official route |
| [JARVIS superconductivity 2D DFT cohort — data](<https://figshare.com/ndownloader/files/38950433>) | Catalog official route |
| [ZINC20-ML](<https://files.docking.org/zinc20-ML/>) | blaiszik/awesome-matchem-datasets |
| [Mat-Instructions](<https://github.com/AI4MOL/Mat-Instruction>) | blaiszik/awesome-matchem-datasets |
| [AlphaFlow](<https://github.com/AbolhasaniLab/AlphaFlow>) | blaiszik/awesome-matchem-datasets |
| [QMOF author repository](<https://github.com/Andrew-S-Rosen/QMOF>) | Catalog evidence; Catalog official route |
| [MatScholar Task-Schema QA (MatSci-NLP)](<https://github.com/BangLab-UdeM-Mila/NLP4MatSci-ACL23>) | blaiszik/awesome-matchem-datasets |
| [ChemDataExtractor/Snowball Curie–Néel dataset (2025) — code](<https://github.com/C-R-Kelly/Curie-Neel-temperature-dataset>) | Catalog official route |
| [Materials Project Trajectory (MPtrj) — homepage](<https://github.com/CederGroupHub/chgnet>) | Catalog official route |
| [A-Lab (Autonomous Inorganic Synthesis, LBNL) — source](<https://github.com/CederGroupHub/s4>) | blaiszik/awesome-matchem-datasets |
| [Text-Mined Solution-Based Synthesis (CederGroup)](<https://github.com/CederGroupHub/text-mined-solution-synthesis_public>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [Text-Mined Solid-State Synthesis (CederGroup)](<https://github.com/CederGroupHub/text-mined-synthesis_public>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [ChemQA](<https://github.com/ChemFoundationModels/ChemLLMBench>) | blaiszik/awesome-matchem-datasets |
| [Experimental design with Citrination](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/ExperimentalDesign.ipynb>) | REMI: REsource for Materials Informatics |
| [Import Instron](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/ImportInstron.ipynb>) | REMI: REsource for Materials Informatics |
| [Citrination t-SNE API](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/TsneDemo.ipynb>) | REMI: REsource for Materials Informatics |
| [Importing data from VASP calculations into Citrination](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/1_ImportVASP.ipynb>) | REMI: REsource for Materials Informatics |
| [Working with PIFs](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/2_WorkingWithPIFs.ipynb>) | REMI: REsource for Materials Informatics |
| [Introduction to Queries](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/3_IntroQueries.ipynb>) | REMI: REsource for Materials Informatics |
| [Machine Learning on Citrination](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/4_MLonCitrination.ipynb>) | REMI: REsource for Materials Informatics |
| [Advanced PIF Tutorial](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/AdvancedPif.ipynb>) | REMI: REsource for Materials Informatics |
| [Advanced Queries](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_api_examples/tutorial_sequence/AdvancedQueries.ipynb>) | REMI: REsource for Materials Informatics |
| [Citrination Demo on Shape Memory Alloys](<https://github.com/CitrineInformatics/learn-citrination/blob/master/citrination_ui_examples/JournalPaperToModel.ipynb>) | REMI: REsource for Materials Informatics |
| [Compare Band Gaps From Citrination and Materials Project](<https://github.com/CitrineInformatics/learn-citrination/blob/master/matminer_examples/BandGapComparisonCitrinationVsMP.ipynb>) | REMI: REsource for Materials Informatics |
| [Citrine Data Retrieval Example](<https://github.com/CitrineInformatics/learn-citrination/blob/master/matminer_examples/DataRetrievalWithMatMiner.ipynb>) | REMI: REsource for Materials Informatics |
| [Synthetic Data Demo](<https://github.com/CitrineInformatics/learn-citrination/blob/master/synthetic_data_examples/SyntheticDataDemo.ipynb>) | REMI: REsource for Materials Informatics |
| [Citrination t-SNE API](<https://github.com/CitrineInformatics/learn-citrination/tree/master/citrination_api_examples>) | REMI: REsource for Materials Informatics |
| [Advanced Queries](<https://github.com/CitrineInformatics/learn-citrination/tree/master/citrination_api_examples/tutorial_sequence>) | REMI: REsource for Materials Informatics |
| [Citrination Demo on Shape Memory Alloys](<https://github.com/CitrineInformatics/learn-citrination/tree/master/citrination_ui_examples>) | REMI: REsource for Materials Informatics |
| [Synthetic Data Demo](<https://github.com/CitrineInformatics/learn-citrination/tree/master/synthetic_data_examples>) | REMI: REsource for Materials Informatics |
| [PatCID (IBM)](<https://github.com/DS4SD/PatCID>) | blaiszik/awesome-matchem-datasets |
| [NanoMine](<https://github.com/Duke-MatSci/nanomine>) | sedaoturak/data-resources-for-materials-science |
| [Perovskite Database Project (solar cells) — code](<https://github.com/FAIRmat-NFDI/nomad-perovskite-solar-cells-database>) | Catalog official route |
| [BOOM: Benchmarks for Out-Of-distribution Molecules](<https://github.com/FLASK-LLNL/BOOM>) | blaiszik/awesome-matchem-datasets |
| [MC-PDFT-OPESf](<https://github.com/Ferg-Lab/PDFT_OPESf>) | blaiszik/awesome-matchem-datasets |
| [JARVIS-Tools Notebooks](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks>) | Navigation resource; Requested collection; sedaoturak/data-resources-for-materials-science |
| [alt text](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/actions/workflows/test-notebooks.yml/badge.svg>) | JARVIS-Tools Notebooks |
| [Analyzing data in the JARVIS DFT dataset](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Analyzing_data_in_the_JARVIS_DFT_dataset.ipynb>) | REMI: REsource for Materials Informatics |
| [BoltzTrap Example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/BoltztrapExample.ipynb>) | REMI: REsource for Materials Informatics |
| [JARVIS DFT Formation Energies Accuracy Check](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_DFT_FormationEnergiesAccuracyCheck.ipynb>) | REMI: REsource for Materials Informatics |
| [GPU can accelerate model training with respect to CPU using JARVIS-ML CFID dataset](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_LightGBM_GPUvsCPU.ipynb>) | REMI: REsource for Materials Informatics |
| [JARVIS ML TensorFlow Example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TensorFlowExample.ipynb>) | REMI: REsource for Materials Informatics |
| [JARVIS ML Training GPU](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_ML_TrainingGPU.ipynb>) | REMI: REsource for Materials Informatics |
| [JARVIS Wannier 90 Example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/JARVIS_Wannier90Example.ipynb>) | REMI: REsource for Materials Informatics |
| [Si band structure & density of states](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Si_bandstructure%26densityof_states.ipynb>) | REMI: REsource for Materials Informatics |
| [Simple Machine learning training example with CFID descriptors](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Machine_learning_training_example_with_CFID_descriptors.ipynb>) | REMI: REsource for Materials Informatics |
| [Simple Silicon atomic structure and analysis example](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Simple_Silicon_atomic_structure_and_analysis_example.ipynb>) | REMI: REsource for Materials Informatics |
| [Python for novice](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/python_beginners_notebook.ipynb>) | REMI: REsource for Materials Informatics |
| [Basic external tutorial on linear models](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/blob/master/training_linear_models>) | JARVIS-Tools Notebooks |
| [Github issues](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues>) | JARVIS-Tools Notebooks |
| [https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues)(preferred](<https://github.com/JARVIS-Materials-Design/jarvis-tools-notebooks/issues)(preferred>) | JARVIS-Tools Notebooks |
| [LeMat-GenBench](<https://github.com/LeMaterial/lemat-genbench>) | Navigation resource |
| [LeMat-Synth synthesis-procedure corpus — code](<https://github.com/LeMaterial/lematerial-llm-synthesis>) | Catalog official route |
| [SNUMAT hybrid-functional band-gap dataset — code](<https://github.com/MDIL-SNU/AMP2>) | Catalog official route |
| [Material Synthesis 2025 (MatSyn25) — code](<https://github.com/MatSynAI/MatSyn25>) | Catalog official route |
| [FreeSolv](<https://github.com/MobleyLab/FreeSolv>) | blaiszik/awesome-matchem-datasets |
| [PaRoutes](<https://github.com/MolecularAI/PaRoutes>) | blaiszik/awesome-matchem-datasets |
| [BEAST DB — code](<https://github.com/Nick-Singstock/BEAST_DB_Manager>) | Catalog official route |
| [ChemNLP](<https://github.com/OpenBioML/chemnlp>) | blaiszik/awesome-matchem-datasets |
| [ChemDFM](<https://github.com/OpenDFM/ChemDFM>) | blaiszik/awesome-matchem-datasets |
| [RadonPy Polymer Properties Data](<https://github.com/RadonPy/RadonPy/blob/648c9a492808339c9bb7ad2c1137e5a7b07614ca/data/PI1070.csv>) | blaiszik/awesome-matchem-datasets |
| [Data](<https://github.com/Shorku/rhnet/tree/main/data>) | blaiszik/awesome-matchem-datasets |
| [ChemDataExtractor battery materials database (2020) — code](<https://github.com/ShuHuang/batterydatabase>) | Catalog official route |
| [PDB-Struct](<https://github.com/WANG-CR/PDB-Struct>) | blaiszik/awesome-matchem-datasets |
| [Computational Single-Atom Catalyst Database (NCEPU) — code](<https://github.com/Weijie-Yang/AML>) | Catalog official route |
| [MaScQA](<https://github.com/abhijeetgangan/MaSTeA>) | blaiszik/awesome-matchem-datasets |
| [AFLOW — code](<https://github.com/aflow-org/aflow>) | Catalog official route |
| [3DSC_MP — code](<https://github.com/aimat-lab/3DSC>) | Catalog official route |
| [opXRD: Open Experimental Powder X-ray Diffraction Database — code](<https://github.com/aimat-lab/opXRD>) | Catalog official route |
| [Olympus — source](<https://github.com/aspuru-guzik-group/olympus>) | blaiszik/awesome-matchem-datasets |
| [https://github.com/atomgptlab/jarvis-tools-notebooks](<https://github.com/atomgptlab/jarvis-tools-notebooks>) | JARVIS-Tools Notebooks |
| [Basic external tutorial on linear models](<https://github.com/atomgptlab/jarvis-tools-notebooks/blob/master/training_linear_models>) | JARVIS-Tools Notebooks |
| [Phonondb author repository](<https://github.com/atztogo/phonondb>) | Catalog evidence; Catalog official route |
| [Phono3py 103-compound finite-displacement dataset (PBEsol) — data](<https://github.com/atztogo/phonondb/tree/main/mdr/phono3py_103compounds_fd>) | Catalog official route |
| [PhononDB lattice thermal conductivity (MDR) — data](<https://github.com/atztogo/phonondb/tree/main/mdr/phonondb_LTC>) | Catalog official route |
| [blaiszik/awesome-matchem-datasets](<https://github.com/blaiszik/awesome-matchem-datasets>) | Navigation resource; Requested collection; Resource evidence |
| [ChemDataExtractor Curie and Néel database (2018) — code](<https://github.com/cjcourt/magdb>) | Catalog official route |
| [CoRE COF author repository](<https://github.com/core-cof/CoRE-COF-Database>) | Catalog evidence; Catalog official route |
| [Computation-Ready Experimental COF Database (CoRE COF) — data](<https://github.com/core-cof/CoRE-COF-Database/blob/master/CoRE-COFs_DT1242-v7.0.zip>) | Catalog official route |
| [CURATED covalent organic frameworks — code](<https://github.com/danieleongari/CURATED-COFs>) | Catalog official route |
| [OpenLAM official repository](<https://github.com/deepmodeling/openlam>) | Catalog evidence; Catalog official route |
| [OpenLAM Crystal Philately challenge collection — data](<https://github.com/deepmodeling/openlam#query-crystal-structures-from-openlam-database>) | Catalog official route |
| [LLM-EO](<https://github.com/deepprinciple/llmeo>) | blaiszik/awesome-matchem-datasets |
| [Mechanical-MNIST](<https://github.com/elejeune11/Mechanical-MNIST>) | sedaoturak/data-resources-for-materials-science |
| [ZeoSyn](<https://github.com/eltonpan/zeosyn_dataset>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [ZeoSyn zeolite synthesis dataset — data](<https://github.com/eltonpan/zeosyn_dataset/blob/master/dataset/ZEOSYN.xlsx>) | Catalog official route |
| [Pfizer HiTEA](<https://github.com/emmaking-smith/HiTEA>) | blaiszik/awesome-matchem-datasets |
| [SciGlass](<https://github.com/epam/SciGlass>) | sedaoturak/data-resources-for-materials-science |
| [Open Catalyst 2020 (OC20) — code](<https://github.com/facebookresearch/fairchem>) | Catalog official route |
| [Open Catalyst 2020 (OC20) — data](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc20.md>) | Catalog evidence; Catalog official route |
| [OC22 official data documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc22.md>) | Catalog evidence; Catalog official route |
| [OC25 official data documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/catalysts/datasets/oc25.md>) | Catalog evidence |
| [ODAC23 official download documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac23.md>) | Catalog evidence; Catalog official route |
| [ODAC25 official dataset documentation](<https://github.com/facebookresearch/fairchem/blob/main/docs/dac/datasets/odac25.md>) | Catalog evidence |
| [OMol25 Electronic Structures](<https://github.com/facebookresearch/fairchem/blob/main/docs/molecules/datasets/omol25_elec.md>) | blaiszik/awesome-matchem-datasets |
| [OCx24](<https://github.com/facebookresearch/fairchem/tree/main/src/fairchem/applications/ocx/data>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [Flavor Analysis and Recognition Transformer](<https://github.com/fart-lab/fart/tree/main/dataset>) | blaiszik/awesome-matchem-datasets |
| [Stress-Strain Properties Database](<https://github.com/gh-PankajKumar/chemdataextractorv2.3-stresseng>) | sedaoturak/data-resources-for-materials-science |
| [GNoME released stable-materials set — homepage](<https://github.com/google-deepmind/materials_discovery>) | Catalog official route |
| [GNoME released stable-materials set — data](<https://github.com/google-deepmind/materials_discovery/blob/main/DATASET.md>) | Catalog evidence; Catalog official route |
| [GNoME](<https://github.com/google-deepmind/materials_discovery?tab=readme-ov-file#dataset>) | sedaoturak/data-resources-for-materials-science |
| [matminer repository](<https://github.com/hackingmaterials/matminer>) | Navigation resource; Resource evidence |
| [Automatminer Basic Tutorial](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/automatminer-nb/automatminer_basic.ipynb>) | REMI: REsource for Materials Informatics |
| [Data Retrieval Basics](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/data_retrieval_basics.ipynb>) | REMI: REsource for Materials Informatics |
| [Plot and compare experimental and computational bandgaps](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/expt_vs_comp_bandgap.ipynb>) | REMI: REsource for Materials Informatics |
| [Interacting with Jarvis via MDF Search](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/jarvis.ipynb>) | REMI: REsource for Materials Informatics |
| [Uranium-oxygen bond length analysis using MPDS](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/data_retrieval-nb/mpds.ipynb>) | REMI: REsource for Materials Informatics |
| [Advanced Visualization using FigRecipes](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/figrecipes-nb/figrecipes_advanced.ipynb>) | REMI: REsource for Materials Informatics |
| [Visualization using FigRecipes](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/figrecipes-nb/figrecipes_basics.ipynb>) | REMI: REsource for Materials Informatics |
| [Matminer introduction - Predicting bulk modulus](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/bulk_modulus.ipynb>) | REMI: REsource for Materials Informatics |
| [Train a Model to Predict Formation Energy using the OQMD](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/formation_e.ipynb>) | REMI: REsource for Materials Informatics |
| [Recreating Ling IMMI (2017) - Random Forest with Uncertainty](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/rf-with-uncertainty.ipynb>) | REMI: REsource for Materials Informatics |
| [Using sklearn Pipeline with matminer](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/sklearn_pipeline.ipynb>) | REMI: REsource for Materials Informatics |
| [Using the Crystal Structure Representation of Ward et al. to predict formation enthalpy,using the FLLA dataset.](<https://github.com/hackingmaterials/matminer_examples/blob/master/matminer_examples/machine_learning-nb/voronoi-ward-prb-2017.ipynb>) | REMI: REsource for Materials Informatics |
| [MOFs_CO2N2O2_ML](<https://github.com/hasancangulbalkan/MOFs_CO2N2O2_ML>) | sedaoturak/data-resources-for-materials-science |
| [ProtBENCH](<https://github.com/hevalatas/ProtBENCH>) | blaiszik/awesome-matchem-datasets |
| [Getting Started](<https://github.com/hyperspy/hyperspy-demos/blob/master/1_Getting_Started.ipynb>) | REMI: REsource for Materials Informatics |
| [SVD and BSS](<https://github.com/hyperspy/hyperspy-demos/blob/master/2_SVD_and_BSS.ipynb>) | REMI: REsource for Materials Informatics |
| [Fitting tutorial](<https://github.com/hyperspy/hyperspy-demos/blob/master/Fitting_tutorial.ipynb>) | REMI: REsource for Materials Informatics |
| [Online Robust PCA](<https://github.com/hyperspy/hyperspy-demos/blob/master/Online_Robust_PCA.ipynb>) | REMI: REsource for Materials Informatics |
| [SEM EDS 4D visualization](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/EDS/SEM_EDS_4D_visualisation.ipynb>) | REMI: REsource for Materials Informatics |
| [TEM EDS nanoparticles](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/EDS/TEM_EDS_nanoparticles.ipynb>) | REMI: REsource for Materials Informatics |
| [EELS analysis](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/EELS/EELS_analysis.ipynb>) | REMI: REsource for Materials Informatics |
| [Holography](<https://github.com/hyperspy/hyperspy-demos/blob/master/electron_microscopy/Holography/Holography.ipynb>) | REMI: REsource for Materials Informatics |
| [Working with image data](<https://github.com/hyperspy/hyperspy-demos/blob/master/image_data/working_with_imagedata.ipynb>) | REMI: REsource for Materials Informatics |
| [Working with image data](<https://github.com/hyperspy/hyperspy-demos/tree/master/image_data>) | REMI: REsource for Materials Informatics |
| [GPQA Diamond](<https://github.com/idavidrein/gpqa>) | blaiszik/awesome-matchem-datasets |
| [WBM / Matbench Discovery stability test set — code](<https://github.com/janosh/matbench-discovery>) | Catalog official route |
| [Carbon Data](<https://github.com/jla-gardner/carbon-data>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [Carbon-data synthetic atomistic trajectories — data](<https://github.com/jla-gardner/carbon-data/tree/main/results>) | Catalog official route |
| [ALIGNN Superconductor training](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ALIGNN_Sc.ipynb>) | JARVIS-Tools Notebooks |
| [ParsingWebpages(JARVIS_DFT)](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT>) | JARVIS-Tools Notebooks |
| [https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ParsingWebpages(JARVIS_DFT).ipynb>) | JARVIS-Tools Notebooks |
| [QMCPACK_Basic_Example](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/QMCPACK_Basic_Example.ipynb>) | JARVIS-Tools Notebooks |
| [Quantum computation and Qiskit based electronic bandstructure](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/Qiskit_based_electronic_bandstructure_latest_qiskit.ipynb>) | JARVIS-Tools Notebooks |
| [WTBH_MagneticMats.ipynb](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/WTBH_MagneticMats.ipynb>) | JARVIS-Tools Notebooks |
| [XRD Matching](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/XRD_Matching.ipynb>) | JARVIS-Tools Notebooks |
| [Open catalyst project load model](<https://github.com/knc6/jarvis-tools-notebooks/blob/master/jarvis-tools-notebooks/ocp_load_pretrained_models.ipynb>) | JARVIS-Tools Notebooks |
| [https://github.com/knc6/slides](<https://github.com/knc6/slides>) | JARVIS-Tools Notebooks |
| [SuperBand official repository](<https://github.com/ljcj007/SuperBand>) | Catalog evidence; Catalog official route |
| [ChemTable](<https://github.com/lqzxt/ChemTable>) | blaiszik/awesome-matchem-datasets |
| [Introduction](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/1-Introduction.ipynb>) | REMI: REsource for Materials Informatics |
| [Core Query Builder Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/2-Core_Query_Builder_Functions.ipynb>) | REMI: REsource for Materials Informatics |
| [General Helper Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/4-General_Helper_Functions.ipynb>) | REMI: REsource for Materials Informatics |
| [Field Specific Helper Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/5-Field-Specific_Helper_Functions.ipynb>) | REMI: REsource for Materials Informatics |
| [Data Retrieval Functions](<https://github.com/materials-data-facility/forge/blob/master/docs/tutorials/6-Data_Retrieval_Functions.ipynb>) | REMI: REsource for Materials Informatics |
| [Matbench jdft2d — code](<https://github.com/materialsproject/matbench>) | Catalog official route |
| [Matbench jdft2d — data](<https://github.com/materialsproject/matbench/tree/main/matbench>) | Catalog official route |
| [Materials Project elastic tensor release (2015) — code](<https://github.com/materialsproject/pymatgen>) | Catalog official route |
| [MPF.2021.2.8 — homepage](<https://github.com/materialsvirtuallab/m3gnet>) | Catalog official route |
| [How to extract or plot the NiO band structure from a VASP calculation using pymagen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Bandstructure%20of%20NiO.ipynb>) | REMI: REsource for Materials Informatics |
| [core functionality of pymatgen,including the core objects representing Elements,Species,Lattices,and Structures](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Basic%20functionality.ipynb>) | REMI: REsource for Materials Informatics |
| [calculate reaction energies using the Materials API and pymatgen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Calculating%20Reaction%20Energies%20with%20the%20Materials%20API.ipynb>) | REMI: REsource for Materials Informatics |
| [how to plot an XRD plot for the two polymorphs of CsCl ($Pm\overline{3}m$ and $Fm\overline{3}m$)](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Calculating%20XRD%20patterns.ipynb>) | REMI: REsource for Materials Informatics |
| [how to obtain an explaination of the different corrections being applied in the Materials Project](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Explanation%20of%20Corrections.ipynb>) | REMI: REsource for Materials Informatics |
| [Getting crystal structures from online sources](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Getting%20crystal%20structures%20from%20online%20sources.ipynb>) | REMI: REsource for Materials Informatics |
| [matgen's functionality in terms of creating and editing molecules,as well as its integration with OpenBabel](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Molecule.ipynb>) | REMI: REsource for Materials Informatics |
| [ordering of a disordered structure using pymatgen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Ordering%20Disordered%20Structures.ipynb>) | REMI: REsource for Materials Informatics |
| [Plotting and Analyzing a Phase Diagram using the Materials API](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Plotting%20and%20Analyzing%20a%20Phase%20Diagram%20using%20the%20Materials%20API.ipynb>) | REMI: REsource for Materials Informatics |
| [Plotting the electronic structure of Fe](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Plotting%20the%20electronic%20structure%20of%20Fe.ipynb>) | REMI: REsource for Materials Informatics |
| [Units](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2013-01-01-Units.ipynb>) | REMI: REsource for Materials Informatics |
| [Data-driven First Principles Methods for the Study and Design of Alkali Superionic Conductors Part 1 - Structure Generation](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-08-Data-driven%20First%20Principles%20Methods%20for%20the%20Study%20and%20Design%20of%20Alkali%20Superionic%20Conductors%20Part%201%20-%20Structure%20Generation.ipynb>) | REMI: REsource for Materials Informatics |
| [Data-driven First Principles Methods for the Study and Design of Alkali Superionic Conductors Part 2 - Phase and Electrochemical Stability](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-08-Data-driven%20First%20Principles%20Methods%20for%20the%20Study%20and%20Design%20of%20Alkali%20Superionic%20Conductors%20Part%202%20-%20Phase%20and%20Electrochemical%20Stability.ipynb>) | REMI: REsource for Materials Informatics |
| [Data-driven First Principles Methods for the Study and Design of Alkali Superionic Conductors Part 3 - Diffusivity and Ionic Conductivity](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-08-Data-driven%20First%20Principles%20Methods%20for%20the%20Study%20and%20Design%20of%20Alkali%20Superionic%20Conductors%20Part%203%20-%20Diffusivity%20and%20Ionic%20Conductivity.ipynb>) | REMI: REsource for Materials Informatics |
| [how to use the output from VASP DFPT calculation and the phonopy interface to plot the phonon bandstructure and density of states](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2016-09-25-Plotting%20phonon%20bandstructure%20and%20dos.ipynb>) | REMI: REsource for Materials Informatics |
| [how you can obtain various data from the Materials Project using pymatgen's interface to the Materials API](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-03-02-Getting%20data%20from%20Materials%20Project.ipynb>) | REMI: REsource for Materials Informatics |
| [Slab generation and Wulff shape](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-04-03-Slab%20generation%20and%20Wulff%20shape.ipynb>) | REMI: REsource for Materials Informatics |
| [Inputs and Analysis of VASP runs](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-04-14-Inputs%20and%20Analysis%20of%20VASP%20runs.ipynb>) | REMI: REsource for Materials Informatics |
| [Running Jupyter Notebook on clusters](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-05-11-Running%20Jupyter%20Notebook%20on%20clusters.ipynb>) | REMI: REsource for Materials Informatics |
| [Analyze and plot band structures](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-09-03-Analyze%20and%20plot%20band%20structures.ipynb>) | REMI: REsource for Materials Informatics |
| [Plotting a Pourbaix Diagram](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2017-12-15-Plotting%20a%20Pourbaix%20Diagram.ipynb>) | REMI: REsource for Materials Informatics |
| [ChemEnv - How to automatically identify coordination environments in a structure](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-01-01-ChemEnv%20-%20How%20to%20automatically%20identify%20coordination%20environments%20in%20a%20structure.ipynb>) | REMI: REsource for Materials Informatics |
| [Computing the Reaction Diagram between Two Compounds](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-03-09-Computing%20the%20Reaction%20Diagram%20between%20Two%20Compounds.ipynb>) | REMI: REsource for Materials Informatics |
| [Plotting COHP from LOBSTER](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-03-14-Plotting%20COHP%20from%20LOBSTER.ipynb>) | REMI: REsource for Materials Informatics |
| [Adsorption on solid surfaces](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-07-24-Adsorption%20on%20solid%20surfaces.ipynb>) | REMI: REsource for Materials Informatics |
| [Structure Prediction using Pymatgen and the Materials API](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-09-25-Structure%20Prediction%20using%20Pymatgen%20and%20the%20Materials%20API.ipynb>) | REMI: REsource for Materials Informatics |
| [Dopant suggestions using Pymatgen](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2018-11-6-Dopant%20suggestions%20using%20Pymatgen.ipynb>) | REMI: REsource for Materials Informatics |
| [How to use Boltztra2 interface](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2019-01-04-How%20to%20use%20Boltztra2%20interface.ipynb>) | REMI: REsource for Materials Informatics |
| [How to plot and evaluate output files from Lobster](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2019-01-11-How%20to%20plot%20and%20evaluate%20output%20files%20from%20Lobster.ipynb>) | REMI: REsource for Materials Informatics |
| [Interface Reactions](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2019-03-11-Interface%20Reactions.ipynb>) | REMI: REsource for Materials Informatics |
| [How to plot a Fermi surface](<https://github.com/materialsvirtuallab/matgenb/blob/master/notebooks/2020-07-15-How%20to%20plot%20a%20Fermi%20surface.ipynb>) | REMI: REsource for Materials Informatics |
| [How to plot a Fermi surface](<https://github.com/materialsvirtuallab/matgenb/tree/master/notebooks>) | REMI: REsource for Materials Informatics |
| [MatPES — code](<https://github.com/materialyzeai/matpes>) | Catalog evidence; Catalog official route |
| [ChemistryQA](<https://github.com/microsoft/chemistry-qa>) | blaiszik/awesome-matchem-datasets |
| [Alex-MP-20 (MatterGen) — code](<https://github.com/microsoft/mattergen>) | Catalog official route |
| [Alex-MP-20 (MatterGen) — data](<https://github.com/microsoft/mattergen/tree/main/data-release/alex-mp>) | Catalog official route |
| [MatterGen MP-20 reprocessed release](<https://github.com/microsoft/mattergen/tree/main/data-release/mp-20>) | Navigation resource |
| [MatterSim training data availability](<https://github.com/microsoft/mattersim/blob/main/MODEL_CARD.md>) | Navigation resource; Resource evidence |
| [Syntheseus](<https://github.com/microsoft/syntheseus>) | blaiszik/awesome-matchem-datasets |
| [MolecularIQ](<https://github.com/ml-jku/moleculariq>) | blaiszik/awesome-matchem-datasets |
| [CoRE MOF Database — code](<https://github.com/mtap-research/CoRE-MOF-Tools>) | Catalog official route |
| [Quantum-Chemical Bonding Database for Solid-State Materials (2023) — code](<https://github.com/naik-aakash/lobster-database-paper-analysis-scripts>) | Catalog official route |
| [Darcy-Flow (FNO)](<https://github.com/neuraloperator/neuraloperator>) | blaiszik/awesome-matchem-datasets |
| [ARROWS³ — source](<https://github.com/njszym/ARROWS>) | blaiszik/awesome-matchem-datasets |
| [AstraZeneca ELN Buchwald–Hartwig](<https://github.com/nsf-c-cas>) | blaiszik/awesome-matchem-datasets |
| [ChemDataExtractor thermoelectric materials database — code](<https://github.com/odysie/thermoelectricsdb>) | Catalog official route |
| [WeatherBench 2](<https://github.com/pangeo-data/WeatherBench>) | blaiszik/awesome-matchem-datasets |
| [PDEBench](<https://github.com/pdebench/PDEBench>) | blaiszik/awesome-matchem-datasets |
| [Phonix anharmonic phonon database — code](<https://github.com/phonix-db/auto-kappa>) | Catalog official route |
| [PhononDB lattice thermal conductivity (MDR) — code](<https://github.com/phonopy/phono3py>) | Catalog official route |
| [PhononDB / MDR harmonic phonon calculation database — code](<https://github.com/phonopy/phonopy>) | Catalog official route |
| [Static force spectroscopy simulation over a viscoelastic material](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/AFM_simulations/Force_Spectroscopy/Static_Force_Spectroscopy.ipynb>) | REMI: REsource for Materials Informatics |
| [Introduction to dynamic AFM simulations](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/AFM_simulations/IntroductionToSimulations/IntroToAFMSimulations.ipynb>) | REMI: REsource for Materials Informatics |
| [Dynamic atomic force microscopy simulations over a viscoelastic material](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/AFM_simulations/Multifrequency_Viscoelasticity/Simulation_SoftMatter.ipynb>) | REMI: REsource for Materials Informatics |
| [Band Excitation data processing](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/BE_Processing.ipynb>) | REMI: REsource for Materials Informatics |
| [Band Excitation & Contact Kelvin Probe Force Microscopy (cKPFM) data processing](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/BE_Processing_cKPFM.ipynb>) | REMI: REsource for Materials Informatics |
| [Band Excitation Relaxation Spectroscopy Data Processing](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/BE_Relaxation%20Processing.ipynb>) | REMI: REsource for Materials Informatics |
| [G-Mode KPFM with Fast Free Force Recovery (F3R)](<https://github.com/pycroscopy/pycroscopy/blob/master/jupyter_notebooks/GKPFM_base_notebook.ipynb>) | REMI: REsource for Materials Informatics |
| [NLR MatDB (formerly NRELMatDB) — code](<https://github.com/pylada/pylada-light>) | Catalog official route |
| [Multimodal Spectroscopic Dataset](<https://github.com/rxn4chemistry/multimodal-spectroscopic-dataset>) | blaiszik/awesome-matchem-datasets |
| [Pfizer Suzuki–Miyaura HTE](<https://github.com/rxn4chemistry/rxn_yields>) | blaiszik/awesome-matchem-datasets |
| [Minerva HTE](<https://github.com/schwallergroup/minerva>) | blaiszik/awesome-matchem-datasets |
| [SciAssess](<https://github.com/sci-assess/SciAssess>) | blaiszik/awesome-matchem-datasets |
| [Data Resources for Materials Science](<https://github.com/sedaoturak/data-resources-for-materials-science>) | Navigation resource; Requested collection; Resource evidence |
| [Solid-state synthesis recipes with impurity phases — code](<https://github.com/slee-lab/solid-state-recipes-with-impurity>) | Catalog official route |
| [mech-USPTO-31k — source](<https://github.com/snu-micc/MechFinder>) | blaiszik/awesome-matchem-datasets |
| [StarryData2](<https://github.com/starrydata/starrydata_datasets>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [Starrydata — Air Battery Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Air Battery Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Air Battery Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/AirBatteryMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Battery Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Battery Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Battery Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/BatteryMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Condensed Matter — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_curves.csv.gz>) | Catalog official route |
| [Starrydata — Condensed Matter — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_papers.csv.gz>) | Catalog official route |
| [Starrydata — Condensed Matter — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/CondensedMatter_samples.csv.gz>) | Catalog official route |
| [Starrydata — Dielectric Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Dielectric Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Dielectric Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/DielectricMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — General DB — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_curves.csv.gz>) | Catalog official route |
| [Starrydata — General DB — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_papers.csv.gz>) | Catalog official route |
| [Starrydata — General DB — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/GeneralDB_samples.csv.gz>) | Catalog official route |
| [Starrydata — High Thermal Conductivity Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — High Thermal Conductivity Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — High Thermal Conductivity Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/HighThermalConductivityMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Hypermaterial — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_curves.csv.gz>) | Catalog official route |
| [Starrydata — Hypermaterial — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_papers.csv.gz>) | Catalog official route |
| [Starrydata — Hypermaterial — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Hypermaterial_samples.csv.gz>) | Catalog official route |
| [Starrydata — Low Thermal Conductivity Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Low Thermal Conductivity Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Low Thermal Conductivity Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/LowThermalConductivityMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Magnetic Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Magnetic Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Magnetic Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/MagneticMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Organic Thermoelectric Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Organic Thermoelectric Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Organic Thermoelectric Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/OrganicThermoelectricMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Piezoelectric Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Piezoelectric Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Piezoelectric Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/PiezoelectricMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Resistor — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_curves.csv.gz>) | Catalog official route |
| [Starrydata — Resistor — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_papers.csv.gz>) | Catalog official route |
| [Starrydata — Resistor — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/Resistor_samples.csv.gz>) | Catalog official route |
| [Starrydata — Solid State Battery Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Solid State Battery Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Solid State Battery Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/SolidStateBatteryMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata — Thermoelectric Materials — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_curves.csv.gz>) | Catalog official route |
| [Starrydata — Thermoelectric Materials — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_papers.csv.gz>) | Catalog official route |
| [Starrydata — Thermoelectric Materials — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/ThermoelectricMaterials_samples.csv.gz>) | Catalog official route |
| [Starrydata2 experimental materials datasets — curves](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_curves.csv.gz>) | Catalog official route |
| [Starrydata2 experimental materials datasets — papers](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_papers.csv.gz>) | Catalog official route |
| [Starrydata2 experimental materials datasets — samples](<https://github.com/starrydata/starrydata_datasets/releases/download/latest/all_samples.csv.gz>) | Catalog official route |
| [Starrydata — Resistor — data](<https://github.com/starrydata/starrydata_datasets/releases/tag/latest>) | Catalog official route |
| [sysTEm](<https://github.com/tankylz/sysTEm_dataset>) | sedaoturak/data-resources-for-materials-science |
| [Awesome Materials Informatics](<https://github.com/tilde-lab/awesome-materials-informatics>) | blaiszik/awesome-matchem-datasets |
| [MP-20 (CDVAE benchmark) — code](<https://github.com/txie-93/cdvae>) | Catalog official route |
| [Carbon-24 (CDVAE benchmark) — data](<https://github.com/txie-93/cdvae/tree/main/data/carbon_24>) | Catalog official route |
| [MP-20 (CDVAE benchmark) — data](<https://github.com/txie-93/cdvae/tree/main/data/mp_20>) | Catalog official route |
| [Perov-5 / Matbench perovskites — data](<https://github.com/txie-93/cdvae/tree/main/data/perov_5>) | Catalog official route |
| [ab initio REPEAT Charge MOF Database (ARC-MOF) — code](<https://github.com/uowoolab>) | Catalog official route |
| [MOSAEC MOF Database (MOSAEC-DB) — code](<https://github.com/uowoolab/MOSAEC-DB>) | Catalog official route |
| [https://github.com/usnistgov/aims2024_workshop](<https://github.com/usnistgov/aims2024_workshop>) | JARVIS-Tools Notebooks |
| [ALIGNN-FF training dataset — homepage](<https://github.com/usnistgov/alignn>) | Catalog official route |
| [JARVIS-DFT 3D — code](<https://github.com/usnistgov/jarvis>) | Catalog official route |
| [Code of conduct](<https://github.com/usnistgov/jarvis/blob/master/CODE_OF_CONDUCT.md>) | JARVIS-Tools Notebooks |
| [Contribution instructions](<https://github.com/usnistgov/jarvis/blob/master/Contribution.rst>) | JARVIS-Tools Notebooks |
| [NIST License](<https://github.com/usnistgov/jarvis/blob/master/LICENSE.rst>) | JARVIS-Tools Notebooks |
| [ALIGNN-FF training dataset — data](<https://github.com/usnistgov/jarvis/blob/master/jarvis/db/figshare.py>) | Catalog evidence; Catalog official route |
| [issue](<https://github.com/usnistgov/remi/issues>) | REMI: REsource for Materials Informatics |
| [Fe-Co-Ni](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni>) | Catalog evidence; Catalog official route; REMI: REsource for Materials Informatics |
| [Fe-Ga-Pd](<https://github.com/usnistgov/remi/tree/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd>) | Catalog evidence; Catalog official route; REMI: REsource for Materials Informatics |
| [MAST-ML toolkit](<https://github.com/uw-cmg/MAST-ML>) | Machine Learning Materials Datasets / MAST-ML education |
| [OpenQDC Hub](<https://github.com/valence-labs/openQDC>) | blaiszik/awesome-matchem-datasets |
| [AM26](<https://github.com/vldgroup/AM26>) | sedaoturak/data-resources-for-materials-science |
| [PDBench](<https://github.com/wells-wood-research/PDBench>) | blaiszik/awesome-matchem-datasets |
| [Bayesian Optimization and Regression Analysis for Ferromagnetic Materials](<https://github.com/will-colea/BO_Magnetics>) | REMI: REsource for Materials Informatics |
| [repository commit history](<https://github.com/your-repo/commits>) | blaiszik/awesome-matchem-datasets |
| [matminer dataset summary](<https://hackingmaterials.lbl.gov/matminer/dataset_summary.html>) | Resource evidence |
| [Van der Waals 2D Heterostructure Database (HetDB)](<https://hetdb.fysik.dtu.dk/>) | blaiszik/awesome-matchem-datasets |
| [NASA High Lift Prediction Workshop (HLPW)](<https://hiliftpw.larc.nasa.gov/>) | blaiszik/awesome-matchem-datasets |
| [Wilmer hypothetical MOF database (hMOF) — homepage](<http://hmofs.northwestern.edu/>) | Catalog official route |
| [HTEM-DB](<https://htem.nrel.gov>) | blaiszik/awesome-matchem-datasets |
| [High Throughput Experimental Materials Database (HTEM DB)](<https://htem.nrel.gov/>) | Catalog official route; sedaoturak/data-resources-for-materials-science |
| [MegaScience](<https://huggingface.co/MegaScience>) | blaiszik/awesome-matchem-datasets |
| [STEM Bank 26](<https://huggingface.co/buckets/ghollyer/STEM-Bank-26>) | sedaoturak/data-resources-for-materials-science |
| [SCQA (Solar Cell QA)](<https://huggingface.co/collections/CambridgeMolecularEngineering/solar-cell-qa-datasets-67b398f1b9c0f0dd7600a159>) | blaiszik/awesome-matchem-datasets |
| [ChemPile](<https://huggingface.co/collections/jablonkagroup/chempile-6824e88c60d3286ba9b0dae1>) | blaiszik/awesome-matchem-datasets |
| [Mol-Instructions](<https://huggingface.co/collections/zjunlp/mol-instructions-662e0b9435ab6df9593e8ea0>) | blaiszik/awesome-matchem-datasets |
| [ChemBench 4K](<https://huggingface.co/datasets/AI4Chem/ChemBench4K>) | blaiszik/awesome-matchem-datasets |
| [ChemData 700K](<https://huggingface.co/datasets/AI4Chem/ChemData700K>) | blaiszik/awesome-matchem-datasets |
| [MateriaViva Open — homepage](<https://huggingface.co/datasets/AI4QC/MateriaViva-Open>) | Catalog evidence; Catalog official route |
| [AgentFEM Controlled Transient Heat](<https://huggingface.co/datasets/HaomingLuo/AgentFEM-Controlled-Transient-Heat>) | blaiszik/awesome-matchem-datasets |
| [AgentFEM Material Loading Memory](<https://huggingface.co/datasets/HaomingLuo/AgentFEM-Material-Loading-Memory>) | blaiszik/awesome-matchem-datasets |
| [LeMaterial Atompack](<https://huggingface.co/datasets/LeMaterial/Atompack>) | Navigation resource; Resource evidence |
| [LeMat-Bulk](<https://huggingface.co/datasets/LeMaterial/LeMat-Bulk>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [LeMat-BulkUnique — homepage](<https://huggingface.co/datasets/LeMaterial/LeMat-BulkUnique>) | Catalog evidence; Catalog official route |
| [LeMat-Rho — homepage](<https://huggingface.co/datasets/LeMaterial/LeMat-Rho>) | Catalog evidence; Catalog official route |
| [LeMat-Synth synthesis-procedure corpus — data](<https://huggingface.co/datasets/LeMaterial/LeMat-Synth>) | Catalog official route |
| [LeMat-Traj](<https://huggingface.co/datasets/LeMaterial/LeMat-Traj>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [MatSyn25](<https://huggingface.co/datasets/MatSynAI/MatSyn25>) | Catalog official route; blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [MatSyn25 provider data card](<https://huggingface.co/datasets/MatSynAI/MatSyn25/raw/main/README.md>) | Catalog evidence |
| [ChemCoTBench](<https://huggingface.co/datasets/OpenMol/ChemCoTDataset>) | blaiszik/awesome-matchem-datasets |
| [AQCat25](<https://huggingface.co/datasets/SandboxAQ/aqcat25-dataset>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [BioInstruct 25K](<https://huggingface.co/datasets/bio-nlp-umass/bioinstruct>) | blaiszik/awesome-matchem-datasets |
| [MolOpt-Instructions](<https://huggingface.co/datasets/blazerye/MolOpt-Instructions>) | blaiszik/awesome-matchem-datasets |
| [CAMEL](<https://huggingface.co/datasets/camel-ai/chemistry>) | blaiszik/awesome-matchem-datasets |
| [OPoly26 (Open Polymers 2026)](<https://huggingface.co/datasets/colabfit/OPoly26-train>) | blaiszik/awesome-matchem-datasets |
| [PubChemQCR](<https://huggingface.co/datasets/divelab/PubChemQCR>) | blaiszik/awesome-matchem-datasets |
| [Open Materials 2024 (OMat24) — data](<https://huggingface.co/datasets/facebook/OMAT24>) | Catalog evidence; Catalog official route |
| [Open Molecular Crystals 2025 (OMC25) — data](<https://huggingface.co/datasets/facebook/OMC25>) | Catalog official route |
| [OMC25 official dataset card](<https://huggingface.co/datasets/facebook/OMC25/blob/main/README.md>) | Catalog evidence |
| [OMat24 (Meta)](<https://huggingface.co/datasets/fairchem/OMAT24>) | blaiszik/awesome-matchem-datasets |
| [Lab-Bench](<https://huggingface.co/datasets/futurehouse/lab-bench>) | blaiszik/awesome-matchem-datasets |
| [MoleculeQA](<https://huggingface.co/datasets/hcaoaf/MoleculeQA>) | blaiszik/awesome-matchem-datasets |
| [Open Materials Guide (OMG)](<https://huggingface.co/datasets/iknow-lab/open-materials-guide-2024>) | blaiszik/awesome-matchem-datasets |
| [ELEMENTA Spin — homepage](<https://huggingface.co/datasets/kairosmaterial/ELEMENTA>) | Catalog evidence; Catalog official route |
| [MolTextNet](<https://huggingface.co/datasets/liuganghuggingface/moltextnet>) | blaiszik/awesome-matchem-datasets |
| [MatPES — data](<https://huggingface.co/datasets/materialyze/matpes>) | Catalog official route |
| [MatText](<https://huggingface.co/datasets/n0w0f/MatText>) | blaiszik/awesome-matchem-datasets |
| [SmolInstruct](<https://huggingface.co/datasets/osunlp/SMolInstruct>) | blaiszik/awesome-matchem-datasets |
| [PMC Open Access Subset](<https://huggingface.co/datasets/pmc/open_access>) | blaiszik/awesome-matchem-datasets |
| [OC25 (Open Catalyst 2025)](<https://huggingface.co/facebook/OC25>) | Catalog official route; blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [Open Direct Air Capture 2025 (ODAC25) — data](<https://huggingface.co/facebook/ODAC25>) | Catalog official route |
| [ODAC25 official access page](<https://huggingface.co/facebook/ODAC25/tree/main>) | Catalog evidence |
| [OMC25](<https://huggingface.co/facebook/OMC25>) | blaiszik/awesome-matchem-datasets |
| [OMol25 (Meta)](<https://huggingface.co/facebook/OMol25>) | blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [OPoly26](<https://huggingface.co/facebook/OMol25#open-polymers-2026-opoly26-dataset>) | sedaoturak/data-resources-for-materials-science |
| [Microsoft MatterGen data summary card](<https://huggingface.co/microsoft/mattergen/blob/main/data_summary_card.md>) | Catalog evidence |
| [PDEArena (collection)](<https://huggingface.co/pdearena>) | blaiszik/awesome-matchem-datasets |
| [MolecularIQ — source](<https://huggingface.co/spaces/ml-jku/molecularIQ_leaderboard>) | blaiszik/awesome-matchem-datasets |
| [Inorganic Crystal Structure Database (ICSD) — data](<https://icsd.fiz-karlsruhe.de/>) | Catalog official route |
| [NIST ICSD (subset)](<https://icsd.products.fiz-karlsruhe.de>) | blaiszik/awesome-matchem-datasets |
| [ICSD home](<https://icsd.products.fiz-karlsruhe.de/en>) | Catalog evidence; Catalog official route |
| [About ICSD](<https://icsd.products.fiz-karlsruhe.de/en/about/about-icsd>) | Catalog evidence |
| [ICSD products](<https://icsd.products.fiz-karlsruhe.de/en/products/icsd-products>) | Catalog evidence |
| [various other publications](<https://jarvis-tools.readthedocs.io/en/master/publications.html>) | JARVIS-Tools Notebooks |
| [JARVIS-Tools](<https://jarvis-tools.readthedocs.io/en/master/tutorials.html>) | JARVIS-Tools Notebooks |
| [NIST-AIMS workshop](<http://jarvis.nist.gov/events/aims>) | JARVIS-Tools Notebooks |
| [JARVIS-DFT (NIST)](<https://jarvis.nist.gov>) | blaiszik/awesome-matchem-datasets |
| [NIST-JARVIS](<https://jarvis.nist.gov/>) | Catalog official route; JARVIS-Tools Notebooks; REMI: REsource for Materials Informatics; sedaoturak/data-resources-for-materials-science |
| [More info](<https://jarvis.nist.gov/events/aims>) | JARVIS-Tools Notebooks |
| [More info](<https://jarvis.nist.gov/events/school>) | JARVIS-Tools Notebooks |
| [JARVIS superconductivity 2D DFT cohort — homepage](<https://jarvis.nist.gov/supercon>) | Catalog official route |
| [Frustrated Lewis Pairs Database](<https://jingyun-ye.github.io/FLPDB/>) | blaiszik/awesome-matchem-datasets |
| [ROD primary descriptor](<https://journals.iucr.org/j/issues/2019/03/00/nb5236/>) | Catalog evidence; Catalog official route |
| [Pluto Notebooks](<https://juliahub.com/docs/Pluto/OJqMt/0.7.4/>) | REMI: REsource for Materials Informatics |
| [List of Tutorials](<https://julialang.org/learning/tutorials/>) | REMI: REsource for Materials Informatics |
| [Polymer Genome](<https://khazana.gatech.edu/dataset/>) | blaiszik/awesome-matchem-datasets |
| [LeMat-Synth official overview](<https://lematerial.org/lemat-synth/overview/>) | Catalog evidence; Catalog official route |
| [DigHyd author descriptor](<https://link.springer.com/article/10.1007/s00339-026-09903-6>) | Catalog evidence; Catalog official route |
| [MaCBench](<https://macbench.lamalab.org>) | blaiszik/awesome-matchem-datasets |
| [More info](<https://march.aps.org/events/tutorial-graph-neural-networks>) | JARVIS-Tools Notebooks |
| [NIMS MatDaCs](<https://mat-dacs.dxmt.nims.go.jp/en/>) | Navigation resource |
| [NIMS MatDaCs: AtomWork-Adv](<https://mat-dacs.dxmt.nims.go.jp/en/list/316>) | Resource evidence |
| [NIMS MatDaCs: COD](<https://mat-dacs.dxmt.nims.go.jp/en/list/350>) | Resource evidence |
| [WBM / Matbench Discovery stability test set — homepage](<https://matbench-discovery.materialsproject.org/>) | Catalog official route |
| [Matbench Discovery](<https://matbench-discovery.materialsproject.org/data>) | blaiszik/awesome-matchem-datasets |
| [Matbench Discovery data sets](<https://matbench-discovery.materialsproject.org/data/sets>) | Navigation resource |
| [Matbench v0.1](<https://matbench.materialsproject.org/>) | Catalog official route; Navigation resource; blaiszik/awesome-matchem-datasets |
| [ColabFit Exchange](<https://materials.colabfit.org/>) | Navigation resource; Resource evidence |
| [NLR MatDB official portal](<https://materials.nlr.gov/>) | Catalog evidence; Catalog official route |
| [NLR MatDB help](<https://materials.nlr.gov/help>) | Catalog evidence |
| [NRELMatDB](<https://materials.nrel.gov/>) | sedaoturak/data-resources-for-materials-science |
| [Materials Resource Registery](<https://materials.registry.nist.gov/>) | REMI: REsource for Materials Informatics |
| [NIST Materials Resource Registry](<https://materials.registry.nist.gov/explore/keyword/>) | sedaoturak/data-resources-for-materials-science |
| [SpringerMaterials](<https://materials.springer.com/>) | Navigation resource; sedaoturak/data-resources-for-materials-science |
| [CURATED covalent organic frameworks — homepage](<https://materialscloud-org.github.io/mc-frontend/discover/curated-cofs>) | Catalog official route |
| [Materials Commons](<https://materialscommons.org/>) | sedaoturak/data-resources-for-materials-science |
| [NIST Materials Data Repository](<https://materialsdata.nist.gov/>) | Navigation resource; Resource evidence; sedaoturak/data-resources-for-materials-science |
| [UHCSDB (Ultra-High Carbon Steel Micrograph DB) — source](<https://materialsdata.nist.gov/handle/11256/940>) | blaiszik/awesome-matchem-datasets |
| [Materials Data Facility](<https://materialsdatafacility.org/>) | Navigation resource; Resource evidence; sedaoturak/data-resources-for-materials-science |
| [Foundry-ML](<https://materialsdatafacility.org/portal>) | blaiszik/awesome-matchem-datasets |
| [Materials Project (LBL)](<https://materialsproject.org>) | blaiszik/awesome-matchem-datasets |
| [Materials Project](<https://materialsproject.org/>) | Catalog official route; REMI: REsource for Materials Informatics; sedaoturak/data-resources-for-materials-science |
| [Matmatch](<https://matmatch.com/>) | sedaoturak/data-resources-for-materials-science |
| [MatPES](<https://matpes.ai>) | blaiszik/awesome-matchem-datasets |
| [MatPES](<https://matpes.ai/>) | Catalog official route; sedaoturak/data-resources-for-materials-science |
| [MatScholar](<https://matscholar.com>) | blaiszik/awesome-matchem-datasets |
| [Materials Cloud Two-Dimensional Structure Database (MC2D) — homepage](<https://mc2d.materialscloud.org/>) | Catalog official route |
| [Materials Data Curation System](<https://mdcs.nist.gov/>) | REMI: REsource for Materials Informatics |
| [MDR NIMS Materials Data Repository](<https://mdr.nims.go.jp/>) | sedaoturak/data-resources-for-materials-science |
| [MDR SuperCon](<https://mdr.nims.go.jp/collections/4c428a0c-d209-4990-ad1f-656d05d1cfe2>) | blaiszik/awesome-matchem-datasets |
| [MDR XAFS DB collection](<https://mdr.nims.go.jp/collections/a0f3fbf1-f94a-4be7-8a66-6b91a24f6b54>) | Catalog evidence; Catalog official route |
| [MDR phonon calculation database](<https://mdr.nims.go.jp/collections/d7aab932-8512-4b9a-b93d-b61f6e5e7019?locale=en>) | Catalog evidence; Catalog official route |
| [Lattice thermal conductivity calculation datasets for 103 binary compounds by finite displacement method](<https://mdr.nims.go.jp/collections/e85f8f40-d810-42ae-91c4-0a07b9641219?locale=en>) | Catalog evidence |
| [MDR SuperCon Datasheet Ver.240322](<https://mdr.nims.go.jp/datasets/650c4826-f0ca-42e8-8dd9-94025a5307ce?locale=ja>) | Catalog evidence |
| [NIMS MatNavi](<https://mits.nims.go.jp/en/>) | Catalog evidence; Catalog official route; Navigation resource; Resource evidence; sedaoturak/data-resources-for-materials-science |
| [OpenDataScience Open Machine Learning Course](<https://mlcourse.ai/>) | REMI: REsource for Materials Informatics |
| [MOFX-DB](<https://mof.tech.northwestern.edu/>) | Navigation resource |
| [BACE](<http://moleculenet.org/>) | blaiszik/awesome-matchem-datasets |
| [MPDS](<https://mpds.io>) | sedaoturak/data-resources-for-materials-science |
| [MPDS provider home](<https://mpds.io/>) | Catalog evidence; Catalog official route |
| [Materials Platform for Data Science (MPDS / PAULING FILE) — data](<https://mpds.io/#start>) | Catalog official route |
| [Materials Platform for Data Science (MPDS / PAULING FILE) — code](<https://mpds.io/developer/>) | Catalog official route |
| [MPDS introduction](<https://mpds.io/tutorial/>) | Catalog evidence |
| [Quantum Cluster Database](<https://muellergroup.jhu.edu/qcd/>) | blaiszik/awesome-matchem-datasets |
| [Deem PCOD author download page](<https://mwdeem.org/PCOD/index.html>) | Catalog evidence; Catalog official route |
| [https://nanohub.org/FAIR_workshop_2024](<https://nanohub.org/FAIR_workshop_2024>) | JARVIS-Tools Notebooks |
| [nanoHUB](<https://nanohub.org/publications/datasets>) | sedaoturak/data-resources-for-materials-science |
| [BibTex](<https://nanohub.org/resources/32730/citation?citationFormat=bibtex&no_html=1&rev=36>) | nanoHUB Machine Learning Lab Module |
| [EndNote](<https://nanohub.org/resources/32730/citation?citationFormat=endnote&no_html=1&rev=36>) | nanoHUB Machine Learning Lab Module |
| [Module_1_-_Machine_Learning_Basics_in_Materials_Science.pptx](<https://nanohub.org/resources/34383/download/Module_1_-_Machine_Learning_Basics_in_Materials_Science.pptx>) | nanoHUB Machine Learning Lab Module |
| [Module_2_-_Data_Cleaning_and_Featurizing.pptx](<https://nanohub.org/resources/34384/download/Module_2_-_Data_Cleaning_and_Featurizing.pptx>) | nanoHUB Machine Learning Lab Module |
| [Module_3_-_Model_Assessment_Optimization_Predictions.pptx](<https://nanohub.org/resources/34385/download/Module_3_-_Model_Assessment_Optimization_Predictions.pptx>) | nanoHUB Machine Learning Lab Module |
| [Module_4_-_Machine_Learning_Tools_for_Materials_Science.pptx](<https://nanohub.org/resources/34386/download/Module_4_-_Machine_Learning_Tools_for_Materials_Science.pptx>) | nanoHUB Machine Learning Lab Module |
| [Module_5_-_Machine_Learning_Tools_for_Materials_Science.pptx](<https://nanohub.org/resources/34387/download/Module_5_-_Machine_Learning_Tools_for_Materials_Science.pptx>) | nanoHUB Machine Learning Lab Module |
| [Reading_List.docx](<https://nanohub.org/resources/34388/download/Reading_List.docx>) | nanoHUB Machine Learning Lab Module |
| [Quiz_Questions.docx](<https://nanohub.org/resources/34389/download/Quiz_Questions.docx>) | nanoHUB Machine Learning Lab Module |
| [Quiz_Questions_-_Answers.docx](<https://nanohub.org/resources/34390/download/Quiz_Questions_-_Answers.docx>) | nanoHUB Machine Learning Lab Module |
| [Teachers_Guide.docx](<https://nanohub.org/resources/34391/download/Teachers_Guide.docx>) | nanoHUB Machine Learning Lab Module |
| [Machine Learning Lab Module](<https://nanohub.org/resources/intromllab>) | Collection evidence; nanoHUB Machine Learning Lab Module |
| [About : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/about>) | nanoHUB Machine Learning Lab Module |
| [cite this](<https://nanohub.org/resources/intromllab/about#citethis>) | nanoHUB Machine Learning Lab Module |
| [0 Citation(s)](<https://nanohub.org/resources/intromllab/citations>) | nanoHUB Machine Learning Lab Module |
| [3 questions](<https://nanohub.org/resources/intromllab/questions>) | nanoHUB Machine Learning Lab Module |
| [Ask a question](<https://nanohub.org/resources/intromllab/questions?action=new>) | nanoHUB Machine Learning Lab Module |
| [0 review(s)](<https://nanohub.org/resources/intromllab/reviews>) | nanoHUB Machine Learning Lab Module |
| [Review this](<https://nanohub.org/resources/intromllab/reviews?action=addreview#commentform>) | nanoHUB Machine Learning Lab Module |
| [Supporting Docs list](<https://nanohub.org/resources/intromllab/supportingdocs>) | Collection evidence; nanoHUB Machine Learning Lab Module |
| [1893 users (currently updating)](<https://nanohub.org/resources/intromllab/usage>) | nanoHUB Machine Learning Lab Module |
| [Versions : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/versions>) | nanoHUB Machine Learning Lab Module |
| [Wishlist : Machine Learning Lab Module](<https://nanohub.org/resources/intromllab/wishlist>) | nanoHUB Machine Learning Lab Module |
| [license](<https://nanohub.org/resources/license?tool=intromllab_r36&tmpl=component>) | Collection evidence; Resource evidence; nanoHUB Machine Learning Lab Module |
| [download](<https://nanohub.org/resources/sourcecode?tool=intromllab_r36>) | nanoHUB Machine Learning Lab Module |
| [Public module page](<https://nanohub.org/tools/intromllab>) | Collection evidence; Navigation resource; Requested collection; Resource evidence; sedaoturak/data-resources-for-materials-science |
| [plot representation quadrics for some rank 2 tensors](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_10_principal_directions_and_representation_quadrics/Representation_quadrics.ipynb>) | REMI: REsource for Materials Informatics |
| [plot an XRD plot for the two polymorphs of CsCl (Pm3¯¯¯m and Fm3¯¯¯m) by computing the structure factors](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_13_xrd/XRD%20CsCl.ipynb>) | REMI: REsource for Materials Informatics |
| [NANO106 - Symmetry Computations on m3¯¯¯m (Oh) Point Group](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_4_point_group_symmetry/Symmetry%20Computations%20on%20m-3m%20%28O_h%29%20Point%20Group.ipynb>) | REMI: REsource for Materials Informatics |
| [NANO106 - Symmetry Computations on mmm(D2h) Point Group](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_4_point_group_symmetry/Symmetry%20Computations%20on%20mmm%20%28D_2h%29%20Point%20Group.ipynb>) | REMI: REsource for Materials Informatics |
| [Using pymatgen to mine the Materials Project](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/blob/master/lectures/lecture_5_the_230_space_groups/Datamining%20the%20Materials%20Project%20for%20Space%20Group%20statistics.ipynb>) | REMI: REsource for Materials Informatics |
| [plot an XRD plot for the two polymorphs of CsCl (Pm3¯¯¯m and Fm3¯¯¯m) by computing the structure factors](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/tree/master/lectures/lecture_13_xrd/>) | REMI: REsource for Materials Informatics |
| [NANO106 - Symmetry Computations on mmm(D2h) Point Group](<https://nbviewer.jupyter.org/github/materialsvirtuallab/nano106/tree/master/lectures/lecture_4_point_group_symmetry/>) | REMI: REsource for Materials Informatics |
| [Metallic_Glass_Forming_with_features.csv](<https://ndownloader.figshare.com/files/12978419>) | Collection evidence; Machine Learning Materials Datasets / MAST-ML education |
| [Official perovskite educational CSV](<https://ndownloader.figshare.com/files/12978425>) | Catalog evidence; Catalog official route; Collection evidence; Machine Learning Materials Datasets / MAST-ML education |
| [Official diffusion educational CSV](<https://ndownloader.figshare.com/files/13007075>) | Catalog evidence; Catalog official route; Collection evidence; Machine Learning Materials Datasets / MAST-ML education |
| [README.txt](<https://ndownloader.figshare.com/files/13008500>) | Catalog evidence; Collection evidence; Collection provenance; Machine Learning Materials Datasets / MAST-ML education; Resource evidence |
| [2DMatPedia official JSONL data](<https://ndownloader.figshare.com/files/14399918>) | Catalog evidence |
| [Official JARVIS 2D payload](<https://ndownloader.figshare.com/files/38521268>) | Catalog evidence |
| [NOMAD Repository and Archive](<https://nomad-lab.eu/>) | Navigation resource |
| [notebooks](<https://nomad-lab.eu/aitoolkit>) | sedaoturak/data-resources-for-materials-science |
| [The Novel Materials Discovery (NOMAD) Laboratory](<https://nomad-lab.eu/index.php?page=repo-arch>) | sedaoturak/data-resources-for-materials-science |
| [NOMAD](<https://nomad-lab.eu/prod/v1/gui/search/entries/search/entries>) | blaiszik/awesome-matchem-datasets |
| [Perovskite Database Project](<https://nomad-lab.eu/prod/v1/gui/search/perovskite-solar-cells-database>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [OMDB-GAP1 — homepage](<https://omdb.mathub.io/>) | Catalog official route; sedaoturak/data-resources-for-materials-science |
| [OMDB-GAP1 — data](<https://omdb.mathub.io/dataset/>) | Catalog evidence; Catalog official route |
| [OpenDAC](<https://open-dac.github.io/>) | Catalog official route; sedaoturak/data-resources-for-materials-science |
| [Open Reaction Database (ORD)](<https://open-reaction-database.org>) | blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [OpenBind (first release)](<https://openbind.uk>) | blaiszik/awesome-matchem-datasets |
| [Open Catalyst 2020 (OC20)](<https://opencatalystproject.org>) | blaiszik/awesome-matchem-datasets |
| [Open Catalyst 2020 (OC20) — homepage](<https://opencatalystproject.org/>) | Catalog official route |
| [Knowledgebase of Interatomic Models (OpenKIM)](<https://openkim.org/>) | sedaoturak/data-resources-for-materials-science |
| [OQMD: Open Quantum Materials Database](<http://oqmd.org/>) | REMI: REsource for Materials Informatics; sedaoturak/data-resources-for-materials-science |
| [OQMD](<https://oqmd.org>) | blaiszik/awesome-matchem-datasets |
| [OQMD — homepage](<https://oqmd.org/>) | Catalog evidence; Catalog official route |
| [OQMD — data](<https://oqmd.org/download/>) | Catalog official route |
| [OpenExp](<https://osf.io/e68v4/files/3dv4k>) | blaiszik/awesome-matchem-datasets |
| [JARVIS data registry](<https://pages.nist.gov/jarvis/databases/>) | Catalog evidence; Catalog official route |
| [REMI public homepage](<https://pages.nist.gov/remi/>) | Collection evidence; Navigation resource; Requested collection; sedaoturak/data-resources-for-materials-science |
| [Open Access Data](<https://pages.nist.gov/remi/data/>) | Catalog official route; REMI: REsource for Materials Informatics |
| [Learning Resources](<https://pages.nist.gov/remi/learn/>) | REMI: REsource for Materials Informatics |
| [Pauling File](<https://paulingfile.com/>) | sedaoturak/data-resources-for-materials-science |
| [NIST Materials Data Curation System (Part of MGI)](<https://phasedata.nist.gov/>) | sedaoturak/data-resources-for-materials-science |
| [Phonix official database documentation](<https://phonix-db.org/>) | Catalog evidence; Catalog official route |
| [Phonix v2026.03.28 release statistics](<https://phonix-db.org/ver2026.03.28/index.html>) | Catalog evidence; Catalog official route |
| [Density of States](<https://plotly.com/python/v3/ipython-notebooks/density-of-states/>) | REMI: REsource for Materials Informatics |
| [A comprehensive data network for data-driven study of battery materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC11573338/>) | Catalog evidence |
| [SuperBand: an Electronic-band and Fermi surface structure database of superconductors](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12056090/>) | Catalog evidence |
| [OMC25 Scientific Data descriptor](<https://pmc.ncbi.nlm.nih.gov/articles/PMC12979844/>) | Catalog evidence |
| [Charting the complete elastic properties of inorganic crystalline compounds](<https://pmc.ncbi.nlm.nih.gov/articles/PMC4432655/>) | Catalog evidence |
| [A database to enable discovery and design of piezoelectric materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC4587372/>) | Catalog evidence |
| [High-throughput screening of inorganic compounds for the discovery of novel dielectric and optical materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC5315501/>) | Catalog evidence |
| [An ab initio electronic transport database for inorganic materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC5496472/>) | Catalog evidence |
| [High-throughput density-functional perturbation theory phonons for inorganic materials](<https://pmc.ncbi.nlm.nih.gov/articles/PMC5928854/>) | Catalog evidence |
| [Catalysis-Hub primary data descriptor](<https://pmc.ncbi.nlm.nih.gov/articles/PMC6538711/>) | Resource evidence |
| [Polyinfo](<https://polymer.nims.go.jp/>) | sedaoturak/data-resources-for-materials-science |
| [PoLyInfo](<https://polymer.nims.go.jp/en/>) | blaiszik/awesome-matchem-datasets |
| [Polymer Scholar](<https://polymerscholar.org/>) | sedaoturak/data-resources-for-materials-science |
| [Polymer Property Predictor and Database](<https://pppdb.uchicago.edu/>) | sedaoturak/data-resources-for-materials-science |
| [SAIR](<https://pub.sandboxaq.com/data/ic50-dataset>) | blaiszik/awesome-matchem-datasets |
| [PubChem](<https://pubchem.ncbi.nlm.nih.gov>) | blaiszik/awesome-matchem-datasets |
| [PCBA](<https://pubchem.ncbi.nlm.nih.gov/bioassay>) | blaiszik/awesome-matchem-datasets |
| [Author abstract of 2024 X23 DMC paper](<https://pubmed.ncbi.nlm.nih.gov/39121404/>) | Catalog evidence |
| [CoRE MOF 2019](<https://pubs.acs.org/doi/10.1021/acs.jced.9b00835>) | blaiszik/awesome-matchem-datasets |
| [Computational Single-Atom Catalyst Database primary article](<https://pubs.acs.org/doi/10.1021/acs.jpcc.5c00491>) | Catalog evidence |
| [Python for Glass Genomics (PyGGi)](<https://pyggi.iitd.ac.in/>) | sedaoturak/data-resources-for-materials-science |
| [ANI-1x / 1ccx](<https://qcawebapps.molssi.org/ml_datasets/>) | blaiszik/awesome-matchem-datasets |
| [Quantum Point Defects Database (QPOD)](<https://qpod.fysik.dtu.dk/>) | blaiszik/awesome-matchem-datasets |
| [QM9](<http://quantum-machine.org/datasets/>) | blaiszik/awesome-matchem-datasets |
| [Requested notebook README](<https://raw.githubusercontent.com/JARVIS-Materials-Design/jarvis-tools-notebooks/master/README.md>) | Collection evidence; Collection provenance; Resource evidence |
| [LeMat-GenBench official README](<https://raw.githubusercontent.com/LeMaterial/lemat-genbench/main/README.md>) | Resource evidence |
| [Successor JARVIS notebook README](<https://raw.githubusercontent.com/atomgptlab/jarvis-tools-notebooks/master/README.md>) | Collection evidence |
| [Phonondb lattice thermal conductivity data on MDR at NIMS](<https://raw.githubusercontent.com/atztogo/phonondb/main/mdr/phonondb_LTC/README.md>) | Catalog evidence |
| [blaiszik/awesome-matchem-datasets README](<https://raw.githubusercontent.com/blaiszik/awesome-matchem-datasets/d3b1d551eb6abcfd2ea62bcd75ac18c9471900c8/README.md>) | Collection evidence; Collection provenance |
| [CoRE COF v7 archive](<https://raw.githubusercontent.com/core-cof/CoRE-COF-Database/master/CoRE-COFs_DT1242-v7.0.zip>) | Catalog evidence |
| [ZeoSyn repository licence](<https://raw.githubusercontent.com/eltonpan/zeosyn_dataset/master/LICENSE>) | Catalog evidence |
| [ZeoSyn author README](<https://raw.githubusercontent.com/eltonpan/zeosyn_dataset/master/README.md>) | Catalog evidence |
| [OCx24 pinned raw experimental CSV](<https://raw.githubusercontent.com/facebookresearch/fairchem/61266df4188eeca70fc56baebfba8abd74a0c695/src/fairchem/applications/ocx/data/experimental_data/ExpDataDump_241113.csv>) | Catalog evidence; Catalog official route |
| [OCx24 author data documentation](<https://raw.githubusercontent.com/facebookresearch/fairchem/main/src/fairchem/applications/ocx/data/README.md>) | Catalog evidence |
| [Matminer dataset metadata](<https://raw.githubusercontent.com/hackingmaterials/matminer/main/src/matminer/datasets/dataset_metadata.json>) | Catalog evidence |
| [Matbench Discovery dataset registry](<https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/datasets.yml>) | Resource evidence |
| [WBM benchmark test-set documentation](<https://raw.githubusercontent.com/janosh/matbench-discovery/main/data/wbm/readme.md>) | Catalog evidence |
| [Carbon-data author README](<https://raw.githubusercontent.com/jla-gardner/carbon-data/main/README.md>) | Catalog evidence |
| [Official Matbench v0.1 task metadata](<https://raw.githubusercontent.com/materialsproject/matbench/main/matbench/matbench_v0.1_dataset_metadata.json>) | Catalog evidence |
| [MatterGen official README](<https://raw.githubusercontent.com/microsoft/mattergen/main/README.md>) | Catalog evidence |
| [MatterGen Alex-MP data-release README](<https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/alex-mp/README.md>) | Catalog evidence |
| [MatterGen MP-20 data-release README](<https://raw.githubusercontent.com/microsoft/mattergen/main/data-release/mp-20/README.md>) | Resource evidence |
| [sedaoturak/data-resources-for-materials-science README](<https://raw.githubusercontent.com/sedaoturak/data-resources-for-materials-science/0df2e06e7caa6a49f807c20a068ce98050a14d13/README.md>) | Collection provenance |
| [CDVAE Carbon-24 dataset documentation](<https://raw.githubusercontent.com/txie-93/cdvae/main/data/carbon_24/README.md>) | Catalog evidence |
| [CDVAE MP-20 dataset documentation](<https://raw.githubusercontent.com/txie-93/cdvae/main/data/mp_20/README.md>) | Catalog evidence |
| [CDVAE Perov-5 dataset documentation](<https://raw.githubusercontent.com/txie-93/cdvae/main/data/perov_5/README.md>) | Catalog evidence |
| [Official JARVIS dataset loader](<https://raw.githubusercontent.com/usnistgov/jarvis/master/jarvis/db/figshare.py>) | Catalog evidence |
| [REMI: REsource for Materials Informatics README](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/README.md>) | Collection provenance |
| [Primary resource CSV](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/_data/resources.csv>) | Collection evidence; REMI: REsource for Materials Informatics; Resource evidence |
| [FeCoNi_benchmark_dataset_220501a.mat](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni/FeCoNi_benchmark_dataset_220501a.mat>) | Collection evidence; REMI: REsource for Materials Informatics |
| [data description.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Co-Ni/data%20description.txt>) | Catalog evidence; Collection evidence; REMI: REsource for Materials Informatics |
| [FeGaPd_CMP.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_CMP.txt>) | Collection evidence; REMI: REsource for Materials Informatics |
| [FeGaPd_DFT_regions.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_DFT_regions.txt>) | Collection evidence; REMI: REsource for Materials Informatics |
| [FeGaPd_Mag.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_Mag.txt>) | Collection evidence; REMI: REsource for Materials Informatics |
| [FeGaPd_XRD.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/FeGaPd_XRD.txt>) | Collection evidence; REMI: REsource for Materials Informatics |
| [data description.txt](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/Combinatorial%20Libraries/Fe-Ga-Pd/data%20description.txt>) | Catalog evidence; Collection evidence; REMI: REsource for Materials Informatics |
| [Open Access Data list](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/data/index.md>) | Catalog evidence; Collection evidence; Resource evidence |
| [REMI: REsource for Materials Informatics inspected document](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/index.html>) | Collection evidence |
| [REMI learning resource list](<https://raw.githubusercontent.com/usnistgov/remi/nist-pages/learn/index.md>) | Collection evidence |
| [RetroRules 2026](<https://retrorules.org>) | blaiszik/awesome-matchem-datasets |
| [SAFE Database (LANL)](<https://safe.lanl.gov>) | blaiszik/awesome-matchem-datasets |
| [SciBench](<https://scibench-ucla.github.io>) | blaiszik/awesome-matchem-datasets |
| [SciCode](<https://scicode-bench.github.io>) | blaiszik/awesome-matchem-datasets |
| [ScienceQA](<https://scienceqa.github.io/>) | blaiszik/awesome-matchem-datasets |
| [Scikit-Image](<https://scikit-image.org/>) | REMI: REsource for Materials Informatics |
| [Scikit-Learn](<https://scikit-learn.org/stable/>) | REMI: REsource for Materials Informatics |
| [SIDER](<http://sideeffects.embl.de/>) | blaiszik/awesome-matchem-datasets |
| [ROD homepage](<https://solsa.crystallography.net/rod/>) | Catalog evidence; Catalog official route |
| [NIST Structural Ceramics Database (SCD) Database](<https://srdata.nist.gov/CeramicDataPortal/scd>) | sedaoturak/data-resources-for-materials-science |
| [Starrydata — Resistor — homepage](<https://starrydata.github.io/starrydata_datasets/>) | Catalog official route |
| [Starrydata live release manifest](<https://starrydata.github.io/starrydata_datasets/manifest.json>) | Catalog evidence |
| [Elements of Statistical Learning](<http://statweb.stanford.edu/~tibs/ElemStatLearn/>) | REMI: REsource for Materials Informatics |
| [qcMol](<https://structpred.life.tsinghua.edu.cn/qcmol/>) | blaiszik/awesome-matchem-datasets |
| [CCDC: Access Structures downloads](<https://support.ccdc.cam.ac.uk/support/solutions/articles/103000306361/>) | Catalog evidence |
| [Git](<http://swcarpentry.github.io/git-novice/>) | REMI: REsource for Materials Informatics |
| [Software Carpentry: Plotting and Programming in Python](<http://swcarpentry.github.io/python-novice-gapminder/>) | REMI: REsource for Materials Informatics |
| [Software Carpentry: R for Reproducible Scientific Analysis](<http://swcarpentry.github.io/r-novice-gapminder/>) | REMI: REsource for Materials Informatics |
| [Software Carpentry: Programming with R](<http://swcarpentry.github.io/r-novice-inflammation/>) | REMI: REsource for Materials Informatics |
| [Software Carpentry: Python](<https://swcarpentry.github.io/python-novice-inflammation/>) | REMI: REsource for Materials Informatics |
| [Introduction to high-performance computing](<https://tacc-reproducible-intro-hpc.readthedocs.io/en/latest/intro_to_hpc/overview.html>) | JARVIS-Tools Notebooks |
| [USPTO-50k (Schneider) — source](<http://tdcommons.ai/generation_tasks/retrosyn/>) | blaiszik/awesome-matchem-datasets |
| [MAGNDATA bulk download instructions](<https://test2.cryst.ehu.eus/magndata/magndata_download.html>) | Catalog evidence |
| [NIST Alloy Data](<https://trc.nist.gov/metals_data/>) | sedaoturak/data-resources-for-materials-science |
| [Tox21](<https://tripod.nih.gov/tox21/challenge/>) | blaiszik/awesome-matchem-datasets |
| [Machine Learning in Materials Science: Recent Progress And Emerging Applications 2016](<https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=915933>) | REMI: REsource for Materials Informatics |
| [MOFX-DB primary descriptor](<https://tsapps.nist.gov/publication/get_pdf.cfm?pub_id=931567>) | Resource evidence |
| [UT Austin Channel-DNS Suite](<https://turbulence.oden.utexas.edu>) | blaiszik/awesome-matchem-datasets |
| [Johns Hopkins Turbulence DB (JHTDB)](<https://turbulence.pha.jhu.edu>) | blaiszik/awesome-matchem-datasets |
| [UHCSDB (Ultra-High Carbon Steel Micrographs)](<http://uhcsdb.materials.cmu.edu>) | blaiszik/awesome-matchem-datasets |
| [HIV](<https://wiki.nci.nih.gov/display/NCIDTPdata/AIDS+Antiviral+Screen+Data>) | blaiszik/awesome-matchem-datasets |
| [Introduction to Statistical Learning](<http://www-bcf.usc.edu/~gareth/ISL/>) | REMI: REsource for Materials Informatics |
| [The Cambridge Cluster Database](<https://www-wales.ch.cam.ac.uk/CCD.html>) | blaiszik/awesome-matchem-datasets |
| [2DMatPedia — homepage](<http://www.2dmatpedia.org/>) | Catalog official route |
| [AFLOW: Automatic FLOW for Materials Discovery](<http://www.aflow.org/>) | REMI: REsource for Materials Informatics |
| [Automatic Flow for Materials Discovery (AFLOW)](<http://www.aflowlib.org/>) | sedaoturak/data-resources-for-materials-science |
| [OpenLAM TrainingSet — homepage](<https://www.aissquare.com/datasets/detail?pageType=datasets&name=OpenLAM-TrainingSet-v1&id=308>) | Catalog evidence; Catalog official route |
| [Battery Imaging Library (BIL)](<https://www.batteryimaginglibrary.com>) | blaiszik/awesome-matchem-datasets |
| [BindingDB](<https://www.bindingdb.org/>) | blaiszik/awesome-matchem-datasets |
| [DigCat 2024 author preprint](<https://www.cambridge.org/engage/chemrxiv/article-details/6760cd4381d2151a02fb5356>) | Resource evidence |
| [Carolina Materials DB](<http://www.carolinamatdb.org>) | blaiszik/awesome-matchem-datasets |
| [Carolina Materials Database — homepage](<http://www.carolinamatdb.org/>) | Catalog evidence; Catalog official route |
| [Catalysis-Hub](<https://www.catalysis-hub.org>) | blaiszik/awesome-matchem-datasets |
| [Catalysis-Hub.org](<https://www.catalysis-hub.org/>) | Navigation resource; sedaoturak/data-resources-for-materials-science |
| [CSD (Cambridge)](<https://www.ccdc.cam.ac.uk>) | blaiszik/awesome-matchem-datasets |
| [CCDC CSD Publication Year Statistics, 1 January 2026](<https://www.ccdc.cam.ac.uk/media/CSD-Publication-Year-Statistics-2026.pdf>) | Catalog evidence |
| [Cambridge Structural Database (CSD) — homepage](<https://www.ccdc.cam.ac.uk/solutions/software/csd/>) | Catalog official route |
| [CCDC/FIZ Access Structures](<https://www.ccdc.cam.ac.uk/structures/>) | Catalog evidence; Catalog official route |
| [CoRE MOF 2024](<https://www.ccdc.cam.ac.uk/support-and-resources/downloads/>) | blaiszik/awesome-matchem-datasets |
| [CRIPT Polymer Data](<https://www.criptapp.org>) | blaiszik/awesome-matchem-datasets |
| [Crystallography Open Database (COD)](<http://www.crystallography.net/cod/>) | sedaoturak/data-resources-for-materials-science |
| [Crystallography Open Database (COD)](<https://www.crystallography.net/cod>) | blaiszik/awesome-matchem-datasets |
| [Crystallography Open Database (COD) — homepage](<https://www.crystallography.net/cod/>) | Catalog official route |
| [Crystallography Open Database (COD) — data](<https://www.crystallography.net/cod/archives/>) | Catalog official route |
| [NIST Self-Diffusion Data](<https://www.ctcms.nist.gov/~gkl/selfdiffusion.html>) | sedaoturak/data-resources-for-materials-science |
| [DataCamp](<https://www.datacamp.com>) | REMI: REsource for Materials Informatics |
| [DigBat / Dynamic Database of Solid-State Electrolytes — data](<https://www.digbat.org>) | Catalog official route |
| [Digital Catalysis Platform (DigCat)](<https://www.digcat.org/>) | Navigation resource |
| [Digital Hydrogen Platform (DigHyd) — data](<https://www.dighyd.org>) | Catalog official route |
| [DFT Solvation Energy Dataset](<https://www.doi.org/10.18126/jos5-wj65>) | blaiszik/awesome-matchem-datasets |
| [DoITPoMS Micrograph Library](<https://www.doitpoms.ac.uk/miclib/index.php>) | sedaoturak/data-resources-for-materials-science |
| [Ductile Cast Iron Project](<https://www.ductilecastironproject.com/>) | sedaoturak/data-resources-for-materials-science |
| [ChEMBL](<https://www.ebi.ac.uk/chembl/>) | blaiszik/awesome-matchem-datasets |
| [The Engineering Toolbox](<https://www.engineeringtoolbox.com/material-properties-t_24.html>) | sedaoturak/data-resources-for-materials-science |
| [ToxCast](<https://www.epa.gov/chemical-research/toxicity-forecaster-toxcasttm-data>) | blaiszik/awesome-matchem-datasets |
| [Practical Deep Learning for Coders](<https://www.fast.ai/>) | REMI: REsource for Materials Informatics |
| [GNU GPL v3 text](<https://www.gnu.org/licenses/gpl-3.0.en.html>) | nanoHUB Machine Learning Lab Module |
| [ICDD Powder Diffraction File PDF-5+ — homepage](<https://www.icdd.com/>) | Catalog official route |
| [ICDD 2026 product booklet](<https://www.icdd.com/assets/files/2026-Product-Booklet.pdf>) | Catalog evidence |
| [ICDD licensing process](<https://www.icdd.com/licensing-process/>) | Catalog evidence |
| [ICDD Powder Diffraction File PDF-5+ — data](<https://www.icdd.com/pdf-5/>) | Catalog official route |
| [ICEM Database](<https://www.innomat.se/icem>) | sedaoturak/data-resources-for-materials-science |
| [IZA Database of Zeolite Structures — data](<https://www.iza-structure.org/IZA-SC/ftc_table.php>) | Catalog official route |
| [IZA official database](<https://www.iza-structure.org/databases/>) | Catalog evidence; Catalog official route |
| [NeurIPS Open Polymer Prediction 2025](<https://www.kaggle.com/competitions/neurips-open-polymer-prediction-2025/data>) | blaiszik/awesome-matchem-datasets |
| [Catechol Benchmark](<https://www.kaggle.com/datasets/aichemy/catechol-benchmark>) | blaiszik/awesome-matchem-datasets |
| [ML Turbulence (Kaggle)](<https://www.kaggle.com/datasets/ryleymcconkey/ml-turbulence-dataset>) | blaiszik/awesome-matchem-datasets |
| [DigCat provider laboratory page](<https://www.li-lab-cat-design.com/code--database.html>) | Resource evidence |
| [Materials Cloud](<https://www.materialscloud.org/>) | sedaoturak/data-resources-for-materials-science |
| [Materials Cloud 3D (MC3D) — homepage](<https://www.materialscloud.org/discover/mc3d>) | Catalog official route |
| [Materials Cloud Datasets](<https://www.materialscloud.org/discover/menu>) | blaiszik/awesome-matchem-datasets |
| [The Materials Data Facility](<https://www.materialsdatafacility.org>) | blaiszik/awesome-matchem-datasets |
| [Materials Data Facility](<https://www.materialsdatafacility.org/>) | Navigation resource; REMI: REsource for Materials Informatics; Resource evidence |
| [MatWeb](<http://www.matweb.com/>) | sedaoturak/data-resources-for-materials-science |
| [MEXT materials data reference, NIMS-provided table](<https://www.mext.go.jp/content/20200602-mxt_nanozai-000007507_6_2.pdf>) | Catalog evidence |
| [MEXT/NIMS materials data infrastructure presentation](<https://www.mext.go.jp/content/20260522-mxt_jyohoka01-000050160_3.pdf>) | Catalog evidence |
| [Machine Learning for Materials Research Bootcamp and Workshop](<https://www.nanocenter.umd.edu/events/mlmr-2021/>) | REMI: REsource for Materials Informatics |
| [Wilmer et al., Nature Chemistry](<https://www.nature.com/articles/nchem.1192>) | Catalog evidence |
| [Kusne, A. G., et al. Nature communications 11.1 (2020): 1-11.](<https://www.nature.com/articles/s41467-020-19597-w>) | REMI: REsource for Materials Informatics |
| [Optimizing cross-domain transfer for universal machine learning interatomic potentials](<https://www.nature.com/articles/s41467-026-70195-8>) | Resource evidence |
| [The joint automated repository for various integrated simulations (JARVIS) for data-driven materials design](<https://www.nature.com/articles/s41524-020-00440-1>) | JARVIS-Tools Notebooks |
| [MPF.2021.2.8 — primary documentation](<https://www.nature.com/articles/s41524-024-01227-4>) | Catalog evidence |
| [Phonix anharmonic phonon database — paper](<https://www.nature.com/articles/s41524-026-02033-w>) | Catalog official route |
| [An open-access database and analysis tool for perovskite solar cells based on the FAIR data principles](<https://www.nature.com/articles/s41560-021-00941-3>) | Catalog evidence |
| [A-Lab (Autonomous Inorganic Synthesis)](<https://www.nature.com/articles/s41586-023-06734-w>) | blaiszik/awesome-matchem-datasets |
| [Solid-state synthesis Scientific Data descriptor](<https://www.nature.com/articles/s41597-019-0224-1>) | Catalog evidence; Catalog official route |
| [Battery materials Scientific Data descriptor](<https://www.nature.com/articles/s41597-020-00602-2>) | Catalog evidence; Catalog official route |
| [A band-gap database for semiconducting inorganic materials calculated with hybrid functional](<https://www.nature.com/articles/s41597-020-00723-8>) | Catalog evidence |
| [Zeo-1 Scientific Data descriptor](<https://www.nature.com/articles/s41597-022-01160-5.pdf>) | Catalog evidence |
| [Solution-synthesis Scientific Data descriptor](<https://www.nature.com/articles/s41597-022-01317-2>) | Catalog evidence; Catalog official route |
| [ChemDataExtractor thermoelectric materials database — paper](<https://www.nature.com/articles/s41597-022-01752-1>) | Catalog official route |
| [Thermoelectric Scientific Data descriptor](<https://www.nature.com/articles/s41597-022-01752-1.pdf>) | Catalog evidence |
| [Quantum-Chemical Bonding Database for Solid-State Materials (2023) — paper](<https://www.nature.com/articles/s41597-023-02477-5>) | Catalog official route |
| [3DSC_MP — paper](<https://www.nature.com/articles/s41597-023-02721-y>) | Catalog evidence; Catalog official route |
| [HYPOD-X Scientific Data descriptor](<https://www.nature.com/articles/s41597-024-04043-z>) | Catalog evidence; Catalog official route |
| [Impurity-aware synthesis Scientific Data descriptor](<https://www.nature.com/articles/s41597-025-06222-y>) | Catalog evidence; Catalog official route |
| [2025 magnetic temperature Scientific Data descriptor](<https://www.nature.com/articles/s41597-025-06244-6>) | Catalog evidence; Catalog official route |
| [https://www.nature.com/articles/sdata201654](<https://www.nature.com/articles/sdata201654>) | Machine Learning Materials Datasets / MAST-ML education |
| [Magnetic transition Scientific Data descriptor](<https://www.nature.com/articles/sdata2018111>) | Catalog evidence; Catalog official route |
| [HTEM Scientific Data descriptor](<https://www.nature.com/articles/sdata201853>) | Catalog evidence; Catalog official route |
| [Scientific Data collections](<https://www.nature.com/sdata/collections?page=3&type=collection>) | Navigation resource; Resource evidence |
| [Scientific Data data policies](<https://www.nature.com/sdata/policies/data-policies>) | Resource evidence |
| [NIST AM-Bench](<https://www.nist.gov/ambench/am-bench-2025-measurements-and-challenge-problems>) | blaiszik/awesome-matchem-datasets |
| [https://www.nist.gov/mgi](<https://www.nist.gov/mgi>) | JARVIS-Tools Notebooks; sedaoturak/data-resources-for-materials-science |
| [NIST Standard Reference Data (SRD)](<https://www.nist.gov/srd/srd-catalog>) | sedaoturak/data-resources-for-materials-science |
| [SPICE (OpenQDC)](<https://www.openqdc.io/datasets>) | blaiszik/awesome-matchem-datasets |
| [QMugs](<https://www.openqdc.io/datasets/qmugs>) | blaiszik/awesome-matchem-datasets |
| [OPTIMADE](<https://www.optimade.org/>) | Navigation resource; Resource evidence |
| [ORNL_AISD-Ex](<https://www.osti.gov/biblio/1907919>) | sedaoturak/data-resources-for-materials-science |
| [PDBbind](<http://www.pdbbind.org.cn/>) | blaiszik/awesome-matchem-datasets |
| [The Perovskite Database Project](<https://www.perovskitedatabase.com/>) | Catalog evidence; Catalog official route; sedaoturak/data-resources-for-materials-science |
| [Perovskite Database license](<https://www.perovskitedatabase.com/how-to-cite/>) | Catalog evidence |
| [Polymer Genome](<https://www.polymergenome.org/>) | sedaoturak/data-resources-for-materials-science |
| [RRUFF home](<https://www.rruff.net/>) | Catalog evidence; Catalog official route |
| [RRUFF data downloads](<https://www.rruff.net/about/download-data/>) | Catalog evidence; Catalog official route |
| [RRUFF FAQ: AMCSD](<https://www.rruff.net/help/faq/>) | Catalog evidence |
| [RRUFF: ZIP download](<https://www.rruff.net/help/zip-download/>) | Catalog evidence |
| [COD_HEM associated paper](<https://www.sciencedirect.com/science/article/abs/pii/S0927025624008097>) | sedaoturak/data-resources-for-materials-science |
| [https://www.sciencedirect.com/science/article/pii/S0022309300000648](<https://www.sciencedirect.com/science/article/pii/S0022309300000648>) | Machine Learning Materials Datasets / MAST-ML education |
| [https://www.sciencedirect.com/science/article/pii/S0927025617301738](<https://www.sciencedirect.com/science/article/pii/S0927025617301738>) | Machine Learning Materials Datasets / MAST-ML education |
| [https://www.sciencedirect.com/science/article/pii/S092702561830274X](<https://www.sciencedirect.com/science/article/pii/S092702561830274X>) | Machine Learning Materials Datasets / MAST-ML education |
| [Yoo, Y. K. et al. Intermetallics 14, 241–247 (2006).](<https://www.sciencedirect.com/science/article/pii/S096697950500186X>) | REMI: REsource for Materials Informatics |
| [DigBat author paper](<https://www.sciencedirect.com/science/article/pii/S2589965126001236>) | Catalog evidence |
| [SlideShare](<https://www.slideshare.net/KAMALCHOUDHARY4>) | JARVIS-Tools Notebooks |
| [SNUMAT hybrid-functional band-gap dataset — homepage](<http://www.snumat.com/>) | Catalog official route |
| [SpringerMaterials publisher overview](<https://www.springernature.com/gp/librarians/products/databases-solutions/springermaterials>) | Resource evidence |
| [SuperBand electronic-band / superconductivity dataset — homepage](<https://www.superband.work/>) | Catalog official route |
| [Tohoku University DigBat provider announcement](<https://www.tohoku.ac.jp/en/press/digbat_an_ai_ready_digital_platform_for_solid_state_battery_research.html>) | Catalog evidence |
| [Topological Quantum Chemistry all-band materials catalog — homepage](<https://www.topologicalquantumchemistry.com/>) | Catalog official route |
| [Topological Quantum Chemistry](<https://www.topologicalquantumchemistry.com/#/>) | sedaoturak/data-resources-for-materials-science |
| [Topological Quantum Chemistry all-band materials catalog — data](<https://www.topologicalquantumchemistry.fr/>) | Catalog official route |
| [https://www.youtube.com/@dr_k_choudhary](<https://www.youtube.com/@dr_k_choudhary>) | JARVIS-Tools Notebooks |
| [X2DB live provider table](<https://x2db.fysik.dtu.dk/>) | Catalog evidence; Catalog official route; blaiszik/awesome-matchem-datasets |
| [opXRD: Open Experimental Powder X-ray Diffraction Database — homepage](<https://xrd.aimat.science/>) | Catalog official route |
| [Zenodo](<https://zenodo.org/>) | sedaoturak/data-resources-for-materials-science |
| [Zenodo release metadata](<https://zenodo.org/api/records/10703249>) | Catalog evidence |
| [opXRD Zenodo metadata](<https://zenodo.org/api/records/15298026>) | Catalog evidence |
| [CoRE MOF 2025 deposit metadata](<https://zenodo.org/api/records/15621349>) | Catalog evidence |
| [ARC-MOF rights metadata](<https://zenodo.org/api/records/16802743>) | Catalog evidence |
| [LOBSTER database Part 1 author deposit](<https://zenodo.org/api/records/8091844>) | Catalog evidence |
| [LOBSTER database Part 2 author deposit](<https://zenodo.org/api/records/8092187>) | Catalog evidence |
| [Swiss Cat+ CO₂ Hydrogenation HTE](<https://zenodo.org/doi/10.5281/zenodo.8314734>) | blaiszik/awesome-matchem-datasets |
| [MatSci-Instruct (HoneyBee)](<https://zenodo.org/record/10119842>) | blaiszik/awesome-matchem-datasets |
| [AlSi10Mg LPBF Process–Structure–Property](<https://zenodo.org/records/10008435>) | blaiszik/awesome-matchem-datasets |
| [Work function and cleavage energy dataset](<https://zenodo.org/records/10703249>) | Catalog evidence; Catalog official route; sedaoturak/data-resources-for-materials-science |
| [MS25](<https://zenodo.org/records/10901820>) | blaiszik/awesome-matchem-datasets |
| [RDB19-Rad](<https://zenodo.org/records/11493786>) | blaiszik/awesome-matchem-datasets |
| [RDB7](<https://zenodo.org/records/13328872>) | blaiszik/awesome-matchem-datasets |
| [USPTO-LLM](<https://zenodo.org/records/14396156>) | blaiszik/awesome-matchem-datasets |
| [QCML](<https://zenodo.org/records/14859804>) | blaiszik/awesome-matchem-datasets; sedaoturak/data-resources-for-materials-science |
| [CoRE MOF 2024 release history](<https://zenodo.org/records/15055758>) | Catalog evidence |
| [opXRD archive v11](<https://zenodo.org/records/15298026>) | Catalog evidence; Catalog official route |
| [MSR-ACC/TAE25](<https://zenodo.org/records/15387280>) | blaiszik/awesome-matchem-datasets |
| [Aurora Robotic Battery Platform](<https://zenodo.org/records/15481956>) | blaiszik/awesome-matchem-datasets |
| [CoRE MOF 2025 v1.0](<https://zenodo.org/records/15621349>) | Catalog evidence; Catalog official route |
| [MOSAEC-DB author deposit](<https://zenodo.org/records/15808197>) | Catalog evidence; Catalog official route |
| [ARC-MOF v7](<https://zenodo.org/records/16802743>) | Catalog evidence; Catalog official route |
| [NMRexp](<https://zenodo.org/records/17296666>) | blaiszik/awesome-matchem-datasets |
| [MSR-ACC/TAE25](<https://zenodo.org/records/17629321>) | sedaoturak/data-resources-for-materials-science |
| [BOS-TMC Dataset](<https://zenodo.org/records/19410245>) | sedaoturak/data-resources-for-materials-science |
| [Materials Project Phonon database v1.1 - (26,413 compounds)](<https://zenodo.org/records/20196565>) | Catalog evidence |
| [PaRoutes — source](<https://zenodo.org/records/6275421>) | blaiszik/awesome-matchem-datasets |
| [Ti-6Al-4V LPBF Process–Structure–Property](<https://zenodo.org/records/6587905>) | blaiszik/awesome-matchem-datasets |
| [https://zenodo.org/records/8091844](<https://zenodo.org/records/8091844>) | Catalog official route; blaiszik/awesome-matchem-datasets |
| [https://zenodo.org/records/8092187](<https://zenodo.org/records/8092187>) | blaiszik/awesome-matchem-datasets |

[Back to the catalog](README.md) · [Search the HTML directory](https://usccolumbia.github.io/matverse/)
