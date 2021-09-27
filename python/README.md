## Python script to plot maps for Atlas

The scripts and notebooks contained in this folder are used to generate content for Atlas page. They are made for the following purposes:

- Preprocess model outputs (.nc) and prepare the data for plotting
- Plot maps in a uniform way based on the preprocessed netcdf files

The model outputs are preprocessed and saved as netcdf4 files, following the format:
**coordinates:**
- lon (lon) (float64) [-10, ..., 40]
- lat (lat) (float64) [30, ..., 75]
- percentile (percentile) (int64) [10, 25, 50, 75, 90]
- constrained (constrained) (int64) [1, 0]
- season (season) (object) ['DJF', 'JJA']

**variables**
- tas (season, constrained, percentile, lat, lon) (float64)
- pr (season, constrained, percentile, lat, lon) (float64)

The folder contains multiple files to handle these tasks:

*Preprocess netCDF data from different models with different methods*
- [`Preprocess ETHZ-ClimWIP data`](cleanup_ETHZ_ClimWIP_atlas_netcdf.ipynb)
- [`Preprocess IPSL-REA data`](cleanup_IPSL_REA_atlas_netcdf_.ipynb)

*Plot maps using preprocessed data (batch processing)*
- [`Plot maps`](maps_creator_atlas_data.py)

*Tweak plot settings and preview maps using raw model data*
- [`Preview map of relative precipitation`](maps_prototype_prec.ipynb)
- [`Preview map of temperature`](maps_prototype_tas.ipynb)
