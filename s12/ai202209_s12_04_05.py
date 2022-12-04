#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 22:29:27 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.timeseries

#
# command-line argument analysis
#

# constructing parser object
parser = argparse.ArgumentParser (description='Lomb-Scargle periodogram')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.data", \
                     help='output data file name')
parser.add_argument ('-n', type=int, default=30, \
                     help='samples per peak for frequency grid spacing')
parser.add_argument ('-a', type=float, default=0.01, \
                     help='minimum trial period in min (default: 0.01)')
parser.add_argument ('-b', type=float, default=14400.0, \
                     help='maximum trial period in min (default: 14400)')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_in = args.i

# output file name
file_out = args.o

# samples per peak
n = args.n

# minimum trial period
per_min_min  = args.a
per_min_hr   = per_min_min / 60.0
per_min_day  = per_min_min / 1440.0
freq_max_day = 1.0 / per_min_day

# maximum trial period
per_max_min  = args.b
per_max_hr   = per_max_min / 60.0
per_max_day  = per_max_min / 1440.0
freq_min_day = 1.0 / per_max_day

#
# period search
#

# empty numpy arrays for storing data
data_mjd = numpy.array ([])
data_mag = numpy.array ([])
data_err = numpy.array ([])

# opening file for reading
with open (file_in, 'r') as fh_in:
    # reading file line-by-line
    for line in fh_in:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (datetime_str, mjd_str, mag_str, err_str) = line.split ()
        # conversion from string into float
        mjd = float (mjd_str)
        mag = float (mag_str)
        err = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd = numpy.append (data_mjd, mjd)
        data_mag = numpy.append (data_mag, mag)
        data_err = numpy.append (data_err, err)

# Lomb-Scargle periodogram
freq, power = astropy.timeseries.LombScargle (data_mjd, data_mag) \
                                .autopower (minimum_frequency=freq_min_day, \
                                            maximum_frequency=freq_max_day, \
                                            samples_per_peak=n)

# opening file for writing
with open (file_out, 'w') as fh_out:
    # writing header to file
    header  = f"# result of period search by Lomb-Scargle periodogram\n"
    header += f"# using astropy.timeseries.LombScargle ()\n"
    header += f"#\n"
    header += f"# input file           = '{file_in}'\n"
    header += f"# output file          = '{file_out}'\n"
    header += f"# minimum trial period = {per_min_min} min = {per_min_hr} hr\n"
    header += f"# maximum trial period = {per_max_min} min = {per_max_hr} hr\n"
    header += f"# samples_per_peak     = {n}\n"
    header += f"#\n"
    header += f"# frequency in cycle day^-1, period in day, period in hr, "
    header += f"period in min, power\n"
    header += f"#\n"
    fh_out.write (header)

    # writing data to file
    for i in range ( len (freq) ):
        record = f"{freq[i]:15.8f} {1.0 / freq[i]:15.8f}" \
            + f" {1.0 / freq[i] * 24.0:15.8f} {1.0 / freq[i] * 1440:15.8f}" \
            + f" {power[i]:15.8f}\n"
        fh_out.write (record)
