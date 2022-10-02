#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 16:20:35 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.backends.backend_agg
import matplotlib.figure

# semimajor axis and orbital period of planets
dic_planets = {
    'Mercury': {'a':  0.3871, 'P':    88.0, 'marker': 's', 'colour': 'b'},
    'Venus':   {'a':  0.7233, 'P':   224.7, 'marker': '^', 'colour': 'y'}, 
    'Earth':   {'a':  1.0000, 'P':   365.2, 'marker': 'o', 'colour': 'g'},
    'Mars':    {'a':  1.5237, 'P':   687.0, 'marker': 'v', 'colour': 'r'},
    'Jupiter': {'a':  5.2034, 'P':  4331.0, 'marker': 's', 'colour': 'm'},
    'Saturn':  {'a':  9.5371, 'P': 10747.0, 'marker': '^', 'colour': 'g'},
    'Uranus':  {'a': 19.1913, 'P': 30589.0, 'marker': 'o', 'colour': 'c'},
    'Neptune': {'a': 30.0690, 'P': 59800.0, 'marker': 'v', 'colour': 'b'},
}

# line to be plotted
line_x = numpy.linspace (0.1, 100.0, 10**3)
line_y = 365.256363004 * line_x**1.5

# output file name
file_output = 'ai202209_s04_21.png'

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# making a plot using object-oriented interface
ax.plot (line_x, line_y, linestyle='--', linewidth=3, color='coral')
for planet in dic_planets.keys ():
    ax.plot (dic_planets[planet]['a'], dic_planets[planet]['P'], \
             linestyle='None', \
             marker=dic_planets[planet]['marker'], markersize=10, \
             color=dic_planets[planet]['colour'], label=planet)

# setting log-scale
ax.set_xscale ('log')
ax.set_yscale ('log')

# setting labels for x-axis and y-axis
ax.set_xlabel ('Semimajor Axis [au]')
ax.set_ylabel ('Orbital Period [day]')

# showing grid
ax.grid ()

# adding legend to the plot
ax.legend ()

# saving a plot as a file
fig.savefig (file_output)
