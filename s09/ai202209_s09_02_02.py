#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 23:43:24 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.modeling.models
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'solar_spec.data'

# figure file name
file_output = 'ai202209_s09_02_02.png'

# units
unit_W  = astropy.units.W
unit_m  = astropy.units.m
unit_nm = astropy.units.nm
unit_sr = astropy.units.sr
unit_K  = astropy.units.K

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

# wavelength
wl2_min = -7.0
wl2_max = -5.0
wl2 = numpy.logspace (wl2_min, wl2_max, 10**4) * 10**9 * unit_nm

# temperature
T = 5780.0 * unit_K

# blackbody radiation
bb = astropy.modeling.models.BlackBody \
    (temperature=T, \
     scale=7.0 * 10**-5 * unit_W / (unit_m**2 * unit_nm * unit_sr) )
bb_data = bb (wl2)
        
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
ax.plot (wl2, bb_data, linestyle=':', color='b', linewidth=2, \
         label='T=5780 K Blackbody')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
