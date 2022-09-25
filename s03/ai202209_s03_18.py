#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:20:47 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.arange ()
array19 = numpy.arange (0, 10, 2)

# printing Numpy array
print (f'array19:\n{array19}')

# printing information
print (f'information:')
print (f'  ndim     = {array19.ndim}')
print (f'  size     = {array19.size}')
print (f'  shape    = {array19.shape}')
print (f'  dtype    = {array19.dtype}')
print (f'  itemsize = {array19.itemsize} byte')
