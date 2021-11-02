"""
Update content of the Atlas - generate maps based on the preprocessed netcdf data
Function        : Plot maps in a uniform way based on the netcdf files
Author          : Team BETA
First Built     : 2021.08.12
Last Update     : 2021.10.29
Library         : os, glob, netcdf4, matplotlib, cartopy, argparse
Description     : In this notebook serves to extract netcdf data and generate maps
                  for Atlas page.
Return Values   : png files
Note            : All the maps are generated in a uniform way.
"""

import os
from pathlib import Path
import argparse
import matplotlib
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from textwrap import wrap
import xarray as xr
# Generate images without having a window appear
matplotlib.use('Agg')


def files(datapath, output_path):
    """
    Generate maps in a uniform way based on the netcdf files.
    """
    # get the list of .nc files in the target directory
    # nc_files = glob.glob(Path(datapath,"*.nc"))
    all_files = os.listdir(datapath)
    nc_files = [x for x in all_files if ".nc" in x]  # get files with .nc
    # plot maps
    for i in nc_files:
        print("Processing file: {}".format(i))
        prepareData(i, datapath, output_path)


def prepareData(nc_file, datapath, output_path):
    """
    Extract data and names for plotting.
    """
    # extract data - weighted (constrained) and unweighted (unconstrained)
    dataset = xr.open_dataset(Path(datapath, nc_file))

    # string operations for naming
    input_file_name = dict(
        zip(["prefix", "activity", "institution_id", "source", "method", "sub_method", "cmor_var"],
        Path(nc_file).stem.split('_')
    )
    )

    project = input_file_name["source"]
    method = input_file_name["method"]
    c = input_file_name["sub_method"]

    SEASONS = ["JJA", "DJF"]

    # loop
    for i, t in enumerate(dataset['time'].values):
        for  p in dataset['percentile'].values:
            data = dataset.sel(percentile=p, time=t)
            plot(data, project, method, SEASONS[i], c, p, output_path)


def plot(data, project, method,
         season, constrained, percentile, output_path):
    """
    Plot relative precipitation and temperature using cartopy.
    """

    # plot fig
    fig = plt.figure(figsize=(12.8, 9.6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    # East, West, South, Nouth
    ax.set_extent([-10, 40, 30, 75], ccrs.PlateCarree())
    ax.coastlines(resolution='110m', color='black', linewidth=2)
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True,
                      linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.top_labels = False
    gl.bottom_labels = True
    gl.left_labels = True
    gl.right_labels = False
    gl.xlines = False
    gl.ylines = False
    gl.xlabel_style = {'size': 20, 'color': 'black'}
    gl.ylabel_style = {'size': 20, 'color': 'black'}
    if 'pr' in list(data.keys()):
        variable = 'pr'
        cmap = "BrBG"
        vmin = -50
        vmax = 50
        title = "\n".join(
          wrap(f'{method} {constrained} {season.lower()} relative precipitation projections (%) - {percentile}th percentile projected changes for 2050 with respect to present-day climate', 60)
            )
    elif 'tas' in list(data.keys()):
        variable = 'tas'
        cmap = "YlOrRd"
        vmin = 0
        vmax = 5
        title = "\n".join(
        wrap(f'{method} {constrained} {season.lower()} temperature projections (degC) - {percentile}th percentile projected changes for 2050 with respect to present-day climate', 60)
        )

    cs = data[variable].plot(cmap=cmap, vmin=vmin, vmax=vmax, ax=ax, x='longitude', y='latitude', add_colorbar=False)
    cbar = fig.colorbar(cs, extend='both', orientation='vertical',
                        shrink=0.8, pad=0.08, spacing="uniform")
    cbar.ax.tick_params(labelsize=20)
    # plt.show()
    ax.set_title(title, fontsize=20)
    output_file_name = Path(
      output_path,
      f"eur_{method}_{variable}_41-60_{season.lower()}_{project.lower()}_{percentile}perc_{constrained}.png"
      )
    print(f"saving {output_file_name}")
    fig.savefig(output_file_name, dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    # define command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputdir', required=True, type=str, default="./",
                        help="directory containing preprocessed netCDF files [default current location]")
    parser.add_argument('-o', '--outputdir', required=True, type=str, default="./",
                        help="directory for output [default current location]")
    # get arguments
    args = parser.parse_args()
    # call plot()
    files(args.inputdir, args.outputdir)
