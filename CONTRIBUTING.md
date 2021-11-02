# Contributing guidelines

## In general

Contributions are very welcome. Please make sure there is a github issue
associated with with every pull request. Creating an issue is also a good way to
propose new features.

## Add maps to the Atlas

The maps shown in Atlas are created using the data available at [FIXME](FIXME),
and are stored in `.png` format in the [assets](./assets) directory of this
repository. You can use the scripts and notebooks as examples to develop a new
script for your own data.

### Processing data and preparing plots

Content for the Atlas page is generated in multiple steps:

- Preprocess data to clean netCDF files
- Plot maps in a uniform way based on the clean data files

The scripts that perform these actions are stored in the [python](./python)
directory.

When adding a new script or notebook, please place a short description in the
[README](./python/README.md) of this directory.

### Clean data

The clean data has a netCDF4 format, and follows the following standards:

#### coordinates

- lon (lon) (float64) [-10, ..., 40]
- lat (lat) (float64) [30, ..., 75]
- percentile (percentile) (int64) [10, 25, 50, 75, 90]
- constrained (constrained) (int64) [1, 0]
- season (season) (object) ['DJF', 'JJA']

#### variables

- tas (season, constrained, percentile, lat, lon) (float64)
- pr (season, constrained, percentile, lat, lon) (float64)

### Plots

To generate uniform data plots, the python script
[`maps_creator_atlas_data.py`](python/maps_creator_atlas_data.py) is used.

To add a new plot to the Atlas, save the image to the [assets](./assets)
directory, and add a reference in [FIXME].

## Edit the Atlas pages

The atlas is created with
[Nuxt.js](https://nuxtjs.org/docs/get-started/installation).

### Create a local build

To locally render the Atlas, run the following:

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

For detailed explanations on how things work, check out [Nuxt.js
docs](https://nuxtjs.org).

### Edit the pages

The [pages](./pages) directory contains your Application Views and Routes. The
framework reads all the `*.vue` files inside this directory and creates the
router of your application.

More information about the usage of this directory in [the
documentation](https://nuxtjs.org/guide/routing).

## Making a release

### Author information

Ensure all authors are present in:

- `CITATION.cff`

### Confirm release info

Ensure the right date and upcoming version number is set in:

- `CITATION.cff`
- `package.json`

### Release on GitHub

Open [releases](https://github.com/eucp-project/atlas/releases) and draft a new
release.

Tag the release according to semantic versioning guidelines, preceded with a `v`
(e.g.: v1.0.0). The release title is the tag and the release date together
(e.g.: v1.0.0 (2019-07-25)). Tick the pre-release box in case the release is a
candidate release, and amend the version tag with `rc` and the candidate number.

### Release on Zenodo

Confirm the new release on [Zenodo]((FIXME). (TBD)

### Release on the Research Software Directory

Wait a few hours, then confirm the addition of a new release on the
[RSD](https://www.research-software.nl/software/eucp-atlas).
