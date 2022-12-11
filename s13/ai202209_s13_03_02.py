#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 20:37:02 (CST) daisuke>
#

# importing numpy module
import numpy

# importing rebound module
import rebound

# name of simulation file
file_sim = 'simple0.bin'

# reading a simulation from a file
sim = rebound.Simulation (file_sim)

# moving to centre of momentum frame
sim.move_to_com ()

# particles in simulation
ps = sim.particles

# parameters for simulation
#  for G=1, one year is equal to 2 pi
#  0.01 time unit = 365.25 / (2 pi) * 0.01 = 0.58 day
year       = 2.0 * numpy.pi
t_interval = 0.01
n_output   = 1000

# settings for orbital integration
sim.integrator = 'ias15'

# orbital integration
print (f"# days from start of simulation, star's (x, y, z), planet's (x, y, z)")
for i in range (n_output):
    # time
    t     = t_interval * i
    t_day = t_interval * i * 365.25 / (2.0 * numpy.pi)
    # orbital integration
    sim.integrate (t)
    # position of star
    star_x = ps[0].x
    star_y = ps[0].y
    star_z = ps[0].z
    # position of planet
    planet_x = ps[1].x
    planet_y = ps[1].y
    planet_z = ps[1].z
    # printing position of star and planet
    print (f"{t_day:12.6f} {star_x:+10.6f} {star_y:+10.6f} {star_z:+10.6f}", \
           f"{planet_x:+10.6f} {planet_y:+10.6f} {planet_z:+10.6f}")
