#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 16:44:48 (CST) daisuke>
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

# time
time_guess = astropy.time.Time ('2022-11-01 16:00:00', \
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

# printing result
for i in range (len (time_guess)):
    print (f'{time_guess[i]} {obs_time[i]:8.5f} hr')
