This repository contains the datasets as described in the paper:

- Trinquet, V., Evans, M. L., & Rignanese, G.-M. (2025). Accelerating the discovery of high-performance nonlinear optical materials using active learning and high-throughput screening. arXiv, 2504.01526. Retrieved from https://arxiv.org/abs/2504.01526v1

- See the _References_ section of the Materials Cloud Archive repository for the official peer-reviewed paper

The dataset can be queried via an OPTIMADE API access at https://optimade.materialscloud.org/archive/wk-qm/v1/info. For example, the full query is:

```bash
optimade-get --output-file dataset_full.json https://optimade.materialscloud.org/archive/wk-qm
```

The dataset can also be visualized in an interactive manner [here](https://nlo.modl-uclouvain.org/) or via the Chemiscope application in the Materials Cloud Archive.

A Github repository is made available with Python scripts for various purposes including the manipulation of the form of the second-harmonic generation (SHG) or dielectric tensor and the benchmark code of machine learning models.

## The datasets

The archive "structures.tar.gz" contains CIF files of the crystal structures in the SHG datasets.

The archive "data.tar.gz" contains the file "dataset.csv", which is comprised of all the data presented in the paper. It can be loaded as follows:
```Python
import json
import pandas as pd

# Load the file as a pandas DataFrame
df_curated = pd.read_csv("dataset.csv", index_col=0)

# Since csv does not support dict nor list, need to use json.loads to convert them back to proper dict or list
for ir, r in df_curated.iterrows():
    for c in ['structure', 'structure_rot', 'hse_structure', 'hse_structure_rot', 'd_ijk', 'd_ijk_rot', 'd_ijk_conv', 'd_ijk_conv_neum', 'hse_d_ijk', 'hse_d_ijk_rot', 'hse_d_ijk_conv', 'hse_d_ijk_conv_neum', 'eps_ij', 'eps_ij_rot', 'hse_eps_ij', 'hse_eps_ij_rot']:
        if isinstance(r[c], str):
            df_curated.at[ir, c] = json.loads(r[c])
```

The data fields are described hereafter:

- name: src_id
    - title: Source ID
    - description: The ID of the material in the source database
    - unit: null
    - type: string
- name: structure
    - title: Structure
    - description: Structure of the crystal as a Pymatgen Structure object dictionary. (need json.loads to convert it back to dict though)
    - unit: null
    - type: dict
- name: d_ijk
    - title: LDA SHG tensor 
    - description: The 3x3x3 static SHG tensor as computed at the LDA level by DFPT.
    - unit: pm/V
    - type: list
- name: d_kp
    - title: LDA effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the LDA SHG tensor.
    - unit: pm/V
    - type: float
    - aliases: 
        - d_KP
- name: d_ijk_conv_neum
    - title: Conventional LDA SHG tensor
    - description: The conventional form of the LDA SHG tensor after rotation and after Neumann's principle was enforced.
    - unit: pm/V
    - type: list
    - aliases:
        - dijk_conv_neum
- name: d_kp_conv_neum
    - title: Conventional LDA effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the conventional LDA SHG tensor.
    - unit: pm/V
    - type: float
    - aliases: 
        - d_KP_conv_neum
- name: eps_ij
    - title: LDA dielectric tensor
    - description: The 3x3 static dielectric tensor (electronic contribution) as computed at the LDA level by DFPT.
    - unit: null
    - type: list
- name: n
    - title: LDA refractive index 
    - description: The static DFPT refractive index from the LDA dielectric tensor.
    - unit: null
    - type: float
- name: biref
    - title: LDA birefringence
    - description: The difference between the maximum and the minimum eigenvalues of the LDA dielectric tensor.
    - unit: null
    - type: float
- name: hse_d_ijk
    - title: HSE scissor-corrected SHG tensor 
    - description: The 3x3x3 static SHG tensor as computed at the HSE scissor-corrected level by DFPT.
    - unit: pm/V
    - type: list
- name: hse_d_kp
    - title: HSE scissor-corrected effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the HSE scissor-corrected SHG tensor.
    - unit: pm/V
    - type: float
    - aliases: 
    -   - hse_d_KP
- name: hse_d_ijk_conv_neum
    - title: Conventional HSE scissor-corrected SHG tensor
    - description: The conventional form of the HSE scissor-corrected SHG tensor after rotation and after Neumann's principle was enforced.
    - unit: pm/V
    - type: list
    - aliases:
    -   - hse_dijk_conv_neum
- name: d_kp_conv_neum
    - title: Conventional HSE scissor-corrected effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the conventional HSE scissor-corrected SHG tensor.
    - unit: pm/V
    - type: float
    - aliases: 
    -   - d_KP_conv_neum
- name: hse_eps_ij
    - title: HSE scissor-corrected dielectric tensor
    - description: The 3x3 static dielectric tensor (electronic contribution) as computed at the HSE scissor-corrected level by DFPT.
    - unit: null
    - type: list
- name: hse_n
    - title: HSE scissor-corrected refractive index 
    - description: The static DFPT refractive index from the HSE scissor-corrected dielectric tensor.
    - unit: null
    - type: float
- name: hse_biref
    - title: HSE scissor-corrected birefringence
    - description: The difference between the maximum and the minimum eigenvalues of the HSE scissor-corrected dielectric tensor.
    - unit: null
    - type: float
- name: lda_bandgap_fund
    - title: Fundamental LDA band gap
    - description: The fundamental LDA band gap.
    - unit: eV
    - type: float
- name: lda_bandgap_dir
    - title: Direct LDA band gap
    - description: The direct LDA band gap.
    - unit: eV
    - type: float
- name: hse_bandgap_fund
    - title: Fundamental HSE band gap
    - description: The fundamental HSE band gap.
    - unit: eV
    - type: float
- name: hse_bandgap_dir
    - title: Direct HSE band gap
    - description: The direct HSE band gap.
    - unit: eV
    - type: float
- name: hse_lda_scissor
    - title: Scissor-correction
    - description: The difference between the fundamental HSE and LDA band gaps.
    - unit: eV
    - type: float
- name: src
    - title: Source database
    - description: The name of the source database.
    - unit: null
    - type: string
- name: src_bandgap
    - title: Source band gap
    - description: The PBE band gap reported by the source database.
    - unit: eV 
    - type: float
- name: src_ehull
    - title: Energy above hull
    - description: The energy above hull reported by the source database.
    - unit: eV/atom
    - type: float
- name: abi_spg_number
    - title: ABINIT space group number
    - description: The space group number as detected by ABINIT with default tolerance.
    - unit: null
    - type: integer
- name: abi_spg_symbol
    - title: ABINIT space group symbol
    - description: The space group symbol as detected by ABINIT with default tolerance.
    - unit: null
    - type: string 
- name: abi_pg_symbol
    - title: ABINIT point group symbol
    - description: The point group symbol as detected by ABINIT with default tolerance.
    - unit: null
    - type: string
- name: structure_rot
    - title: Rotated structure
    - description: Structure of the crystal as a Pymatgen Structure object dictionary after rotation to find the conventional form of the d_ijk tensor (d_ijk_rot).
    - unit: null
    - type: dict
- name: hse_structure
    - title: Structure for the HSE-corrected calculation
    - description: Structure of the crystal as a Pymatgen Structure object dictionary for the calculation at the HSE level. Is equivalent to "structure".
    - unit: null
    - type: dict
- name: hse_structure_rot
    - title: Rotated structure for the HSE-corrected calculation
    - description: Structure of the crystal as a Pymatgen Structure object dictionary after rotation to find the conventional form of the hse_d_ijk tensor (hse_d_ijk_rot).
    - unit: null
    - type: dict
- name: d_ijk_rot
    - title: Rotated LDA SHG tensor
    - description: The 3x3x3 static SHG tensor as computed at the LDA level by DFPT after rotation to find its conventional form.
    - unit: pm/V
    - type: list
- name: d_ijk_conv
    - title: Rotated and cleaned LDA SHG tensor 
    - description: The 3x3x3 static SHG tensor as computed at the LDA level by DFPT after rotation to find its conventional form and after setting the proper components to exactly zero (instead of 1e-8 e.g.).
    - unit: pm/V
    - type: list
- name: eps_ij_rot
    - title: Rotated LDA dielectric tensor
    - description: The 3x3 static dielectric tensor (electronic contribution) as computed at the LDA level by DFPT and after roation to find d_ijk conventional form.
    - unit: null
    - type: list
- name: d_kp_rot
    - title: Rotated LDA effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the LDA SHG tensor after rotation to find its conventional form.
    - unit: pm/V
    - type: float
    - aliases: 
        - d_KP_rot
- name: d_kp_conv
    - title: Rotated and cleaned LDA effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the LDA SHG tensor after rotation to find its conventional form and after setting the proper components to exactly zero (instead of 1e-8 e.g.).
    - unit: pm/V
    - type: float
    - aliases: 
        - d_KP_conv
- name: hse_d_ijk_rot
    - title: Rotated HSE SHG tensor
    - description: The 3x3x3 static SHG tensor as computed at the HSE scissor-corrected level by DFPT after rotation to find its conventional form.
    - unit: pm/V
    - type: list
- name: d_ijk_conv
    - title: Rotated and cleaned HSE SHG tensor 
    - description: The 3x3x3 static SHG tensor as computed at the HSE scissor-corrected level by DFPT after rotation to find its conventional form and after setting the proper components to exactly zero (instead of 1e-8 e.g.).
    - unit: pm/V
    - type: list
- name: hse_eps_ij_rot
    - title: Rotated HSE dielectric tensor
    - description: The 3x3 static dielectric tensor (electronic contribution) as computed at the HSE scissor-corrected level by DFPT and after roation to find hse_d_ijk conventional form.
    - unit: null
    - type: list
- name: hse_d_kp_rot
    - title: Rotated HSE effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the HSE scissor-corrected SHG tensor after rotation to find its conventional form.
    - unit: pm/V
    - type: float
    - aliases: 
        - hse_d_KP_rot
- name: hse_d_kp_conv
    - title: Rotated and cleaned HSE scissor-corrected effective SHG coefficient
    - description: The effective Kurtz-Perry powder coefficient from the HSE scissor-corrected SHG tensor after rotation to find its conventional form and after setting the proper components to exactly zero (instead of 1e-8 e.g.).
    - unit: pm/V
    - type: float
    - aliases: 
        - hse_d_KP_conv
