#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 10:43:44 (CST) daisuke>
#

# importing astropy module
import astropy.table

# VOTable file
file_vot = 'exoplanet.vot'

# reading VOTable file and making an Astropy table
table_exoplanet = astropy.table.Table.read (file_vot)

# printing information of planet "51 Peg b"
for i in range (len (table_exoplanet)):
    if (table_exoplanet[i]["name"] == "51 Peg b"):
        print (table_exoplanet[i]["name", "mass", "semi_major_axis", \
                                  "orbital_period", "detection_type", \
                                  "discovered"])
