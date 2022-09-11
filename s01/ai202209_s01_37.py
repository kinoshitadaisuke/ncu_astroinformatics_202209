#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/11 17:56:00 (CST) daisuke>
#

# sample string
string1 = 'National Central University'

# printing a string
print (f'string1       = {string1}')

# using index for a string
print (f'string1[0]    = {string1[0]}')
print (f'string1[1]    = {string1[1]}')
print (f'string1[2]    = {string1[2]}')
print (f'string1[-1]   = {string1[-1]}')
print (f'string1[-2]   = {string1[-2]}')

# using slice for a string
print (f'string1[9:16] = {string1[9:16]}')
print (f'string1[9:]   = {string1[9:]}')
print (f'string1[:16]  = {string1[:16]}')

# using replace method
string2 = string1.replace ('Central', 'Tsing-Hua')
print (f'string2       = {string2}')

# concatenating strings
string3 = 'Institute'
string4 = 'of'
string5 = 'Astronomy'
string6 = string3 + ' ' + string4 + ' ' + string5
print (f"{string3} + ' ' + {string4} + ' ' + {string5} = {string6}")
