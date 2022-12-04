#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 16:47:23 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy
import numpy

# importing astropy module
import astropy.time
import astropy.units

#
# command-line argument analysis
#

# constructing parser object
parser = argparse.ArgumentParser (description='generating synthetic data')

# adding arguments
parser.add_argument ('-a', type=float, default=0.5, \
                     help='amplitude of brightness change (default: 0.5)')
parser.add_argument ('-p', type=float, default=12.0, \
                     help='period of brightness change in hr (default: 12.0)')
parser.add_argument ('-d', type=float, default=0.0, \
                     help='initial phase of brightness change (default: 0.0)')
parser.add_argument ('-m', type=float, default=20.0, \
                     help='mean magnitude (default: 20.0)')
parser.add_argument ('-s', type=str, default='2023-01-01T12:00:00', \
                     help='start date/time (default: 2023-01-01T12:00:00)')
parser.add_argument ('-e', type=str, default='2023-01-05T20:00:00', \
                     help='end date/time (default: 2023-01-05T20:00:00)')
parser.add_argument ('-n1', type=float, default=12.0, \
                     help='start of night in UT (default: 12)')
parser.add_argument ('-n2', type=float, default=20.0, \
                     help='end of night in UT (default: 20)')
parser.add_argument ('-c1', type=float, default=16.0, \
                     help='start of calibration in UT (default: 16)')
parser.add_argument ('-c2', type=float, default=17.0, \
                     help='end of calibration in UT (default: 17)')
parser.add_argument ('-t', type=float, default=180.0, \
                     help='exposure time in sec (default: 180.0)')
parser.add_argument ('-r', type=float, default=30.0, \
                     help='overhead time in sec (default: 30.0)')
parser.add_argument ('-u', type=float, default=0.03, \
                     help='error of photometry in mag (default: 0.03)')
parser.add_argument ('-o', type=str, default="out.data", \
                     help='output data file name')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# amplitude (mag)
A = args.a

# period (day)
P = args.p / 24

# phase
delta = 2.0 * numpy.pi * args.d

# average magnitude
c = args.m

# observable time
start_night = args.n1 / 24.0
end_night   = args.n2 / 24.0

# time for calibration data
start_calib = args.c1 / 24.0
end_calib   = args.c2 / 24.0

# start of observation
start_date = args.s
start_t = astropy.time.Time (start_date, scale='utc')
start_mjd = start_t.mjd

# end of observation
end_date = args.e
end_t = astropy.time.Time (end_date, scale='utc')
end_mjd = end_t.mjd

# exposure time (sec)
exptime = args.t

# overhead time (sec)
overhead = args.r

# interval between exposures (sec)
interval = exptime + overhead

# error
mean  = 0.0
sigma = args.u

# output file name
file_output = args.o

#
# generating synthetic data
#

# random number generator
rng = numpy.random.default_rng ()

# sine curve
def func (x, A, P, delta, c):
    y = A * numpy.sin (2.0 * numpy.pi * x / P + delta) + c
    return (y)

# opening file handle for writing
with open (file_output, 'w') as fh:
    # header of synthetic data
    header  = f"#\n"
    header += f"# synthetic data for period search\n"
    header += f"#\n"
    header += f"#  input parameters\n"
    header += f"#\n"
    header += f"#   start of obs. = {start_date} = MJD {start_mjd}\n"
    header += f"#   end of obs.   = {end_date} = MJD {end_mjd}\n"
    header += f"#   amplitude     = {A} mag\n"
    header += f"#   period        = {P} day = {P * 24.0} hr\n"
    header += f"#   delta         = {delta}\n"
    header += f"#   mean mag      = {c} mag\n"
    header += f"#   exposure time = {exptime} sec\n"
    header += f"#   overhead time = {overhead} sec\n"
    header += f"#   error         = {sigma} mag\n"
    header += f"#\n"
    header += f"#  generated data\n"
    header += f"#\n"
    header += f"#   date/time, MJD, mag, err\n"
    header += f"#\n"

    # writing header to file
    fh.write (header)
    
    # generation of a synthetic time-series data
    t = start_t
    while (t < end_t):
        # MJD
        mjd = t.mjd
        fractional_day = mjd - int (mjd)
        # error
        err = numpy.random.normal (mean, sigma)
        # apparent magnitude
        mag = func (mjd, A, P, delta, c) + err
        # writing data to file
        if ( ( (fractional_day >= start_night) \
               and (fractional_day <= end_night) ) \
             and ( (fractional_day < start_calib) \
                   or (fractional_day > end_calib) ) ):
            data = f"{t} {mjd:15.8f} {mag:9.6f} {abs (err):9.6f}\n"
            fh.write (data)
        # calculation of time of next exposure
        t += (interval + rng.uniform (0.0, 60.0) ) * astropy.units.second
