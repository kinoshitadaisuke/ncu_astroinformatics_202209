#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/10 16:35:10 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s09_00_04.png'

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

#
# function to calculate blackbody curve
#
def bb_lambda (T):
    # calculation of Planck function
    blackbody = 2.0 * h[0] * c[0]**2 / wavelength**5 \
        / (numpy.exp (h[0] * c[0] / (wavelength * k[0] * T) ) - 1.0 )
    # returning blackbody curve
    return (blackbody)

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

# T = 5800 K blackbody spectrum
bb_5800 = bb_lambda (T)

# printing Planck function
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Planck function:')
print (f'{bb_5800}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Specific Intensity [W sr$^{-1}$ m$^{-3}$]')

# axes
ax.set_xlim (0.03, 5.0)
ax.set_ylim (0.0, bb_5800.max () * 1.2)

# plotting data
ax.plot (wavelength * 10**6, bb_5800, linestyle='-', color='r', \
         linewidth=3, label='Blackbody of T = 5800 K')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
