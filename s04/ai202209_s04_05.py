#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/01 22:03:58 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x = numpy.linspace (0.0, 10.0, 1001)
data_y = 2.0 * (data_x - 5.0)**2 + 3.0

# output file name
file_output = 'ai202209_s04_05.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, label='$f(x) = 2 (x-5)^2 + 3$')

# setting ranges of x-axis and y-axis
ax.set_xlim (-1.0, +11.0)
ax.set_ylim (0.0, +70.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$ [arbitrary unit]')
ax.set_ylabel ('$y$ [arbitrary unit]')

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
