#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/20 13:03:17 (CST) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# date/time
date = astropy.time.Time ('2023-01-01 00:00:00')

# target asteroid name
asteroid = 'Ceres'

# set-up a query for JPL Horizons
query = astroquery.jplhorizons.Horizons (id=asteroid, \
                                         id_type='smallbody', \
                                         epochs=date.jd)

# fetching ephemeris of asteroid
eph = query.ephemerides ()

# printing position of asteroid
print (f"Ephemeris of asteroid '{eph['targetname'][0]}':")
print (f"  RA  = {eph['RA'][0]:8.4f} deg")
print (f"  Dec = {eph['DEC'][0]:+8.4f} deg")
