#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/14 06:42:33 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# function of f(x) = 2x + 1
def line (x):
    # curve
    y = 2.0 * x + 1
    # returning a value
    return (y)

# data points
data_x = numpy.linspace (0.0, 1.0, 1001)
data_y = line (data_x)

# printing data_x and data_y
print (f'data_x = {data_x}')
print (f'data_y = {data_y}')

# numerical integration of given data points by trapezoidal rule
I = scipy.integrate.trapezoid (data_y, x=data_x)

# printing result of numerical integration
print (f'I = {I}')
