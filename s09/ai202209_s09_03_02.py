#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/14 00:17:42 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.constants
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'hd61005_spec.data'

# output file name
file_output = 'ai202209_s09_03_02.png'

# speed of light
c = scipy.constants.c

# Planck constant
h = scipy.constants.h

# Boltzmann constant
k = scipy.constants.k

# making empty numpy arrays
data_wl        = numpy.array ([])
data_flux      = numpy.array ([])
data_flux_err  = numpy.array ([])
data_wl1       = numpy.array ([])
data_flux1     = numpy.array ([])
data_flux_err1 = numpy.array ([])
data_wl2       = numpy.array ([])
data_flux2     = numpy.array ([])
data_flux_err2 = numpy.array ([])

# opening data file
with open (file_input, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the word '+or-' is found, then we process the line
        if ('+or-' in line):
            # splitting data
            data = line.split ('+or-')
            # wavelength and flux
            (wl_str, flux_str) = data[0].split ()
            # error of flux
            flux_error_str = data[1].split ()[0]
            # conversion from string into float
            wl         = float (wl_str)
            flux       = float (flux_str)
            flux_error = float (flux_error_str)
            # appending data into numpy arrays
            data_wl       = numpy.append (data_wl, wl)
            data_flux     = numpy.append (data_flux, flux)
            data_flux_err = numpy.append (data_flux_err, flux_error)
            if (wl < 20.0):
                data_wl1       = numpy.append (data_wl1, wl)
                data_flux1     = numpy.append (data_flux1, flux)
                data_flux_err1 = numpy.append (data_flux_err1, flux_error)
            if (wl > 30.0):
                data_wl2       = numpy.append (data_wl2, wl)
                data_flux2     = numpy.append (data_flux2, flux)
                data_flux_err2 = numpy.append (data_flux_err2, flux_error)

# initial values of coefficients of fitted function
T1 = 5000.0
T2 = 100.0
a1 = 10**6
a2 = 10**6
init1 = [T1, a1]
init2 = [T2, a2]

# function
def func (x, T, a):
    x_m = x * 10**-6
    f = c / x_m
    y = a * 2.0 * h * f**3 / c**2 / (numpy.exp (h * f / (k * T) ) - 1.0 )
    return (y)

# least-squares method
popt1, pcov1 = scipy.optimize.curve_fit (func, data_wl1, data_flux1, \
                                         p0=init1, sigma=data_flux_err1)
popt2, pcov2 = scipy.optimize.curve_fit (func, data_wl2, data_flux2, \
                                         p0=init2, sigma=data_flux_err2)

print (f"T1 = {popt1[0]} K")
print (f"T2 = {popt2[0]} K")

# fitted curve
wl_min = -0.4
wl_max = 2.7
n      = 10**4
fitted_x = numpy.logspace (wl_min, wl_max, n)
fitted_y = func (fitted_x, popt1[0], popt1[1]) \
    + func (fitted_x, popt2[0], popt2[1])

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Wavelength [$\mu$m]')
ax.set_ylabel ('Flux [Jy]')

# axes
ax.set_xscale ('log')
ax.set_yscale ('log')

# plotting data
ax.plot (fitted_x, fitted_y, linestyle='-', color='b', linewidth=3, \
         label='Blackbody fitting')
ax.errorbar (data_wl, data_flux, yerr=data_flux_err, \
             linestyle='', color='r', marker='o', markersize=5, \
             ecolor='black', capsize=3, label='HD61005')
ax.legend ()

# saving the plot into a file
fig.savefig (file_output, dpi=225)
