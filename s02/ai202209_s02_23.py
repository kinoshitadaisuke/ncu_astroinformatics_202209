#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 08:32:15 (CST) daisuke>
#

# importing datetime module
import datetime

# current time in local time
time_now_local = datetime.datetime.now ()

# printing result
print ("local time:       ", time_now_local)

# getting year, month, day, hour, minute, and second
YYYY = time_now_local.year
MM   = time_now_local.month
DD   = time_now_local.day
hh   = time_now_local.hour
mm   = time_now_local.minute
ss   = time_now_local.second + time_now_local.microsecond * 10**-6

# printing results
print (f'current date/time:',
       f'{YYYY:04d}/{MM:02d}/{DD:02d}T{hh:02d}:{mm:02d}:{ss:09.6f}')

# current time in UTC
time_now_utc   = datetime.datetime.now (tz=datetime.timezone.utc)

# printing result
print ("UTC:              ", time_now_utc)

# the other way to get current time in UTC
time_now_utc2  = datetime.datetime.utcnow ()

# printing result
print ("UTC:              ", time_now_utc2)
