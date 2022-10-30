#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 09:25:08 (CST) daisuke>
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

# accessing to elements of table
print (f'Name of star for the first row:')
print (f'  stars[0]["Name"]             = {stars[0]["Name"]}')
print (f'  stars["Name"][0]             = {stars["Name"][0]}')
print (f'V-band mag of star for the second row:')
print (f'  stars[1]["V-band mag"]       = {stars[1]["V-band mag"]}')
print (f'  stars["V-band mag"][1]       = {stars["V-band mag"][1]}')
print (f'(B-V) colour of star for the 9th row:')
print (f'  stars[9]["B-V colour index"] = {stars[9]["B-V colour index"]}')
print (f'  stars["B-V colour index"][9] = {stars["B-V colour index"][9]}')
print (f'Parallax of star for the 7th row:')
print (f'  stars[7]["Parallax"]         = {stars[7]["Parallax"]}')
print (f'  stars["Parallax"][7]         = {stars["Parallax"][7]}')
