#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/10 10:16:19 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.stats

# generating 10000 random numbers of Gaussian distribution
# of mean=100.0 and stddev=10.0
rg = scipy.stats.norm.rvs (loc=100.0, scale=10.0, size=10000)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{rg}')

# calculation of arithmetic mean of distribution
mean = scipy.stats.tmean (rg)

# calculation of standard deviation of distribution
stddev = scipy.stats.tstd (rg)

# calculation of first moment about the mean
moment_1 = scipy.stats.moment (rg, moment=1)

# calculation of second moment about the mean
moment_2 = scipy.stats.moment (rg, moment=2)

# calculation of skewness
skew = scipy.stats.skew (rg)

# printing arithmetic mean and standard deviation of distribution
print (f'statistical values:')
print (f'  mean                 = {mean:8.4f}')
print (f'  stddev               = {stddev:8.4f}')
print (f'  first moment         = {moment_1:8.4f}')
print (f'  second moment        = {moment_2:8.4f}')
print (f'  sqrt (second moment) = {numpy.sqrt (moment_2):8.4f}')
print (f'  skewness             = {skew:8.4f}')
