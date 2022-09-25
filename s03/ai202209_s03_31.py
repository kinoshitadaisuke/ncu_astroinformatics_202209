#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 22:26:42 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays
a = numpy.array ([ [1, 2], [3, 4] ])
b = numpy.array ([ [5, 6], [7, 8] ])

# printing a and b
print (f'a:\n{a}')
print (f'b:\n{b}')

# calculation
# no need of using "for"
c = a + b

# printing c
print (f'c = a + b:\n{c}')
