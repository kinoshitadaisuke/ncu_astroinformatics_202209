#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 19:51:52 (CST) daisuke>
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

# printing sunset time
print (f'sunset = JD {sunset.jd} = {sunset.iso}')

# getting position of the Sun
sun = astropy.coordinates.get_body ('sun', sunset, location=location)

# conversion from equatorial into horizontal
altaz     = astropy.coordinates.AltAz (obstime=sunset, location=location)
sun_altaz = sun.transform_to (altaz)
sun_alt   = sun_altaz.alt
sun_az    = sun_altaz.az

# printing altitude and azimuth
print (f'position of the Sun at sunset:')
print (f'  alt = {sun_alt}')
print (f'  az  = {sun_az}')
