#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/06 21:38:40 (CST) daisuke>
#

# importing astroplan module
import astroplan

# getting coordinate of a fixed target
omega_centauri = astroplan.FixedTarget.from_name ('NGC 5139')

# printing coordinate
print (f'{omega_centauri}')
