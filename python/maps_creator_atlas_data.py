"""
Update content of the Atlas - generate maps based on the preprocessed netcdf data
Function        : Plot maps in a uniform way based on the netcdf files
Author          : Team BETA
First Built     : 2021.08.12
Last Update     : 2021.09.20
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
    #nc_files = glob.glob(Path(datapath,"*.nc"))
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
    constrained = dataset['constrained'][:]
    season = dataset['season'][:]
    key_p = dict(zip(percentile, range(len(percentile))))
    key_c = dict(zip(constrained, range(len(constrained))))
    key_s = dict(zip(season, range(len(season))))
    # string operations for naming
    project = nc_file.split('_')[-1][:-3]
    #institute = nc_file.split('_')[1]
    method = nc_file.split('_')[2]
    # latitudes and longitudes
    lat = dataset['lat'][:]
    lon = dataset['lon'][:]
    # loop
    for s in season:
        for c in constrained:
            for p in percentile:
                try:
                    data_pr = dataset['pr'][key_s[s], key_c[c], key_p[p], :, :]
                    # plot precipitation
                    plot(data_pr, lat, lon, "pr", project,
                         method, s, c, p, output_path)
                except IndexError:
                    pass
                try:
                    data_tas = dataset['tas'][key_s[s],
                                              key_c[c], key_p[p], :, :]
                    # plot temperature
                    plot(data_tas, lat, lon, "tas", project,
                         method, s, c, p, output_path)
                except IndexError:
                    pass


def plot(data, lat, lon, variable, project, method,
         season, constrained, percentile, output_path):
    """
    Plot relative precipitation and temperature using cartopy.
    """
    # name list
    cons = ["uncons", "cons"]  # 0: unconstrained 1: constrained
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
        cs = plt.pcolormesh(lon, lat, data, cmap="BrBG", vmin=-50, vmax=50)
    elif variable == "tas":
        cs = plt.pcolormesh(lon, lat, data, cmap="YlOrRd", vmin=0, vmax=5)
    cbar = fig.colorbar(cs, extend='both', orientation='vertical',
                        shrink=0.8, pad=0.08, spacing="uniform")
    cbar.ax.tick_params(labelsize=20)
    if variable == "pr":
        ax.set_title("\n".join(wrap(
            f'{method} {cons[constrained]} {season.lower()} relative precipitation projections (%) - {percentile} percentile projected changes for 2050 with respect to present-day climate', 60)), fontsize=20)
    elif variable == "tas":
        ax.set_title("\n".join(wrap(
            f'{method} {cons[constrained]} {season.lower()} temperature projections (degC) - {percentile} percentile projected changes for 2050 with respect to present-day climate', 60)), fontsize=20)
    # plt.show()
    fig.savefig(Path(output_path,
                f"eur_{method}_{variable}_41-60_{season.lower()}_{project.lower()}_{percentile}perc_{cons[constrained]}.png"),
                dpi=150)
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
