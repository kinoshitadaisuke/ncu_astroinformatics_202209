#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 11:47:09 (CST) daisuke>
#

# importing statistics module
import statistics

# generation of a synthetic data set
dataset1 = [ 6.0, 7.0, 8.0, 9.0, 9.0, \
             10.0, 10.0, 11.0, 11.0, 11.0, \
             12.0, 13.0, 14.0]

# printing data set
print (f'dataset1:\n{dataset1}')

# calculation of mean
mean = statistics.fmean (dataset1)

# printing calculated mean
print (f'mean of dataset1   = {mean}')

# calculation of median
median = statistics.median (dataset1)

# printing calculated median
print (f'median of dataset1 = {median}')

# calculation of mode
mode = statistics.mode (dataset1)

# printing calculated mode
print (f'mode of dataset1   = {mode}')

# calculation of sample variance
var = statistics.variance (dataset1)

# printing calculated sample variance
print (f'sample variance of dataset1               = {var}')

# calculation of population variance
pvar = statistics.pvariance (dataset1)

# printing calculated population variance
print (f'population variance of dataset1           = {pvar}')

# calculation of sample standard deviation
stddev = statistics.stdev (dataset1)

# printing calculated sample variance
print (f'sample standard deviation of dataset1     = {stddev}')

# calculation of population standard deviation
pstddev = statistics.pstdev (dataset1)

# printing calculated population standard deviation
print (f'population standard deviation of dataset1 = {pstddev}')
