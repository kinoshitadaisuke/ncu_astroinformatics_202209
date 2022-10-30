#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 19:19:15 (CST) daisuke>
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
sun = astropy.coordinates.get_body ('sun', t_utc, location=observer)

# printing position of the Sun
print (f'position of the Sun as observed at NCU main campus at {t_utc}:')
print (f'  RA:  {int (sun.ra.hms.h):02d}:{int (sun.ra.hms.m):02d}', \
       f':{sun.ra.hms.s:06.3f}', sep='')
print (f'  Dec: {int (sun.dec.dms.d):02d}', \
       f':{abs (int (sun.dec.dms.m)):02d}:{abs (sun.dec.dms.s):06.3f}', \
       sep='')
