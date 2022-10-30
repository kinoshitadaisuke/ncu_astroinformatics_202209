#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 10:50:12 (CST) daisuke>
#

# importing astropy module
import astropy.table

# VOTable file
file_vot = 'exoplanet.vot'

# reading VOTable file and making an Astropy table
table_exoplanet = astropy.table.Table.read (file_vot)

# printing information of planet discovered in 1995, 1996, and 1997
mask = (table_exoplanet["discovered"] >= 1995) \
    & (table_exoplanet["discovered"] <= 1997)
print (table_exoplanet[mask]["name", "mass", "semi_major_axis", \
                             "orbital_period", "detection_type", \
                             "discovered"])
