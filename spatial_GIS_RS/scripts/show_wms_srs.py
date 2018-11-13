#!/usr/bin/env python3
#-*- coding: utf-8 -*-

try:
	from owslib.wms import WebMapService
except:
	print("[ERROR] - This script requires 'owslib' package. To install, use the command 'pip install owslib' ")

url = "http://ogc.bgs.ac.uk/cgi-bin/BGS_1GE_Geology/wms"

get_wms_url = WebMapService(url)
crs_list = get_wms_url.contents['GBR_Kilmarnock_BGS_50K_CompressibleGround'].crsOptions

print(crs_list)