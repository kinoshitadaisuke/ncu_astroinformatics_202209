#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 16:00:10 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x = numpy.linspace (-5.0, 5.0, 101)
data_y = 10.0**data_x

# output file name
file_output = 'ai202209_s04_20.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, linestyle='-', linewidth=3.0, color='orange', \
         label='Sample data')

# setting log-scale
ax.set_yscale ('log')

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
