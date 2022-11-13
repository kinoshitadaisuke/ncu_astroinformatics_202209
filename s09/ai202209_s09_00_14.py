#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 15:04:06 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s09_00_14.png'

#
# function to calculate blackbody curve
#
def bb_nu (frequency, T):
    # speed of light
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Planck constant
    h = scipy.constants.physical_constants['Planck constant']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Planck function
    blackbody = 2.0 * h[0] * frequency**3 / c[0]**2 \
        / (numpy.exp (h[0] * frequency / (k[0] * T) ) - 1.0 )

    # returning blackbody curve
    return (blackbody)

# function to calculate Rayleigh-Jeans law
def rj_nu (frequency, T):
    # speed of light
    c = scipy.constants.physical_constants['speed of light in vacuum']

    # Boltzmann constant
    k = scipy.constants.physical_constants['Boltzmann constant']

    # calculation of Rayleigh-Jeans law
    blackbody = 2.0 * frequency**2 * k[0] * T / c[0]**2

    # returning blackbody curve by Rayleigh-Jeans law
    return (blackbody)

# temperature of blackbody
T = 5800.0

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of frequency (from 10**0 Hz to 10**16 Hz)
frequency_min = 0.0
frequency_max = 16.0

# frequency in Hz
frequency = numpy.logspace (frequency_min, frequency_max, num=16001)

# T = 5800 K blackbody spectrum
bb_5800 = bb_nu (frequency, T)
rj_5800 = rj_nu (frequency, T)

# printing Planck function
print (f'Frequency:')
print (f'{frequency}')
print (f'Planck function:')
print (f'{bb_5800}')
print (f'Rayleigh-Jeans law:')
print (f'{rj_5800}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Frequency [Hz]')
ax.set_ylabel ('Specific Intensity [W sr$^{-1}$ m$^{-2}$ Hz$^{-1}$]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (10**1, 10**18)
ax.set_ylim (10**-30, 10**-3)

# make secondary X-axis
c   = scipy.constants.physical_constants['speed of light in vacuum'][0]
ax2 = ax.secondary_xaxis (location='top', \
                          functions=(lambda x: c/x, lambda x: c/x) )
ax2.set_xlabel ('Wavelength [m]')

# plotting data
ax.plot (frequency, bb_5800, linestyle='-', color='r', \
         linewidth=5, label='Blackbody of T = 5800 K')
ax.plot (frequency, rj_5800, linestyle='--', color='b', \
         linewidth=3, label='Rayleigh-Jeans law for T = 5800 K')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
