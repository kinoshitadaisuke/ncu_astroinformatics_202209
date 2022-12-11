#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 22:17:51 (CST) daisuke>
#

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

# simulation file to be generated
file_sim = 'comets.bin'

# major bodies
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

# minor bodies
minorbody = {
    '1P/Halley':                 'DES=1P; CAP',
    '2P/Encke':                  'DES=2P; CAP',
    '8P/Tuttle':                 'DES=8P; CAP',
    '21P/Giacobini-Zinner':      'DES=21P; CAP',
    '29P/Schwassmann-Wachmann':  'DES=29P; CAP',
    '55P/Tempel-Tuttle':         'DES=55P; CAP',
    '67P/Churyumov-Gerasimenko': 'DES=67P; CAP',
}

# epoch of orbital elements
t_epoch = '2022-12-12 00:00'

# construction of a simulation
sim = rebound.Simulation ()

# adding major bodies
for name in majorbody.keys ():
    sim.add (majorbody[name], date=t_epoch, hash=name)

# adding minor bodies
for name in minorbody.keys ():
    sim.add (minorbody[name], date=t_epoch, hash=name)

# printing simulation
print (sim)
    
# saving simulation to a file
sim.save (file_sim)
