#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/14 00:38:06 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'cmb_cobe.data'

# output file name
file_output = 'ai202209_s09_04_01.png'

#
# constants
#

# speed of light
c = scipy.constants.c
# Planck constant
h = scipy.constants.h
# Boltzmann constant
k = scipy.constants.k

# numpy arrays for storing data
data_freq_kayser = numpy.array ([])
data_intensity   = numpy.array ([])
data_residual    = numpy.array ([])
data_uncertainty = numpy.array ([])
data_galspec     = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # reading data file
    for line in fh:
        # skip if the line starts with '#'.
        if (line[0] == '#'):
            continue
        # splitting the data
        (freq_kayser_str, intensity_str, residual_str, uncertainty_str,
         galspec_str) = line.split ()
        # conversion from string into float
        freq_kayser = float (freq_kayser_str)
        intensity   = float (intensity_str)
        residual    = float (residual_str)
        uncertainty = float (uncertainty_str)
        galspec     = float (galspec_str)
        # appending data to numpy arrays
        data_freq_kayser = numpy.append (data_freq_kayser, freq_kayser)
        data_intensity   = numpy.append (data_intensity, intensity)
        data_residual    = numpy.append (data_residual, residual)
        data_uncertainty = numpy.append (data_uncertainty, uncertainty)
        data_galspec     = numpy.append (data_galspec, galspec)

# conversion from wavenumber into wavelength
data_wavelength_mm = 10.0 / data_freq_kayser
data_wavelength_m  = data_wavelength_mm / 10**3

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavenumber [cm$^{-1}$]')
ax.set_ylabel ('Intensity [MJy sr$^{-1}$]')

# axes
ax.set_xlim (0.0, 23.0)
ax.set_ylim (0.0, 500.0)

# plotting data
ax.errorbar (data_freq_kayser, data_intensity, yerr=data_uncertainty, \
             linestyle='', marker='o', color='r', markersize=5, \
             ecolor='black', capsize=3, label='CMB measured by COBE/FIRAS')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
