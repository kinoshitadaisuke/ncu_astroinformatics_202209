#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:22:47 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.linspace ()
array20 = numpy.linspace (100, 200, 11)

# printing Numpy array
print (f'array20:\n{array20}')

# printing information
print (f'information:')
print (f'  ndim     = {array20.ndim}')
print (f'  size     = {array20.size}')
print (f'  shape    = {array20.shape}')
print (f'  dtype    = {array20.dtype}')
print (f'  itemsize = {array20.itemsize} byte')
