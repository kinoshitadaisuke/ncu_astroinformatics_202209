#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/17 02:06:43 (CST) daisuke>
#

# importing sys module
import sys

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'ai202209_s05_52.data'

# output file name
file_output = 'ai202209_s05_53.png'

# making empty numpy arrays
data_x   = numpy.array ([])
data_y   = numpy.array ([])
data_err = numpy.array ([])

# opening file for reading
with open (file_input, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # splitting line into "x" and "y"
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
             label='synthetic data for least-squares method')

# legend
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225)
