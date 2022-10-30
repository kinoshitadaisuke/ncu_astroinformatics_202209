#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 21:17:53 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# units
u_m = astropy.units.m

# date/time in UTC
t_str = '2022-10-25 11:00:00'
t_utc = astropy.time.Time (t_str, format='iso', scale='utc')

# location of observer: NCU main campus
longitude = '121d11m12s'
latitude  = '+24d58m12s'
height    = 151.6 * u_m
observer = astropy.coordinates.EarthLocation (longitude, latitude, height)

# getting position of the Sun
sun = astropy.coordinates.get_body ('sun', t_utc, location=observer)

# getting position of the Moon
moon = astropy.coordinates.get_body ('moon', t_utc, location=observer)

# RA and Dec
(sun_ra, sun_dec)   = sun.to_string ('hmsdms').split ()
(moon_ra, moon_dec) = moon.to_string ('hmsdms').split ()

# calculation of angular distance
separation = sun.separation (moon)

# printing result of calculation
print (f'Position of the Sun:')
print (f'  (RA, Dec) = ({sun_ra}, {sun_dec})')
print (f'Position of the Moon:')
print (f'  (RA, Dec) = ({moon_ra}, {moon_dec})')
print (f'Angular distance between the Sun and the Moon on {t_utc}')
print (f'  separation = {separation}')
