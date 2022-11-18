#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/18 15:41:25 (CST) daisuke>
#

# importing gzip module
import gzip

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# catalogue file name
file_catalogue = 'mpcorb.dat.gz'

# output file name
file_output = 'ai202209_s10_00_04.png'

#
# parameters for histogram
#

# width of a bin in au
bin_width = 0.1

# number of bins
n_bins = 100

# bins
bins = numpy.linspace (0.0, bin_width * (n_bins - 1), n_bins)

# making a numpy array for histogram
hist_a = numpy.zeros (n_bins, dtype=int)

# opening catalogue file
with gzip.open (file_catalogue, 'rb') as fh:
    # reading catalogue line-by-line
    for line in fh:
        # number of provisional designation
        try:
            designation = line[0:7].strip ().decode ('utf-8')
        except:
            continue
        # absolute magnitude
        try:
            absmag = float (line[8:13])
        except:
            absmag = -999.99
        # mean anomaly
        try:
            M = float (line[26:35])
        except:
            M = -999.99
        # argument of perihelion
        try:
            peri = float (line[37:46])
        except:
            peri = -999.99
        # longitude of ascending node
        try:
            node = float (line[48:57])
        except:
            node = -999.99
        # inclination
        try:
            i = float (line[59:68])
        except:
            i = -999.99
        # eccentricity
        try:
            e = float (line[70:79])
        except:
            e = -999.99
        # semimajor axis
        try:
            a = float (line[92:103])
        except:
            a = -999.99
        # number of observations
        try:
            nobs = int (line[117:122])
        except:
            nobs = -999
        # residual
        try:
            residual = float (line[137:141])
        except:
            residual = -999.99
        # 4-hexdigit flags
        try:
            flag = line[161:165].strip ().decode ('utf-8')
        except:
            flag = '9999'
        # readable name
        try:
            name = line[166:194].strip ().decode ('utf-8')
        except:
            name = '__NONE__'
        # last observation date
        try:
            lastobs = int (line[194:202])
        except:
            lastobs = 99999999

        # skip when reading the header
        if ( (a < -999.0) and (e < -999.0) and (i < -999.0) \
             and (peri < -999.0) and (node < -999.0) and (M < -999.0) ):
            continue
            
        # counting number of asteroids in each bin
        if (a * 10 < n_bins):
            i = int (a * 10)
            hist_a[i] += 1

# printing histogram
for i in range (n_bins):
    start = i * bin_width
    end   = (i + 1) * bin_width
    print (f"from {start:5.2f} au to {end:5.2f} au : {hist_a[i]:8d}")

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Semimajor axis [au]')
ax.set_ylabel ('Number of asteroids')

# axes
fig.tight_layout ()
ax.set_xlim (0.0, 10.0)
ax.set_xticks (numpy.linspace (0.0, 10.0, 11))

# plotting a histogram
ax.bar (bins, height=hist_a, width=bin_width, align='edge')

# saving the plot into a file
fig.savefig (file_output, dpi=225)
