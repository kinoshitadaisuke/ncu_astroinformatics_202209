#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 11:05:50 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x = numpy.concatenate ([
    numpy.linspace (1.0, 4.0, 4), \
    numpy.linspace (1.0, 4.0, 4), \
    numpy.linspace (1.0, 4.0, 4), \
    numpy.linspace (1.0, 4.0, 4) ])
data_y = numpy.concatenate ([
    numpy.repeat (1.0, 4), \
    numpy.repeat (2.0, 4), \
    numpy.repeat (3.0, 4), \
    numpy.repeat (4.0, 4) ])

# output file name
file_output = 'ai202209_s04_16.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
for i in range (len (data_x)):
    ax.plot (data_x[i], data_y[i], ls='None', marker='o', \
             markersize=i+1, label=f'markersize={i+1}')

# setting ranges of x-axis and y-axis
ax.set_xlim (0.0, +8.0)
ax.set_ylim (0.0, +6.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (0.0, +8.0, 9))
ax.set_yticks (numpy.linspace (0.0, +6.0, 7))

# setting aspect ratio
ax.set_aspect ('equal')

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
