#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 14:56:29 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# speeed of light in vacuum
c = astropy.constants.c

# calculation
v = 0.1 * c

# printing c and v
print (f'c = {c}')
print (f'v = 0.1 * {c}\n  = {v}')
