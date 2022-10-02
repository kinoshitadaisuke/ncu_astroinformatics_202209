#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 15:41:25 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x = numpy.linspace (1.0, 10.0, 10)
data_y = 2.0 * data_x + 3.0

# generating random numbers for errors of y-value
rng = numpy.random.default_rng ()
data_x_err = rng.uniform (0.3, 0.7, 10)
data_y_err = rng.uniform (1.0, 3.0, 10)

# output file name
file_output = 'ai202209_s04_18.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.errorbar (data_x, data_y, xerr=data_x_err, yerr=data_y_err,
             linestyle='None', marker='o', markersize=8.0, color='green', \
             elinewidth=2.0, ecolor='black', capsize=5.0, \
             label='Sample data')

# setting ranges of x-axis and y-axis
ax.set_xlim (0.0, +11.0)
ax.set_ylim (0.0, +30.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (0.0, +10.0, 11))
ax.set_yticks (numpy.linspace (0.0, +30.0, 7))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
