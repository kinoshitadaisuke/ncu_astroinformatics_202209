#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 20:07:07 (CST) daisuke>
#

# importing numpy module
import numpy

# making a 3-dim Numpy array (ndarray) with elements all equal to zeros
array18 = numpy.zeros ( (3, 3, 3) )

# printing Numpy array
print (f'array18:\n{array18}')

# printing information
print (f'information:')
print (f'  ndim     = {array18.ndim}')
print (f'  size     = {array18.size}')
print (f'  shape    = {array18.shape}')
print (f'  dtype    = {array18.dtype}')
print (f'  itemsize = {array18.itemsize} byte')
