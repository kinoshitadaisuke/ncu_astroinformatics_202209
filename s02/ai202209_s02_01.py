#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/16 16:09:04 (CST) daisuke>
#

# importing math module
import math

#
# some useful functions
#

# two floats "a" and "b"
a = 12.34
b = -56.78

# floor
a_floor = math.floor (a)
b_floor = math.floor (b)

# printing results
print (f'Use of floor () function:')
print (f'  a         = {a}')
print (f'  floor (a) = {a_floor}')
print (f'  {a_floor} is the largest integer less than or equal to {a}.')
print (f'  b         = {b}')
print (f'  floor (b) = {b_floor}')
print (f'  {b_floor} is the largest integer less than or equal to {b}.')
print (f'')

# ceil
a_ceil = math.ceil (a)
b_ceil = math.ceil (b)

# printing results
print (f'Use of ceil () function:')
print (f'  a         = {a}')
print (f'  ceil (a)  = {a_ceil}')
print (f'  {a_ceil} is the smallest integer greater than or equal to {a}.')
print (f'  b         = {b}')
print (f'  ceil (b) = {b_ceil}')
print (f'  {b_ceil} is the smallest integer greater than or equal to {b}.')
print (f'')

# trunc
a_trunc = math.trunc (a)
b_trunc = math.trunc (b)

# printing results
print (f'Use of trunc () function:')
print (f'  a         = {a}')
print (f'  trunc (a)  = {a_trunc}')
print (f'  {a_trunc} is the integer part of {a}.')
print (f'  b         = {b}')
print (f'  trunc (b) = {b_trunc}')
print (f'  {b_trunc} is the integer part of {b}.')
print (f'')

# modf
(a_fractional, a_integer) = math.modf (a)
(b_fractional, b_integer) = math.modf (b)

# printing results
print (f'Use of modf () function:')
print (f'  a                    = {a}')
print (f'  integer part of a    = {a_integer}')
print (f'  fractional part of a = {a_fractional}')
print (f'  b                    = {b}')
print (f'  integer part of b    = {b_integer}')
print (f'  fractional part of b = {b_fractional}')
print (f'')

# fabs
a_abs = math.fabs (a)
b_abs = math.fabs (b)

# printing results
print (f'Use of fabs () function:')
print (f'  a                   = {a}')
print (f'  absolute value of a = {a_abs}')
print (f'  b                   = {b}')
print (f'  absolute value of b = {b_abs}')
print (f'')

# two integers "c" and "d"
c = 30
d = 45

# gcd
gcd_c_d = math.gcd (c, d)

# printing results
print (f'Use of gcd () function:')
print (f'  c                                  = {c}')
print (f'  d                                  = {d}')
print (f'  greatest common divisor of c and d = {gcd_c_d}')
print (f'')

# lcm
lcm_c_d = math.lcm (c, d)

# printing results
print (f'Use of lcm () function:')
print (f'  c                                = {c}')
print (f'  d                                = {d}')
print (f'  least common multiple of c and d = {lcm_c_d}')
print (f'')

# factorial
factorial_5 = math.factorial (5)
factorial_8 = math.factorial (8)

# printing results
print (f'Use of factorial () function:')
print (f'  5! = 1 * 2 * 3 * 4 * 5\n     = {factorial_5}')
print (f'  8! = 1 * 2 * 3 * 4 * 5 * 6 * 7 * 8\n     = {factorial_8}')
print (f'')

# perm
p_5_3 = math.perm (5, 3)
p_8_4 = math.perm (8, 4)

fac_2 = math.factorial (2)
fac_4 = math.factorial (4)
fac_5 = math.factorial (5)
fac_8 = math.factorial (8)

# printing results
print (f'Use of perm () function:')
print (f'  P (5, 3) = (5!) / (2!)')
print (f'           = {fac_5} / {fac_2}')
print (f'           = {p_5_3}')
print (f'  P (8, 4) = (8!) / (4!)')
print (f'           = {fac_8} / {fac_4}')
print (f'           = {p_8_4}')
print (f'')

# comb
c_5_3 = math.comb (5, 3)
c_8_4 = math.comb (8, 4)

fac_2 = math.factorial (2)
fac_3 = math.factorial (3)
fac_4 = math.factorial (4)
fac_5 = math.factorial (5)
fac_8 = math.factorial (8)

# printing results
print (f'Use of comb () function:')
print (f'  C (5, 3) = (5!) / (3! * 2!)')
print (f'           = {fac_5} / ({fac_3} * {fac_2})')
print (f'           = {c_5_3}')
print (f'  C (8, 4) = (8!) / (4! * 4!)')
print (f'           = {fac_8} / ({fac_4} * {fac_4})')
print (f'           = {c_8_4}')
print (f'')
