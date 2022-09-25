#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:32:45 (CST) daisuke>
#

# importing numpy module
import numpy

# making a Numpy array (ndarray) using numpy.linspace ()
array22 = numpy.linspace (0, 10, 11)

# printing Numpy array
print (f'array22:\n{array22}')

# printing information
print (f'information:')
print (f'  ndim     = {array22.ndim}')
print (f'  size     = {array22.size}')
print (f'  shape    = {array22.shape}')
print (f'  dtype    = {array22.dtype}')
print (f'  itemsize = {array22.itemsize} byte')

# appending one more data to "array22"
array22 = numpy.append (array22, 11.0)

# printing Numpy array
print (f'array22:\n{array22}')

# printing information
print (f'information:')
print (f'  ndim     = {array22.ndim}')
print (f'  size     = {array22.size}')
print (f'  shape    = {array22.shape}')
print (f'  dtype    = {array22.dtype}')
print (f'  itemsize = {array22.itemsize} byte')
