#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 19:14:39 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array10 = numpy.array ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], \
                       dtype=numpy.float32)

# printing Numpy array
print (f'array10:\n{array10}')

# printing information
print (f'information:')
print (f'  ndim     = {array10.ndim}')
print (f'  size     = {array10.size}')
print (f'  shape    = {array10.shape}')
print (f'  dtype    = {array10.dtype}')
print (f'  itemsize = {array10.itemsize} byte')
