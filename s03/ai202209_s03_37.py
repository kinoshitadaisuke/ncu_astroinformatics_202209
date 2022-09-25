#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 22:54:03 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy array (2x2 matrix)
A = numpy.array ([ [1.0, 2.0], [3.0, 4.0] ])

# printing A
print (f'A:\n{A}')

# making Numpy array (2x2 unit matrix)
E2 = numpy.identity (2)

# printing E2
print (f'E2:\n{E2}')

# calculation
B = A @ E2

# printing B
print (f'B = A @ E2:\n{B}')

# making Numpy array (3x3 matrix)
C = numpy.array ([ [1.0, 2.0, 3.0], [4.0, 5.0, 6.0], [7.0, 8.0, 9.0] ])

# printing C
print (f'C:\n{C}')

# making Numpy array (3x3 unit matrix)
E3 = numpy.identity (3)

# printing E3
print (f'E3:\n{E3}')

# calculation
D = E3 @ C

# printing D
print (f'D = E3 @ C:\n{D}')
