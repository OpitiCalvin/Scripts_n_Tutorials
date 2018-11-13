#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	from osgeo import ogr, gdal
except:
	import ogr,gdal
# set pixel size
pixel_size = 1
no_data_value = -9999

# input shapefile name
# input projection must be in Cartesian system in meters
# input wgs 84 or EPSG:4326 will NOT work
input_shp = r'../geodata/shp/ply_golfcourse-strasslach3857.shp'

# TIFF Raster file to be created
output_raster = r'../geodata/ply_golfcourse-strasslach.tif'

# open the data source, get the layer object and assign extent coordinates
shp_ds = ogr.Open(input_shp)
shp_layer = shp_ds.GetLayer()
x_min,x_max,y_min,y_max = shp_layer.GetExtent()

# calculate raster resolution
x_res = int((x_max - x_min) / pixel_size)
y_res = int((y_max - y_min) / pixel_size)

# set the image type for export
image_type = 'GTiff'
driver = gdal.GetDriverByName(image_type)

new_raster = driver.Create(output_raster,x_res,y_res,1, gdal.GDT_Byte)
new_raster.SetGeoTransform((x_min, pixel_size,0,y_max, 0, -pixel_size))

# get the raster band we want to export to
raster_band = new_raster.GetRasterBand(1)

# assign the no data value to empty cells
raster_band.SetNoDataValue(no_data_value)

# run vector to raster on new raster with input shapefile
gdal.RasterizeLayer(new_raster,[1], shp_layer, burn_values=[255])