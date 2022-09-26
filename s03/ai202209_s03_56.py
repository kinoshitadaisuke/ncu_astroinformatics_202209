#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 14:53:29 (CST) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.default_rng ()

# generating 10^6 random numbers of Gaussian distribution 
# of mean = 10000.0 and stddev = 300.0
r = rng.normal (10000.0, 300.0, 10**6)

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

# finding maximum value
maximum = numpy.amax (r)

# finding minimum value
minimum = numpy.amin (r)

# printing maximum and minimum
print (f'maximum and minimum:')
print (f'  maximum = {maximum}')
print (f'  minimum = {minimum}')
