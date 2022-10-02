#!/usr/pkg/bin/python3.9

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# output image file
file_output = 'ai202209_s04_25.png'

# parameters for random number generation
mean   = 1000.0
stddev = 100.0
n      = 10**6

# parameters for histogram
bin_min   = 500.0
bin_max   = 1500.0
bin_width = 50.0
bin_n     = int ((bin_max - bin_min) / bin_width) + 1

# generating random numbers
rng  = numpy.random.default_rng ()
dist = rng.normal (loc=mean, scale=stddev, size=n)

# initialisation of numpy arrays for histogram
hist_x = numpy.linspace (bin_min, bin_max, bin_n)
hist_y = numpy.zeros (bin_n, dtype='int64')

# construction of a histogram
for i in range (len (dist)):
    # if data is outside of [bin_min, bin_max], then skip
    if ( (dist[i] < bin_min) or (dist[i] > bin_max) ):
        continue
    # counting number of data in each bin
    hist_y[int ( (dist[i] - bin_min) / bin_width)] += 1

# printing histogram
for i in range (bin_n):
    bin_0 = bin_min + bin_width * i
    bin_1 = bin_min + bin_width * (i+1)
    print (f'{bin_0:6.1f}-{bin_1:6.1f}  {hist_y[i]:6d}')
    
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
ax.bar (hist_x, hist_y, bin_width, edgecolor='black', linewidth=0.3, \
        align='edge', label='Gaussian distribution')

# legend
ax.legend ()

# saving the figure to a file
fig.savefig (file_output)
