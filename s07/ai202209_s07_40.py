#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 16:40:30 (CST) daisuke>
#

# importing datetime module
import datetime

# importing astropy module
import astropy.time

# getting current date/time
now = astropy.time.Time.now ()

# printing date/time
print (f'now  = {now}')
print (f'     = JD  {now.jd:14.6f}')
print (f'     = MJD {now.mjd:14.6f}')
