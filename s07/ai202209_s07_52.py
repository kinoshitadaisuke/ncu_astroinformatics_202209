#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 20:24:12 (CST) daisuke>
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
t_str = '2022-06-21 04:00:00'
t_utc = astropy.time.Time (t_str, format='iso', scale='utc')

# location of observer: NCU main campus
longitude = '121d11m12s'
latitude  = '+24d58m12s'
height    = 151.6 * u_m
observer = astropy.coordinates.EarthLocation (longitude, latitude, height)

# getting position of the Sun
sun = astropy.coordinates.get_body ('sun', t_utc, location=observer)

# RA and Dec
(sun_ra, sun_dec) = sun.to_string ('hmsdms').split ()

# conversion from equatorial into ecliptic
ecliptic     = astropy.coordinates.GeocentricMeanEcliptic (obstime=t_utc)
sun_ecliptic = sun.transform_to (ecliptic)
sun_lambda   = sun_ecliptic.lon
sun_beta     = sun_ecliptic.lat

# conversion from equatorial into horizontal
altaz     = astropy.coordinates.AltAz (obstime=t_utc, location=observer)
sun_altaz = sun.transform_to (altaz)
sun_alt   = sun_altaz.alt
sun_az    = sun_altaz.az
    

# printing position of the Sun
print (f'position of the Sun as observed at NCU main campus at {t_utc}:')
print (f'  (RA, Dec)      = ({sun_ra}, {sun_dec})')
print (f'  (lambda, beta) = ({sun_lambda}, {sun_beta})')
print (f'  (az, alt)      = ({sun_az}, {sun_alt})')
