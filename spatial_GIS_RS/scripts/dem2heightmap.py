#!/usr/bin/env python
# -*- coding: utf-8 -*-

import subprocess
import os
try:
	from osgeo import gdal
except:
	import gdal

path_base = '../geodata/'
input_dem_asc = "original_dem.asc"

# gdal_translate converts raster data between different formats

# Check environment of usage
if os.name == 'nt':
	###########################################
	#		WINDOWS ENVIRONMENT
	#==========================================
	command_gdal_translate = "c:/OSGeo4W/bin/gdal_translate.exe"
	command_gdalinfo = "c:/OSGeo4W/bin/gdalinfo.exe"
	###########################################
elif os.name =='posix':
	###########################################
	#		LINUX ENVIRONMENT
	#==========================================	
	command_gdal_translate = "gdal_translate"
	command_gdalinfo = "gdalinfo"
	command_gdaldem = "gdaldem"
#################################################
# variable to hold input DEM, output, temporary and final output files
orig_dem_asc = path_base + input_dem_asc
temp_tiff = path_base + "temp_image.tif"
output_envi = path_base + "final_envi.bin"

# transforn dem to tiff
dem2tiff = command_gdal_translate + " " + orig_dem_asc + " " + temp_tiff
print("Now executing this command: " + dem2tiff)
subprocess.call(dem2tiff.split(), shell=False)

# open the temp tiff file and extract min and max height values
ds = gdal.Open(temp_tiff, gdal.GA_ReadOnly)
band = ds.GetRasterBand(1)
print("Band Type = ", gdal.GetDataTypeName(band.DataType))
min_val = band.GetMinimum()
max_val = band.GetMaximum()
if min_val is None or max is None:
	(min,max) = band.ComputeRasterMinMax(1)
print("Min = %.3f, Max = %.3f" %(min_val,max_val))
min_elevation = str(int(round(min_val)))
max_elevation = str(int(round(max_val)))

tiff_2_envi = command_gdal_translate + " -scale -ot UInt16 -outsize 500 500 -of ENVI "\
+ temp_tiff + " " + output_envi

subprocess.call(tiff_2_envi.split(), shell=False)