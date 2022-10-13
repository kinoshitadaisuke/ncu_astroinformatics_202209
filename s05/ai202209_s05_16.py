#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/13 08:51:11 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.interpolate

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# output image file
file_output = 'ai202209_s05_16.png'

# generating data for interpolation
data_x = numpy.linspace (0.0, 10.0, 11)
data_y = 0.5 * (data_x - 4.0)**2 + 3.0

# printing data_x and data_y
print (f'data_x = {data_x}')
print (f'data_y = {data_y}')

# making a function for quadratic interpolation
func_interp = scipy.interpolate.interp1d (data_x, data_y, kind='quadratic')

# getting Y-value for X-value at x=5.5
x1 = 5.5
y1 = func_interp (x1)

# printing result
print (f'func_interp ({x1}) = {y1}')
print (f'what we expect is: x={x1} --> y={0.5*(x1-4.0)**2+3.0}')

# getting Y-value for X-value at x=7.8
x2 = 7.8
y2 = func_interp (x2)

# printing result
print (f'func_interp ({x2}) = {y2}')
print (f'what we expect is: x={x2} --> y={0.5*(x2-4.0)**2+3.0}')

#
# making a plot using matplotlib
#

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# plotting data points
ax.plot (data_x, data_y, linestyle='None', marker='o', markersize=8.0, \
         color='blue', label='raw data', zorder=0.2)

# plotting original curve
data_x0 = numpy.linspace (0.0, 10.0, 1001)
data_y0 = 0.5 * (data_x0 - 4.0)**2 + 3.0
ax.plot (data_x0, data_y0, linestyle='--', linewidth=2.0, color='cyan', \
         label='original curve', zorder=0.0)

# plotting result of interpolation
data_xi = numpy.linspace (0.0, 10.0, 1001)
data_yi = func_interp (data_xi)
ax.plot (data_xi, data_yi, linestyle=':', linewidth=3.0, color='red', \
         label='quadratic interpolation', zorder=0.1)

# plotting interpolated values
ax.plot (x1, y1, linestyle='None', marker='^', markersize=10.0, \
         color='magenta', label='result of interpolation #1', zorder=0.3)
ax.plot (x2, y2, linestyle='None', marker='v', markersize=10.0, \
         color='yellow', label='result of interpolation #2', zorder=0.4)

# labels
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=225)
