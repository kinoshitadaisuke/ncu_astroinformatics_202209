#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 20:27:18 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.stats

# output file name
file_output = 'ai202209_s05_48.data'

# generating random numbers
err = scipy.stats.norm.rvs (loc=0.0, scale=5.0, size=32)

# function for a line
def curve (x):
    # coefficients
    a = 2.0
    b = 13.0
    c = 5.0
    # line
    y = a * (x - b)**2 + c
    # returning y
    return y

# synthetic data for least-squares method
data_x   = numpy.linspace (0.0, 31.0, 32)
data_y   = curve (data_x) + err
data_err = numpy.absolute (err)
for i in range (0, 7):
    data_y[i]   -= 50.0
    data_err[i] += 50.0
for i in range (25, 32):
    data_y[i]   += 50.0
    data_err[i] += 50.0

# opening file for writing
with open (file_output, 'w') as fh:
    # writing generated synthetic data into file
    for i in range (len (data_x)):
        fh.write (f'{data_x[i]:8.3f}  {data_y[i]:8.3f}  {data_err[i]:8.3f}\n')
