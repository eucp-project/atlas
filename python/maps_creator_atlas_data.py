"""
Update content of the Atlas - generate maps based on the preprocessed netcdf data
Function        : Plot maps in a uniform way based on the netcdf files
Author          : Team BETA
First Built     : 2021.08.12
Last Update     : 2021.08.13
Library         : os, glob, netcdf4, matplotlib, cartopy, argparse
Description     : In this notebook serves to extract netcdf data and generate maps
                  for Atlas page.
Return Values   : png files
Note            : All the maps are generated in a uniform way.
"""

import os
import argparse
import glob
from netCDF4 import Dataset
import matplotlib
import matplotlib.pyplot as plt
import cartopy.crs as ccrs
# Generate images without having a window appear
matplotlib.use('Agg')

def files(datapath, output_path):
    """
    Generate maps in a uniform way based on the netcdf files.
    """
    # get the list of .nc files in the target directory
    #nc_files = glob.glob(os.path.join(datapath,"*.nc"))
    all_files = os.listdir(datapath)
    nc_files = [x for x in all_files if ".nc" in x] # get files with .nc
    # plot maps
    for i in nc_files:
        print("Processing file: {}".format(i))
        prepareData(i, datapath, output_path)

def prepareData(nc_file, datapath, output_path):
    """
    Extract data and names for plotting.
    """
    # extract data - weighted (constrained) and unweighted (unconstrained)
    dataset = Dataset(os.path.join(datapath, nc_file))
    data_pr = dataset['pr'][:]
    data_tas = dataset['tas'][:]
    # key dictionary to get dimensions
    percentile = dataset['percentile'][:]
    constrained = dataset['constrained'][:]
    season = dataset['season'][:]
    key_p = dict(zip(percentile, range(len(percentile))))
    key_c = dict(zip(constrained, range(len(constrained))))
    key_s = dict(zip(season, range(len(season))))
    # string operations for naming
    project = nc_file.split('_')[-1][:-3]
    model = nc_file.split('_')[1]
    method = nc_file.split('_')[2]
    # latitudes and longitudes
    lat = dataset['lat'][:]
    lon = dataset['lon'][:]
    # loop
    for s in season:
        for c in constrained:
            for p in percentile:
                data_pr = dataset['pr'][key_s[s],key_c[c],key_p[p],:,:]
                data_tas = dataset['tas'][key_s[s],key_c[c],key_p[p],:,:]
                # plot temperature
                plot(data_tas, lat, lon, "tas", project,
                     model, method, s, c, p, output_path)
                # plot precipitation
                plot(data_pr, lat, lon, "pr", project,
                     model, method, s, c, p, output_path)

def plot(data, lat, lon, variable, project, model,
         method, season, constrained, percentile, output_path):
    """
    Plot relative precipitation and temperature using cartopy.
    """
    # name list
    cons = ["uncons","cons"] # 0: unconstrained 1: constrained
    # plot fig
    fig = plt.figure(figsize=(12.8,9.6))
    ax = plt.axes(projection=ccrs.PlateCarree())
    ax.set_extent([-10,40,30,75],ccrs.PlateCarree()) # East, West, South, Nouth
    ax.coastlines(resolution='110m', color='black', linewidth=2)
    gl = ax.gridlines(crs=ccrs.PlateCarree(), draw_labels=True, linewidth=1, color='gray', alpha=0.5, linestyle='--')
    gl.xlabels_top = False
    gl.xlabels_bottom = True
    gl.ylabels_left = True
    gl.ylabels_right = False
    gl.xlines = False
    gl.ylines = False
    gl.xlabel_style = {'size': 20, 'color': 'black'}
    gl.ylabel_style = {'size': 20, 'color': 'black'}
    if variable == "pr":
        cs = plt.pcolormesh(lon, lat, data, cmap="BrBG") #vmin=-100, vmax=50)
    elif variable == "tas":
        cs = plt.pcolormesh(lon, lat, data, cmap="coolwarm")
    cbar = fig.colorbar(cs, extend='both', orientation='vertical',
                        shrink =0.8, pad=0.08, spacing="uniform")
    cbar.ax.tick_params(labelsize = 20)
    if variable == "pr":
        ax.set_title(f'EUR relative precipitation difference (%) {percentile}perc', fontsize=20)
    elif variable == "tas":
        ax.set_title(f'EUR temperature difference (K) {percentile}perc', fontsize=20)
    plt.show()
    fig.savefig(os.path.join(output_path,
                f"eur_{model}_{method}_{variable}_41-60_{season.lower()}_{project.lower()}_{percentile}perc_{cons[constrained]}.png"),
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