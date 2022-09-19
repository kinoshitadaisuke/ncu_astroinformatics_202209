#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 11:51:01 (CST) daisuke>
#

# importing statistics module
import statistics

# importing random module
import random

# number of data in dataset2
ndata = 1000

# making an empty list for a synthetic dataset
dataset3 = []

# distribution parameters
mean   = 100.0
stddev = 10.0

# generation of a synthetic dataset using random number generator
for i in range (ndata):
    # generating a random number
    r = random.gauss (mean, stddev)
    # appending generated random number to list
    dataset3.append (r)

# printing generated dataset
print (f'dataset3:')
for i in range (ndata):
    if ( (i > 4) and (i < ndata - 1) ):
        continue
    elif (i == ndata - 1):
        print (f'  ...')
    print (f'  {dataset3[i]}')

# number of data in dataset3
print (f'number of data in dataset3 = {len (dataset3)}')
        
# calculation of mean, median, and standard deviation
mean   = statistics.fmean (dataset3)
median = statistics.median (dataset3)
stddev = statistics.stdev (dataset3)

# printing mean, median, and standard deviation
print (f'mean of dataset3   = {mean}')
print (f'median of dataset3 = {median}')
print (f'stddev of dataset3 = {stddev}')
