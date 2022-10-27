#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/27 15:15:42 (CST) daisuke>
#

# importing astropy module
import astropy.constants

# astronomical unit
au = astropy.constants.au

# printing au
print (au)
print ()

# parsec
pc = astropy.constants.pc

# printing pc
print (pc)
print ()

# 1 au
print (f'1 au = {au:g}')

# 1 pc
print (f'1 pc = {pc:g}\n     = {pc / au} au')
