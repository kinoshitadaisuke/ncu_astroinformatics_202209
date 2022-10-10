#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/10 20:44:00 (CST) daisuke>
#

# importing scipy module
import scipy.stats

# generating 10000 random numbers of Gaussian distribution
# of mean=100.0 and stddev=10.0
rg = scipy.stats.norm.rvs (loc=100.0, scale=10.0, size=10000)

# printing generated random numbers
print (f'generated random numbers:')
print (f'{rg}')

# calculation of statistical values
stat_values = scipy.stats.describe (rg)

print (f'statistical values:')
print (f'  number of data = {stat_values.nobs}')
print (f'  minimum value  = {stat_values.minmax[0]:8.4f}')
print (f'  maximum value  = {stat_values.minmax[1]:8.4f}')
print (f'  mean           = {stat_values.mean:8.4f}')
print (f'  variance       = {stat_values.variance:8.4f}')
print (f'  skewness       = {stat_values.skewness:8.4f}')
print (f'  kurtosis       = {stat_values.kurtosis:8.4f}')
