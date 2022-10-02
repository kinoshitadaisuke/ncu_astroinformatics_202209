#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 22:38:24 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# output file name
file_output = 'ai202209_s04_38.png'

# parameters for random number generation
mean   = 0.0
stddev = 100.0
n      = 10**4

# data to be plotted
rng = numpy.random.default_rng ()
x   = rng.normal (loc=mean, scale=stddev, size=n)
y   = rng.normal (loc=mean, scale=stddev, size=n)
z   = rng.normal (loc=mean, scale=stddev, size=n)

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='3d')

# settings for plot
ax.set_xlim (-500.0, +500.0)
ax.set_ylim (-500.0, +500.0)
ax.set_zlim (-500.0, +500.0)
ax.set_box_aspect ( (1.0, 1.0, 1.0) )

# viewing angles of camera
el = 45.0
az = 60.0
ax.view_init (elev=el, azim=az)

# plotting data points
ax.scatter (x, y, z, s=1.0, color='blue', alpha=0.1)

# saving file
fig.savefig (file_output, dpi=200)
