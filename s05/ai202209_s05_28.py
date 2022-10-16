#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/17 00:25:08 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy
import scipy.integrate

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output image file
file_output = 'ai202209_s05_28.png'

# coefficient
k = 0.1

# initial condition
y_0 = 100.0

# equation to solve
def dydx (t, y):
    # dy/dx = -ky
    dy = -k * y
    # returning value
    return dy

# x values
output_x = numpy.linspace (0.0, 50.0, 5001)

# solving differential equation using Runge-Kutta method
solution = scipy.integrate.solve_ivp (dydx, [0.0, 50.0], [y_0], \
                                      method='RK45', dense_output=True, \
                                      t_eval=output_x, \
                                      rtol=10**-6, atol=10**-9)

# x and y
numerical_x = solution.t
numerical_y = solution.y[0]

# printing solution
print (f'{solution}')

# analytical solution
analytical_x = output_x
analytical_y = y_0 * numpy.exp (-k * analytical_x)
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_title (r'$dy/dx = -ky$')
ax.set_xlabel (r'$x$')
ax.set_ylabel (r'$y$')

# plotting data
ax.plot (numerical_x, numerical_y, linestyle='--', linewidth=3.0, \
         color='blue', label='numerical solution', zorder=0.2)
ax.plot (analytical_x, analytical_y, linestyle='-', linewidth=5.0, \
         color='red', label='analytical solution', zorder=0.1)
ax.legend ()

# writing figure to file
fig.savefig (file_output, dpi=225)
