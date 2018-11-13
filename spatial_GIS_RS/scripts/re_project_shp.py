#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import ogr, osr
import os


shp_driver = ogr.GetDriverByName('ESRI Shapefile')

# input SpatialReference
input_srs = osr.SpatialReference()
input_srs.ImportFromEPSG(4326)

# output SpatialReference
output_srs = osr.SpatialReference()
output_srs.ImportFromEPSG(3857)

#create the CoordinateTransformation
coord_trans = osr.CoordinateTransformation(input_srs, output_srs)

# get the input layer
input_shp = shp_driver.Open(r'../geodata/shp/UTM_Zone_Boundaries.shp')
in_shp_layer = input_shp.GetLayer()

# create the output layer
output_shp_file = r'../geodata/UTM_Zone_Boundaries_3857.shp'
# check if output file exists. If yes, delete it
if os.path.exists(output_shp_file):
	shp.DeleteDataSource(output_shp_file)

# create a new shapefile object
output_shp_dataset = shp_driver.CreateDataSource(output_shp_file)

# Create a new layer in output shapefile object and define its geometry
output_shp_layer = output_shp_dataset.CreateLayer("basemap_3857", geom_type=ogr.wkbMultiPolygon)


# add field to the new output shapefile layers
# get list of attribute fields
# create new fields for output
in_layer_def = in_shp_layer.GetLayerDefn
for in in range(0,in_layer_def.GetFieldCount()):
	field_def = in_layer_def.GetFieldDefn(i)
	output_shp_layer.CreateField(field_def)

# get the output layer's feature definition
output_layer_def = output_shp_layer.GetLayerDefn()

# loop through the input features
in_feature = in_shp_layer.GetNextFeature()
while in_feature:
	# get the input geometry
	geom = in_feature.GetGeometryRef()
	# reproject the geometry
	geom.Transform(coord_trans)
	# create a new feature
	output_feature = ogr.Feature(output_layer_def)
	# set the geometry and the attribute
	output_feature.SetGeometry(geom)
	for i in range(0,output_layer_def.GetFieldCount()):
		output_feature.SetField(output_layer_def.GetFieldDefn(i).GetNameRef(), in_feature.GetField(i))
	# add the feature to the shapefile
	output_shp_layer.CreateFeature(output_feature)
	# destroy the features and get the next input feature
	output_feature.Destroy()
	in_feature.Destroy()
	in_feature = in_shp_layer.GetNextFeature()

# close the shapefiles
input_shp.Destroy()
output_shp_dataset.Destroy()

spatialRef = osr.SpatialReference()
spatialRef.ImportFromEPSG(3857)

spatialRef.MorphToESRI()
prj_file = open('UTM_Zone_Boundaries_3857.prj','w')
prj_file.write(spatialRef.ExportToWkt())
prj_file.close()