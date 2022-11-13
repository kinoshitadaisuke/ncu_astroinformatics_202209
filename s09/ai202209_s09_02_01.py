#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 23:33:09 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'solar_spec.data'

# figure file name
file_output = 'ai202209_s09_02_01.png'

# initialisation of numpy arrays for storing data
wl = numpy.array ([])
irradiance = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # initialisation of the parameter "i" for counting lines
    i = 0
    # reading data line-by-line
    for line in fh:
        # incrementing line number
        i += 1
        # skipping first 9 lines
        if (i < 10):
            continue
        # splitting data into wavelength and irradiance
        line = line.strip ()
        (wl_str, irradiance_str) = line.split ()
        # converting string into float
        wl_float = float (wl_str)
        irradiance_float = float (irradiance_str)
        # appending data to numpy arrays
        wl = numpy.append (wl, wl_float)
        irradiance = numpy.append (irradiance, irradiance_float)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [nm]')
ax.set_ylabel ('Irradiance [W m$^{-2}$ nm$^{-1}$]')

# axes
ax.set_xlim (100, 10000)
ax.set_ylim (0.0, 2.5)
ax.set_xscale ('log')

# plotting data
ax.plot (wl, irradiance, linestyle='-', color='r', linewidth=2, label='Sun')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
