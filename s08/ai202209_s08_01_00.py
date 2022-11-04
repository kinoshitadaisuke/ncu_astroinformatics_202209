#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/04 16:35:47 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan

# units
u_m = astropy.units.m

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

# local apparent solar midnight
local_midnight_guess = astropy.time.Time ('2022-11-07 16:00:00', \
                                          format='iso', scale='utc')
local_midnight = observer.midnight (local_midnight_guess)

# printing local apparent solar midnight
print (f'local midnight = JD {local_midnight.jd} = {local_midnight.iso}')
