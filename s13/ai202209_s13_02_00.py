#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 16:23:59 (CST) daisuke>
#

#
# Time-stamp: <2021/05/23 16:39:10 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astroquery module
import astroquery.jplhorizons

# querying JPL Horizons
obj_earth   = astroquery.jplhorizons.Horizons (id_type=None, \
                                               id='399', \
                                               location='@ssb', \
                                               epochs={'start': '2000-01-01', \
                                                       'stop': '2023-01-01', \
                                                       'step': '1y'})
obj_hektor = astroquery.jplhorizons.Horizons (id_type='smallbody', \
                                              id='Hektor', \
                                              location='@ssb', \
                                               epochs={'start': '2000-01-01', \
                                                       'stop': '2023-01-01', \
                                                       'step': '1y'})

# state vector of the target object
v_0 = obj_earth.vectors ()
v_1 = obj_hektor.vectors ()

# printing result
print (f"# Distance between the Earth and Jovian Trojan asteroid (624) Hektor:")
print (f"# date/time, (x, y, z) of Earth, (x, y, z) of Hektor, distance in au")
for i in range ( len (v_0) ):
    datetime        = v_0['datetime_str'][i]
    datetime_fields = datetime.split ()
    dx   = v_0['x'][i] - v_1['x'][i]
    dy   = v_0['y'][i] - v_1['y'][i]
    dz   = v_0['z'][i] - v_1['z'][i]
    dist = numpy.sqrt (dx**2 + dy**2 + dz**2)
    print (f"  {datetime_fields[1]}", \
           f" {v_0['x'][i]:+6.3f} {v_0['y'][i]:+6.3f} {v_0['z'][i]:+6.3f}", \
           f" {v_1['x'][i]:+6.3f} {v_1['y'][i]:+6.3f} {v_1['z'][i]:+6.3f}", \
           f" {dist:6.3f}")
