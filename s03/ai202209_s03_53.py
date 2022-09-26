#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 14:04:49 (CST) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.default_rng ()

# generating 10^6 random numbers of uniform distribution 
# between 10000 and 20000
r = rng.uniform (10000.0, 20000.0, 10**6)

# printing generated random numbers
print (f'{r}')

# printing number of data
print (f'number of data = {len (r):g}')

# statistical values calculated by numpy module
mean_n     = numpy.mean (r)
median_n   = numpy.median (r)
variance_n = numpy.var (r)
stddev_n   = numpy.std (r)

# printing statistical values
print (f'statistical values by Numpy:')
print (f'  mean     = {mean_n}')
print (f'  median   = {median_n}')
print (f'  variance = {variance_n}')
print (f'  stddev   = {stddev_n}')

# statistical values calculated by statistics module
mean_s     = statistics.fmean (r)
median_s   = statistics.median (r)
variance_s = statistics.pvariance (r)
stddev_s   = statistics.pstdev (r)

# printing statistical values
print (f'statistical values by statistics module:')
print (f'  mean     = {mean_s}')
print (f'  median   = {median_s}')
print (f'  variance = {variance_s}')
print (f'  stddev   = {stddev_s}')
