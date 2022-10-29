#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 05:15:06 (CST) daisuke>
#

# importing astropy module
import astropy.table
import astropy.units

# units
u_ct     = astropy.units.ct
u_sec    = astropy.units.s
u_mag    = astropy.units.mag
u_arcsec = astropy.units.arcsec

# making an empty Astropy table
stars \
    = astropy.table.QTable (names=('HR number', 'Name', 'V-band mag', \
                                   'B-V colour index', 'Parallax', \
                                   'Spectral Type'), \
                            dtype=('i4', 'U32', 'f8', 'f8', 'f8', 'U16'), \
                            units=(None, None, u_mag, None, u_arcsec, None))

# adding rows to table
stars.add_row ( (2491, 'Sirius',         -1.46 * u_mag, +0.00, \
                 0.375 * u_arcsec, 'A1V') )
stars.add_row ( (2326, 'Canopus',        -0.72 * u_mag, +0.15, \
                 0.028 * u_arcsec, 'F0II') )
stars.add_row ( (5340, 'Arcturus',       -0.04 * u_mag, +1.23, \
                 0.090 * u_arcsec, 'K1.5III') )
stars.add_row ( (5459, 'Alpha Centauri', -0.01 * u_mag, +0.71, \
                 0.751 * u_arcsec, 'G2V') )
stars.add_row ( (7001, 'Vega',           +0.03 * u_mag, +0.00, \
                 0.123 * u_arcsec, 'A0V') )
stars.add_row ( (1708, 'Capella',        +0.08 * u_mag, +0.80, \
                 0.073 * u_arcsec, 'G5III') )
stars.add_row ( (1713, 'Rigel',          +0.12 * u_mag, -0.03, \
                 0.013 * u_arcsec, 'B8I') )
stars.add_row ( (2943, 'Procyon',        +0.38 * u_mag, +0.42, \
                 0.288 * u_arcsec, 'F5IV') )
stars.add_row ( ( 472, 'Achernar',       +0.46 * u_mag, -0.16, \
                  0.026 * u_arcsec, 'B3V') )
stars.add_row ( (2061, 'Betelgeuse',     +0.50 * u_mag, +1.85, \
                 0.005 * u_arcsec, 'M2I') )

# printing table
print (stars)

# printing information of table
print (stars.info)
