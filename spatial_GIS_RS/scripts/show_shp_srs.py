#!/usr/bin/env python3
#-*- coding: utf-8 -*-

try:
	import ogr
except:
	from osgeo import ogr

shp_driver = ogr.GetDriverByName('ESRI Shapefile')
shp_dataset = shp_driver.Open(r'../geodata/schools.shp')
shp_layer = shp_dataset.GetLayer()
shp_srs = shp_layer.GetSpatialRef()
print(shp_srs)