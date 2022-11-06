#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 16:36:41 (CST) daisuke>
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

# end of evening twilight
twilight_evening_guess = astropy.time.Time ('2022-11-07 10:00:00', \
                                            format='iso', scale='utc')
twilight_evening = observer.twilight_evening_astronomical \
    (twilight_evening_guess, which='nearest', n_grid_points=500)

# start of morning twilight
twilight_morning_guess = astropy.time.Time ('2022-11-07 22:00:00', \
                                            format='iso', scale='utc')
twilight_morning = observer.twilight_morning_astronomical \
    (twilight_morning_guess, which='nearest', n_grid_points=500)

# length of observable time
obs_time = (twilight_morning.jd - twilight_evening.jd) * 24.0

# printing result
print (f'end of evening twilight = JD {twilight_evening.jd}', \
       f'= {twilight_evening.iso}')
print (f'start of morning twilight = JD {twilight_morning.jd}', \
       f'= {twilight_morning.iso}')
print (f'length of observable time = {obs_time} hr')
