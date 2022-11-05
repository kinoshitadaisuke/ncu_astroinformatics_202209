#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 23:12:42 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan

# units
u_m = astropy.units.m

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

# printing created observer object
print (observer)

# sunset time
sunset_guess = astropy.time.Time ('2022-11-07 10:00:00', \
                                  format='iso', scale='utc')
sunset = observer.sun_set_time (sunset_guess, which='nearest', \
                                n_grid_points=500)

# sunrise time
sunrise_guess = astropy.time.Time ('2022-11-08 00:00:00', \
                                   format='iso', scale='utc')
sunrise = observer.sun_rise_time (sunrise_guess, which='nearest', \
                                  n_grid_points=500)

# nighttime length
night_length_day = sunrise.jd - sunset.jd
night_length_hr  = night_length_day * 24.0

# printing sunset time, sunrise time, and length of nighttime
print (f'sunset  = JD {sunset.jd:14.6f} = {sunset.iso}')
print (f'sunrise = JD {sunrise.jd:14.6f} = {sunrise.iso}')
print (f'nighttime length = {night_length_day} day = {night_length_hr} hr')
