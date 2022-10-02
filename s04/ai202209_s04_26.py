#!/usr/pkg/bin/python3.9

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# output image file
file_output = 'ai202209_s04_26.png'

# parameters for random number generation
mean   = 1000.0
stddev = 100.0
n      = 10**7

# parameters for histogram
bin_min   = 500.0
bin_max   = 1500.0
bin_width = 20.0
bin_n     = int ((bin_max - bin_min) / bin_width) + 1

# generating random numbers
rng  = numpy.random.default_rng ()
dist = rng.normal (loc=mean, scale=stddev, size=n)

# initialisation of numpy arrays for histogram
bins = numpy.linspace (bin_min, bin_max, bin_n)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# labels
ax.set_xlabel ('$x$')
ax.set_ylabel ('Number of data')

# axis settings
ax.set_xlim (bin_min, bin_max)

# plotting data
ax.hist (dist, bins=bins, histtype='bar', \
         edgecolor='black', linewidth=0.3, align='mid', \
         label='Gaussian distribution')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
