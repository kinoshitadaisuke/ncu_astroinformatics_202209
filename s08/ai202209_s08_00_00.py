#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/04 15:29:44 (CST) daisuke>
#

# importing astropy module
import astropy.units

# importing astroplan module
import astroplan

# units
u_m = astropy.units.m

# location of observer: NCU main campus
longitude = '121d11m12s'
latitude  = '+24d58m12s'
height    = 151.6 * u_m

# making an observer object
observer = astroplan.Observer (longitude=longitude, latitude=latitude, \
                               elevation=height, name='NCU', \
                               timezone='Asia/Taipei')

# printing created observer object
print (observer)
