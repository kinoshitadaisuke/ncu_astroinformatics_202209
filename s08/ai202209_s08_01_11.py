#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 22:51:24 (CST) daisuke>
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

# output file name
file_output = 'sun_sunrise_az_uppsala.png'

# units
u_m   = astropy.units.m
u_day = astropy.units.day

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# empty arrays for plotting
dates = numpy.array ([])
azs   = numpy.array ([])

# location of observer: Uppsala Observatory
longitude = '+17d38m13.1s'
latitude  = '+59d51m35.5s'
height    = 37.9 * u_m

# making a location object using Astropy
location = astropy.coordinates.EarthLocation.from_geodetic (lon=longitude, \
                                                            lat=latitude, \
                                                            height=height)

# making an observer object
observer = astroplan.Observer (location=location, name='Uppsala')

# sunset time
time_guess = astropy.time.Time ('2022-11-01 09:00:00', \
                                format='iso', scale='utc') \
                                + numpy.linspace (0.0, 500.0, 501) * u_day

# calculation of azimuth angle at sunrise
for i in range (len (time_guess)):
    # printing status
    if (i % 50 == 0):
        print (f'Now, calculating sunrise on {time_guess[i]}...')
    
    # sunrise time
    sunrise = observer.sun_rise_time (time_guess[i], which='nearest', \
                                      n_grid_points=500)

    # getting position of the Sun
    sun = astropy.coordinates.get_body ('sun', sunrise, location=location)

    # conversion from equatorial into horizontal
    altaz = astropy.coordinates.AltAz (obstime=sunrise, location=location)
    sun_altaz = sun.transform_to (altaz)

    # appending data to numpy arrays
    dates = numpy.append (dates, sunrise.plot_date)
    azs   = numpy.append (azs, sun_altaz.az.value)

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date')
ax.set_ylabel ('Azimuth Angle [deg]')
ax.set_title ('Change of azimuth of the Sun at sunrise')

# plotting data
ax.plot (dates, azs, linestyle='-', linewidth=3.0, color='red', \
         label='Uppsala')
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
