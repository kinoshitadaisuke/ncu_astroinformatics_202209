#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/12 01:43:47 (CST) daisuke>
#

# importing gzip module
import gzip

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing rebound module
import rebound

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# MPC's orbital elements file
file_mpcorb = 'MPCORB.DAT.gz'

# simulation file to be generated
file_sim = 'iss.bin'

majorbody = {
    'Sun':     '10',
    'Mercury': '1',
    'Venus':   '2',
    'Earth':   '3',
    'Mars':    '4',
    'Jupiter': '5',
    'Saturn':  '6',
    'Uranus':  '7',
    'Neptune': '8',
    'Pluto':   '9',
}

# number of asteroids to process
n_asteroids = 3000

# epoch of orbital elements
# K232P => 2023-Feb-25
# if the epoch is not K232P, then change following line
t_epoch = '2023-02-25 00:00'

# construction of a simulation
sim = rebound.Simulation ()

# adding major bodies
for name in majorbody.keys ():
    sim.add (majorbody[name], date=t_epoch)

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

# processing each asteroid orbit
for number in sorted (dic_elements.keys ()):
    # adding an asteroid
    sim.add (m=0.0, \
             a=dic_elements[number]['a'], \
             e=dic_elements[number]['e'], \
             inc=dic_elements[number]['i'], \
             omega=dic_elements[number]['peri'], \
             Omega=dic_elements[number]['node'], \
             M=dic_elements[number]['M'], \
             date=t_epoch)

# printing simulation object
print (sim)

# saving simulation to a file
sim.save (file_sim)
