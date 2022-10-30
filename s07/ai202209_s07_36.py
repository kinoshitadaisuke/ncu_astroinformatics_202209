#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 10:56:43 (CST) daisuke>
#

# importing astropy module
import astropy.table

# VOTable file
file_vot = 'exoplanet.vot'

# reading VOTable file and making an Astropy table
table_exoplanet = astropy.table.Table.read (file_vot)

# printing information of planet discovered by direct imaging in 2020
mask = (table_exoplanet["detection_type"] == "Imaging") \
    & (table_exoplanet["discovered"] == 2020)
print (table_exoplanet[mask]["name", "mass", "semi_major_axis", \
                             "orbital_period", "detection_type", \
                             "discovered"])
