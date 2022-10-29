#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/29 08:30:01 (CST) daisuke>
#

# importing astropy module
import astropy.table
import astropy.units

# units
u_mag    = astropy.units.Magnitude (1.0)
u_arcsec = astropy.units.arcsec

# making an empty Astropy table
stars = astropy.table.QTable ()

# adding data to table
stars['HR number'] = [2491, 2326, 5340, 5459, 7001, \
                      1708, 1713, 2943, 472, 2061]
stars['Name'] = ['Sirius', 'Canopus', 'Arcturus', 'Alpha Centauri', 'Vega', \
                 'Capella', 'Rigel', 'Procyon', 'Achernar', 'Betelgeuse']
stars['V-band mag'] = [-1.46, -0.72, -0.04, -0.01, 0.03, \
                       0.08, 0.12, 0.38, 0.46, 0.50] * u_mag
stars['(B-V) colour index'] = [0.00, 0.15, 1.23, 0.71, 0.00, \
                               0.80, -0.03, 0.42, -0.16, 1.85]
stars['Parallax'] = [0.375, 0.028, 0.090, 0.751, 0.123, \
                     0.073, 0.013, 0.288, 0.026, 0.005] * u_arcsec
stars['Spectral type'] = ['A1V', 'F0II', 'K1.5III', 'G2V', 'A0V', \
                          'G5III', 'B8I', 'F5IV', 'B3V', 'M2I']

# printing table
print (stars)

# printing information of table
print (stars.info)
