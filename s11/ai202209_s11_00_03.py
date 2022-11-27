#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 17:43:35 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.units

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_hr  = astropy.units.hr
u_day = astropy.units.day

# data file name
file_data = 'ai202209_s11_00_00.data'

# output file name
file_output = 'ai202209_s11_00_03.png'

# trial period
p_hr = numpy.array ([1.0, 1.5, 2.0, 2.5, 3.0, 3.5]) * u_hr
p_day = p_hr.to (u_day)

# empty numpy arrays for storing data
data_mjd   = numpy.array ([])
data_phase = numpy.array ([])
data_mag   = numpy.array ([])

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
        (datetime, mjd_str, mag_str) = line.split ()
        # conversion from string into float
        mjd   = float (mjd_str)
        mag   = float (mag_str)
        # appending the data at the end of numpy arrays
        data_mjd   = numpy.append (data_mjd, mjd)
        data_mag   = numpy.append (data_mag, mag)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making a plot of 2x3 panels
for i in range (len (p_day)):
    # making a subplot
    subplot = 320 + int (i) + 1
    ax = fig.add_subplot (subplot)

    # calculation of phase
    p = p_day[i].value
    data_phase = numpy.array ([])
    for mjd in data_mjd:
        phase = mjd / p - int (mjd / p)
        data_phase = numpy.append (data_phase, phase)

    # labels
    ax.set_xlabel ('Phase')
    ax.set_ylabel ('Mag [mag]')

    # range
    ax.set_xlim (0.0, 1.0)
    ax.set_ylim (18.5, 20.7)
    ax.invert_yaxis ()

    # plotting data
    label = f"trial period of {p_hr[i]:3.1f}"
    ax.plot (data_phase, data_mag, \
             linestyle='None', marker='o', markersize=3, color='blue', \
             label=label)
    ax.legend ()

# saving the plot into a file
fig.tight_layout ()
fig.savefig (file_output, dpi=225)
