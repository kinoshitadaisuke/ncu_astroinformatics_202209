#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 11:06:30 (CST) daisuke>
#

# importing random module
import random

# initialisation of random number generator
random.seed ()

#
# generating 10 random numbers of uniform distribution between 0 and 1
#

# generating 10 random numbers
print (f'10 random numbers of uniform distribution between 0 and 1')
for i in range (10):
    # generation of a random number of uniform distribution between 0 and 1
    r = random.random ()
    # printing generated random number
    print (f'  {r:15.13f}')

#
# generating 10 random numbers of uniform distribution between 100 and 200
#

# parameters
a = 100.0
b = 200.0

# generating 10 random numbers
print (f'10 random numbers of uniform distribution between {a} and {b}')
for i in range (10):
    # generation of a random number of uniform distribution between 100 and 200
    r = random.uniform (a, b)
    # printing generated random number
    print (f'  {r:15.11f}')

#
# generating 10 random numbers of Gaussian dist. of mean=100 and stddev=10
#

# parameters
mean   = 100.0
stddev = 10.0

# generating 10 random numbers
print (f'10 random numbers of Gaussian distribution', \
       f'of mean={mean} and stddev={stddev}')
for i in range (10):
    # generation of a random number of Gaussian distribution
    r = random.gauss (mean, stddev)
    # printing generated random number
    print (f'  {r:15.11f}')
