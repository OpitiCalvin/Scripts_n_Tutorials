#!/usr/bin/env python3
#-*- coding: utf-8 -*-

import urllib.request
import os

def get_epsg_code(epsg):
	"""
	Get the ESRI formatted .prj definition

	Usage: get_epsg_code(4326)

	We use the http://spatialreference.org/ref/epsg/4326/esriwkt/
	"""

	proxy = urllib.request.ProxyHandler({'http':r'http://students\1408593:cl1pp3rnat10n@proxyss.wits.ac.za:80'})
	auth = urllib.request.HTTPBasicAuthHandler()
	opener = urllib.request.build_opener(proxy,auth,urllib.request.HTTPHandler)
	urllib.request.install_opener(opener)


	f = urllib.request.urlopen("http://spatialreference.org/ref/epsg/{0}/esriwkt/".format(epsg))
	return (f.read())

# Shapefile filename must equal  the new .prj filename
shp_filename = "../geodata/UTM_Zone_Boundaries"

# Here we write out a new .prj file with the same name
# as our Shapefile named 'UTM_Zone_Boundaries' in this example

with open('../geodata/{0}.prj'.format(shp_filename), "w") as prj:
	epsg_code = get_epsg_code(4326)
	prj.write(str(epsg_code))
	print("Done writing projection definition.")