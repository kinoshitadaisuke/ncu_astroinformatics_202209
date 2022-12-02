#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/02 23:51:16 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# command-line argument analysis
parser = argparse.ArgumentParser (description='synthetic data generation')
parser.add_argument ('-o', type=str, default="out.data", \
                     help='output file name')
parser.add_argument ('-s', type=str, default="2000-01-01T12:00:00", \
                     help='start date/time of observation')
parser.add_argument ('-e', type=str, default="2000-01-02T12:00:00", \
                     help='end date/time of observation')
parser.add_argument ('-p', type=float, default=1.0, \
                     help='period in hour')
parser.add_argument ('-a', type=float, default=1.0, \
                     help='amplitude in mag')
parser.add_argument ('-m', type=float, default=20.0, \
                     help='mean magnitude')
parser.add_argument ('-u', type=float, default=0.1, \
                     help='error in mag')
parser.add_argument ('-t', type=float, default=180.0, \
                     help='time interval between exposures in sec')
args = parser.parse_args ()

# output file name
file_data = args.o

# start date/time of observation
datetime_start = args.s
t_start        = astropy.time.Time (datetime_start, scale='utc')
mjd_start      = t_start.mjd

# end date/time of observation
datetime_end = args.e
t_end        = astropy.time.Time (datetime_end, scale='utc')
mjd_end      = t_end.mjd

# period in hour
period_hr  = args.p
period_day = period_hr / 24.0

# amplitude in mag
amplitude = args.a

# mean magnitude
mag_mean = args.m

# error in magnitude
mag_error = args.u

# time interval between exposures
interval_sec = args.t
interval_day = interval_sec / 86400.0

# function
def func (t, t_epoch, period_day, amplitude, mag_mean):
    mag = amplitude \
        * numpy.sin (2.0 * numpy.pi * (t - t_epoch) / period_day) \
        + mag_mean
    return (mag)

# opening file for writing
with open (file_data, 'w') as fh:
    # printing header
    header  = f"#\n"
    header  = f"# synthetic time-series data for period search\n"
    header += f"#\n"
    header += f"# input parameters\n"
    header += f"#\n"
    header += f"#  output file name = '{file_data}'\n"
    header += f"#  start date/time of observation = '{datetime_start}'\n"
    header += f"#                                 = '{t_start}'\n"
    header += f"#                                 = MJD {mjd_start}\n"
    header += f"#  end date/time of observation   = '{datetime_end}'\n"
    header += f"#                                 = '{t_end}'\n"
    header += f"#                                 = MJD {mjd_end}\n"
    header += f"#  period in hour            = {period_hr} hour\n"
    header += f"#  period in day             = {period_day} day\n"
    header += f"#  amplitude in mag          = {amplitude} mag\n"
    header += f"#  mean magnitude            = {mag_mean} mag\n"
    header += f"#  error in magnitude        = {mag_error} mag\n"
    header += f"#  time interval between exp = {interval_sec} sec\n"
    header += f"#\n"
    header += f"# generated synthetic data\n"
    header += f"#\n"
    header += f"# date/time, MJD, mag, err\n"
    header += f"#\n"
    fh.write (header)

    # epoch
    t_epoch = mjd_start

    # generation of data
    t = mjd_start
    while (t < mjd_end):
        # magnitude
        mag = func (t, t_epoch, period_day, amplitude, mag_mean)

        # date/time
        datetime = astropy.time.Time (t, format='mjd')

        # writing data
        obs = f"{datetime.fits} {t:14.8f} {mag:9.6f} {mag_error:9.6f}\n"
        fh.write (obs)
    
        # adding interval_day to t
        t += interval_day
