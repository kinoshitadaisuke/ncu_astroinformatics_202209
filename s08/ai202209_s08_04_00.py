#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 23:32:38 (CST) daisuke>
#

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

# output file name
file_output = 'airmass_plot_00.png'

# getting coordinate of a fixed target
fomalhaut = astroplan.FixedTarget.from_name ('Fomalhaut')
sirius    = astroplan.FixedTarget.from_name ('Sirius')
m31       = astroplan.FixedTarget.from_name ('M31')

# printing coordinate
print (f'{fomalhaut}')
print (f'{sirius}')
print (f'{m31}')

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
time = astropy.time.Time ('2022-11-07 16:00:00', format='iso', scale='utc')

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# plotting airmass change
astroplan.plots.plot_airmass (fomalhaut, observer, time, ax=ax)
astroplan.plots.plot_airmass (sirius, observer, time, ax=ax)
astroplan.plots.plot_airmass (m31, observer, time, ax=ax)

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225, bbox_inches='tight')
