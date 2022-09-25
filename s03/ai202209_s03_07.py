#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 19:08:47 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array8 = numpy.array ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], \
                      dtype=numpy.int16)

# printing Numpy array
print (f'array8:\n{array8}')

# printing information
print (f'information:')
print (f'  ndim     = {array8.ndim}')
print (f'  size     = {array8.size}')
print (f'  shape    = {array8.shape}')
print (f'  dtype    = {array8.dtype}')
print (f'  itemsize = {array8.itemsize} byte')
