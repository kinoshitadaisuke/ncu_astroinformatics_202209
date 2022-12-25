#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 22:14:09 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.ascii
import astropy.units
import astropy.constants

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc = 'making Hubble diagram using NED-D data'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
args = parser.parse_args ()

# file names
file_data = args.input
file_fig  = args.output

# speed of light
c = astropy.constants.c

# units
unit_m_per_s = astropy.units.m / astropy.units.s

# reading CSV data
rawdata = astropy.io.ascii.read (file_data, format='csv')

# dictionary to store data
data = {}

# examining the data
for i in range ( len (rawdata) ):
    # extracting data
    # name of galaxy
    name = rawdata[i]['Galaxy ID']
    # distance modulus
    distmod = rawdata[i]['m-M']
    # error of distance modulus
    distmod_err = rawdata[i]['err']
    # distance in Mpc
    dist_Mpc = rawdata[i]['D (Mpc)']
    # redshift
    z = rawdata[i]['_1']
    # velocity
    v = ( (z + 1.0)**2 - 1.0 ) / ( (z + 1.0)**2 + 1.0 ) * c

    # appending data to the dictionary
    # skip if redshift is missing.
    # skip if error of distance modulus is large.
    # skip if distance is larger than 500 Mpc
    # skip if velocity is larger than 50000 km/s
    if ( (z > 0.0) and (distmod_err < 0.05) and (dist_Mpc < 500.0) \
         and (v / unit_m_per_s < 5*10**7) ):
        # if the data is not in the dictionary, add data
        if not name in data:
            data[name] = {}
            data[name]['distmod'] = distmod
            data[name]['distmod_err'] = distmod_err
            data[name]['dist_Mpc'] = dist_Mpc
            data[name]['z'] = z
            data[name]['v'] = v

# making numpy arrays for plotting data
data_d = numpy.array ([])
data_v = numpy.array ([])
for name in sorted (data, key=lambda x: data[x]['dist_Mpc']):
    data_d = numpy.append (data_d, data[name]['dist_Mpc'])
    data_v = numpy.append (data_v, data[name]['v'] * 10**-3 / unit_m_per_s)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Distance [Mpc]')
ax.set_ylabel ('Velocity [km/s]')
ax.grid ()

# making a Hubble diagram
ax.plot (data_d, data_v, \
         linestyle='None', marker='o', color='blue', markersize=2, \
         label='galaxies in NED-1D')
ax.legend ()

# saving the plot into a file
fig.savefig (file_fig, dpi=225)
