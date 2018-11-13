import pysal

#####################################
#       CONTIGUITY BASED WIGHTS     #
#####################################

#example
#=======
# Using the default ROOK criterion
print('Using ROOK Criteion -Default. Use pysal.lat2W(rook=False) for QUEEN criterion')
w = pysal.lat2W(5,5) # A  5 by 5 lattice - composed of 25 spatial units
print(w.n) #number of spatial units
print(w.pct_nonzero) # sparseness of the matrix
#The key attributes used to store contiguity relations in W are the
# neighbors and weights attributes.
print(w.weights[0]) # Show weights of the neigbors of feature id=0
print(w.neighbors[0]) # show no. of neighbors for feature id=0. Shows feature id's for the neighbors
print(w.neighbors[5])
# Histogram attribute is a set of tuples indicating cardinality of the neighbor relations.
# ie [(2,4),(3,12,(4,9)] -> 4 units that have 2 neighbors (corner cells),
#   12 units with 3 neighbors (edge cells) & 9 units with 4 neighbors(internal cells)
print(w.histogram)


