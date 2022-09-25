#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 18:35:00 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) with a specified data type
array6 = numpy.array ([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10], \
                      dtype=numpy.dtype ('u1') )

# printing Numpy array
print (f'array6:\n{array6}')

# printing information
print (f'information:')
print (f'  ndim     = {array6.ndim}')
print (f'  size     = {array6.size}')
print (f'  shape    = {array6.shape}')
print (f'  dtype    = {array6.dtype}')
print (f'  itemsize = {array6.itemsize} byte')
