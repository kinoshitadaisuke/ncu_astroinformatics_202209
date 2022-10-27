#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 15:31:10 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# Solar radius
R_S = astropy.constants.R_sun

# Jupiter radius
R_J = astropy.constants.R_jup

# Earth radius
R_E = astropy.constants.R_earth

# printing Solar radius, Jupiter radius, and Earth radius
print (R_S)
print ()
print (R_J)
print ()
print (R_E)
print ()

# amount of 1 Earth radius in the unit of Solar radius
print (f'1 R_E = {R_E:g}\n      = {R_E / R_S:g} R_S')
