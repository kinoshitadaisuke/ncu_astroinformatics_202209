#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 23:08:28 (CST) daisuke>
#

# importing argparse module
import argparse

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

#
# command-line argument analysis
#

# constructing parser object
parser = argparse.ArgumentParser (description='plotting power spectrum')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')
parser.add_argument ('-x1', type=float, default=0.0, \
                     help='minimum period to be plotted in day')
parser.add_argument ('-x2', type=float, default=100.0, \
                     help='maximum period to be plotted in day')
parser.add_argument ('-f1', type=float, default=1.0, \
                     help='minimum period to be used for fitting in day')
parser.add_argument ('-f2', type=float, default=10.0, \
                     help='maximum period to be used for fitting in day')
parser.add_argument ('-a', type=float, default=1.0, \
                     help='initial value of coefficient "a" (default: 1.0)')
parser.add_argument ('-b', type=float, default=1.0, \
                     help='initial value of coefficient "b" (default: 1.0)')
parser.add_argument ('-c', type=float, default=1.0, \
                     help='initial value of coefficient "c" (default: 1.0)')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

# minimum period to be plotted
per_min_day = args.x1

# maximum period to be plotted
per_max_day = args.x2

# minimum period to be used for fitting
fitting_min_day = args.f1

# maximum period to be used for fitting
fitting_max_day = args.f2

# coefficients
a = args.a
b = args.b
c = args.c

#
# reading data from file
#

# empty numpy arrays for storing data
data_freq    = numpy.array ([])
data_per_day = numpy.array ([])
data_per_hr  = numpy.array ([])
data_per_min = numpy.array ([])
data_power   = numpy.array ([])
fit_freq     = numpy.array ([])
fit_per_day  = numpy.array ([])
fit_per_hr   = numpy.array ([])
fit_per_min  = numpy.array ([])
fit_power    = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (freq_str, per_day_str, per_hr_str, per_min_str, power_str) \
            = line.split ()
        # conversion from string into float
        freq    = float (freq_str)
        per_day = float (per_day_str)
        per_hr  = float (per_hr_str)
        per_min = float (per_min_str)
        power   = float (power_str)
        # appending the data at the end of numpy arrays
        if ( (per_day >= per_min_day) and (per_day <= per_max_day) ):
            data_freq    = numpy.append (data_freq, freq)
            data_per_day = numpy.append (data_per_day, per_day)
            data_per_hr  = numpy.append (data_per_hr, per_hr)
            data_per_min = numpy.append (data_per_min, per_min)
            data_power   = numpy.append (data_power, power)
        if ( (per_day >= fitting_min_day) and (per_day <= fitting_max_day) ):
            fit_freq    = numpy.append (fit_freq, freq)
            fit_per_day = numpy.append (fit_per_day, per_day)
            fit_per_hr  = numpy.append (fit_per_hr, per_hr)
            fit_per_min = numpy.append (fit_per_min, per_min)
            fit_power   = numpy.append (fit_power, power)

#
# least-squares method
#

# function to be used for least-squares fitting
def func (x, a, b, c):
    y = -a * (x - b)**2 + c
    return y

# least-squares fitting using scipy.optimize.curve_fit
popt, pcov = scipy.optimize.curve_fit (func, fit_per_day, fit_power, \
                                       p0=[a, b, c], maxfev=3000, \
                                       method='lm')

# fitted coefficients
print ("popt:")
print (popt)

# covariance matrix
print ("pcov:")
print (pcov)

# fitted a and b
a_fitted = popt[0]
b_fitted = popt[1]
c_fitted = popt[2]

# degree of freedom
dof = len (fit_per_day) - 3
print (f"dof = {dof}")

# residual
residual = fit_power - func (fit_per_day, a_fitted, b_fitted, c_fitted)
reduced_chi2 = (residual**2).sum () / dof
print (f"reduced chi^2 = {reduced_chi2}")

# errors of a and b
a_err = numpy.sqrt (pcov[0][0])
b_err = numpy.sqrt (pcov[1][1])
c_err = numpy.sqrt (pcov[2][2])
print (f"a = {a_fitted:15.8f} +/- {a_err:15.8f} ({a_err/a_fitted*100:8.4f} %)")
print (f"b = {b_fitted:15.8f} +/- {b_err:15.8f} ({b_err/b_fitted*100:8.4f} %)")
print (f"c = {c_fitted:15.8f} +/- {c_err:15.8f} ({c_err/c_fitted*100:8.4f} %)")

# fitted line
fitted_x = numpy.linspace (fitting_min_day, fitting_max_day, 10**3)
fitted_y = func (fitted_x, a_fitted, b_fitted, c_fitted)

#
# making a plot
#

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Period [day]')
ax.set_ylabel ('Power')

# range
ax.set_xlim (per_min_day, per_max_day)

# plotting data
ax.plot (data_per_day, data_power, \
         linestyle='-', linewidth=5, color='blue', \
         label='result of Lomb-Scargle periodogram')
ax.plot (fitted_x, fitted_y, \
         linestyle=':', linewidth=3, color='red', \
         label='result of least-squares fitting')
ax.legend (bbox_to_anchor=(1.0, 1.16), loc='upper right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
