#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 18:28:08 (CST) daisuke>
#

# importing math module
import math

# initialisation of a variable "a"
a_deg = 0.0

# calculating sin (0 deg), sin (15 deg), sin (30 deg), ..., sin (180 deg)
while (a_deg <= 180.0):
    # converting from degree into radian
    a_rad = math.radians (a_deg)
    # calculation of sine
    sin_a = math.sin (a_rad)
    # printing result of calculation
    print (f'sin ({a_deg:5.1f} deg) = {sin_a:8.6f}')
    # incrementing variable "a"
    a_deg += 15.0
