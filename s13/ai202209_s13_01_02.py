#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/09 12:42:58 (CST) daisuke>
#

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# target name
target = 'Sun'

# observatory (D35 ==> Lulin Observatory)
obs_site = 'D35'

# date/time
t  = astropy.time.Time ('2023-03-21T04:00:00', scale='utc', format='isot')
jd = t.jd

# sending a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type=None, id=target, \
                                       location=obs_site, epochs=jd)

# printing a query object
print (obj)

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing 'targetname', 'datetime_str', 'RA', 'DEC', 'AZ', 'EL',
# 'ObsEclLon', 'ObsEclLat', 'GlxLon', 'GlxLat', 'V', 'r', and 'delta'
columns = ['RA', 'DEC', 'AZ', 'EL', 'ObsEclLon', 'ObsEclLat', \
           'GlxLon', 'GlxLat', 'V', 'r', 'delta']
print (f"{ephemerides[0]['targetname']}")
for eph in ephemerides:
    print (f"  {eph['datetime_str']}")
    for col in columns:
        print (f"    {col:12s} = {eph[col]}")
