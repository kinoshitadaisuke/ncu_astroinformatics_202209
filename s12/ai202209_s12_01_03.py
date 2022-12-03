#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/03 23:08:38 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='making folded lightcurves')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.png", \
                     help='output figure file name')
parser.add_argument ('periods', type=float, nargs=6, \
                     help='list of trial periods in hr')

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
list_p_trial = [x / 24.0 for x in args.periods]

#
# reading data from file
#

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_mag   = numpy.array ([])
data_err   = numpy.array ([])

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

#
# making a plot
#
        
# making objects "fig" and "canvas"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making a plot of 2x3 panels
for i in range (len (list_p_trial)):
    # trial period
    p_trial = list_p_trial[i]
    
    # calculation of phase using trial period
    data_phase = (data_mjd - data_mjd[0]) / p_trial
    data_phase -= numpy.int_ (data_phase)

    # making a subplot
    subplot = 321 + int (i)
    ax      = fig.add_subplot (subplot)

    # labels
    ax.set_xlabel ('Phase')
    ax.set_ylabel ('Magnitude [mag]')
    title = f"trial period of {p_trial * 24.0:3.1f} hr"
    ax.set_title (title)
    
    # axes
    ax.invert_yaxis ()

    # plotting data
    ax.errorbar (data_phase, data_mag, yerr=data_err, \
                 linestyle='None', marker='.', markersize=5, color='blue', \
                 ecolor='black', capsize=0)
    ax.errorbar (data_phase + 1.0, data_mag, yerr=data_err, \
                 linestyle='None', marker='.', markersize=5, color='blue', \
                 ecolor='black', capsize=0)

# saving the plot into a file
fig.tight_layout ()
fig.savefig (file_fig, dpi=225)
