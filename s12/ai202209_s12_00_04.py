#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/02 22:17:46 (CST) daisuke>
#

# importing argparse module
import argparse

# importing sys module
import sys

#
# command-line argument analysis
#

# constructing parser object
desc = f"simple calculator"
parser = argparse.ArgumentParser (description=desc)

# choices
operators = ['+', '-', 'x', '/']

# adding options
parser.add_argument ('-a', '--number1', type=float, default=1.0, \
                     help=f"number 1 (default: 1.0)")
parser.add_argument ('-b', '--number2', type=float, default=2.0, \
                     help=f"number 2 (default: 2.0)")
parser.add_argument ('-p', '--operator', choices=operators, default='+', \
                     help=f"operator (choices: {operators}, default: +)")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
a  = args.number1
b  = args.number2
op = args.operator

#
# calculation
#

# arithmetic calculation
if (op == '+'):
    c = a + b
elif (op == '-'):
    c = a - b
elif (op == 'x'):
    c = a * b
elif (op == '/'):
    c = a / b
else:
    print (f"Something is wrong.")
    sys.exit ()

# printing result
print (f"a = {a}")
print (f"b = {b}")
if (op == '+'):
    print (f"c = a + b = {c}")
elif (op == '-'):
    print (f"c = a - b = {c}")
elif (op == 'x'):
    print (f"c = a x b = {c}")
elif (op == '/'):
    print (f"c = a / b = {c}")
