#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 00:32:00 (CST) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.default_rng ()

# generating 10 random numbers of uniform distribution between 100 and 200
r = rng.uniform (100.0, 200.0, 10)

# printing generated random numbers
print (f'{r}')
