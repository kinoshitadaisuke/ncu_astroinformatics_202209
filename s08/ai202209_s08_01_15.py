#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 16:11:14 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# units
u_m   = astropy.units.m
u_day = astropy.units.day

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# output file name
file_output = 'nighttime_length_greenwich.png'

# location of observer: Greenwich Observatory
longitude = '-0d00m05s'
latitude  = '+51d28m40s'
height    = 45.0 * u_m

# making a location object using Astropy
location = astropy.coordinates.EarthLocation.from_geodetic (lon=longitude, \
                                                            lat=latitude, \
                                                            height=height)

# making an observer object
observer = astroplan.Observer (location=location, name='Greenwich', \
                               timezone='UTC')

# sunset time and sunrise time
time_guess = astropy.time.Time ('2022-11-01 23:00:00', \
                                format='iso', scale='utc') \
                                + numpy.linspace (0.0, 500.0, 501) * u_day
sunset = observer.sun_set_time (time_guess, which='nearest', \
                                n_grid_points=500)
sunrise = observer.sun_rise_time (time_guess, which='nearest', \
                                  n_grid_points=500)

# nighttime length
night_length_hr = (sunrise.jd - sunset.jd) * 24.0

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date')
ax.set_ylabel ('Nighttime length [hr]')
ax.set_title ('Change of nighttime length')

# plotting data
ax.plot (time_guess.plot_date, night_length_hr, \
         linestyle='-', linewidth=3.0, color='red', label='Greenwich')
ax.grid ()

# legend
ax.legend (loc='upper right')

# ticks
months     = matplotlib.dates.MonthLocator ()
days       = matplotlib.dates.DayLocator ()
months_fmt = matplotlib.dates.DateFormatter ('%Y-%m-%d')
ax.xaxis.set_major_locator (months)
ax.xaxis.set_major_formatter (months_fmt)
ax.xaxis.set_minor_locator (days)

# formatting labels
fig.autofmt_xdate()

# saving file
fig.savefig (file_output, dpi=225)
