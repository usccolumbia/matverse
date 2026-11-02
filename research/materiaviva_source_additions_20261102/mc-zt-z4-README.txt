- `structures.tar.gz` contains CIFs of every structure considered, with the exact structures used for initial ELFCar calculations, as well as by the MP compatibility relaxation (in the corresponding sub-folders).
- `data.csv` contains computed ELF max and stability info for each structure.
- `raw.tar.gz` contains additional raw data, including bandstructures and phonon dispersion curves for every structure.
- `mp_comparison.json.gz` contains a list of pymatgen `ComputedEntry` containing the results of atomate2 `MPGGARelax` calculations to enable direct comparison with the Materials Project's convex hull (as of 20/11/2023).
- `scripts.zip` is a directory containing Python scripts used for the re-relaxation and stability calculations of the structures, alongside a requirements file
with the dependencies required for repeating them, as well as the script required to create this archive from the raw data.
- `optimade.yaml` a config file for the MCloud/OPTIMADE integration that allows ingestion of the data into an OPTIMADE API.
