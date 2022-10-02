#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/02 23:05:00 (CST) daisuke>
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

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.animation
import matplotlib.backends.backend_agg
import matplotlib.figure

# output file name prefix
file_prefix = 'solsys_3d_struct3'

# output file name extension
file_ext    = 'png'

# units
u_au = astropy.units.au
u_hr = astropy.units.hour

# number of steps to calculate
n_steps = 5000

# number of asteroids to plot
n_asteroids = 5000

# step size in hr
step_hr  = 12
step_str = f'{step_hr}h'
step     = step_hr * u_hr

# an empty list for storing asteroids positions
list_asteroids = []

# date/time to start the simulation
t_start_str = f'2022-07-01T00:00:00.000'
    
# time to start the simulation in astropy.time object
t_start = astropy.time.Time (t_start_str, format='isot', scale='utc')

# time to stop the simulation in astropy.time object
t_stop  = t_start + step * n_steps

# an empty list for storing major planets positions
list_major = []

# major body names (Sun, Mercury, Venus, Earth, Mars, Jupiter)
list_names = ['10', '199', '299', '399', '499', '599']

# getting positions of the Sun, Mercury, Venus, Earth, Mars, and Jupiter
# from JPL/Horizons
print (f'Now, getting positions of the Sun and planets...')
for i in list_names:
    print (i)
    query = astroquery.jplhorizons.Horizons (id_type=None, id=f'{i}', \
                                             location='@0', \
                                             epochs={'start': t_start.iso, \
                                                     'stop': t_stop.iso, \
                                                     'step': step_str})
    vec = query.vectors ()
    print (vec)
    x = vec['x']
    y = vec['y']
    z = vec['z']
    list_major.append ( [x, y, z] )
print (f'Finished getting positions of the Sun and planets!')

# getting asteroids positions from JPL/Horizons
print (f'Now, getting asteroids positions...')
for i in range (1, n_asteroids + 1):
    if (i % 10 == 0):
        print (f'  now, getting positions of asteroid ({i})...')
    ast_query = astroquery.jplhorizons.Horizons (id_type='smallbody', \
                                                 id=f'{i}', \
                                                 location='@0', \
                                                 epochs={'start': t_start.iso, \
                                                         'stop': t_stop.iso, \
                                                         'step': step_str})
    ast_vec = ast_query.vectors ()
    x = ast_vec['x']
    y = ast_vec['y']
    z = ast_vec['z']
    list_asteroids.append ( [x, y, z] )
print (f'Finished getting asteroids positions...')

# making a fig object using object-oriented interface
fig = matplotlib.figure.Figure ()
fig.subplots_adjust (left=0.0, right=1.0, bottom=0.0, top=1.0)

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111, projection='3d')

# an empty list of frames for animation
list_frame = []

# definition of a function for making a sphere
def make_sphere (x_c, y_c, z_c, radius, colour):
    u = numpy.linspace (0, 2 * numpy.pi, 1000)
    v = numpy.linspace (0, numpy.pi, 1000)
    x = radius * numpy.outer (numpy.cos(u), numpy.sin(v)) + x_c
    y = radius * numpy.outer (numpy.sin(u), numpy.sin(v)) + y_c
    z = radius * numpy.outer (numpy.ones(numpy.size(u)), numpy.cos(v)) + z_c
    # plotting the surface
    sphere = ax.plot_surface (x, y, z, color=colour, antialiased=False, \
                               shade=True, rcount=100, ccount=100)
    return (sphere)

# initial value of 'elev' angle
el0 = 90.0

# initial value of 'azim' angle
az0 = 0.0

for i in range (n_steps):
    # clearing previous axes
    ax.cla ()
    
    # camera viewing angle
    if (i < 200):
        el = el0
        az = az0
    elif ( (i >= 200) and (i < 1400) ):
        el = el0 - (i - 200) * 0.1
        az = az0
    elif ( (i >= 1400) and (i < 1600) ):
        el = -30.0
        az = az0
    elif ( (i >= 1600) and (i < 1900) ):
        el = -30 + (i - 1600) * 0.1
        az = az0
    elif ( (i >= 1900) and (i < 2100) ):
        el = 0.0
        az = az0
    elif ( (i >= 2100) and (i < 2700) ):
        el = (i - 2100) * 0.1
        az = az0
    elif ( (i >= 2700) and (i < 3600) ):
        el = 60.0
        az = 360.0 - (i - 2700) * 0.1
    elif ( (i >= 3600) and (i < 3800) ):
        el = 60.0
        az = 270.0
    elif ( (i >= 3800) and (i < 4700) ):
        el = 60.0
        az = 270.0 - (i - 3800) * 0.1
    else:
        el = 60.0
        az = 180.0
    
    # time t
    t = t_start + i * 12.0 * u_hr

    # printing positions of the Sun, planets, and asteroids
    if (i % 10 == 0):
        print (f'Now, making a plot for {t}...')

    # settings for plot
    ax.set_xlim (-6.0, +6.0)
    ax.set_ylim (-6.0, +6.0)
    ax.set_zlim (-2.0, +2.0)
    ax.set_box_aspect ( (6.0, 6.0, 2.0) )

    # viewing angles of camera
    ax.view_init (elev=el, azim=az)

    # using black background colour
    fig.set_facecolor ('black')
    ax.set_facecolor ('black')
    ax.grid (False)
    ax.w_xaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.w_yaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))
    ax.w_zaxis.set_pane_color ((0.0, 0.0, 0.0, 0.0))

    # plotting the Sun
    sun = make_sphere (list_major[0][0][i], \
                       list_major[0][1][i], \
                       list_major[0][2][i], \
                       0.25, 'yellow')

    # plotting Mercury
    mercury = make_sphere (list_major[1][0][i], \
                           list_major[1][1][i], \
                           list_major[1][2][i], \
                           0.05, 'cyan')
    
    # plotting Venus
    venus = make_sphere (list_major[2][0][i], \
                         list_major[2][1][i], \
                         list_major[2][2][i], \
                         0.15, 'gold')

    # plotting Earth
    earth = make_sphere (list_major[3][0][i], \
                         list_major[3][1][i], \
                         list_major[3][2][i], \
                         0.15, 'blue')

    # plotting Mars
    mars = make_sphere (list_major[4][0][i], \
                        list_major[4][1][i], \
                        list_major[4][2][i], \
                        0.15, 'red')

    # plotting Jupiter
    jupiter = make_sphere (list_major[5][0][i], \
                           list_major[5][1][i], \
                           list_major[5][2][i], \
                           0.15, 'bisque')

    # plotting asteroids
    for j in range (0, n_asteroids):
        asteroid = ax.scatter (list_asteroids[j][0][i], \
                               list_asteroids[j][1][i], \
                               list_asteroids[j][2][i], \
                               s=0.1, \
                               color='saddlebrown')
    
    # title
    title = ax.text2D (0.5, 0.95, f'Inner Solar System', \
                       color='white', \
                       horizontalalignment='center', \
                       transform=ax.transAxes)

    # plotting the time
    time = ax.text2D (0.5, 0.05, f'Date/Time: {t} (UTC)', \
                      color='white', \
                      horizontalalignment='center', \
                      transform=ax.transAxes)

    # image file
    file_image = f'{file_prefix}_{i:06d}.{file_ext}'
    fig.savefig (file_image, dpi=255)
