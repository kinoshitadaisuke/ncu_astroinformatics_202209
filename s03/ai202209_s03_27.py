#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:59:48 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a = numpy.linspace (0.0, 10.0, 11)

# printing a
print (f'a = {a}')

# calculation
# no need of using "for"
b = a**2

# printing b
print (f'b = a**2 = {b}')
