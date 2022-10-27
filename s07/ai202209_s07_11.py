#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 16:11:50 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_sec = astropy.units.s
u_min = astropy.units.min
u_hr  = astropy.units.h

# t1 = 3600 sec
t1 = 3600.0 * u_sec

# t2 = 900 sec
t2 = 900.0 * u_sec

# calculation of t3 = t1 - t2
t3 = t1 - t2

# conversion of unit
t4 = t3.to (u_min)
t5 = t3.to (u_hr)

# printing t1, t2, and t3
print (f't1 = {t1}')
print (f't2 = {t2}')
print (f't3 = t1 - t2 = {t3} = {t4} = {t5}')
