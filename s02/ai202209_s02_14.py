#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 15:49:50 (CST) daisuke>
#

# importing decimal module
import decimal

# importing math module
import math

# precision
decimal.getcontext ().prec = 50

# first 50 digits of pi
pi50 = decimal.Decimal ('3.1415926535897932384626433832795028841971693993751')

# number of terms to calculate
n = 10**6

# initial value of pi
pi = decimal.Decimal ('0.0')

# calculation of pi using Leibniz formula
for i in range (n):
    pi += decimal.Decimal ('4.0') / (2 * i + 1) * (-1)**i

# printing math.pi, pi by Leibniz formula, first 50 digits of pi
print (f'math.pi               = {math.pi:51.49f}')
print (f'pi by Leibniz formula = {pi}')
print (f'first 50 digits of pi = {pi50}')
