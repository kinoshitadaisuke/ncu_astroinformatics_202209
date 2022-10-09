#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/09 13:58:59 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# some units for length
au     = scipy.constants.au
ly     = scipy.constants.light_year
parsec = scipy.constants.parsec

# printing units for length
print (f'au     = {au:g} [m]')
print (f'ly     = {ly:g} [m]')
print (f'parsec = {parsec:g} [m]')
