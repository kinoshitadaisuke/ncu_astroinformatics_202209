#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/10 13:38:24 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s09_00_02.png'

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

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Specific Intensity [W sr$^{-1}$ m$^{-3}$]')

# axes
ax.set_xlim (0.01, 100)
ax.set_ylim (0.0, 3.0 * 10**13)

# plotting data
ax.plot (wavelength * 10**6, blackbody, linestyle='-', color='r', \
         linewidth=3, label='Blackbody of T = 5800 K')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
