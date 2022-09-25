#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 18:09:35 (CST) daisuke>
#

# importing numpy
import numpy

# making a Numpy array (ndarray)
array4 = numpy.array ([ [0.0, 1.0, 2.0, 3.0, 4.0], \
                        [5.0, 6.0, 7.0, 8.0, 9.0], \
                        [10.0, 11.0, 12.0, 13.0, 14.0] ])

# printing Numpy array
print (f'array4 = {array4}')

# type of "array4"
type_array4 = type (array4)

# printing type of "array4"
print (f'type of "array4" = {type_array4}')

# dimension of "array4"
ndim_array4 = array4.ndim

# size of "array4"
size_array4 = array4.size

# shape of "array4"
shape_array4 = array4.shape

# data type of elements in "array4"
dtype_array4 = array4.dtype

# size of one element in "array4"
itemsize_array4 = array4.itemsize

# printing information
print (f'information of "array4":')
print (f'  ndim     = {ndim_array4}')
print (f'  size     = {size_array4}')
print (f'  shape    = {shape_array4}')
print (f'  dtype    = {dtype_array4}')
print (f'  itemsize = {itemsize_array4} byte')
