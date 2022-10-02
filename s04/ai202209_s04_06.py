#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/01 22:15:28 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x = numpy.linspace (0.0, 720.0, 7201)
data_y = numpy.sin ( numpy.deg2rad (data_x) )

# output file name
file_output = 'ai202209_s04_06.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, label='$f(x) = \sin (x)$')

# setting ranges of x-axis and y-axis
ax.set_xlim (0.0, +720.0)
ax.set_ylim (-1.2, +1.2)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$ [deg]')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (0.0, 720.0, 9))
ax.set_yticks (numpy.linspace (-1.0, +1.0, 11))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
