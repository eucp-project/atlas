# Atlas of constrained climate projections- EUCP WP2

[![Quality Gate Status](https://sonarcloud.io/api/project_badges/measure?project=eucp-project_atlas&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=eucp-project_atlas)

This repository contains the source code and content for an [Atlas of constrained climate projections](https://eucp-project.github.io/atlas/). The atlas demonstrates outputs from the probabilistic projection methods developed or assessed in the [European Climate Projection system](https://www.eucp-project.eu/) (EUCP)
Horizon2020 project. For more info, see the [Atlas about page](https://eucp-project.github.io/atlas/about).

## Citation

To cite this repository, use the information avialable at [FIXME](FIXME),
and to cite the content of the Atlas, see the [Atlas references page]FIXME.

## Maintainers

Current maintainers of the Atlas are Research software engineers from the
[Netherlands eScience Center](https://www.esciencecenter.nl/).
If you have any questions or concerns, please submit an
[issue](https://github.com/eucp-project/atlas/issues). Maintainers will do their
best to help you.

## Contributing

The atlas is created with [Nuxt.js](https://nuxtjs.org/docs/get-started/installation). This section provides instructions for adding maps to Atlas.

1. Create a local build of the application

```bash
# install dependencies
$ npm install

# serve with hot reload at localhost:3000
$ npm run dev

# build for production and launch server
$ npm run build
$ npm run start

# generate static project
$ npm run generate
```

For detailed explanations on how things work, check out [Nuxt.js docs](https://nuxtjs.org).

2. Add maps

The maps shown in Atlas are created using the data available at [FIXME](FIXME),
and are stored in `png` format in `assets` directory of this repository. The
Python scripts to process the data and to create the maps are stored in `python`
directory. Read more [here](./python/README.md).
You can use the scripts as examples to develp a new script for your own data.
Then add new maps and scripts by submitting a new [pull request](https://github.com/eucp-project/atlas/pulls).

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


## PAGES

The pages directory contains your Application Views and Routes.
The framework reads all the `*.vue` files inside this directory and creates the router of your application.

More information about the usage of this directory in [the documentation](https://nuxtjs.org/guide/routing).



## Acknowledgement

FIXME
