#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/03 00:01:16 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='plotting time-series data')
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name (default: in.data)')
parser.add_argument ('-o', type=str, default="out.png", \
                     help='output figure file name (default: out.png)')
args = parser.parse_args ()

# data file name
file_data = args.i

# output file name
file_fig = args.o

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])
data_err = numpy.array ([])

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
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)
        data_err = numpy.append (data_err, err)

# making objects "fig" and "ax"
fig     = matplotlib.figure.Figure ()
canvasu = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax      = fig.add_subplot (111)

# labels
ax.set_xlabel ('MJD [day]')
ax.set_ylabel ('Magnitude [mag]')

# axes
ax.invert_yaxis ()
ax.get_xaxis ().get_major_formatter ().set_useOffset (False)

# plotting data
ax.plot (data_mjd, data_mag, \
         linestyle='None', marker='.', color='b', \
         label='synthetic time-series data')
ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
