#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/26 00:30:03 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# data file
file_data = 'usc.data'

# constant
c = scipy.constants.c

# opening file
with open (file_data, 'r') as fh:
    # reading file
    for line in fh:
        # extracting data
        name_str     = line[0:6].strip ()
        type_str     = line[86:104].strip ()
        z_str        = line[226:234].strip ()
        dist_str     = line[237:244].strip ()
        dist_err_str = line[245:251].strip ()

        # skip if redshift is missing
        if (z_str == ''):
            continue
        # skip if distance is missing
        if (dist_str == ''):
            continue
        # skip if type is not Ia
        if not (type_str == 'Ia'):
            continue

        # conversion from string to float
        z = float (z_str)
        dist = float (dist_str)
        dist_err = float (dist_err_str)
        dist_err_rel = dist_err / dist

        # calculation of velocity from redshift
        v = ( (z + 1.0)**2 - 1.0 ) / ( (z + 1.0)**2 + 1.0 ) * c * 10**-3

        # skip if redshift is negative
        if (z < 0.0):
            continue

        # skip if distance measurement is not accurate
        if (dist_err_rel > 0.1):
            continue
        
        # printing data
        print (f"{dist:15.8f} {dist_err:15.8f} {z:15.8f} {v:15.8f} # {name_str}")
