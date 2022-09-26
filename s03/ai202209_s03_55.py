#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 14:27:59 (CST) daisuke>
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

# constructing a histogram
hist = numpy.histogram (r, bins=20, range=(9000.0, 11000.0))

# printing histogram
for i in range (20):
    print (f'{hist[1][i]:7.1f}-{hist[1][i]+100:7.1f} : {hist[0][i]:6d}')
