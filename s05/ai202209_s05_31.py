#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 13:27:14 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.integrate
import scipy.stats

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.animation

#
# initial conditions
#

# mass of the star (unit: solar mass)
M   = 1.0

# initial position of the planet (unit: astronomical unit)
qx0 = 1.0
qy0 = 0.0

# initial velocity of the planet (unit: astronomical unit per year)
vx0 = 0.0
vy0 = 1.3

# printing initial conditions
print (f'initial conditions for calculation of planetary motion:')
print (f'  qx0 = {qx0:8.3f} [au]')
print (f'  qy0 = {qy0:8.3f} [au]')
print (f'  vx0 = {vx0:8.3f} [au/year]')
print (f'  vx0 = {vy0:8.3f} [au/year]')

#
# other parameters
#

# gravitational constant
GM = 4.0 * numpy.pi**2

# time step in year
dt = 0.01

# end time of simulation in year
time_end = 15.0

# output image file
file_output = 'ai202209_s05_31.mp4'

#
# equation of motion
#
def eqmo (t, y):
    # initialisation of dy
    dy = numpy.zeros_like (y)
    # r^3 (cube of distance between star and planet)
    r_cubed = ( y[0]**2 + y[2]**2 )**1.5
    # Runge-Kutta method
    dy[0] = y[1]
    dy[1] = -GM * y[0] / r_cubed
    dy[2] = y[3]
    dy[3] = -GM * y[2] / r_cubed
    # returning dy
    return dy

# number of time steps of simulation
n_step = int (time_end / dt) + 1

# times to calculate position and velocity of planet
times = numpy.linspace (0.0, time_end, n_step)

# initial values
y_init = (qx0, vx0 * numpy.sqrt (GM), qy0, vy0 * numpy.sqrt (GM))

# orbital integration of planet
solution = scipy.integrate.solve_ivp (eqmo, [0.0, time_end], y_init, \
                                      t_eval=times, dense_output=True, \
                                      rtol=10**-6, atol=10**-9)

# results (positions and velocities of planet)
qx = solution.y[0]
qy = solution.y[2]
vx = solution.y[1]
xy = solution.y[3]

# finding maximum and minimum values for plotting
qx_max = scipy.stats.tmax (qx)
qy_max = scipy.stats.tmax (qy)
qx_min = scipy.stats.tmin (qx)
qy_min = scipy.stats.tmin (qy)
maxmin = sorted ([abs (qx_max), abs (qy_max), abs (qx_min), abs (qy_min)])
x_max  = maxmin[-1] * +1.3
x_min  = maxmin[-1] * -1.3
y_max  = maxmin[-1] * +1.3
y_min  = maxmin[-1] * -1.3

#
# making animation using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# an empty list for animation
list_frame = []

for i in range (n_step):
    # empty list for objects on a plot
    list_obj = []
    
    # axes
    ax.set_title ('Trajectory of Planetary Motion')
    ax.set_xlabel ('X [au]')
    ax.set_ylabel ('Y [au]')
    ax.set_xlim (x_min, x_max)
    ax.set_ylim (y_min, y_max)
    ax.set_aspect ('equal')

    # plotting the position of the star
    star, = ax.plot (0.0, 0.0, linestyle='None', marker='o', \
                     markersize=10.0, color='yellow', label='star')
    list_obj.append (star)

    # plotting the trajectory of orbital motion of planet
    orb, = ax.plot (qx, qy, linestyle='-', linewidth=1.0, color='cyan', \
                    label='orbit of planet')
    list_obj.append (orb)
    planet, = ax.plot (qx[i], qy[i], linestyle='None', marker='o', \
                       markersize=5.0, color='blue', label='planet')
    list_obj.append (planet)

    # texts
    text_time = "Time: %8.2f year" % (i * dt)
    text_initial = "Initial conditions"
    text_mass    = "mass of star = %5.2f solar mass" % (M)
    text_iq      = "(qx0, qy0) = (%4.2f au, %4.2f au)" % (qx0, qy0)
    text_iv      = "(vx0, vy0) = (%4.2f au/yr, %4.2f au/yr)" % (vx0, vy0)
    text_1 = ax.text (0.03, 0.95, text_time, transform=ax.transAxes)
    list_obj.append (text_1)
    text_2 = ax.text (0.03, 0.18, text_initial, transform=ax.transAxes)
    list_obj.append (text_2)
    text_3 = ax.text (0.05, 0.13, text_mass, transform=ax.transAxes)
    list_obj.append (text_3)
    text_4 = ax.text (0.05, 0.08, text_iq, transform=ax.transAxes)
    list_obj.append (text_4)
    text_5 = ax.text (0.05, 0.03, text_iv, transform=ax.transAxes)
    list_obj.append (text_5)

    # appending plot to animation
    list_frame.append (list_obj)

# making animation
ani = matplotlib.animation.ArtistAnimation (fig, list_frame, interval=50)

# saving file
ani.save (file_output, dpi=225)
