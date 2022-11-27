#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 19:23:38 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# constant
pi = numpy.pi

# units
u_sec = astropy.units.s
u_hr  = astropy.units.hr
u_day = astropy.units.day

#
# parameters for synthetic data generation
#

# amplitude (mag)
A = 0.5

# period (hr)
P = 2.0 * u_hr

# phase
delta = 2.0 * pi * 0.25

# average magnitude
mag_mean = 20.0

# start of observation
date_start = '2022-12-01T12:00:00'
t_start    = astropy.time.Time (date_start, scale='utc', format='isot')
mjd_start  = t_start.mjd

# end of observation
date_end = '2022-12-01T20:00:00'
t_end    = astropy.time.Time (date_end, scale='utc', format='isot')
mjd_end  = t_end.mjd

# exposure time (sec)
exptime = 120.0 * u_sec

# overhead time (sec)
overhead = 10.0 * u_sec

# interval between exposures (sec)
interval = exptime + overhead

# printing input parameters
print (f"#")
print (f"#")
print (f"# Synthetic data for period search")
print (f"#")
print (f"#")
print (f"# input parameters")
print (f"#")
print (f"#  start of obs. = {t_start} = MJD {t_start.mjd}")
print (f"#  end of obs.   = {t_end} = MJD {t_end.mjd}")
print (f"#  amplitude     = {A} mag")
print (f"#  period        = {P}")
print (f"#  delta         = {delta}")
print (f"#  average mag.  = {mag_mean} mag")
print (f"#  exposure time = {exptime}")
print (f"#  overhead      = {overhead}")

# function for sine curve
def sine_curve (datetime, A, P, delta, mag_mean):
    # date/time
    t = astropy.time.Time (datetime)
    # calculation of magnitude at given time t
    mag = A * numpy.sin (2.0 * pi * t.mjd / P.to (u_day).value + delta) \
        + mag_mean
    # returning magnitude
    return (mag)

#
# generation of synthetic data
#

# time between start date/time and end date/time
n_data = int ( (mjd_end - mjd_start) * u_day / interval) + 1

# generating a numpy array for date/time
data_t = t_start + numpy.linspace (0.0, interval * (n_data - 1), n_data)

# generating a numpy array for magnitude
data_mag = sine_curve (data_t, A, P, delta, mag_mean)

# printing generated synthetic data
print (f"#")
print (f"# date/time, MJD, magnitude")
print (f"#")
for i in range (len (data_t)):
    print (f"{data_t[i]} {data_t[i].mjd:15.9f} {data_mag[i]:9.6f}")
