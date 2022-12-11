#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 21:25:34 (CST) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'simple1.bin'

# constructing a simulation object
sim = rebound.Simulation ()

# adding 2 solar mass star
sim.add (m=2.0)

# adding 1 solar mass star of a=20 au and e=0.6
sim.add (m=1.0, a=20.0, e=0.6)

# printing simulation object
print (sim)

# saving simulation into a file
sim.save (file_sim)
