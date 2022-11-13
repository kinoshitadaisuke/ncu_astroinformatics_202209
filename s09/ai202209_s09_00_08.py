#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 08:20:13 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

# speed of light
c = scipy.constants.physical_constants['speed of light in vacuum']

# Planck constant
h = scipy.constants.physical_constants['Planck constant']

# Boltzmann constant
k = scipy.constants.physical_constants['Boltzmann constant']

# temperature of blackbody
T = 5800.0

# function for solving the equation (x-5) * exp(x) + 5 = 0
def peak (x):
    y = ( (x - 5.0) * numpy.exp (x) + 5 )**2
    return (y)

# finding the minimum x corresponding to the peak of blackbody radiation
x_min = scipy.optimize.minimize_scalar (peak, bracket=(2.0, 5.0), \
                                        method='Brent')

# printing the minimum x
print (x_min)

# finding a peak of T=5800 K blackbody radiation spectrum
wavelength_peak = h[0] * c[0] / (x_min.x * k[0] * T)

# printing peak wavelength of black body radiation
print (f'peak wavelength of T={T} K blackbody = {wavelength_peak} m')
