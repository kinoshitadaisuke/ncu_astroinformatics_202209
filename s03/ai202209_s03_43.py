#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 23:42:51 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.linspace (0.0, 10.0, 11)

# printing "a"
print (f'a:\n{a}')

# trying b = a
b = a

# printing "b"
print (f'b:\n{b}')

# IDs of "a" and "b"
print (f'id (a) = {id (a)}')
print (f'id (b) = {id (b)}')

# changing "a[5]"
a[5] += 10

# printing "a"
print (f'a:\n{a}')

# printing "b"
print (f'b:\n{b}')

# IDs of "a" and "b"
print (f'id (a) = {id (a)}')
print (f'id (b) = {id (b)}')
