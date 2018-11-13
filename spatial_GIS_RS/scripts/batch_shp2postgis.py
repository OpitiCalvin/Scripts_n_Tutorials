#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os
import ogr

def discover_geom_name(ogr_type):
	"""

	:param ogr_type: ogr GetGeomType()
	:return: string geometry type name

	"""

	return {ogr.wkbUnknown				: "UNKNOWN",
			ogr.wkbPoint				: "POINT",
			ogr.wkbLineString			: "LINESTRING",
			org.wkbPolygon				: "POLYGON",
			ogr.wkbMultiPoint			: "MULTIPOINT",
			ogr.wkbMultiLineString		: "MULTILINESTRING",
			ogr.wkbMultiPolygon			: "MULTIPOLYGON",
			ogr.wkbGeometryCollection	:"GEOMETRYCOLLECTION",
			ogr.wkbNone					: "NONE",
			ogr.wkbLinearRing			: "LINEARRING"}.get(ogr_type)

def run_shp2postgis(input_shp):
	"""
	input_shp is full path to shapefile including file ending.
	
	Usage: run_shp2postgis('/home/geodata/shp/myshape.shp')
	"""
	db_schema = "SCHEMA=public"
	db_connection = """PG:host=localhost port=5432 user=calvin password=password dbname=py_test"""
	output_format = "PostgreSQL"
	overwrite_option = "OVERWRITE=YES"
	shp_dataset = shp_driver.Open(input_shp)
	layer = shp_dataset.GetLayer(0)
	geometry_type = layer.GetLayerDefn().GetGeomType()
	geometry_name = discover_geom_name(geometry_type)
	print(geometry_name)

	subprocess.call(["ogr2ogr","-lco", db_schema, "-lco", overwrite_option,\
		"-nlt", geometry_name, "-skipfailures", "-f", output_format, db_connection, input_shp])


# directory full of shapefiles
shapefile_dir = os.path.realpath('../geodata/shp')

# define the ogr spatial driver type
shp_driver  = ogr.GetDriverByName('ESRI Shapefile')

# empty list to hold names of all shapefiles in directory
shapefile_list = []

for shp_file in on.listdir(shapefile_dir):
	if shp_file.endswith(".shp"):
		# append join path to file name to output "../geodata/shp/myshape.shp"
		full_shapefile_path = os.path.join(shapefile_dir,shp_file)
		shapefile_list.append(full_shapefile_path)

# loop over list of shapefiles running our import function
for each_shapefile in shapefile_list:
	run_shp2postgis(each_shapefile)
	print("import shapefile: " + each_shapefile)