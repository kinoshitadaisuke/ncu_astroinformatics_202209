#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 20:37:26 (CST) daisuke>
#

# importing sys module
import sys

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize
import scipy.stats

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'ai202209_s05_48.data'

# output file name
file_output = 'ai202209_s05_50.png'

# making empty numpy arrays
data_x   = numpy.array ([])
data_y   = numpy.array ([])
data_err = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # splitting line into "x", "y", and "err"
        (x_str, y_str, err_str) = line.split ()
        # converting string into float
        try:
            x = float (x_str)
        except:
            print (f'cannot convert "{x_str}" into float.')
            print (f'something is wrong.')
            print (f'exiting...')
            sys.exit (1)
        try:
            y = float (y_str)
        except:
            print (f'cannot convert "{y_str}" into float.')
            print (f'something is wrong.')
            print (f'exiting...')
            sys.exit (1)
        try:
            err = float (err_str)
        except:
            print (f'cannot convert "{err_str}" into float.')
            print (f'something is wrong.')
            print (f'exiting...')
            sys.exit (1)
        # appending data into numpy arrays
        data_x   = numpy.append (data_x, x)
        data_y   = numpy.append (data_y, y)
        data_err = numpy.append (data_err, err)

# printing data
for i in range (len (data_x)):
    print (f'(x_{i:02d}, y_{i:02d}, err_{i:02d})', \
           f'= ({data_x[i]:8.3f}, {data_y[i]:8.3f}, {data_err[i]:8.3f})')

# a function for curve
def curve (x, a, b, c):
    # line
    y = a * (x - b)**2 + c
    # returning y
    return y

# initial guess of coefficients
param0 = [1.0, 1.0, 1.0]

# fitting
popt, pcov = scipy.optimize.curve_fit (curve, data_x, data_y, p0=param0)

# result of fitting
print (f'popt:\n{popt}')
print (f'pcov:\n{pcov}')

# fitted a and b
a_fitted, b_fitted, c_fitted = popt

# degree of freedom
dof = len (data_x) - len (popt)
print (f'dof = {dof}')

# reduced chi-squared
residual     = data_y - curve (data_x, a_fitted, b_fitted, c_fitted)
reduced_chi2 = (residual**2).sum () / dof
print (f'reduced chi-squared = {reduced_chi2}')

# fitted a and b
a_err, b_err, c_err = numpy.sqrt ( numpy.diagonal (pcov) )
print (f'a = {a_fitted:8.3f} +/- {a_err:8.3f} ({a_err/a_fitted*100.0:8.3f}%)')
print (f'b = {b_fitted:8.3f} +/- {b_err:8.3f} ({b_err/b_fitted*100.0:8.3f}%)')
print (f'c = {c_fitted:8.3f} +/- {c_err:8.3f} ({c_err/c_fitted*100.0:8.3f}%)')

# range of data
x_min = scipy.stats.tmin (data_x)
x_max = scipy.stats.tmax (data_x)

# fitted curve
fitted_x = numpy.linspace (x_min, x_max, 1000)
fitted_y = curve (fitted_x, a_fitted, b_fitted, c_fitted)

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('X [arbitrary unit]')
ax.set_ylabel ('Y [arbitrary unit]')

# plotting data
ax.errorbar (data_x, data_y, yerr=data_err, \
             linestyle='None', marker='o', markersize=5.0, color='blue', \
             elinewidth=2.0, ecolor='black', capsize=5.0, \
             label='synthetic data for least-squares method', \
             zorder=0.2)
ax.plot (fitted_x, fitted_y, linestyle=':', linewidth=3.0, color='red', \
         label='fitted curve by least-squares method', zorder=0.1)

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225)
