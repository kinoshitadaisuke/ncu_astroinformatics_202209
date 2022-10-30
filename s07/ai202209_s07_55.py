#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 20:54:29 (CST) daisuke>
#

# importing astropy module
import astropy.coordinates
import astropy.units

# unit
u_deg = astropy.units.degree

# Galactic centre
centre_l = 0.0 * u_deg
centre_b = 0.0 * u_deg

# Galactic anti-centre
anti_l = 180.0 * u_deg
anti_b = 0.0 * u_deg

# north Galactic pole
npole_l = 0.0 * u_deg
npole_b = +90.0 * u_deg

# south Galactic pole
spole_l = 0.0 * u_deg
spole_b = -90.0 * u_deg

# making SkyCoord objects
centre = astropy.coordinates.SkyCoord (l=centre_l, b=centre_b, \
                                       frame='galactic')
anti   = astropy.coordinates.SkyCoord (l=anti_l, b=anti_b, \
                                       frame='galactic')
npole  = astropy.coordinates.SkyCoord (l=npole_l, b=npole_b, \
                                       frame='galactic')
spole  = astropy.coordinates.SkyCoord (l=spole_l, b=spole_b, \
                                       frame='galactic')

# conversion between galactic system and equatorial system
centre_radec = centre.transform_to ('icrs')
(centre_ra, centre_dec) = centre_radec.to_string ('hmsdms').split ()
anti_radec = anti.transform_to ('icrs')
(anti_ra, anti_dec) = anti_radec.to_string ('hmsdms').split ()
npole_radec = npole.transform_to ('icrs')
(npole_ra, npole_dec) = npole_radec.to_string ('hmsdms').split ()
spole_radec = spole.transform_to ('icrs')
(spole_ra, spole_dec) = spole_radec.to_string ('hmsdms').split ()

# printing coordinate of Betelgeuse
print (f'Coordinate of Galactic centre:')
print (f'  (l, b)    = ({centre_l}, {centre_b})')
print (f'  (RA, Dec) = ({centre_ra}, {centre_dec})')
print (f'Coordinate of Galactic anti-centre:')
print (f'  (l, b)    = ({anti_l}, {anti_b})')
print (f'  (RA, Dec) = ({anti_ra}, {anti_dec})')
print (f'Coordinate of north Galactic pole:')
print (f'  (l, b)    = ({npole_l}, {npole_b})')
print (f'  (RA, Dec) = ({npole_ra}, {npole_dec})')
print (f'Coordinate of south Galactic pole:')
print (f'  (l, b)    = ({spole_l}, {spole_b})')
print (f'  (RA, Dec) = ({spole_ra}, {spole_dec})')
