#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/10 13:09:49 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

#
# constants
#

# speed of light
c = scipy.constants.c

# Planck constant
h = scipy.constants.h

# Boltzmann constant
k = scipy.constants.k

# printing values of constants
print (f'Constants:')
print (f'  c = {c:g}')
print (f'  h = {h:g}')
print (f'  k = {k:g}')

# temperature of blackbody
T = 5800.0

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of wavelength (from 10**-8 m = 10 nm to 10**-4 m = 100 micron)
wavelength_min = -8.0
wavelength_max = -4.0

# wavelength in metre
wavelength = numpy.logspace (wavelength_min, wavelength_max, num=4001)

# calculation of Planck function
blackbody = 2.0 * h * c**2 / wavelength**5 \
    / (numpy.exp (h * c / (wavelength * k * T) ) - 1.0 )

# printing Planck function
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Planck function:')
print (f'{blackbody}')
