#!/usr/bin/env python
# -*- coding: utf-8 -*-

try:
	from osgeo import ogr, gdal
except:
	import ogr, gdal

# get raster data source
raster_ds = gdal.Open("../geodata/cadaster_borders-2tone-black-white.png")
input_band = raster_ds.GetRasterBand(3)

# create output data source
out_shp_name = "../geodata/cadaster_raster"
shp_driver = ogr.GetDriverByName("ESRI Shapefile")

# create output file name
out_shp = shp_driver.CreateDataSource(out_shp_name + ".shp")
new_shp = out_shp.CreateLayer(out_shp_name, srs=None)

gdal.Polygonize(input_band, None, new_shp, -1, [], callback=None)
new_shp.SyncToDisk()