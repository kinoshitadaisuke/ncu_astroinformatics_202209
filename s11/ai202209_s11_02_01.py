#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/27 22:54:34 (CST) daisuke>
#

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = '201498.tb2.txt'

# output file name
file_output = 'ai202209_s11_02_01.data'

# shortest trial period in minute and in day
period_min_min = 10.0
period_min_day = period_min_min / (60.0 * 24.0)

# longest trial period in minute and in day
period_max_min = 1000.0
period_max_day = period_max_min / (60.0 * 24.0)

# step size of trial period in minute and in day
step_min = 0.01
step_day = step_min / (60.0 * 24.0)

# number of bins
n_bins = 10

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

        # appending the data at the end of numpy arrays
        data_jd      = numpy.append (data_jd, jd)
        data_mag_app = numpy.append (data_mag_app, mag_app)
        data_mag_abs = numpy.append (data_mag_abs, mag_abs)

# opening file for writing
with open (file_output, 'w') as fh_out:
    # writing header to output file
    header  = f"#\n"
    header += f"# parameters for PDM analysis\n"
    header += f"#\n"
    header += f"# input file = {file_input}\n"
    header += f"# output file = {file_output}\n"
    header += f"# shortest trial period = {period_min_min} min\n"
    header += f"# longest trial period = {period_max_min} min\n"
    header += f"# step size of trial period = {step_min} min\n"
    header += f"# number of bins = {n_bins}\n"
    header += f"#\n"
    header += f"# results of PDM analysis\n"
    header += f"#\n"
    header += f"# trial period (day), trial period (hr), trial period (min), "
    header += f"total variance\n"
    header += f"#\n"
    fh_out.write (header)

    # initial value of trial period
    period_day = period_min_day

    # period search
    while (period_day < period_max_day):
        # calculation of phase with assumed period
        data_phase = numpy.array ([])
        for i in range ( len (data_jd) ):
            phase = (data_jd[i] - data_jd[0]) / period_day
            phase -= int (phase)
            data_phase = numpy.append (data_phase, phase)

        # initialization of parameter
        total_variance = 0.0
        
        # calculation of variance
        for i in range (n_bins):
            # range of bin
            bin_min = i / n_bins
            bin_max = (i + 1) / n_bins

            # finding data within the bin
            data_bin = numpy.array ([])
            for j in range ( len (data_phase) ):
                if ( (data_phase[j] >= bin_min) and (data_phase[j] < bin_max) ):
                    data_bin = numpy.append (data_bin, data_mag_abs[j])

            # if no data in the bin, then we skip.
            if (len (data_bin) == 0):
                continue

            # variance
            variance_in_bin = numpy.var (data_bin)
            # sum of variance
            total_variance += variance_in_bin

        # writing data to file
        output = f"{period_day:12.10f} {period_day * 24.0:12.8f} " \
            + f"{period_day * 24.0 * 60.0:12.6f} {total_variance:10.6f}\n"
        fh_out.write (output)

        # next trial period
        period_day += step_day
