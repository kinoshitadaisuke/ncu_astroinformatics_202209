#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 21:27:46 (CST) daisuke>
#

# importing astroplan module
import astroplan

# getting coordinate of a fixed target
canopus = astroplan.FixedTarget.from_name ('Canopus')

# printing coordinate
print (f'{canopus}')
