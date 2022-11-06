#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 22:05:03 (CST) daisuke>
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
u_m  = astropy.units.m
u_hr = astropy.units.hour

# getting coordinate of a fixed target
canopus = astroplan.FixedTarget.from_name ('Canopus')

# printing coordinate
print (f'{canopus}')

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
times = astropy.time.Time ('2022-11-07 16:00:00', format='iso', scale='utc')

# rise time
risetime = observer.target_rise_time (times, canopus, which='nearest', \
                                      n_grid_points=500)

# printing results
print (f'Rise time of Canopus = {risetime.iso}')
