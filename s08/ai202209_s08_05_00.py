#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/07 00:37:08 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan
import astroplan.plots

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# units
u_m  = astropy.units.m
u_hr = astropy.units.hour

# output file name
file_output = 'sky_plot_00.png'

# getting coordinate of a fixed target
fomalhaut = astroplan.FixedTarget.from_name ('Fomalhaut')
m31       = astroplan.FixedTarget.from_name ('M31')
m45       = astroplan.FixedTarget.from_name ('M45')

# printing coordinate
print (f'{fomalhaut}')
print (f'{m31}')
print (f'{m45}')

# location of observer: NCU main campus
longitude = '121d11m12s'
latitude  = '+24d58m12s'
height    = 151.6 * u_m

# making a location object using Astropy
location = astropy.coordinates.EarthLocation.from_geodetic (lon=longitude, \
                                                            lat=latitude, \
                                                            height=height)

# making an observer object
observer = astroplan.Observer (location=location, name='NCU', \
                               timezone='Asia/Taipei')

# printing location
print (f'{observer}')

# date/time
time = astropy.time.Time ('2022-11-07 16:00:00', format='iso', \
                          scale='utc') \
                          + numpy.linspace (-6, +6, 13) * u_hr

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection='polar')

# grid
ax.grid ()

# plotting airmass change
astroplan.plots.plot_sky (fomalhaut, observer, time, ax=ax)
astroplan.plots.plot_sky (m31, observer, time, ax=ax)
astroplan.plots.plot_sky (m45, observer, time, ax=ax)

# title
ax.set_title ('Sky chart on 07/Nov/2022')

# legend
ax.legend (bbox_to_anchor=(1.05, 1.00), loc='upper left', shadow=True)

# saving file
fig.savefig (file_output, dpi=225, bbox_inches='tight')
