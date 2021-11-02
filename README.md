# Atlas of constrained climate projections- EUCP WP2

This repository contains the source code and content for an [Atlas of constrained climate projections](https://eucp-project.github.io/atlas/). The atlas demonstrates outputs from the probabilistic projection methods developed or assessed in the [European Climate Projection system](https://www.eucp-project.eu/) (EUCP)
Horizon2020 project. For more info, see the [Atlas about page](https://eucp-project.github.io/atlas/about).

## Citation

To cite this repository, use the information avialable at [FIXME](FIXME),
and to cite the content of the Atlas, see the [Atlas references page]FIXME.

## License

The source code is licensed under [Apache 2.0](./LICENSE), whereas the content
e.g. maps in the `static` directory of this repository, are licensed under
[CC-BY 4.0](https://creativecommons.org/licenses/by/4.0/).

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

## Acknowledgement

FIXME
