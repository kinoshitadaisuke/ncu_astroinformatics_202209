#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 19:15:05 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array11 = numpy.array ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], \
                       dtype='float32')

# printing Numpy array
print (f'array11:\n{array11}')

# printing information
print (f'information:')
print (f'  ndim     = {array11.ndim}')
print (f'  size     = {array11.size}')
print (f'  shape    = {array11.shape}')
print (f'  dtype    = {array11.dtype}')
print (f'  itemsize = {array11.itemsize} byte')
