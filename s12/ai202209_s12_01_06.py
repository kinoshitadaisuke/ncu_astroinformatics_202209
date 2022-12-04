#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 00:50:33 (CST) daisuke>
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
parser = argparse.ArgumentParser (description='plotting power spectrum')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.pdf", \
                     help='output figure file name')
parser.add_argument ('-a', type=float, default=0.0, \
                     help='minimum period to be plotted in hour')
parser.add_argument ('-b', type=float, default=100.0, \
                     help='maximum period to be plotted in hour')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

# minimum period to be plotted
per_min_hr = args.a

# maximum period to be plotted
per_max_hr = args.b

#
# reading data from file
#

# empty numpy arrays for storing data
data_freq    = numpy.array ([])
data_per_day = numpy.array ([])
data_per_hr  = numpy.array ([])
data_per_min = numpy.array ([])
data_power   = numpy.array ([])

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
        (freq_str, per_day_str, per_hr_str, per_min_str, power_str) \
            = line.split ()
        # conversion from string into float
        freq    = float (freq_str)
        per_day = float (per_day_str)
        per_hr  = float (per_hr_str)
        per_min = float (per_min_str)
        power   = float (power_str)
        # appending the data at the end of numpy arrays
        data_freq    = numpy.append (data_freq, freq)
        data_per_day = numpy.append (data_per_day, per_day)
        data_per_hr  = numpy.append (data_per_hr, per_hr)
        data_per_min = numpy.append (data_per_min, per_min)
        data_power   = numpy.append (data_power, power)

#
# making a plot
#
        
# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Period [hr]')
ax.set_ylabel ('Power')

# axes
ax.set_xlim (per_min_hr, per_max_hr)

# plotting data
ax.plot (data_per_hr, data_power, \
         linestyle='-', linewidth=3, color='blue', \
         label='result of Lomb-Scargle periodogram')
ax.legend (bbox_to_anchor=(1.0, 1.12), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
