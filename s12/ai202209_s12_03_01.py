#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 18:52:55 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'linear/4672469.dat'

# output file name
file_output = 'ai202209_s12_03_01.png'

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])
data_err = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
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
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)
        data_err = numpy.append (data_err, err)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('MJD [day]')
ax.set_ylabel ('Apparent Magnitude [mag]')

# axes
ax.invert_yaxis ()

# plotting data
ax.errorbar (data_mjd, data_mag, yerr=data_err, \
             linestyle='None', marker='o', markersize=5, color='green', \
             ecolor='black', capsize=5, \
             label='LINEAR time-series data for object 4672469')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
