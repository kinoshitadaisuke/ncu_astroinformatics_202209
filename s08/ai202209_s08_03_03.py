#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 21:45:42 (CST) daisuke>
#

# importing astroplan module
import astroplan

# getting coordinate of a fixed target
m31 = astroplan.FixedTarget.from_name ('Andromeda Galaxy')

# printing coordinate
print (f'{m31}')
