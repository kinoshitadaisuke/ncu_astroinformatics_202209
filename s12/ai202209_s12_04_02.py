#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/04 22:04:15 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

#
# command-line argument analysis
#

# constructing parser object
parser = argparse.ArgumentParser (description='plotting time-series data')

# adding arguments
parser.add_argument ('-i', type=str, default="in.data", \
                     help='input data file name')
parser.add_argument ('-o', type=str, default="out.eps", \
                     help='output figure file name')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# data file name
file_data = args.i

# output file name
file_fig = args.o

#
# reading data
#

# empty numpy arrays for storing data
data_mjd  = numpy.array ([])
data_flux = numpy.array ([])
data_err  = numpy.array ([])

mjd_min = +9999999.0
mjd_max = -9999999.0

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
        (datetime_str, mjd_str, flux_str, err_str) = line.split ()
        # data check
        if (flux_str == 'nan'):
            continue
        # conversion from string into float
        mjd  = float (mjd_str)
        flux = float (flux_str)
        err  = float (err_str)
        # appending the data at the end of numpy arrays
        data_mjd  = numpy.append (data_mjd, mjd)
        data_flux = numpy.append (data_flux, flux)
        data_err  = numpy.append (data_err, err)

        # range of data
        if (mjd < mjd_min):
            mjd_min = mjd
        if (mjd > mjd_max):
            mjd_max = mjd

#
# fitting
#

# initial values of coefficients of fitted function
a = 1.0
b = 1.7 * 10**6

# function to be used for least-squares fitting
def func (x, a, b):
    y = -a * x + b
    return y

# least-squares fitting using scipy.optimize.curve_fit
popt, pcov = scipy.optimize.curve_fit (func, data_mjd, data_flux, \
                                       sigma=data_err, p0=[a, b])

# fitted coefficients
print ("popt:")
print (popt)

# covariance matrix
print ("pcov:")
print (pcov)

# fitted a and b
a_fitted = popt[0]
b_fitted = popt[1]

# degree of freedom
dof = len (data_mjd) - 2
print (f"dof = {dof}")

# residual
residual = data_flux - func (data_mjd, a_fitted, b_fitted)
reduced_chi2 = (residual**2).sum () / dof
print (f"reduced chi^2 = {reduced_chi2}")

# errors of a and b
a_err = numpy.sqrt (pcov[0][0])
b_err = numpy.sqrt (pcov[1][1])
print (f"a = {a_fitted} +/- {a_err} ({a_err / a_fitted * 100.0} %)")
print (f"b = {b_fitted} +/- {b_err} ({b_err / b_fitted * 100.0} %)")

# fitted line
fitted_x = numpy.linspace (mjd_min, mjd_max, 10**3)
fitted_y = func (fitted_x, a_fitted, b_fitted)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('MJD [day]')
ax.set_ylabel ('Flux [10^6 e-/sec]')

# plotting data
ax.plot (data_mjd, data_flux, \
         linestyle='-', linewidth=3, color='blue', \
         label='Photometry of Kepler-13')
ax.plot (fitted_x, fitted_y, \
         linestyle=':', linewidth=5, color='red', \
         label='Baseline')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
