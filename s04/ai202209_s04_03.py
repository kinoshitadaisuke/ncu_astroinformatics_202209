#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/01 13:10:13 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# data to be plotted
data_x = [1.0, 2.0, 3.0, 4.0, 5.0]
data_y = [3.0, 2.0, 5.0, 1.0, 4.0]

# output file name
file_output = 'ai202209_s04_03.png'

#
# for making a plot using object-oriented interface,
# we first construct "fig" and "axes" objects,
# and then use methods for these "fig" and "axes".
#

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, label='Sample data')

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
