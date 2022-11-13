#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 23:11:34 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants

# importing astropy module
import astropy.modeling.models
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s09_01_01.png'

# units
unit_K      = astropy.units.K
unit_micron = astropy.units.micron

# temperature of blackbody
T = 3000.0 * unit_K

# printing temperature of blackbody
print (f'Temperature:')
print (f'  T = {T}')

# range of wavelength (from 10**-8 m to 10**-3 m)
wavelength_min = -8.0
wavelength_max = -3.0

# wavelength in micron
wavelength = numpy.logspace (wavelength_min, wavelength_max, num=5001, \
                             dtype=numpy.longdouble) * 10**6 * unit_micron

# T = 3000 K blackbody radiation
bb3000  = astropy.modeling.models.BlackBody (temperature=T)
bb_data = bb3000 (wavelength)

# printing blackbody radiation
print (f'Wavelength:')
print (f'{wavelength}')
print (f'Blackbody radiation:')
print (f'{bb_data}')

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Specific Intensity [erg sec$^{-1}$ sr$^{-1}$ cm$^{-2}$ Hz$^{-1}$]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')
ax.set_xlim (0.01, 100)
ax.set_ylim (10**-12, 10**-2)

# plotting data
ax.plot (wavelength, bb_data, linestyle='-', linewidth=3, \
         label='3000 K blackbody')

# legend
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
