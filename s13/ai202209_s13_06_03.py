#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/12 00:11:23 (CST) daisuke>
#

# importing datetime module
import datetime

# importing numpy module
import numpy

# importing astropy module
import astropy.time
import astropy.units

# importing rebound module
import rebound

# date/time now
now = datetime.datetime.now ()

# units
u_day = astropy.units.day

# simulation file
file_sim = 'trojan.bin'

# output file
file_output = 'trojan.data'

# parameters
year       = 2.0 * numpy.pi
time_epoch = '2023-02-25T00:00:00'
t_interval = 0.1 # 0.1 ==> 365.25/(2.0*pi) * 0.1 = 5.81 days
n_output   = 1000

# major bodies
majorbody = [
    'Sun',
    'Mercury',
    'Venus',
    'Earth',
    'Mars',
    'Jupiter',
    'Saturn',
    'Uranus',
    'Neptune',
    'Pluto',
]

# number of minor bodies
n_minorbody = 3000

# reading simulation from file
sim = rebound.Simulation (file_sim)
sim.integrator = 'mercurius'
sim.dt = +0.01
sim.move_to_com ()

# particles
ps = sim.particles

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    fh.write (f"#\n")
    fh.write (f"# results of orbital integration using rebound\n")
    fh.write (f"#\n")
    fh.write (f"#   start of integration: {now}\n")
    fh.write (f"#\n")
    fh.write (f"#   list of objects:\n")
    for name in majorbody:
        fh.write (f"#     {name}\n")
    fh.write (f"#     and {n_minorbody} minor bodies\n")
    fh.write (f"#\n")
    fh.write (f"#   format of the data:\n")
    fh.write (f"#     JD, date/time, x,y,z,vx,vy,vz of obj1, ")
    fh.write (f"x,y,z,vx,vy,vz of obj2, ...\n")
    fh.write (f"#\n")

    # epoch
    t_epoch = astropy.time.Time (time_epoch, scale='utc', format='isot')

    # orbital integration
    for i in range (n_output):
        # target time
        time = t_interval * i
        # integration
        sim.integrate (time)
        # time after a step of integration
        t_current = t_epoch + 365.25 * sim.t / year * u_day
        jd_current = t_current.jd

        # writing data to file
        fh.write (f"{jd_current:.8f}|{t_current}")
        for j in range ( len (majorbody) + n_minorbody):
            fh.write (f"|{ps[j].x:+.15f},{ps[j].y:+.15f},{ps[j].z:+.15f},")
            fh.write (f"{ps[j].vx:+.15f},{ps[j].vy:+.15f},{ps[j].vz:+.15f}")
        fh.write (f"\n")

        # printing status
        if ( (i + 1) % 100 == 0 ):
            print (f"  status: {i + 1:08d} / {n_output:08d}")
