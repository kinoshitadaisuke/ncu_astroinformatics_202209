#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/02 22:07:46 (CST) daisuke>
#

# importing argparse module
import argparse

# importing math module
import math

#
# command-line argument analysis
#

# constructing parser object
desc = f"calculation of sine"
parser = argparse.ArgumentParser (description=desc)

# adding options
parser.add_argument ('-a', type=float, default=90.0, \
                     help=f"angle in degree (default: 90 deg)")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
a_deg = args.a

#
# calculation
#

# conversion from degree into radian
a_rad = a_deg / 180.0 * math.pi

# calculation of sine
sin_a = math.sin (a_rad)

# printing result
print (f"a       = {a_deg} deg")
print (f"sin (a) = {sin_a}")
