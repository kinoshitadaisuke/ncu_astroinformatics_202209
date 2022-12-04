#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 21:50:27 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

#
# command-line argument analysis
#

# constructing parser object
parser = argparse.ArgumentParser (description='plotting time-series data')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

#
# reading data
#

# empty numpy arrays for storing data
data_mjd  = numpy.array ([])
data_flux = numpy.array ([])
data_err  = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (datetime_str, mjd_str, flux_str, err_str) = line.split ()
        # conversion from string into float
        mjd  = float (mjd_str)
        flux = float (flux_str) / 10**6
        err  = float (err_str) / 10**6
        # appending the data at the end of numpy arrays
        data_mjd  = numpy.append (data_mjd, mjd)
        data_flux = numpy.append (data_flux, flux)
        data_err  = numpy.append (data_err, err)

#
# making a plot
#
        
# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('MJD [day]')
ax.set_ylabel ('Flux [10^6 e-/sec]')

# plotting data
ax.errorbar (data_mjd, data_flux, yerr=data_err, \
             linestyle='None', marker='.', markersize=1, color='blue', \
             ecolor='black', capsize=1, \
             label='photometry of Kepler-13')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
