## Processing data with Python (notebooks)

In this folder all scripts and notebooks are stored that are used to pre-process
data and to generate the maps in the Atlas.

### Preprocess netCDF data

- [Preprocess CNRM-KCC data](cleanup_CNRM_KCC_atlas_netcdf.ipynb)
- [Preprocess Edinburgh University ASK data](cleanup_EdinU_ASK_atlas_netcdf.ipynb)
- [Preprocess ETHZ-ClimWIP data](cleanup_ETHZ_ClimWIP_atlas_netcdf.ipynb)
- [Preprocess IPSL-REA data](cleanup_IPSL_REA_atlas_netcdf.ipynb)
- [Preprocess UKMO-UKCP data](cleanup_UKMO_UKCP_atlas_netcdf.ipynb)
- [Preprocess University of Reading CALL data](cleanup_UoR_CALL_atlas_netcdf.ipynb)

### Plot maps

- [Plot maps using pre-processed data](maps_creator_atlas_data.py) (batch processing)

### Additional notebooks

These notebooks can be used to tweak plot settings and preview maps using raw
model data.
- [Preview map of relative precipitation](maps_prototype_prec.ipynb)
- [Preview map of temperature](maps_prototype_tas.ipynb)

This notebook generates a placeholder map that can be used on the Atlas page.
- [Placeholder map](maps_placeholder.ipynb)