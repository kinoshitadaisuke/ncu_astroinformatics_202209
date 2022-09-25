#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 18:55:14 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array7 = numpy.array ([-5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5], \
                      dtype=numpy.dtype ('i2') )

# printing Numpy array
print (f'array7:\n{array7}')

# printing information
print (f'information:')
print (f'  ndim     = {array7.ndim}')
print (f'  size     = {array7.size}')
print (f'  shape    = {array7.shape}')
print (f'  dtype    = {array7.dtype}')
print (f'  itemsize = {array7.itemsize} byte')
