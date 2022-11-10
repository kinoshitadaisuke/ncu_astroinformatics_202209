#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/10 15:50:55 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

#
# constants
#

# speed of light
c = scipy.constants.physical_constants['speed of light in vacuum']

# Planck constant
h = scipy.constants.physical_constants['Planck constant']

# Boltzmann constant
k = scipy.constants.physical_constants['Boltzmann constant']

# printing values of constants
print (f'Constants:')
print (f'  c = {c[0]:g} [{c[1]}]')
print (f'  h = {h[0]:g} [{h[1]}]')
print (f'  k = {k[0]:g} [{k[1]}]')

# temperature of blackbody
T = 5800.0

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of wavelength (from 10**-8 m = 10 nm to 10**-3 m = 1 mm)
wavelength_min = -8.0
wavelength_max = -3.0

# wavelength in metre
wavelength = numpy.logspace (wavelength_min, wavelength_max, num=5001)

# calculation of Planck function
blackbody = 2.0 * h[0] * c[0]**2 / wavelength**5 \
    / (numpy.exp (h[0] * c[0] / (wavelength * k[0] * T) ) - 1.0 )

# printing Planck function
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Planck function:')
print (f'{blackbody}')
