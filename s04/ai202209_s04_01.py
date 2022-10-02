#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/01 13:09:37 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.pyplot

# data to be plotted
data_x = [1.0, 2.0, 3.0, 4.0, 5.0]
data_y = [3.0, 2.0, 5.0, 1.0, 4.0]

# output file name
file_output = 'ai202209_s04_01.png'

#
# for making a plot using object-oriented interface,
# we first construct "fig" and "axes" objects,
# and then use methods for these "fig" and "axes".
#

# making a fig object using matplot.pyplot.figure function
fig = matplotlib.pyplot.figure ()

# constructing an axes object using object-oriented interface
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (data_x, data_y, label='Sample data')

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
