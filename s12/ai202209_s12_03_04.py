#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 21:22:29 (CST) daisuke>
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
parser.add_argument ('-o', type=str, default="out.png", \
                     help='output figure file name')
parser.add_argument ('-p', type=float, default=1.0, \
                     help='trial period in hr')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

# trial period (day)
p_trial = args.p / 24.0

#
# reading data from file
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
        (mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd   = numpy.append (data_mjd, mjd)
        data_mag   = numpy.append (data_mag, mag)
        data_err   = numpy.append (data_err, err)

        # calculation of phase using trial period
        phase = (mjd - data_mjd[0]) / p_trial
        phase -= int (phase)
        data_phase = numpy.append (data_phase, phase)

#
# making a plot
#
        
# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Phase')
ax.set_ylabel ('Magnitude [mag]')

# axes
ax.invert_yaxis ()

# plotting data
label = f"folded lightcurve constructed from $P = {p_trial * 24.0:6.4f}$ hr"
ax.errorbar (data_phase, data_mag, yerr=data_err, \
             linestyle='None', marker='.', markersize=5, color='blue', \
             ecolor='black', capsize=0, label=label)
ax.errorbar (data_phase + 1.0, data_mag, yerr=data_err, \
             linestyle='None', marker='.', markersize=5, color='blue', \
             ecolor='black', capsize=0)
ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
