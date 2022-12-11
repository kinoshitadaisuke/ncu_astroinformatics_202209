#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 20:01:30 (CST) daisuke>
#

# importing rebound module
import rebound

# name of simulation file
file_sim = 'simple0.bin'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# printing simulation object
print (sim)
