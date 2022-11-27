#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 22:44:43 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file
file_input = '201498.tb2.txt'

# output file
file_output = 'ai202209_s11_02_00.png'

# numpy arrays to store data
data_jd      = numpy.array ([])
data_mag_app = numpy.array ([])
data_mag_abs = numpy.array ([])

# opening file
with open (file_input, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # skipping line if the line does not start with digits
        if not (line[0].isdigit):
            continue
        # skipping line if it is empty
        if (line.strip () == ''):
            continue
        # removing line feed at the end of line
        line = line.strip ()
        # splitting data
        (frame_id_str, month_str, day_str, jd_str, mag_app_str, mag_abs_str) \
            = line.split ()
        # conversion from string into float
        frame_id = float (frame_id_str)
        day = float (day_str)
        jd_str = jd_str.replace (',', '')
        jd = float (jd_str)
        mag_app = float (mag_app_str)
        mag_abs = float (mag_abs_str)

        # only the data taken on 17 Feb are used for plotting
        if not ( (month_str == 'Feb') and (day_str[0:2] == '17') ):
            continue
        
        # appending the data at the end of numpy arrays
        data_jd      = numpy.append (data_jd, jd)
        data_mag_app = numpy.append (data_mag_app, mag_app)
        data_mag_abs = numpy.append (data_mag_abs, mag_abs)
        
# making fig and ax
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('JD - 2451950')
ax.set_ylabel ('R-band Absolute Magnitude [mag]')

# axes
ax.invert_yaxis ()

# plotting a figure
ax.plot (data_jd - 1950.0, data_mag_app, \
         linestyle='None', marker='o', markersize=3, color='red', \
         label='(20000) Varuna')
ax.legend ()

# saving the figure to a file
fig.savefig (file_output, dpi=225)
