#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/26 00:43:19 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing scipy module
import scipy.optimize
import scipy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser \
    (description='Hubble constant from Unified Supernova Catalogue')
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
args = parser.parse_args ()

# file names
file_data = args.input
file_fig  = args.output

# numpy arrays to store data
data_d     = numpy.array ([])
data_d_err = numpy.array ([])
data_z     = numpy.array ([])
data_v     = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading data
    for line in fh:
        # skip the line, if it starts with '#'
        if (line[0] == '#'):
            continue
        # splitting the line
        data  = line.split ()
        # extracting data
        d     = float (data[0])
        d_err = float (data[1])
        z     = float (data[2])
        v     = float (data[3])
        # appending data to numpy arrays
        data_d     = numpy.append (data_d, d)
        data_d_err = numpy.append (data_d_err, d)
        data_z     = numpy.append (data_z, z)
        data_v     = numpy.append (data_v, v)

# initial values of coefficient
H0 = 100.0
init = [H0]

# function
def func (x, H0):
    y = H0 * x
    return (y)

# least-squares method
popt, pcov = scipy.optimize.curve_fit (func, data_d, data_v, p0=init)

# result of fitting
H0_bestfit = popt[0]
print ("popt:")
print (popt)
print ("pcov:")
print (pcov)

# degree of freedom
dof = len (data_d) - len (init)
print (f"dof = {dof}")

# residual
residual = data_v - func (data_d, popt[0])
reduced_chi2 = (residual**2).sum () / dof
print (f"reduced chi^2 = {reduced_chi2}")

# error of H0
H0_err = numpy.sqrt (pcov[0][0])
print (f"H0 = {H0_bestfit} +/- {H0_err} ({H0_err / H0_bestfit * 100.0} %)")

# fitted curve
fitted_x = numpy.linspace (0.0, 300.0, 1000)
fitted_y = func (fitted_x, H0_bestfit)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Distance [Mpc]')
ax.set_ylabel ('Velocity [km/s]')
ax.grid ()

# making a Hubble diagram
label_fitting = "best-fit line (H0=%4.1f)" % (H0_bestfit)
ax.plot (data_d, data_v, \
         linestyle='None', marker='o', color='blue', markersize=2, \
         label='type-Ia supernovae from USC')
ax.plot (fitted_x, fitted_y, linestyle='--', color='red', \
         label=label_fitting)
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225, bbox_inches="tight")
