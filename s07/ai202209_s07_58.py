#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 21:51:27 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.stats

# parameters for random number generation
mean   = 1000.0
stddev = 30.0
n      = 10**4

# generation of a set of random number of Gaussian distribution
rng  = numpy.random.default_rng ()
data = rng.normal (loc=mean, scale=stddev, size=n)

# printing generated data
print (f'Genearated random numbers:')
print (f'{data}')
print (f'Number of random numbers generated: {len (data)}')
