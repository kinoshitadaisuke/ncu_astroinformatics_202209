#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 22:04:47 (CST) daisuke>
#

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize
import scipy.stats

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'solsys.data'

# output file name
file_output = 'ai202209_s05_57.png'

# numpy arrays for storing data
data_a = numpy.array ([])
data_p = numpy.array ([])

# 1 au in km
au = 1.49597871 * 10**8

# 1 year in sec
year = 365.25 * 24 * 3600

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line, if line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line into "x", "y", and "err"
        (name, a_km_str, period_sec_str) = line.split ()
        # converting string into float
        try:
            a_km = float (a_km_str)
        except:
            print (f'cannot convert "{a_km_str}" into float.')
            sys.exit (1)
        try:
            period_sec = float (period_sec_str)
        except:
            print (f'cannot convert "{period_sec_str}" into float.')
            sys.exit (1)
        # converting unit
        a_au = a_km / au
        period_yr = period_sec / year
        # appending data to numpy arrays
        data_a = numpy.append (data_a, a_au)
        data_p = numpy.append (data_p, period_yr)

# printing data
print (f'data_a:\n{data_a}')
print (f'data_p:\n{data_p}')

# a function for straight line
def line (x, a, b):
    # line
    y = a * x + b
    # returning y
    return (y)

# initial guess of coefficients
param0 = [1.0, 1.0]

# least-squares fitting
popt, pcov = scipy.optimize.curve_fit (line, numpy.log10 (data_a), \
                                       numpy.log10 (data_p), p0=param0)

# fitted parameters and covariance matrix
print (f'popt:\n{popt}')
print (f'pcov:\n{pcov}')

# fitted a and b
a_fitted, b_fitted = popt

# degrees of freedom
dof = len (data_a) - len (popt)
print ("dof = %d" % (dof) )

# reduced chi-squared
residual     = data_p - line (data_a, a_fitted, b_fitted)
reduced_chi2 = (residual**2).sum () / dof
print (f'reduced chi-squared = {reduced_chi2}')

# fitted a and b
a_err, b_err = numpy.sqrt ( numpy.diagonal (pcov) )
print (f'a = {a_fitted:8.5f} +/- {a_err:8.5f} ({a_err/a_fitted*100.0:8.5f}%)')
print (f'b = {b_fitted:8.5f} +/- {b_err:8.5f} ({b_err/b_fitted*100.0:8.5f}%)')

# range of data
x_min = scipy.stats.tmin (data_a)
x_max = scipy.stats.tmax (data_a)

# fitted curve
fitted_x = numpy.linspace (x_min, x_max, 1000)
fitted_y = 10**line (numpy.log10 (fitted_x), a_fitted, b_fitted)

#
# making plot using Matplotlib
#
    
# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Semimajor Axis [au]')
ax.set_ylabel ('Orbital Period [yr]')
ax.set_xscale ('log')
ax.set_yscale ('log')

# plotting data
ax.plot (data_a, data_p, linestyle='None', marker='o', markersize=5.0, \
         color='blue', label='planets and dwarf planets in solar system')
ax.plot (fitted_x, fitted_y, linestyle=':', linewidth=3.0, \
         color='red', label='fitted line by least-squares method')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225)
