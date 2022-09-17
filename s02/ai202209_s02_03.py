#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/17 18:46:17 (CST) daisuke>
#

# importing argparse module
import argparse

# command-line argument analysis
parser = argparse.ArgumentParser (description='adding two integers')
parser.add_argument ('-a', type=int, default=1, help='number 1')
parser.add_argument ('-b', type=int, default=1, help='number 2')
args = parser.parse_args ()

# input parameters
a = args.a
b = args.b

# calculation
c = a + b

# printing result
print (f'{a} + {b} = {c}')
