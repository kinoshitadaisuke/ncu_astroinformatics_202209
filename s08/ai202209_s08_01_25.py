#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 20:27:23 (CST) daisuke>
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
u_hr  = astropy.units.hour

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

# date/time
times = astropy.time.Time ('2022-11-07 04:00:00', format='iso', \
                           scale='utc') + numpy.linspace (0, 20, 21) * u_hr

# is it night time?
night = observer.is_night (times)

# printing results
print (f'# night time at NCU?')
for i in range (len (times)):
    print (f'{times[i]} ==> {night[i]}')
