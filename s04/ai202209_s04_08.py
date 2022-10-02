#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/01 22:49:30 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x   = numpy.linspace (-360.0, +360.0, 10**4)
data_sin = numpy.sin ( numpy.deg2rad (data_x) )
data_cos = numpy.cos ( numpy.deg2rad (data_x) )

# output file name
file_output = 'ai202209_s04_08.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_sin, label='sine curve')
ax.plot (data_x, data_cos, label='cosine curve')

# setting ranges of x-axis and y-axis
ax.set_xlim (-360.0, +360.0)
ax.set_ylim (-1.2, +1.2)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$ [deg]')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-360.0, +360.0, 9))
ax.set_yticks (numpy.linspace (-1.0, +1.0, 5))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
