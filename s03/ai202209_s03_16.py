#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 20:04:49 (CST) daisuke>
#

# importing numpy module
import numpy

# making a 2-dim Numpy array (ndarray) with elements all equal to zeros
array17 = numpy.zeros ( (3, 3) )

# printing Numpy array
print (f'array17:\n{array17}')

# printing information
print (f'information:')
print (f'  ndim     = {array17.ndim}')
print (f'  size     = {array17.size}')
print (f'  shape    = {array17.shape}')
print (f'  dtype    = {array17.dtype}')
print (f'  itemsize = {array17.itemsize} byte')
