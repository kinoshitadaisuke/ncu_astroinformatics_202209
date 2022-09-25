#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:24:22 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.logspace ()
array21 = numpy.logspace (0, 3, 10)

# printing Numpy array
print (f'array21:\n{array21}')

# printing information
print (f'information:')
print (f'  ndim     = {array21.ndim}')
print (f'  size     = {array21.size}')
print (f'  shape    = {array21.shape}')
print (f'  dtype    = {array21.dtype}')
print (f'  itemsize = {array21.itemsize} byte')
