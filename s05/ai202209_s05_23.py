#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/14 06:15:00 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# function of standard normal distribution
def curve (x):
    # curve
    y = numpy.exp (-x**2 / 2.0) / numpy.sqrt (2.0 * numpy.pi)
    # returning a value
    return (y)

# numerical integration
#   numpy.NINF = negative infinity
#   numpy.PINF = positive infinity
result0 = scipy.integrate.quad (curve, numpy.NINF, numpy.PINF)
result1 = scipy.integrate.quad (curve, -1.0, +1.0)
result2 = scipy.integrate.quad (curve, -2.0, +2.0)
result3 = scipy.integrate.quad (curve, -3.0, +3.0)
result4 = scipy.integrate.quad (curve, -4.0, +4.0)
result5 = scipy.integrate.quad (curve, -5.0, +5.0)

# printing result of numerical integration
print (f'integ. of std normal func. from -inf to +inf:\n', \
       f' I0 = {result0[0]} +/- {result0[1]}')
print (f'integ. of std normal func. from -1 to +1:\n', \
       f' I1 = {result1[0]} +/- {result1[1]}')
print (f'integ. of std normal func. from -2 to +2:\n', \
       f' I2 = {result2[0]} +/- {result2[1]}')
print (f'integ. of std normal func. from -3 to +3:\n', \
       f' I3 = {result3[0]} +/- {result3[1]}')
print (f'integ. of std normal func. from -4 to +4:\n', \
       f' I4 = {result4[0]} +/- {result4[1]}')
print (f'integ. of std normal func. from -5 to +5:\n', \
       f' I5 = {result5[0]} +/- {result5[1]}')
