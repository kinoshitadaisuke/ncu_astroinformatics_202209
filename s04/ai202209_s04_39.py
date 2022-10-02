#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 22:29:01 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# output file name
file_output = 'ai202209_s04_39.png'

# data to be plotted
theta = numpy.linspace (0.0, 10.0 * numpy.pi, 1000)
x = numpy.cos (theta)
y = numpy.sin (theta)
z = theta * 0.2

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='3d')

# settings for plot
ax.set_xlim (-1.5, +1.5)
ax.set_ylim (-1.5, +1.5)
ax.set_zlim (-0.5, +5.5)
ax.set_box_aspect ( (3.0, 3.0, 6.0) )

# viewing angles of camera
el = 30.0
az = -60.0
ax.view_init (elev=el, azim=az)

# plotting data points
ax.plot (x, y, z, color='blue')

# saving file
fig.savefig (file_output, dpi=200)
