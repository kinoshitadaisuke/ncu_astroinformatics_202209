#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 13:36:43 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s05_32.png'

# function of a curve
def curve (x):
    # coefficients
    a = 2.0
    b = 3.0
    c = 4.0
    # curve
    y = a * (x - b)**2 + c
    # returning y-value
    return y

# data to plot
data_x = numpy.linspace (0.0, 10.0, 1001)
data_y = curve (data_x)

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# plotting data
ax.plot (data_x, data_y, linestyle='-', linewidth=3.0, color='blue', \
         label='$f(x)=2(x-3)^2+4$')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225)
