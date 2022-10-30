#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/29 08:16:05 (CST) daisuke>
#

# importing astropy module
import astropy.table
import astropy.units

# units
u_mag    = astropy.units.Magnitude (1.0)
u_arcsec = astropy.units.arcsec

# data for making Astropy Table
hr       = [2491, 2326, 5340, 5459, 7001, \
            1708, 1713, 2943, 472, 2061]
name     = ['Sirius', 'Canopus', 'Arcturus', 'Alpha Centauri', 'Vega', \
            'Capella', 'Rigel', 'Procyon', 'Achernar', 'Betelgeuse']
vmag     = [-1.46, -0.72, -0.04, -0.01, 0.03, \
            0.08, 0.12, 0.38, 0.46, 0.50] * u_mag
bv       = [0.00, 0.15, 1.23, 0.71, 0.00, \
            0.80, -0.03, 0.42, -0.16, 1.85]
parallax = [0.375, 0.028, 0.090, 0.751, 0.123, \
            0.073, 0.013, 0.288, 0.026, 0.005] * u_arcsec
sptype   = ['A1V', 'F0II', 'K1.5III', 'G2V', 'A0V', \
            'G5III', 'B8I', 'F5IV', 'B3V', 'M2I']

# making Astropy Table
stars = astropy.table.QTable ([hr, name, vmag, bv, parallax, sptype], \
                              names=('HR number', 'Name', 'V-band mag', \
                                     'B-V colour index', 'Parallax', \
                                     'Spectral Type'), \
                              meta={'hr': 'HR number of star', \
                                    'name': 'name of star', \
                                    'vmag': 'V-band apparent magnitude', \
                                    'bv': '(B-V) colour index', \
                                    'parallax': 'parallax in arcsec', \
                                    'sptype': 'spectral type'} )

# printing metadata of table
for key in stars.meta.keys ():
    print (f'{key:8s} : {stars.meta[key]}')
