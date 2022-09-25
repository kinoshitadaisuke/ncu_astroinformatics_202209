#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 23:17:43 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.array ([ [0.0, 1.0, 2.0], [3.0, 4.0, 5.0], [6.0, 7.0, 8.0] ])

# printing A
print (f'a:\n{a}')

# accessing to an element by indexing
print (f'a[0][0] = {a[0][0]}')
print (f'a[1][2] = {a[1][2]}')
print (f'a[1,2] = {a[1,2]}')
print (f'a[0,-1] = {a[0,-1]}')
print (f'a[0] = {a[0]}')
print (f'a[-1] = {a[-1]}')
