#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 00:13:11 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array
a = numpy.array ([5.0, 3.0, 7.0, 4.0, 9.0, 8.0, 1.0, 6.0, 2.0, 0.0])

# printing "a"
print (f'a:\n{a}')

# sorting by descending order
b = numpy.flip (numpy.sort (a))

# printing "b"
print (f'b = flip (sort (a)):\n{b}')
