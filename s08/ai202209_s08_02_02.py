#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 21:02:33 (CST) daisuke>
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
u_deg = astropy.units.degree

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
time = astropy.time.Time ('2022-11-08 11:00:00', format='iso', scale='utc')

# moon illumination
illumination = observer.moon_illumination (time)

# moon phase
phase_rad = observer.moon_phase (time)
phase_deg = phase_rad.to (u_deg)

# printing result
print (f'time: {time}')
print (f'  illumination fraction = {illumination:5.3f}')
print (f'  moon phase            = {phase_deg:6.2f}')
