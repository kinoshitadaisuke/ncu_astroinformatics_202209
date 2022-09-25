#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 20:03:44 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with 10 elements all equal to zeros
array16 = numpy.zeros ( (10,) )

# printing Numpy array
print (f'array16:\n{array16}')

# printing information
print (f'information:')
print (f'  ndim     = {array16.ndim}')
print (f'  size     = {array16.size}')
print (f'  shape    = {array16.shape}')
print (f'  dtype    = {array16.dtype}')
print (f'  itemsize = {array16.itemsize} byte')
