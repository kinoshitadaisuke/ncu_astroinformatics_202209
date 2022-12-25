#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 21:33:37 (CST) daisuke>
#

# importing astropy module
import astropy.io.ascii

# file
file_data = 'ned1d_with_header.csv'

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# printing astropy table summary information
print (rawdata.info ())
