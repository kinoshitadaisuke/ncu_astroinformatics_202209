#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 15:48:30 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s05_36.png'

# coefficients
a = -3.0
b = 5.0
c = 6.0
d = 4.0

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

# saving file
fig.savefig (file_output, dpi=225)
