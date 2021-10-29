"""
Update content of the Atlas - generate maps based on the preprocessed netcdf data
Function        : Plot maps in a uniform way based on the netcdf files
Author          : Team BETA
First Built     : 2021.08.12
Last Update     : 2021.10.01
Library         : os, glob, netcdf4, matplotlib, cartopy, argparse
Description     : In this notebook serves to extract netcdf data and generate maps
                  for Atlas page.
Return Values   : png files
Note            : All the maps are generated in a uniform way.
"""

import os
from pathlib import Path
import argparse
import glob
from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
from textwrap import wrap
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
    dataset = Dataset(Path(datapath, nc_file))
    try:
        data_pr = dataset['pr'][:]
    except IndexError:
        pass
    try:
        data_tas = dataset['tas'][:]
    except IndexError:
        pass

    # key dictionary to get dimensions
    percentile = dataset['percentile'][:]
    season = dataset['time'][:]

    # string operations for naming
    input_file_name = dict(
        zip(["prefix", "activity", "institution_id", "source", "method", "sub_method", "cmor_var"],
        Path(nc_file).stem.split('_')
    )
    )

    project = input_file_name["source"]
    method = input_file_name["method"]
    c = input_file_name["sub_method"]

    # latitudes and longitudes
    lat = dataset['latitude'][:]
    lon = dataset['longitude'][:]

    SEASONS = ["JJA", "DJF"]

    # loop
    for i, s in enumerate(season):
        for k, p in enumerate(percentile):
            try:
                data_pr = dataset['pr'][i, :, :, k]

                # plot precipitation
                plot(data_pr, lat, lon, "pr", project,
                     method, s, c, p, output_path)
            except IndexError:
                pass
            try:
                data_tas = dataset['tas'][i, :, :, k]

                # plot temperature
                plot(data_tas, lat, lon, "tas", project,
                     method, SEASONS[i], c, p, output_path)
            except IndexError:
                pass


def plot(data, lat, lon, variable, project, method,
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
    gl.xlabels_top = False
    gl.xlabels_bottom = True
    gl.ylabels_left = True
    gl.ylabels_right = False
    gl.xlines = False
    gl.ylines = False
    gl.xlabel_style = {'size': 20, 'color': 'black'}
    gl.ylabel_style = {'size': 20, 'color': 'black'}
    if variable == "pr":
      cmap="BrBG"
      vmin=-50
      vmax=50
    elif variable == "tas":
        cmap="YlOrRd"
        vmin=0
        vmax=5

    cs = plt.pcolormesh(lon, lat, data, cmap=cmap, vmin=vmin, vmax=vmax)
    cbar = fig.colorbar(cs, extend='both', orientation='vertical',
                        shrink=0.8, pad=0.08, spacing="uniform")
    cbar.ax.tick_params(labelsize=20)
    if variable == "pr":
        title = "\n".join(
          wrap(f'{method} {constrained} {season.lower()} relative precipitation projections (%) - {percentile} percentile projected changes for 2050 with respect to present-day climate', 60)
            )
    elif variable == "tas":
      title = "\n".join(
        wrap(f'{method} {constrained} {season.lower()} temperature projections (degC) - {percentile} percentile projected changes for 2050 with respect to present-day climate', 60)
        )
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
