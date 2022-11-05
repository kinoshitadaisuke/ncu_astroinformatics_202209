#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 13:20:13 (CST) daisuke>
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
