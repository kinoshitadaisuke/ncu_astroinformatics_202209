#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/09 15:56:31 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# units
u_day = astropy.units.day

# target name
target = '90000090'

# observatory (D35 ==> Lulin Observatory)
obs_site = 'D35'

# date/time
t_start = astropy.time.Time ('2023-01-01T12:00:00', scale='utc', format='isot')
t_end   = t_start + 3.0 * u_day
t_step  = '1d'

# sending a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type='smallbody', id=target, \
                                       location=obs_site, \
                                       epochs={'start': t_start.isot, \
                                               'stop': t_end.isot, \
                                               'step': t_step})

# printing a query object
print (obj)

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing 'targetname', 'datetime_str', 'RA', 'DEC', 'AZ', 'EL',
# 'ObsEclLon', 'ObsEclLat', 'GlxLon', 'GlxLat', 'Tmag', 'r', 'delta'
columns = ['RA', 'DEC', 'AZ', 'EL', 'ObsEclLon', 'ObsEclLat', \
           'GlxLon', 'GlxLat', 'Tmag', 'r', 'delta']
print (f"{ephemerides[0]['targetname']}")
for eph in ephemerides:
    print (f"  {eph['datetime_str']}")
    for col in columns:
        print (f"    {col:12s} = {eph[col]}")
