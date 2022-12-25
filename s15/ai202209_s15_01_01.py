#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 12:27:51 (CST) daisuke>
#

# importing astropy module
import astropy.io.ascii

# CSV file name
file_csv = 'hygdata_v3.csv'

# reading a CSV file and storing data in an astropy table
table = astropy.io.ascii.read (file_csv, format='csv')

# printing astropy table
print (table)
