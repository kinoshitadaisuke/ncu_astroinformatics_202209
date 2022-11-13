#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 09:12:39 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

#
# function to calculate blackbody curve
#
def bb_lambda (wavelength, T):
    # speed of light
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Planck function
    blackbody = 2.0 * h[0] * c[0]**2 / wavelength**5 \
        / (numpy.exp (h[0] * c[0] / (wavelength * k[0] * T) ) - 1.0 )

    # returning blackbody curve
    return (blackbody)

# temperature of blackbody
T = 3000.0

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of wavelength (from 10**-8 m = 10 nm to 10**-3 m = 1 mm)
wavelength_min = -8.0
wavelength_max = -3.0

# wavelength in metre
wavelength = numpy.logspace (wavelength_min, wavelength_max, num=5001)

# T = 3000 K blackbody spectrum
bb_3000 = bb_lambda (wavelength, T)

# printing Planck function
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Planck function:')
print (f'{bb_3000}')
