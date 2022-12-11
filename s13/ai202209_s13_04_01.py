#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 21:35:45 (CST) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# name of simulation file
file_sim = 'simple1.bin'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# moving to centre of momentum frame
sim.move_to_com ()

# particles in simulation
ps = sim.particles

# parameters for simulation
#  for G=1, one year is equal to 2 pi
#  1 time unit = 365.25 / (2 pi) = 58 day
year       = 2.0 * numpy.pi
t_interval = 1.0
n_output   = 1000
dt         = 0.01

# settings for orbital integration
sim.integrator = 'ias15'
sim.dt         = dt

# orbital integration
print (f"# year from start of simulation, star 1 (x, y, z), star 2 (x, y, z)")
for i in range (n_output):
    # time
    t    = t_interval * i
    t_yr = t_interval * i / (2.0 * numpy.pi)
    # orbital integration
    sim.integrate (t)
    # position of star 1
    star1_x = ps[0].x
    star1_y = ps[0].y
    star1_z = ps[0].z
    # position of star 2
    star2_x = ps[1].x
    star2_y = ps[1].y
    star2_z = ps[1].z
    # printing position of star and planet
    print (f"{t_yr:12.6f}", \
           f"{star1_x:+10.6f} {star1_y:+10.6f} {star1_z:+10.6f}", \
           f"{star2_x:+10.6f} {star2_y:+10.6f} {star2_z:+10.6f}")
