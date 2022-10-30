#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 18:04:55 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates

# coordinate of Sirius
sirius_ra  = '06h45m08.9s'
sirius_dec = '-16d42m58s'

# making a SkyCoord object
coord = astropy.coordinates.SkyCoord (ra=sirius_ra, dec=sirius_dec, \
                                      frame='icrs')

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
