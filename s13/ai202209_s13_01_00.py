#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 11:05:47 (CST) daisuke>
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

# printing object type of "ephemerides"
print (type (ephemerides))

# printing ephemerides
print (ephemerides)
