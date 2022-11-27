#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 17:35:03 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# data file name
file_data = 'ai202209_s11_00_00.data'

# output file name
file_output = 'ai202209_s11_00_01.png'

# MJD offset
mjd_offset = 59000.0

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])

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
        (datetime, mjd_str, mag_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('MJD - 59000 [day]')
ax.set_ylabel ('Apparent Magnitude [mag]')

# range
ax.set_ylim (19.3, 20.7)
ax.invert_yaxis ()

# plotting data
ax.plot (data_mjd - mjd_offset, data_mag, \
         linestyle='None', marker='o', markersize=3, color='blue', \
         label='synthetic time-series data')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
