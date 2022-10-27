#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 16:39:45 (CST) daisuke>
#

# importing astropy module
import astropy.units

# units
u_m         = astropy.units.m
u_kg        = astropy.units.kg
u_kg_per_m3 = u_kg / u_m**3

# density in kg/m^3
rho1 = 3000.0 * u_kg_per_m3

# density in g/cm^3
rho2 = rho1.cgs

# printing density in SI and in CGS
print (f'rho1 = {rho1}')
print (f'rho2 = {rho2}')
