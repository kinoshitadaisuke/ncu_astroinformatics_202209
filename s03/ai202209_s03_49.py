#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 00:27:26 (CST) daisuke>
#

# importing numpy module
import numpy

# random number generator
rng = numpy.random.default_rng ()

# generating a random number of uniform distribution between 0 and 1
r = rng.random ()

# printing generated random numbers
print (f'{r}')
