#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 19:22:16 (CST) daisuke>
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
t_str = '2022-10-31 04:00:00'
t_utc = astropy.time.Time (t_str, format='iso', scale='utc')

# location of observer: NCU main campus
longitude = '121d11m12s'
latitude  = '+24d58m12s'
height    = 151.6 * u_m
observer = astropy.coordinates.EarthLocation (longitude, latitude, height)

# getting position of the Sun
moon = astropy.coordinates.get_body ('moon', t_utc, location=observer)

# printing position of the Sun
print (f'position of the Moon as observed at NCU main campus at {t_utc}:')
print (f'  RA:  {int (moon.ra.hms.h):02d}:{int (moon.ra.hms.m):02d}', \
       f':{moon.ra.hms.s:06.3f}', sep='')
print (f'  Dec: {int (moon.dec.dms.d):02d}', \
       f':{abs (int (moon.dec.dms.m)):02d}:{abs (moon.dec.dms.s):06.3f}', \
       sep='')
