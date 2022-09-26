#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/26 15:16:02 (CST) daisuke>
#

# importing numpy module
import numpy

# importing statistics module
import statistics

# random number generator
rng = numpy.random.default_rng ()

# generating 30 random numbers of Gaussian distribution 
# of mean = 1000.0 and stddev = 100.0
r = rng.normal (1000.0, 100.0, 30)

# adding outliers
r[10] += 1500.0
r[20] += 2000.0

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

# finding data outside of [ mean - 3.0 * stddev, mean + 3.0 * stddev ]
llimit = median_n - 3.0 * stddev_n
ulimit = median_n + 3.0 * stddev_n

# making an empty array for a mask
mask = numpy.array ([])

# examining data
for i in range (len (r)):
    if ( (r[i] < llimit) or (r[i] > ulimit) ):
        mask = numpy.append (mask, True)
    else:
        mask = numpy.append (mask, False)

# printing mask
print (f'mask:\n{mask}')

# making masked array
r_masked = numpy.ma.array (r, mask=mask)

# printing masked array
print (f'r_masked:\n{r_masked}')

# calculation of statistical values
mean_m     = numpy.ma.mean (r_masked)
median_m   = numpy.ma.median (r_masked)
variance_m = numpy.ma.var (r_masked)
stddev_m   = numpy.ma.std (r_masked)

# printing statistical values
print (f'statistical values by Numpy.ma:')
print (f'  mean     = {mean_m}')
print (f'  median   = {median_m}')
print (f'  variance = {variance_m}')
print (f'  stddev   = {stddev_m}')
