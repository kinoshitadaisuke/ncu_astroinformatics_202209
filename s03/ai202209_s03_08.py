#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 19:09:55 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array9 = numpy.array ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], \
                      dtype=numpy.dtype ('f4') )

# printing Numpy array
print (f'array9:\n{array9}')

# printing information
print (f'information:')
print (f'  ndim     = {array9.ndim}')
print (f'  size     = {array9.size}')
print (f'  shape    = {array9.shape}')
print (f'  dtype    = {array9.dtype}')
print (f'  itemsize = {array9.itemsize} byte')
