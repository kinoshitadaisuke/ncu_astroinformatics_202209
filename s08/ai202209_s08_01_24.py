#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 20:17:26 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan

# units
u_m   = astropy.units.m
u_day = astropy.units.day

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# output file name
file_output = 'obstime_length_picdumidi.png'

# location of observer: Pic du Midi Observatory
longitude = '+0d08m34s'
latitude  = '+42d56m11s'
height    = 2877.0 * u_m

# making a location object using Astropy
location = astropy.coordinates.EarthLocation.from_geodetic (lon=longitude, \
                                                            lat=latitude, \
                                                            height=height)

# making an observer object
observer = astroplan.Observer (location=location, name='Pic du Midi', \
                               timezone='CET')

# time
time_guess = astropy.time.Time ('2022-11-01 01:00:00', \
                                format='iso', scale='utc') \
                                + numpy.linspace (0.0, 500.0, 501) * u_day

# end of evening twilight
twilight_evening = observer.twilight_evening_astronomical \
    (time_guess, which='nearest', n_grid_points=500)

# start of morning twilight
twilight_morning = observer.twilight_morning_astronomical \
    (time_guess, which='nearest', n_grid_points=500)

# length of observable time
obs_time = (twilight_morning.jd - twilight_evening.jd) * 24.0

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date')
ax.set_ylabel ('Nighttime length [hr]')
ax.set_title ('Change of observable time length')

# plotting data
ax.plot (time_guess.plot_date, obs_time, \
         linestyle='-', linewidth=3.0, color='red', label='Pic du Midi')
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
