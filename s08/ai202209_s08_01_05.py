#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 13:52:32 (CST) daisuke>
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
file_output = 'sun_maxalt_ncu.png'

# empty numpy arrays for plotting
dates = numpy.array ([])
alts  = numpy.array ([])

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

# initial guess of local noon (501 days from 01/Nov/2022)
time_guess = astropy.time.Time ('2022-11-01 05:00:00', \
                                format='iso', scale='utc') \
                                + numpy.linspace (0.0, 500.0, 501) * u_day

# calculation of altitude angle at local noon
for i in range (len (time_guess)):
    # local apparent solar noon
    noon = observer.noon (time_guess[i], which='nearest', n_grid_points=500)

    # getting position of the Sun
    sun = astropy.coordinates.get_body ('sun', noon, location=location)

    # conversion from equatorial into horizontal
    altaz     = astropy.coordinates.AltAz (obstime=noon, location=location)
    sun_altaz = sun.transform_to (altaz)

    # printing result
    print (f'{noon.iso} {sun_altaz.alt}')

    # appending data to numpy arrays
    dates = numpy.append (dates, noon.plot_date)
    alts  = numpy.append (alts, sun_altaz.alt.value)

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date')
ax.set_ylabel ('Altitude Angle [deg]')
ax.set_title ('Change of Maximum Altitude of the Sun')

# plotting data
ax.plot (dates, alts, linestyle='-', linewidth=3.0, color='red', \
         label='NCU, Taiwan')
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
fig.savefig (file_output)
