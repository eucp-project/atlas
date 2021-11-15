# Processing data with Python (notebooks)

In this folder, all scripts and notebooks are stored that are used to pre-process
data and to generate the maps in the Atlas.

## Requirements

The dependencies of the notebooks and scripts can be installed in a Conda environment with

```shell
# From this directory
conda install mamba -n base -c conda-forge -y
mamba env create --file environment.yml
conda activate atlas
```

## Preprocess NetCDF data

We provide some notebooks that check the original/raw data, fix/add the metadata
using
[CF-conventions](https://cfconventions.org/Data/cf-conventions/cf-conventions-1.9/cf-conventions.html)
and save data in a NetCDF format. As the output of a method (i.e.
original/raw data) is provided by a specific institute, there is one notebook
per each `institute`-`method`:

- [Preprocess CNRM-KCC data](cleanup_CNRM_KCC_atlas_netcdf.ipynb)
- [Preprocess EdinU-ASK data](cleanup_EdinU_ASK_atlas_netcdf.ipynb)
- [Preprocess ETHZ-ClimWIP data](cleanup_ETHZ_ClimWIP_atlas_netcdf.ipynb)
- [Preprocess ICTP-REA data](cleanup_ICTP_REA_atlas_netcdf.ipynb)
- [Preprocess UKMO-UKCP data](cleanup_UKMO_UKCP_atlas_netcdf.ipynb)
- [Preprocess Uoxf-CALL data](cleanup_Uoxf_CALL_atlas_netcdf.ipynb)

To run a notebook, you only need to specify the path to raw data as `datapath`
and a path to store the output as `output_path`. Defaults are:

- `datapath = "./AtlasData/raw"`

- `output_path = "./AtlasData/preprocess"`

The pre-processed data follows the following standards:

### coordinates

- climatology_bounds (climatology_bounds) datetime64[ns] ['2050-06-01', '2050-09-01', '2050-12-01', '2051-03-01']
- time (time) (datetime64[ns]) [2050-07-16 2051-01-16] # "JJA", "DJF"
- latitude (lat) (float64) [30, ..., 75]
- longitude (lon) (float64) [-10, ..., 40]
- percentile (percentile) (int64) [10, 25, 50, 75, 90]

### variables

- tas (time, latitude, longitude, percentile) (float64)
- pr (time, latitude, longitude, percentile) (float64)

### attributes

The attributes of variables and coordinates are defined as:

- "tas": {
    "description": "Change in Air Temperature",
    "standard_name": "Change in Air Temperature",
    "long_name": "Change in Near-Surface Air Temperature",
    "units": "K", 
    "cell_methods": "time: mean changes over 20 years 2041-2060 vs 1995-2014",
},
- "pr": {
    "description": "Relative precipitation",
    "standard_name": "Relative precipitation",
    "long_name": "Relative precipitation",
    "units": "%",  
    "cell_methods": "time: mean changes over 20 years 2041-2060 vs 1995-2014",
},
- "latitude": {"units": "degrees_north", "long_name": "latitude", "axis": "Y"},
- "longitude": {"units": "degrees_east", "long_name": "longitude", "axis": "X"},
- "time": {
    "climatology": "climatology_bounds",
    "long_name": "time",
    "axis": "T",
    "climatology_bounds": ["2050-6-1", "2050-9-1", "2050-12-1", "2051-3-1"],
    "description": "mean changes over 20 years 2041-2060 vs 1995-2014. The mid point 2050 is chosen as the representative time.",
},
- "percentile": {"units": "%", "long_name": "percentile", "axis": "Z"},

The attributes of the data is defined as:

- "description": "Contains modified `institute` `method` data used for Atlas in EUCP project.",
- "history": "original `institute` `method` data files ...",

### output file names

output_file_name = `prefix_activity_institution-id_source_method_sub-method_cmor-var`

> example: atlas_EUCP_CNRM_CMIP6_KCC_cons_tas.nc


## Create maps

> make sure that the conda environment `atlas` is activated.

Maps are created using pre-processed data and `maps_creator_atlas_data.py` script:

```shell
python ./atlas/python/maps_creator_atlas_data.py --inputdir "./AtlasData/preprocess" --outputdir "./atlas/assets/processed_figures"
```

## Add new maps

If you want to add new maps to the Atlas, please publish the pre-processed data on
Zenodo and add references to [FIXME].

## Additional notebooks

These notebooks can be used to tweak plot settings and preview maps using raw
model data.

- [Preview map of relative precipitation](maps_prototype_prec.ipynb)
- [Preview map of temperature](maps_prototype_tas.ipynb)
