#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:46:08 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
array23 = numpy.linspace (0, 10, 11)
array24 = numpy.linspace (11, 20, 10)

# printing Numpy array
print (f'array23:\n{array23}')

# printing information
print (f'information:')
print (f'  ndim     = {array23.ndim}')
print (f'  size     = {array23.size}')
print (f'  shape    = {array23.shape}')
print (f'  dtype    = {array23.dtype}')
print (f'  itemsize = {array23.itemsize} byte')

# printing Numpy array
print (f'array24:\n{array24}')

# printing information
print (f'information:')
print (f'  ndim     = {array24.ndim}')
print (f'  size     = {array24.size}')
print (f'  shape    = {array24.shape}')
print (f'  dtype    = {array24.dtype}')
print (f'  itemsize = {array24.itemsize} byte')

# concatenating array23 and array24
array25 = numpy.concatenate ([array23, array24])

# printing Numpy array
print (f'array25:\n{array25}')

# printing information
print (f'information:')
print (f'  ndim     = {array25.ndim}')
print (f'  size     = {array25.size}')
print (f'  shape    = {array25.shape}')
print (f'  dtype    = {array25.dtype}')
print (f'  itemsize = {array25.itemsize} byte')
