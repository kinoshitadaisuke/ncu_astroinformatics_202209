#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/25 21:57:34 (CST) daisuke>
#

# importing numpy module
import numpy

# making Numpy arrays using numpy.linspace ()
a = numpy.linspace (4.0, 40.0, 10)
b = numpy.linspace (2.0, 20.0, 10)

# printing a and b
print (f'a = {a}')
print (f'b = {b}')

# calculation
# no need of using "for"
c = a / b

# printing c
print (f'c = a / b = {c}')
