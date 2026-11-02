This repository contains the dataset as described in the paper:

- Trinquet, V., Evans, M. L., Hargreaves, C. J., De Breuck, P.-P., & Rignanese, G.-M. (2025). Optical materials discovery and design with federated databases and machine learning. Faraday Discuss., 256(0), 459–482. doi: 10.1039/D4FD00092G

The dataset can be queried via an OPTIMADE API access at https://optimade.materialscloud.org/archive/ed-g2/info. For example, the full query is:

```bash
optimade-get --output-file dataset_full.json https://optimade.materialscloud.org/archive/ed-g2
```

It came to our attention that we made a small mistake when computing the refractive index from the dielectric tensor in version 1 of this repository (and in the paper). Although this error has a minimal impact on the refractive index values (< 0.5% for 95% of the dataset), we provide the corrected values in the version 2 of this repository. We also take this opportunity to provide the refractive indices along the 3 cartesian directions for the sake of completeness as well as a Chemiscope visualization file.



## The dataset

The archive "structures.tar.gz" contains CIF files of the crystal structures in the refractive index dataset.

The archive "data.tar.gz" contains the file "dataset.csv", which is comprised of all the data presented in the paper. It can be loaded as follows:
```Python
import json
import pandas as pd

# Load the file as a pandas DataFrame
df_curated = pd.read_csv("dataset.csv", index_col=0)

# Since csv does not support dict nor list, need to use json.loads to convert them back to proper dict or list
for ir, r in df_curated.iterrows():
    for c in ['structure']:
        if isinstance(r[c], str):
            df_curated.at[ir, c] = json.loads(r[c])
```

The data fields are described hereafter:

- name: id
    - title: ID
    - description: The ID of the material in the source database
    - unit: null
    - type: string
- name: structure
    - title: Structure
    - description: Structure of the crystal as a Pymatgen Structure object dictionary. (need json.loads to convert it back to dict though)
    - unit: null
    - type: dict
- name: refractive_index_11
    - title: Static refractive index (11)
    - description: The square root of the (11) eigenvalue of the static dielectric tensor (electronic contribution) as computed at the GGA-PBE level by DFPT.
    - unit: null
    - type: float
- name: refractive_index_22
    - title: Static refractive index (22)
    - description: The square root of the (22) eigenvalue of the static dielectric tensor (electronic contribution) as computed at the GGA-PBE level by DFPT.
    - unit: null
    - type: float
- name: refractive_index_33
    - title: Static refractive index (33)
    - description: The square root of the (33) eigenvalue of the static dielectric tensor (electronic contribution) as computed at the GGA-PBE level by DFPT.
    - unit: null
    - type: float
- name: refractive_index
    - title: Static refractive index
    - description: The refractive index of the static dielectric tensor (electronic contribution) as computed at the GGA-PBE level by DFPT.
    - unit: null
    - type: float
- name: biref
    - title: Static birefringence
    - description: The difference between the maximum and the minimum square root of the eigenvalues of the GGA-PBE static dielectric tensor.
    - unit: null
    - type: float
- name: src_bandgap
    - title: Source band gap
    - description: The PBE band gap reported by the source database.
    - unit: eV 
    - type: float
- name: src
    - title: Source
    - description: The name of the source database.
    - unit: null
    - type: string

