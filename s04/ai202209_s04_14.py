#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 23:36:37 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
rng    = numpy.random.default_rng ()
data_x = rng.uniform (0.0, 100.0, 50)
data_y = rng.uniform (0.0, 100.0, 50)

# output file name
file_output = 'ai202209_s04_14.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, c='b', ls='None', marker='.', label='marker=.')

# setting ranges of x-axis and y-axis
ax.set_xlim (-1.0, +101.0)
ax.set_ylim (-1.0, +101.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (0.0, +100.0, 11))
ax.set_yticks (numpy.linspace (0.0, +100.0, 11))

# setting aspect ratio
ax.set_aspect ('equal')

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
