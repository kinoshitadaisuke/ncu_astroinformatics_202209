#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 21:14:30 (CST) daisuke>
#

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# units
u_au = astropy.units.au

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# time t = 2022-10-03T00:00:00 (UTC)
t = astropy.time.Time ('2022-10-03T00:00:00', format='isot', scale='utc')

# getting positions of Sun, Earth, and Moon
sun     = astropy.coordinates.get_body_barycentric ('sun', t)
mercury = astropy.coordinates.get_body_barycentric ('mercury', t)
venus   = astropy.coordinates.get_body_barycentric ('venus', t)
earth   = astropy.coordinates.get_body_barycentric ('earth', t)
mars    = astropy.coordinates.get_body_barycentric ('mars', t)

# printing positions of the Sun and planets
print (f'Positions of the Sun and the planets at t = {t}')
print (f'  Sun:')
print (f'    X = {sun.x} = {sun.x.to (u_au)}')
print (f'    Y = {sun.y} = {sun.y.to (u_au)}')
print (f'    Z = {sun.z} = {sun.z.to (u_au)}')
print (f'  Mercury:')
print (f'    X = {mercury.x} = {mercury.x.to (u_au)}')
print (f'    Y = {mercury.y} = {mercury.y.to (u_au)}')
print (f'    Z = {mercury.z} = {mercury.z.to (u_au)}')
print (f'  Venus:')
print (f'    X = {venus.x} = {venus.x.to (u_au)}')
print (f'    Y = {venus.y} = {venus.y.to (u_au)}')
print (f'    Z = {venus.z} = {venus.z.to (u_au)}')
print (f'  Earth:')
print (f'    X = {earth.x} = {earth.x.to (u_au)}')
print (f'    Y = {earth.y} = {earth.y.to (u_au)}')
print (f'    Z = {earth.z} = {earth.z.to (u_au)}')
print (f'  Mars:')
print (f'    X = {mars.x} = {mars.x.to (u_au)}')
print (f'    Y = {mars.y} = {mars.y.to (u_au)}')
print (f'    Z = {mars.z} = {mars.z.to (u_au)}')
