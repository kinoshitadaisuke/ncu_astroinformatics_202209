#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 11:49:37 (CST) daisuke>
#

# importing statistics module
import statistics

# importing random module
import random

# number of data in dataset2
ndata = 1000

# making an empty list for a synthetic dataset
dataset2 = []

# distribution parameters
a = 100.0
b = 200.0

# generation of a synthetic dataset using random number generator
for i in range (ndata):
    # generating a random number
    r = random.uniform (a, b)
    # appending generated random number to list
    dataset2.append (r)

# printing generated dataset
print (f'dataset2:')
for i in range (ndata):
    if ( (i > 4) and (i < ndata - 1) ):
        continue
    elif (i == ndata - 1):
        print (f'  ...')
    print (f'  {dataset2[i]}')

# number of data in dataset2
print (f'number of data in dataset2 = {len (dataset2)}')
        
# calculation of mean, median, and standard deviation
mean   = statistics.fmean (dataset2)
median = statistics.median (dataset2)
stddev = statistics.stdev (dataset2)

# printing mean, median, and standard deviation
print (f'mean of dataset2   = {mean}')
print (f'median of dataset2 = {median}')
print (f'stddev of dataset2 = {stddev}')
