#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 16:08:47 (CST) daisuke>
#

# two numbers
a = 23
b = 7

# calculation
quotient  = a // b
remainder = a % b

# printing result of calculation
print (f'a = {a}')
print (f'b = {b}')
print (f'quotient  = {quotient}')
print (f'remainder = {remainder}')
print (f'{b} * {quotient} + {remainder} = {b * quotient + remainder}')
