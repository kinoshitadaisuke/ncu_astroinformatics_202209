#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/12 01:36:55 (CST) daisuke>
#

# importing gzip module
import gzip

# importing numpy module
import numpy

# MPC's orbital elements file
file_mpcorb = 'MPCORB.DAT.gz'

# number of asteroids to process
n_asteroids = 3000

# dictionary to store orbital elements
dic_elements = {}

# opening file
with gzip.open (file_mpcorb, 'rb') as fh:
    # flag
    data_line = 'NO'
    # reading file
    for line in fh:
        # decoding byte data
        line = line.decode ('utf-8')
        if (data_line == 'YES'):
            # number (or provisional designation)
            number = line[0:7]
            # epoch
            epoch = line[20:25]
            # mean anomaly
            M = float (line[26:35])
            M_rad = numpy.deg2rad (M)
            # argument of perihelion
            peri = float (line[37:46])
            peri_rad = numpy.deg2rad (peri)
            # longitude of ascending node
            node = float (line[48:57])
            node_rad = numpy.deg2rad (node)
            # inclination
            i = float (line[59:68])
            i_rad = numpy.deg2rad (i)
            # eccentricity
            e = float (line[70:79])
            # semimajor axis
            a = float (line[92:103])

            # adding data to the dictionary
            dic_elements[number] = {}
            dic_elements[number]['a'] = a
            dic_elements[number]['e'] = e
            dic_elements[number]['i'] = i_rad
            dic_elements[number]['peri'] = peri_rad
            dic_elements[number]['node'] = node_rad
            dic_elements[number]['M'] = M_rad

            # when finish reading expected number of asteroid data, then break
            if (int (number) == n_asteroids):
                break
        # if the line starts with '----------'
        if (line[:10] == '----------'):
            # set the flag to 'YES'
            data_line = 'YES'
            continue
            
for number in sorted (dic_elements.keys ()):
    print (f"{number:8s}", \
           f"{dic_elements[number]['a']:10.8f}", \
           f"{dic_elements[number]['e']:10.8f}", \
           f"{dic_elements[number]['i']:10.8f}", \
           f"{dic_elements[number]['peri']:10.8f}", \
           f"{dic_elements[number]['node']:10.8f}", \
           f"{dic_elements[number]['M']:10.8f}")
