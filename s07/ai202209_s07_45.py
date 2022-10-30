#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 17:30:47 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# units
u_hr = astropy.units.hr

# location of observer
longitude = '120d52m25s'
latitude  = '+23d28m07s'

# t0
t0 = astropy.time.Time ('2022-10-31 10:00:00', format='iso', scale='utc', \
                        location=(longitude, latitude) )

# times
delta_t = numpy.linspace (0.0, 12.0, 13) * u_hr
times   = t0 + delta_t

# calculation of local sidereal time
lsts = times.sidereal_time ('apparent')

# printing results of calculations
print (f'local sidereal time at Lulin ({longitude}, {latitude})')
for i in range (len (times)):
    print (f'UT: {times[i]}  ==>  ', \
           f'LST: {int (lsts[i].hms.h):02d}:{int (lsts[i].hms.m):02d}', \
           f':{lsts[i].hms.s:06.3f}', sep='')
