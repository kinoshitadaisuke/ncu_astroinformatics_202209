#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/16 21:49:37 (CST) daisuke>
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
file_output = 'ai202209_s05_56.png'

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

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225)
