#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 20:31:36 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc = 'making Hubble diagram using LVG data'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
args = parser.parse_args ()

# file names
file_data = args.input
file_fig  = args.output

# numpy arrays to store data
data_d     = numpy.array ([])
data_d_err = numpy.array ([])
data_v     = numpy.array ([])
data_v_err = numpy.array ([])

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
        v     = float (data[2])
        v_err = float (data[3])
        # appending data to numpy arrays
        # reject data with distance error larger than 10.0 Mpc
        if (d_err < 10.0):
            data_d     = numpy.append (data_d, d)
            data_d_err = numpy.append (data_d_err, d_err)
            data_v     = numpy.append (data_v, v)
            data_v_err = numpy.append (data_v_err, v_err)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Distance [Mpc]')
ax.set_ylabel ('Velocity [km/s]')
ax.grid ()

# making a Hubble diagram
ax.errorbar (data_d, data_v, xerr=data_d_err, yerr=data_v_err, \
             linestyle='None', marker='o', color='blue', markersize=3, \
             ecolor='black', capsize=3, label='LVG galaxies')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
