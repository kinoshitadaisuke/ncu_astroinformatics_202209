#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 19:18:47 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_input = 'ai202209_s11_00_00.data'

# output file name
file_output = 'ai202209_s11_00_08.png'

# best fit period (day)
p_best = 2.0007 / 24

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_phase = numpy.array ([])
data_mag   = numpy.array ([])

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
        (datetime, mjd_str, mag_str) = line.split ()
        # conversion from string into float
        mjd   = float (mjd_str)
        mag   = float (mag_str)
        phase = mjd / p_best - int (mjd / p_best)
        # appending the data at the end of numpy arrays
        data_mjd   = numpy.append (data_mjd, mjd)
        data_phase = numpy.append (data_phase, phase)
        data_mag   = numpy.append (data_mag, mag)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Phase')
ax.set_ylabel ('Apparent Magnitude [mag]')

# range
ax.set_ylim (19.3, 20.7)
ax.invert_yaxis ()

# plotting data
ax.plot (data_phase, data_mag, \
         linestyle='None', marker='o', markersize=3, color='blue', \
         label='lightcurve constructed by the best fit period $P = 2.0007$ hr')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
