#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 22:43:29 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays (2x2 matrix)
A = numpy.array ([ [1.0, 2.0], [3.0, 4.0] ])
B = numpy.array ([ [4.0, 2.0], [1.0, 3.0] ])

# printing A and B
print (f'A:\n{A}')
print (f'B:\n{B}')

# the other way to take a matrix product
C = numpy.matmul (A, B)

# printing C
print (f'C = matmul (A, B):\n{C}')
