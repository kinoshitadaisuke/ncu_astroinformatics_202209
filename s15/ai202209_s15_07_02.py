#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/26 01:19:47 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.cosmology

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
desc = 'Hubble diagram of high-z supernovae'
parser = argparse.ArgumentParser (description=desc)
parser.add_argument ('-i', '--input', help='input data file name')
parser.add_argument ('-o', '--output', help='output figure file name')
args = parser.parse_args ()

# file names
file_data = args.input
file_fig  = args.output

# numpy arrays for storing data
data_zcmb   = numpy.array ([])
data_mB     = numpy.array ([])
data_mB_err = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # reading file
    for line in fh:
        # skip if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting the line
        data = line.split ()
        # extracting data
        zcmb   = float (data[1])
        mB     = float (data[4])
        mB_err = float (data[5])
        # appending data to numpy arrays
        data_zcmb   = numpy.append (data_zcmb, zcmb)
        data_mB     = numpy.append (data_mB, mB)
        data_mB_err = numpy.append (data_mB_err, mB_err)

# distance modulus
data_mu = data_mB + 19.30

# cosmology models
cosmo_000_100 = astropy.cosmology.FlatLambdaCDM (H0=70.0, Om0=1.0)
cosmo_070_030 = astropy.cosmology.FlatLambdaCDM (H0=70.0, Om0=0.3)

# redshift
z_min = -2.0
z_max = 1.0
z = numpy.logspace (z_min, z_max, num=300)

# distance modulus
distmod_000_100 = cosmo_000_100.distmod (z)
distmod_070_030 = cosmo_070_030.distmod (z)

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.set_xlabel ('Redshift')
ax.set_ylabel ('Distance Modulus [mag]')
ax.grid ()
ax.set_xlim (0.0, 1.5)
ax.set_ylim (32.5, 47.0)

# making a Hubble diagram
ax.errorbar (data_zcmb, data_mu, yerr=data_mB_err, \
             linestyle='None', marker='o', color='blue', markersize=1, \
             ecolor='black', capsize=2, \
             label='high-z supernovae from SNLS')
ax.plot (z, distmod_000_100, linestyle='-', linewidth=3, color='g', \
         label='$\Omega_\Lambda=0.0$, $\Omega_m=1.0$, flat Universe')
ax.plot (z, distmod_070_030, linestyle='--', linewidth=3, color='r', \
         label='$\Omega_\Lambda=0.7$, $\Omega_m=0.3$, flat Universe')
ax.legend (loc='lower right')

# saving the plot into a file
fig.savefig (file_fig, dpi=225, bbox_inches="tight")
