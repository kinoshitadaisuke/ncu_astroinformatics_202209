#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 19:40:30 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array15 = numpy.array (['Ceres', 'Pallas', 'Juno', 'Vesta', 'Astraea', \
                        'Hebe', 'Iris', 'Flora', 'Metis', 'Hygiea'], \
                       dtype=numpy.dtype ('U10') )

# printing Numpy array
print (f'array15:\n{array15}')

# printing information
print (f'information:')
print (f'  ndim     = {array15.ndim}')
print (f'  size     = {array15.size}')
print (f'  shape    = {array15.shape}')
print (f'  dtype    = {array15.dtype}')
print (f'  itemsize = {array15.itemsize} byte')
