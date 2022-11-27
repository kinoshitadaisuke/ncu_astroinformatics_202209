#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 20:09:09 (CST) daisuke>
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

# random number generator
rng = numpy.random.default_rng ()

#
# parameters for synthetic data generation
#

# amplitude (mag)
A = 0.3

# period (hr)
P = 7.5 * u_hr

# phase
delta = 2.0 * pi * 0.35

# average magnitude
mag_mean = 21.0

# observable time
start_night = (20 - 8) / 24.0 # 12:00 UT
end_night   = (28 - 8) / 24.0 # 20:00 UT

# time for calibration data
start_calib = (24 - 8) / 24.0 # 16:00 UT
end_calib   = (25 - 8) / 24.0 # 17:00 UT

# start of observation
date_start = '2022-12-01T12:00:00'
t_start    = astropy.time.Time (date_start, scale='utc', format='isot')
mjd_start  = t_start.mjd

# end of observation
date_end = '2022-12-04T20:00:00'
t_end    = astropy.time.Time (date_end, scale='utc', format='isot')
mjd_end  = t_end.mjd

# exposure time (sec)
exptime = 180.0 * u_sec

# overhead time (sec)
overhead = 30.0 * u_sec

# interval between exposures (sec)
interval = exptime + overhead

# error
error_mean  = 0.00
error_sigma = 0.03

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
def sine_curve (mjd, A, P, delta, mag_mean):
    # calculation of magnitude at given time t
    mag = A * numpy.sin (2.0 * pi * mjd / P.to (u_day).value + delta) \
        + mag_mean
    # returning magnitude
    return (mag)

#
# generation of synthetic data
#

print (f"#")
print (f"# date/time, MJD, magnitude, error")
print (f"#")
t = t_start
while (t <= t_end):
    # MJD
    mjd = t.mjd
    # fractional day
    fractional_day = mjd - int (mjd)
    # error
    err = rng.normal (loc=error_mean, scale=error_sigma)
    # apparent magnitude
    mag = sine_curve (mjd, A, P, delta, mag_mean) + err
    # printing data
    if ( ( (fractional_day >= start_night) \
           and (fractional_day <= end_night) ) \
         and ( (fractional_day < start_calib) \
               or (fractional_day > end_calib) ) ):
        print (f"{t} {mjd:15.9f} {mag:9.6f} {abs (err):9.6f}")

    # calculation of time of next exposure
    t += interval + rng.uniform (0.0, 60.0) * u_sec
