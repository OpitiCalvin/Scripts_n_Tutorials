#!usr/bin/python

# This script uses PYSAL package with its associated sample data.
# This script shows how to load or read spatial data, of varying formats/extensions.

import pysal

#Reading of SHAPEFILES
shp = pysal.open(pysal.examples.get_path('10740.shp'))
#poly = shp.next()
#print(type(poly))
print(len(shp))
print(shp.get(len(shp)-1).id)
polys = list(shp)
print(len(polys))


#Reading of DBF Files
db = pysal.open(pysal.examples.get_path('10740.dbf'),'r')
print(db.header)
print(db.field_spec)
#print(db.next())
print(db[0])
print(db[0:3])
print(db[0:5,1])
print(db[0:5,0:2])
print(db[-1,-1])
