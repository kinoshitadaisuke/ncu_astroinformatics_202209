#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 19:27:58 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array12 = numpy.array ([1.0 + 2.0j, 3.0j, 4.0, 5.0 - 6.0j, -7.0 + 8.0j, \
                        -9.0 - 10.0j, -11.0j, -12.0, 13.0 + 14.0j, 15.0j], \
                       dtype=numpy.dtype ('c8'))

# printing Numpy array
print (f'array12:\n{array12}')

# printing information
print (f'information:')
print (f'  ndim     = {array12.ndim}')
print (f'  size     = {array12.size}')
print (f'  shape    = {array12.shape}')
print (f'  dtype    = {array12.dtype}')
print (f'  itemsize = {array12.itemsize} byte')
