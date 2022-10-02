#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 09:50:43 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x  = numpy.linspace (-10.0, +10.0, 10**3)
data_c0 = numpy.cos (data_x)
data_c1 = numpy.cos (data_x - numpy.pi / 4.0)
data_c2 = numpy.cos (data_x - numpy.pi / 2.0)
data_c3 = numpy.cos (data_x - numpy.pi * 3.0 / 4.0)

# output file name
file_output = 'ai202209_s04_12.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_c0, c='k', ls='-', linewidth=1, label='linewidth=1')
ax.plot (data_x, data_c1, c='k', ls='-', linewidth=2, label='linewidth=2')
ax.plot (data_x, data_c2, c='k', ls='-', linewidth=3, label='linewidth=3')
ax.plot (data_x, data_c3, c='k', ls='-', linewidth=4, label='linewidth=4')

# setting ranges of x-axis and y-axis
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-1.2, +1.9)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-10.0, +10.0, 11))
ax.set_yticks (numpy.linspace (-1.0, +1.0, 5))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
