#!/usr/pkg/bin/python3.9

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# importing datetime
import datetime

# input data file
file_input = 'alf_ori.data'

# output image file
file_output = 'ai202209_s04_24.png'

# making empty list and Numpy arrays
data_date  = numpy.array ([], dtype='datetime64[ms]')
data_mag   = numpy.array ([], dtype='float64')
data_error = numpy.array ([], dtype='float64')
    
# opening input file
with open (file_input, 'r') as fh_in:
    # reading data line-by-line
    for line in fh_in:
        # splitting data
        (date_str, mag_str, error_str, band, observer) = line.split ()
        # conversion from string to datetime, and then to datetime64
        date1 = datetime.datetime.strptime (date_str[:-4], '%Y-%m-%d')
        day   = float (date_str[-3:]) / 1000
        date2 = datetime.timedelta (days=day)
        date_datetime = date1 + date2
        date_datetime64 = numpy.datetime64 (date_datetime, 'ms')
        # conversion from string to float
        mag   = float (mag_str)
        error = float (error_str)
        # appending data to list and Numpy arrays
        data_date  = numpy.append (data_date, date_datetime64)
        data_mag   = numpy.append (data_mag, mag)
        data_error = numpy.append (data_error, error)

# making a fig object
fig = matplotlib.figure.Figure ()

# making a canvas object
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

# making an axes object
ax = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date [YYYY-MM-DD]')
ax.set_ylabel ('V-band Magnitude [mag]')

# axis settings
ax.set_xlim (numpy.datetime64 ('2019-12-20'), numpy.datetime64 ('2020-04-01'))
ax.set_ylim (+1.9, +0.9)

# plotting data
ax.errorbar (data_date, data_mag, yerr=data_error, linestyle='None', \
             marker='o', markersize=5.0, color='red', \
             elinewidth=2.0, ecolor='black', capsize=5.0, \
             label='Betelgeuse')

# ticks
months     = matplotlib.dates.MonthLocator ()
days       = matplotlib.dates.DayLocator ()
months_fmt = matplotlib.dates.DateFormatter ('%Y-%m-%d')
ax.xaxis.set_major_locator (months)
ax.xaxis.set_major_formatter (months_fmt)
ax.xaxis.set_minor_locator (days)

# legend
ax.legend (loc='upper right')

# formatting labels
fig.autofmt_xdate()

# saving the figure to a file
fig.savefig (file_output)
