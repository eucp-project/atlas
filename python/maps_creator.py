"""
Update content of the Atlas - generate maps based on the netcdf data
Function        : Plot maps in a uniform way based on the netcdf files
Author          : Team BETA
First Built     : 2021.08.09
Last Update     : 2021.08.10
Library         : os, glob, netcdf4, matplotlib, cartopy, argparse
Description     : In this notebook serves to extract netcdf data and generate maps for Atlas page.
Return Values   : png files
Note            : All the maps are generated in a uniform way.
"""

import os
import argparse
import glob
from netCDF4 import Dataset
import matplotlib.pyplot as plt
import cartopy.crs as ccrs

def maps(datapath, output_path, map_type):
    """
    Generate maps in a uniform way based on the netcdf files.
    """
    # get the list of .nc files in the target directory
    #nc_files = glob.glob(os.path.join(datapath,"*.nc"))
    all_files = os.listdir(datapath)
    nc_files = [x for x in all_files if ".nc" in x] # get files with .nc
    # check if the map type is correct or not
    if map_type == "prec":
        print("Plot precipitation map.")
    elif map_type == "tas":
        print("Plot temperature map.")
    else:
        raise IOError("The chosen map type is not supported for plotting!")
    # plot maps
    for i in nc_files:
        print("Processing file: {}".format(i))
        plot(i, datapath, output_path, map_type)

def plot(nc_file, datapath, output_path, map_type):
    """
    Plot precipitation / temperature
    """
    # extract data - weighted (constrained) and unweighted (unconstrained)
    dataset = Dataset(os.path.join(datapath, nc_file))
    if map_type == "prec":
        data_weight = dataset['pr_weighted'][:]
        data_unweight = dataset['pr_unweighted'][:]
        cmap = "BrBG"
    elif map_type == "tas":
        data_weight = dataset['tas_weighted'][:]
        data_unweight = dataset['tas_unweighted'][:]
        cmap = "coolwarm"
    # latitudes and longitudes
    lat = dataset['lat'][:]
    lon = dataset['lon'][:]
    # plot map - constrained
    fig1 = plt.figure(figsize=(12.8,9.6))
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
    cs = plt.pcolormesh(lon, lat, data_weight, cmap=cmap)
                        #vmin=-100, vmax=50)
    cbar = fig1.colorbar(cs, extend='both', orientation='horizontal',
                        shrink =0.8, pad=0.08, spacing="uniform")
    cbar.ax.tick_params(labelsize = 20)
    ax.set_title('EUR relative precipitation difference (%)', fontsize=20)
    plt.show()
    fig1.savefig(os.path.join(output_path,"{}_constrained.png".format(nc_file[:-3])),
                 dpi=150)
    fig1.cloes()
    # plot map - unconstrained
    fig2 = plt.figure(figsize=(12.8,9.6))
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
    cs = plt.pcolormesh(lon, lat, data_unweight, cmap=cmap)
                        #vmin=-100, vmax=50)
    cbar = fig2.colorbar(cs, extend='both', orientation='horizontal',
                        shrink =0.8, pad=0.08, spacing="uniform")
    cbar.ax.tick_params(labelsize = 20)
    ax.set_title('EUR relative precipitation difference (%)', fontsize=20)
    plt.show()
    fig2.savefig(os.path.join(output_path,"{}_unconstrained.png".format(nc_file[:-3])),
                 dpi=150)
    fig2.cloes()

if __name__ == "__main__":
    # define command line arguments
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--inputdir', required=True, type=str, default="./",
                        help="directory containing netCDF files [default current location]")
    parser.add_argument('-o', '--outputdir', required=True, type=str, default="./",
                        help="directory for output [default current location]")
    parser.add_argument('-t', '--typemap', required=True, type=str, default="prec",
                        help="type of plots, either precipitation(prec) or temperture (tas) [default 'prec']")
    # get arguments
    args = parser.parse_args()
    # call plot()
    maps(args.inputdir, args.outputdir, args.typemap)