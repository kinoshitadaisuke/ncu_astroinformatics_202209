#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 15:25:07 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# Solar mass
M_S = astropy.constants.M_sun

# Jupiter mass
M_J = astropy.constants.M_jup

# Earth mass
M_E = astropy.constants.M_earth

# printing Solar mass, Jupiter mass, and Earth mass
print (M_S)
print ()
print (M_J)
print ()
print (M_E)
print ()

# amount of Jupiter mass in the unit of Solar mass
print (f'1 M_J = {M_J}\n      = {M_J / M_S:g} M_S')
