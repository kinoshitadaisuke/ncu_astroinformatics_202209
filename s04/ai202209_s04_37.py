#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 21:32:05 (CST) daisuke>
#

# importing sys module
import sys

# importing numpy module
import numpy

# importing astropy module
import astropy
import astropy.coordinates
import astropy.time
import astropy.units

# importing matplotlib module
import matplotlib.animation
import matplotlib.backends.backend_agg
import matplotlib.figure

# output movie file
file_output = 'ai202209_s04_37.mp4'

# units
u_au = astropy.units.au
u_hr = astropy.units.hour

# setting for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('jpl')

# date/time
t0_str = f'2022-10-01T00:00:00'
    
# time to start the simulation
t0 = astropy.time.Time (t0_str, format='isot', scale='utc')

# number of steps to calculate
n_steps = 600

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# an empty list of frames for animation
list_frame = []

for i in range (n_steps):
    # initialisation of object list
    list_obj = []
    
    # time t
    t = t0 + i * 6.0 * u_hr

    # getting positions of Sun, Earth, and Moon
    sun     = astropy.coordinates.get_body_barycentric ('sun', t)
    mercury = astropy.coordinates.get_body_barycentric ('mercury', t)
    venus   = astropy.coordinates.get_body_barycentric ('venus', t)
    earth   = astropy.coordinates.get_body_barycentric ('earth', t)
    mars    = astropy.coordinates.get_body_barycentric ('mars', t)

    # printing positions of the Sun and planets
    if (i % 100 == 0):
        print (f'Positions of the Sun and the planets at t = {t}')
        print (f'  Sun:')
        print (f'    X = {sun.x} = {sun.x.to (u_au)}')
        print (f'    Y = {sun.y} = {sun.y.to (u_au)}')
        print (f'    Z = {sun.z} = {sun.z.to (u_au)}')
        print (f'  Mercury:')
        print (f'    X = {mercury.x} = {mercury.x.to (u_au)}')
        print (f'    Y = {mercury.y} = {mercury.y.to (u_au)}')
        print (f'    Z = {mercury.z} = {mercury.z.to (u_au)}')
        print (f'  Venus:')
        print (f'    X = {venus.x} = {venus.x.to (u_au)}')
        print (f'    Y = {venus.y} = {venus.y.to (u_au)}')
        print (f'    Z = {venus.z} = {venus.z.to (u_au)}')
        print (f'  Earth:')
        print (f'    X = {earth.x} = {earth.x.to (u_au)}')
        print (f'    Y = {earth.y} = {earth.y.to (u_au)}')
        print (f'    Z = {earth.z} = {earth.z.to (u_au)}')
        print (f'  Mars:')
        print (f'    X = {mars.x} = {mars.x.to (u_au)}')
        print (f'    Y = {mars.y} = {mars.y.to (u_au)}')
        print (f'    Z = {mars.z} = {mars.z.to (u_au)}')

    # settings for plot
    ax.set_aspect ('equal')
    ax.set_xlim (-2.0, +2.0)
    ax.set_ylim (-2.0, +2.0)
    ax.set_xlabel ("X [au]")
    ax.set_ylabel ("Y [au]")
    ax.set_title ("Positions of the Sun and planets")

    # plotting grids
    grid_x = numpy.linspace (-2.0, +2.0, 9)
    grid_y = numpy.linspace (-2.0, +2.0, 9)
    for x in grid_x:
        grid, = ax.plot ([x, x], [-100, +100], \
                         linestyle='-', color='gray', alpha=0.3)
        list_obj.append (grid)
    for y in grid_y:
        grid, = ax.plot ([-100, +100], [y, y], \
                         linestyle='-', color='gray', alpha=0.3)
        list_obj.append (grid)

    # plotting the Sun
    sun_p, = ax.plot (sun.x.to (u_au) / u_au, sun.y.to (u_au) / u_au, \
                      marker='o', markersize=25, color='yellow', label='Sun')
    sun_t = ax.text (sun.x.to (u_au) / u_au + 0.1, \
                     sun.y.to (u_au) / u_au - 0.3, \
                     f'Sun')
    list_obj.append (sun_p)
    list_obj.append (sun_t)

    # plotting Mercury
    mercury_p, = ax.plot (mercury.x.to (u_au) / u_au, \
                          mercury.y.to (u_au) / u_au, \
                          marker='o', markersize=5, color='orange', \
                          label='Mercury')
    mercury_t = ax.text (mercury.x.to (u_au) / u_au + 0.1, \
                          mercury.y.to (u_au) / u_au - 0.3, \
                          f'Mercury')
    list_obj.append (mercury_p)
    list_obj.append (mercury_t)

    # plotting Venus
    venus_p, = ax.plot (venus.x.to (u_au) / u_au, venus.y.to (u_au) / u_au, \
                        marker='o', markersize=15, color='green', label='Venus')
    venus_t = ax.text (venus.x.to (u_au) / u_au + 0.1, \
                        venus.y.to (u_au) / u_au - 0.3, \
                        f'Venus')
    list_obj.append (venus_p)
    list_obj.append (venus_t)
    
    # plotting Earth
    earth_p, = ax.plot (earth.x.to (u_au) / u_au, earth.y.to (u_au) / u_au, \
                        marker='o', markersize=15, color='blue', label='Earth')
    earth_t = ax.text (earth.x.to (u_au) / u_au + 0.1, \
                        earth.y.to (u_au) / u_au - 0.3, \
                        f'Earth')
    list_obj.append (earth_p)
    list_obj.append (earth_t)

    # plotting Mars
    mars_p, = ax.plot (mars.x.to (u_au) / u_au, mars.y.to (u_au) / u_au, \
                       marker='o', markersize=10, color='red', label='Mars')
    mars_t = ax.text (mars.x.to (u_au) / u_au + 0.1, \
                       mars.y.to (u_au) / u_au - 0.3, \
                       f'Mars')
    list_obj.append (mars_p)
    list_obj.append (mars_t)

    # plotting the time
    time_t = ax.text (-1.9, -1.9, f'Date/Time: {t} (UTC)')
    list_obj.append (time_t)

    # appending frame
    list_frame.append (list_obj)

# making animation
anim = matplotlib.animation.ArtistAnimation (fig, list_frame, interval=50)

# saving file
anim.save (file_output, dpi=225)
