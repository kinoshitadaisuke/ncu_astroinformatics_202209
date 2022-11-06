#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 21:34:51 (CST) daisuke>
#

# importing astroplan module
import astroplan

# getting coordinate of a fixed target
crab_nebula = astroplan.FixedTarget.from_name ('M1')

# printing coordinate
print (f'{crab_nebula}')
