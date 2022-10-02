#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 07:39:05 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x  = numpy.linspace (-10.0, +10.0, 10**3)
data_l1 = 2.0 * data_x - 12.0
data_l2 = 2.0 * data_x - 6.0
data_l3 = 2.0 * data_x - 0.0
data_l4 = 2.0 * data_x + 6.0
data_l5 = 2.0 * data_x + 12.0

# output file name
file_output = 'ai202209_s04_09.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_l1, label='$f(x) = 2x - 12$')
ax.plot (data_x, data_l2, label='$f(x) = 2x - 6$')
ax.plot (data_x, data_l3, label='$f(x) = 2x$')
ax.plot (data_x, data_l4, label='$f(x) = 2x + 6$')
ax.plot (data_x, data_l5, label='$f(x) = 2x + 12$')

# setting ranges of x-axis and y-axis
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-30.0, +30.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-10.0, +10.0, 11))
ax.set_yticks (numpy.linspace (-30.0, +30.0, 11))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
