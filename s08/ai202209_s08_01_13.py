#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 10:58:35 (CST) daisuke>
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

# sunset time and sunrise time
time_guess = astropy.time.Time ('2022-11-01 16:00:00', \
                                format='iso', scale='utc') \
                                + numpy.linspace (0.0, 500.0, 501) * u_day
sunset = observer.sun_set_time (time_guess, which='nearest', \
                                n_grid_points=500)
sunrise = observer.sun_rise_time (time_guess, which='nearest', \
                                  n_grid_points=500)

# nighttime length
night_length_hr = (sunrise.jd - sunset.jd) * 24.0

# printing date/time and length of nighttime
for i in range (len (time_guess)):
    print (f'{time_guess[i]} {night_length_hr[i]:8.5f} hr')
