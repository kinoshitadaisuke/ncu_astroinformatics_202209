#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/17 01:06:14 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s05_37.png'

# coefficients
a = -3.0
b = 5.0
c = 6.0
d = 4.0

# function of a curve
def surface (x):
    # curve
    z = a * numpy.exp ( -(x[0] - b)**2 ) * numpy.exp ( -(x[1] - c)**2 ) + d
    # returning y-value
    return z

# finding minimum
minimum = scipy.optimize.minimize (surface, x0=(8.0, 8.0), method='Nelder-Mead')

# printing minimum value
print (f'minimum: z={minimum.fun} at (x, y) = ({minimum.x[0]}, {minimum.x[1]})')

# data to plot
data_x = numpy.linspace (0.0, 10.0, 1001)
data_y = numpy.linspace (0.0, 10.0, 1001)
data_xx, data_yy = numpy.meshgrid (data_x, data_y)
data_zz = a * numpy.exp (-(data_xx - b)**2) * numpy.exp (-(data_yy - c)**2) + d

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection='3d')

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')
ax.set_zlabel ('Z [arbitrary unit]')
ax.set_xlim (0.0, 10.0)
ax.set_ylim (0.0, 10.0)
ax.set_zlim (0.0, 4.5)

# plotting data
ax.plot_surface (data_xx, data_yy, data_zz, \
                 label='$f(x,y) = -3 \exp (x-5)^2 \exp (y-6)^2 + 4$')
ax.contour (data_xx, data_yy, data_zz, zdir='z', offset=0.0)
ax.plot3D (minimum.x[0], minimum.x[1], minimum.fun, linestyle='None', \
           marker='o', markersize=5.0, color='red', label='minimum')

# saving file
fig.savefig (file_output, dpi=225)
