#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/16 16:09:09 (CST) daisuke>
#

# importing math module
import math

#
# some mathematical functions
#

# pow () function
a = math.pow (3, 4)

# printing result
print (f'3^4 = 3 * 3 * 3 * 3 = {a}')
print (f'')

# sqrt () function
b = math.sqrt (3)

# printing result
print (f'sqrt (3) = {b}')
print (f'')

# log () function
c = math.log (100)

# printing result
print (f'log (100) = {c}')
print (f'')

# log () function
d = math.log10 (100)

# printing result
print (f'log10 (100) = {d}')
print (f'')

# conversion from degree into radian
e_deg = 180.0
e_rad = math.radians (e_deg)

# printing result
print (f'{e_deg} deg = {e_rad} rad')
print (f'')

# conversion from radian into degree
f_rad = math.pi / 2.0
f_deg = math.degrees (f_rad)

# printing result
print (f'{f_rad} rad = {f_deg} deg')
print (f'')

# sin (), cos (), and tan ()
g_deg = 60.0
g_rad = math.radians (g_deg)
sin_g = math.sin (g_rad)
cos_g = math.cos (g_rad)
tan_g = math.tan (g_rad)

# printing result
print (f'{g_deg} deg       = {g_rad} rad')
print (f'sin ({g_deg} deg) = {sin_g}')
print (f'cos ({g_deg} deg) = {cos_g}')
print (f'tan ({g_deg} deg) = {tan_g}')
print (f'')

# distance between two points
coord_0  = (0.0, 1.0)
coord_1  = (3.0, 2.0)
dist_0_1 = math.dist (coord_0, coord_1)
coord_2  = (0.0, 0.0, 0.0)
coord_3  = (1.0, 1.0, 1.0)
dist_2_3 = math.dist (coord_2, coord_3)

# printing result
print (f'coord_0 = {coord_0}')
print (f'coord_1 = {coord_1}')
print (f'distance between coord_0 and coord_1 = {dist_0_1}')
print (f'coord_2 = {coord_2}')
print (f'coord_3 = {coord_3}')
print (f'distance between coord_2 and coord_3 = {dist_2_3}')
print (f'')
