#!/usr/bin/env python3
# -*- coding: utf-8 -*-
 
import subprocess

# database options
db_schema = "SCHEMA=public"
overwrite_option = "OVERWRITE=YES"
geom_type = "MULTILINESTRING"
output_format = "PostgreSQL"

# database connection string
db_connection = """PG:host=localhost port=5432 user=calvin password=calv1nw3dd13 dbname=py_test"""

# input shapefile
input_shp = "../geodata/shp/bikeways.shp"

# call ogr2ogr from python
subprocess.call(["ogr2ogr","-lco", db_schema,"-lco" ,overwrite_option,\
	"-nlt", geom_type,"-f", output_format, db_connection,input_shp])