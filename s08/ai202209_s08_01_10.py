#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 21:58:42 (CST) daisuke>
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

# sunrise time
sunrise_guess = astropy.time.Time ('2022-11-08 00:00:00', \
                                   format='iso', scale='utc')
sunrise = observer.sun_rise_time (sunrise_guess, which='nearest', \
                                  n_grid_points=500)

# printing sunrise time
print (f'sunrise = JD {sunrise.jd} = {sunrise.iso}')

# getting position of the Sun
sun = astropy.coordinates.get_body ('sun', sunrise, location=location)

# conversion from equatorial into horizontal
altaz     = astropy.coordinates.AltAz (obstime=sunrise, location=location)
sun_altaz = sun.transform_to (altaz)
sun_alt   = sun_altaz.alt
sun_az    = sun_altaz.az

# printing altitude and azimuth
print (f'position of the Sun at sunrise:')
print (f'  alt = {sun_alt}')
print (f'  az  = {sun_az}')
