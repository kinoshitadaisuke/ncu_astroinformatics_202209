#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 18:06:05 (CST) daisuke>
#

# importing numpy
import numpy

# making a Numpy array (ndarray)
array3 = numpy.array ([0, 1, 2, 3, 4])

# printing Numpy array
print (f'array3 = {array3}')

# type of "array3"
type_array3 = type (array3)

# printing type of "array3"
print (f'type of "array3" = {type_array3}')

# dimension of "array3"
ndim_array3 = array3.ndim

# size of "array3"
size_array3 = array3.size

# shape of "array3"
shape_array3 = array3.shape

# data type of elements in "array3"
dtype_array3 = array3.dtype

# size of one element in "array3"
itemsize_array3 = array3.itemsize

# printing information
print (f'information of "array3":')
print (f'  ndim     = {ndim_array3}')
print (f'  size     = {size_array3}')
print (f'  shape    = {shape_array3}')
print (f'  dtype    = {dtype_array3}')
print (f'  itemsize = {itemsize_array3} byte')
