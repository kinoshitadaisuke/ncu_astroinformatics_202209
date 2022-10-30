#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 18:09:14 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.units

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.degree

# coordinate of Sirius
sirius_ra  = '06:45:08.9'
sirius_dec = '-16:42:58'

# making a SkyCoord object
coord = astropy.coordinates.SkyCoord (ra=sirius_ra, dec=sirius_dec, \
                                      unit=(u_ha, u_deg), frame='icrs')

# printing coordinate
print (f'Coordinate of Sirius:')
print (f'  (RA, Dec) = ({sirius_ra}, {sirius_dec})')
print (f'            = ({coord.ra}, {coord.dec})')
print (f'            = ({int (coord.ra.hms.h):02d}', \
       f':{int (coord.ra.hms.m):02d}:{coord.ra.hms.s:06.3f}, ', \
       f'{int (coord.dec.dms.d):02d}:{abs (int (coord.dec.dms.m)):02d}:', \
       f'{abs (coord.dec.dms.s):06.3f})', sep='')
print (f'            = ({coord.to_string ("decimal")} deg)')
print (f'            = ({coord.to_string ("hmsdms")})')
