#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/01 22:29:43 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
radius = 3.0
theta  = numpy.linspace (0.0, 2.0 * numpy.pi, 1001)
data_x = radius * numpy.cos (theta)
data_y = radius * numpy.sin (theta)

# output file name
file_output = 'ai202209_s04_07.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, label='circle of radius 3')

# setting ranges of x-axis and y-axis
ax.set_xlim (-4.0, +4.0)
ax.set_ylim (-4.0, +4.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-4.0, +4.0, 9))
ax.set_yticks (numpy.linspace (-4.0, +4.0, 9))

# showing grid
ax.grid ()

# setting aspect ratio
ax.set_aspect ('equal', 'box')

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
