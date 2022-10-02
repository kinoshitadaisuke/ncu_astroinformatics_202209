#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 07:39:27 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x  = numpy.linspace (-10.0, +10.0, 10**3)
data_l0 = 2.0 * data_x - 30.0
data_l1 = 2.0 * data_x - 20.0
data_l2 = 2.0 * data_x - 10.0
data_l3 = 2.0 * data_x - 0.0
data_l4 = 2.0 * data_x + 10.0
data_l5 = 2.0 * data_x + 20.0
data_l6 = 2.0 * data_x + 30.0

# output file name
file_output = 'ai202209_s04_10.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_l0, color='red',     label='$f(x) = 2x - 30$')
ax.plot (data_x, data_l1, color='green',   label='$f(x) = 2x - 20$')
ax.plot (data_x, data_l2, color='blue',    label='$f(x) = 2x - 10$')
ax.plot (data_x, data_l3, color='cyan',    label='$f(x) = 2x$')
ax.plot (data_x, data_l4, color='magenta', label='$f(x) = 2x + 10$')
ax.plot (data_x, data_l5, color='yellow',  label='$f(x) = 2x + 20$')
ax.plot (data_x, data_l6, color='grey',    label='$f(x) = 2x + 30$')

# setting ranges of x-axis and y-axis
ax.set_xlim (-10.0, +10.0)
ax.set_ylim (-60.0, +100.0)

# setting labels for x-axis and y-axis
ax.set_xlabel ('$x$')
ax.set_ylabel ('$y$')

# setting ticks
ax.set_xticks (numpy.linspace (-10.0, +10.0, 11))
ax.set_yticks (numpy.linspace (-60.0, +100.0, 17))

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
