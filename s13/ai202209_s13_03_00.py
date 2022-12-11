#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 19:53:02 (CST) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'simple0.bin'

# constructing a simulation object
sim = rebound.Simulation ()

# adding a solar mass star
sim.add (m=1.0)

# adding a planet mass object of a=1 and e=0.3
sim.add (m=10**-3, a=1.0, e=0.3)

# printing simulation object
print (sim)

# saving simulation into a file
sim.save (file_sim)
