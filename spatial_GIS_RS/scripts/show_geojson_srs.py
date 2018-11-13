#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import json

geojson_yes_crs = '../geodata/geojson/schools.geojson'
geojson_no_crs = '../geodata/geojson/golfcourses_bc.geojson'

with open(geojson_yes_crs) as my_geojson:
	data = json.load(my_geojson)

# check if crs is in the data python dictionary data
# if yes print the crs to screen
# else print NO to screen and print geojson data type
if 'crs' in data:
	print("The CRS is : " + data['crs']['properties'][
		'name'])
else:
	print("+++++++++ no crs tag in the file +++++++")
	print("+++++++++ assume EPSG:4326 +++++++++++++")
	if "type" in data:
		print("Current GeoJSON data type is : " + data['type'])