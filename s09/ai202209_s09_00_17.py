#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 20:09:09 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s09_00_17.png'

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

# temperature of blackbody
T = numpy.logspace (0.0, 8.0, num=9, dtype=numpy.longdouble)

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T} K')

# range of frequency (from 10**0 Hz to 10**16 Hz)
frequency_min = 2.0
frequency_max = 20.0

# frequency in Hz
frequency = numpy.logspace (frequency_min, frequency_max, num=16001, \
                            dtype=numpy.longdouble)

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
ax.set_xlim (10**3, numpy.array ([10**20], dtype=numpy.longdouble))
ax.set_ylim (10**-30, 10**6)

# make secondary X-axis
c   = scipy.constants.physical_constants['speed of light in vacuum'][0]
ax2 = ax.secondary_xaxis (location='top', \
                          functions=(lambda x: c/x, lambda x: c/x) )
ax2.set_xlabel ('Wavelength [m]')

# showing gamma-ray region
ax.fill_between (numpy.array ([3*10**19, 10**21], dtype=numpy.longdouble), \
                 10**-30, 10**8, \
                 color='magenta', alpha=0.1)
ax.text (x=4*10**19, y=10**-29, s='$\gamma$-ray')

# showing X-ray region
ax.fill_between (numpy.array ([3*10**16, 3*10**19], dtype=numpy.longdouble), \
                 10**-30, 10**8, \
                 color='cyan', alpha=0.1)
ax.text (x=3*10**17, y=10**-29, s='X-ray')

# showing UV region
ax.fill_between ([10**15, 3*10**16], 10**-30, 10**8, \
                 color='violet', alpha=0.1)
ax.text (x=2*10**15, y=10**-29, s='UV')

# showing visible region
ax.fill_between ([3*10**14, 10**15], 10**-30, 10**8, \
                 color='green', alpha=0.1)
ax.text (x=10**14, y=3*10**-28, s='Visible')

# showing IR region
ax.fill_between ([10**12, 3*10**14], 10**-30, 10**8, \
                 color='red', alpha=0.1)
ax.text (x=10**13, y=10**-29, s='IR')

# showing radio region
ax.fill_between ([10**0, 10**12], 10**-30, 10**8, \
                 color='yellow', alpha=0.1)
ax.text (x=10**8, y=10**-29, s='Radio')

# plotting data
for i in range (len (T)):
    # making model spectrum for given temperature using Planck's radiation law
    bb = bb_nu (frequency, T[i])
    # label
    text_label = f'T = {T[i]:g} K'
    ax.plot (frequency, bb, linestyle='-', linewidth=3, label=text_label)

# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
