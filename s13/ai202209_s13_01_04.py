#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/09 15:25:33 (CST) daisuke>
#

# importing astropy module
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# units
u_hr  = astropy.units.hour

# target name
target = '599'

# observatory (D35 ==> Lulin Observatory)
obs_site = 'D35'

# date/time
t_start = astropy.time.Time ('2022-12-12T10:00:00', scale='utc', format='isot')
t_end   = t_start + 6.0 * u_hr
t_step  = '1h'

# sending a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type=None, id=target, \
                                       location=obs_site, \
                                       epochs={'start': t_start.isot, \
                                               'stop': t_end.isot, \
                                               'step': t_step})

# printing a query object
print (obj)

# getting ephemerides
ephemerides = obj.ephemerides ()

# printing 'targetname', 'datetime_str', 'RA', 'DEC', 'AZ', 'EL',
# 'ObsEclLon', 'ObsEclLat', 'GlxLon', 'GlxLat', 'V', 'r', 'delta'
columns = ['RA', 'DEC', 'AZ', 'EL', 'ObsEclLon', 'ObsEclLat', \
           'GlxLon', 'GlxLat', 'V', 'r', 'delta']
print (f"{ephemerides[0]['targetname']}")
for eph in ephemerides:
    print (f"  {eph['datetime_str']}")
    for col in columns:
        print (f"    {col:12s} = {eph[col]}")
