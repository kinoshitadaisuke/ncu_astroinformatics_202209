#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 23:25:03 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='making folded lightcurve')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')
parser.add_argument ('-p', type=float, default=1.0, \
                     help='period in day')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

# assumed period (day)
p_best = args.p

#
# reading data
#

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_mag   = numpy.array ([])
data_err   = numpy.array ([])
data_phase = numpy.array ([])

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
        (datetime_str, mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd   = numpy.append (data_mjd, mjd)
        data_mag   = numpy.append (data_mag, mag)
        data_err   = numpy.append (data_err, err)

        # calculation of phase using assumed period
        phase = (mjd - data_mjd[0]) / p_best
        phase -= int (phase)
        data_phase = numpy.append (data_phase, phase)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Phase')
ax.set_ylabel ('Relative Brightness')

# plotting data
ax.errorbar (data_phase, data_mag, yerr=data_err, \
             linestyle='None', marker='.', markersize=1, color='blue', \
             ecolor='black', capsize=1, \
             label=f'folded lightcurve of Kepler-13 using {p_best:8.6f} hr')
ax.errorbar (data_phase + 1.0, data_mag, yerr=data_err, \
             linestyle='None', marker='.', markersize=1, color='blue', \
             ecolor='black', capsize=1)
ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
