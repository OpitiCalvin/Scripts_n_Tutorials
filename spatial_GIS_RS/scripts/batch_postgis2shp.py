#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import subprocess
import os

# folder 2 hold output shapefiles
destination_dir = os.path.realpath('../geodata/temp')

# list of postgis tables
postgis_tables_list = ["bikeways","highest_mountains"]

# database connection parameters
db_connection = """PG:host=localhost port=5432 user=calvin dbname=py_test password=password active_schema=public"""

output_format = "ESRI shapefile"

# check if destination directory exists
if not os.path.isdir(destination_dir):
	os.mkdir(destination_dir)
	for table in postgis_tables_list:
		subprocess.call(["ogr2ogr","-f", output_format, destination_dir, db_connection, table])
		print("Running ogr2ogr on table: " + table)
else:
	print("Destination directory " + destination_dir +" already exists. Please remove it the run again.")

# commandline call without using python will look like this
# ogr2ogr -f "ESRI Shapefile" mydatadump \
# PG:"host=myhost user=myloginname dbname=mydbname password=mypassword" neighborhood parcels