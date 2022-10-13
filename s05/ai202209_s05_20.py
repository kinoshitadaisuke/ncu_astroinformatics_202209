#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/13 21:17:03 (CST) daisuke>
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
file_output = 'ai202209_s05_20.png'

# function for a curve
def curve (x):
    y = 10.0 * numpy.sin (x / 2.0) * numpy.cos (x / 3.0)**2 \
        * numpy.exp (-x / 10)
    return (y)

# generating data for interpolation
data_x = numpy.linspace (0.0, 10.0, 11)
data_y = curve (data_x)

# making a function for linear interpolation
spline1 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=1)

# making a function for quadratic interpolation
spline2 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=2)

# making a function for cubic interpolation
spline3 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=3)

# making a function for 4th-order spline interpolation
spline4 = scipy.interpolate.InterpolatedUnivariateSpline (data_x, data_y, k=4)

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
data_y0 = curve (data_x0)
ax.plot (data_x0, data_y0, linestyle=':', linewidth=4.0, color='cyan', \
         label='original curve', zorder=0.0)

# plotting result of interpolation
data_xi1 = numpy.linspace (0.0, 10.0, 1001)
data_yi1 = spline1 (data_xi1)
ax.plot (data_xi1, data_yi1, linestyle='--', linewidth=2.0, color='magenta', \
         label='linear', zorder=0.1)

# plotting result of interpolation
data_xi2 = numpy.linspace (0.0, 10.0, 1001)
data_yi2 = spline2 (data_xi2)
ax.plot (data_xi2, data_yi2, linestyle='--', linewidth=3.0, color='yellow', \
         label='quadratic', zorder=0.1)

# plotting result of interpolation
data_xi3 = numpy.linspace (0.0, 10.0, 1001)
data_yi3 = spline3 (data_xi3)
ax.plot (data_xi3, data_yi3, linestyle='-.', linewidth=2.0, color='red', \
         label='cubic', zorder=0.1)

# plotting result of interpolation
data_xi4 = numpy.linspace (0.0, 10.0, 1001)
data_yi4 = spline4 (data_xi4)
ax.plot (data_xi4, data_yi4, linestyle='-', linewidth=1.0, color='green', \
         label='4th-order spline', zorder=0.1)

# labels
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=225)
