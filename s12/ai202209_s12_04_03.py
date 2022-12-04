#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 22:14:10 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

#
# command-line argument analysis
#

# constructing parser object
parser = argparse.ArgumentParser (description='plotting time-series data')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

# coefficients
a = 57.62567140725382
b = 4892499.279785005

#
# reading data
#

# empty numpy arrays for storing data
data_mjd  = numpy.array ([])
data_flux = numpy.array ([])
data_err  = numpy.array ([])

# opening file for reading
with open (file_data, 'r') as fh_read:
    # opening file for writing
    with open (file_fig, 'w') as fh_write:
        # reading file line-by-line
        for line in fh_read:
            # skipping line if the line starts with '#'
            if (line[0] == '#'):
                continue
            # removing line feed at the end of line
            line = line.strip ()
            # splitting data
            (datetime_str, mjd_str, flux_str, err_str) = line.split ()
            # check data
            if (flux_str == 'nan'):
                continue
            # conversion from string into float
            mjd  = float (mjd_str)
            flux = float (flux_str) / (-a * mjd + b)
            err  = float (err_str) / float (flux_str)
            # writing data
            record = f"{datetime_str} {mjd:.10f} {flux:.10f} {err:.10f}\n"
            fh_write.write (record)
