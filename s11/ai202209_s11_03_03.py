#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/28 00:55:37 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'ai202209_s11_03_02.data'

# output file name
file_output = 'ai202209_s11_03_03.png'

# empty numpy arrays for storing data
data_per = numpy.array ([])
data_var = numpy.array ([])

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
        (per_day_str, per_hr_str, per_min_str, var_str) = line.split ()
        # conversion from string into float
        per_hr = float (per_hr_str)
        var = float (var_str)
        # appending the data at the end of numpy arrays
        data_per = numpy.append (data_per, per_hr)
        data_var = numpy.append (data_var, var)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Period [hr]')
ax.set_ylabel ('Variance')

# axes
ax.set_xlim (0.0, 20.0)

# plotting data
ax.plot (data_per, data_var, \
         linestyle='-', linewidth=3, color='blue', \
         label='result of PDM analysis')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
