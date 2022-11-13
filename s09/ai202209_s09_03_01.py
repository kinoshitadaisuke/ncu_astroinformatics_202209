#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/14 00:02:58 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'hd61005_spec.data'

# output file name
file_output = 'ai202209_s09_03_01.png'

# making empty numpy arrays
data_wl       = numpy.array ([])
data_flux     = numpy.array ([])
data_flux_err = numpy.array ([])

# opening data file
with open (file_input, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the word '+or-' is found, then we process the line
        if ('+or-' in line):
            # splitting data
            data = line.split ('+or-')
            # wavelength and flux
            (wl_str, flux_str) = data[0].split ()
            # error of flux
            flux_error_str = data[1].split ()[0]
            # conversion from string into float
            wl         = float (wl_str)
            flux       = float (flux_str)
            flux_error = float (flux_error_str)
            # appending data into numpy arrays
            data_wl       = numpy.append (data_wl, wl)
            data_flux     = numpy.append (data_flux, flux)
            data_flux_err = numpy.append (data_flux_err, flux_error)
            
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Flux [Jy]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')

# plotting data
ax.errorbar (data_wl, data_flux, yerr=data_flux_err, \
             linestyle='', color='r', marker='o', markersize=5, \
             ecolor='black', capsize=3, label='HD61005')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
