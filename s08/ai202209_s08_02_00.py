#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 20:39:07 (CST) daisuke>
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

# printing observer object
print (f'{observer}')

# date/time
time = astropy.time.Time ('2022-11-07 16:00:00', format='iso', scale='utc')

# moon rise time
moonrise = observer.moon_rise_time (time, which='nearest', \
                                    n_grid_points=500)

# printing result
print (f'moon rise time = {moonrise.iso}')
