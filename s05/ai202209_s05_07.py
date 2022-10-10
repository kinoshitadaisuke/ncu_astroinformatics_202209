#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/10 20:43:27 (CST) daisuke>
#

# importing scipy module
import scipy.stats

# generating 10000 random numbers of Gaussian distribution
# of mean=100.0 and stddev=10.0
rg = scipy.stats.norm.rvs (loc=100.0, scale=10.0, size=10000)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{rg}')

# finding minimum value
tmin = scipy.stats.tmin (rg)

# finding maximum value
tmax = scipy.stats.tmax (rg)

# printing minimum and maximum values
print (f'statistical values:')
print (f'  tmin = {tmin:8.4f}')
print (f'  tmax = {tmax:8.4f}')
