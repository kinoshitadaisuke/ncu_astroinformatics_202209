#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/04 15:53:02 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates

# getting site names
site_names = astropy.coordinates.EarthLocation.get_site_names ()

# printing site names
print (f'Built-in site names of Astropy:')
for site_name in site_names:
    print (f'  {site_name}')
