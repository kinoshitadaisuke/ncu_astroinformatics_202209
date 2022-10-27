#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 16:07:42 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s

# 900 sec
t = 900.0 * u_sec

# printing t
print (f't = {t}')

# value and unit of t
print (f'value of t = {t.value}')
print (f'unit of t  = {t.unit}')
