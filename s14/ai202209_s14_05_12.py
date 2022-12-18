#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/19 00:16:13 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='selection by proper motion')
parser.add_argument ('-i', '--input', help='input file name')
parser.add_argument ('-o', '--output', help='output file name')
args = parser.parse_args ()

# file names
file_input  = args.input
file_output = args.output

# lists to store data
list_id       = []
list_ra       = []
list_dec      = []
list_parallax = []
list_pmra     = []
list_pmdec    = []
list_rv       = []
list_b        = []
list_g        = []
list_r        = []
list_br       = []
list_bg       = []
list_gr       = []

# opening file
with open (file_input, 'r') as fh_in:
    # reading file
    for line in fh_in:
        # removing new line at the end of the line
        line = line.strip ()
        # splitting the line
        data = line.split ()
        # fields
        list_id.append (data[0])
        list_ra.append (float (data[1]) )
        list_dec.append (float (data[2]) )
        list_parallax.append (float (data[3]) )
        list_pmra.append (float (data[4]) )
        list_pmdec.append (float (data[5]) )
        list_rv.append (float (data[6]) )
        list_b.append (float (data[7]) )
        list_g.append (float (data[8]) )
        list_r.append (float (data[9]) )
        list_br.append (float (data[10]) )
        list_bg.append (float (data[11]) )
        list_gr.append (float (data[12]) )

# making numpy arrays
data_id       = numpy.array (list_id)
data_ra       = numpy.array (list_ra)
data_dec      = numpy.array (list_dec)
data_parallax = numpy.array (list_parallax)
data_pmra     = numpy.array (list_pmra)
data_pmdec    = numpy.array (list_pmdec)
data_rv       = numpy.array (list_rv)
data_b        = numpy.array (list_b)
data_g        = numpy.array (list_g)
data_r        = numpy.array (list_r)
data_br       = numpy.array (list_br)
data_bg       = numpy.array (list_bg)
data_gr       = numpy.array (list_gr)

# clearing lists
list_id.clear ()
list_ra.clear ()
list_dec.clear ()
list_parallax.clear ()
list_pmra.clear ()
list_pmdec.clear ()
list_rv.clear ()
list_b.clear ()
list_g.clear ()
list_r.clear ()
list_br.clear ()
list_bg.clear ()
list_gr.clear ()

# normalised proper motion vectors
data_pmra_norm  = numpy.array ([])
data_pmdec_norm = numpy.array ([])
data_pm_length  = numpy.array ([])
for i in range (len (data_pmra) ):
    # length of a vector (data_pmra[i], data_pmdec[i])
    length = numpy.sqrt (data_pmra[i]**2 + data_pmdec[i]**2)
    # normalised vector
    pmra_norm  = data_pmra[i] / length
    pmdec_norm = data_pmdec[i] / length
    # appending vector components to numpy arrays
    data_pmra_norm  = numpy.append (data_pmra_norm, pmra_norm)
    data_pmdec_norm = numpy.append (data_pmdec_norm, pmdec_norm)
    data_pm_length  = numpy.append (data_pm_length, length)

# average direction of proper motion
pmra_mean  = numpy.mean (data_pmra_norm)
pmdec_mean = numpy.mean (data_pmdec_norm)
pmra_mean_norm  = pmra_mean / numpy.sqrt (pmra_mean**2 + pmdec_mean**2)
pmdec_mean_norm = pmdec_mean / numpy.sqrt (pmra_mean**2 + pmdec_mean**2)
pm_length_mean = numpy.mean (data_pm_length)

# opening file for writing
with open (file_output, 'w') as fh_out:
    # angle between a proper motion vector and mean proper motion vector
    for i in range ( len (data_pmra) ):
        # angle
        cos_a = data_pmra_norm[i] * pmra_mean_norm \
            + data_pmdec_norm[i] * pmdec_mean_norm
        a = numpy.arccos (cos_a) / numpy.pi * 180.0
        # length of a vector (data_pmra[i], data_pmdec[i])
        length = numpy.sqrt (data_pmra[i]**2 + data_pmdec[i]**2)
        # rejecting stars with angle larger than 45 deg and large proper motion
        if ( (a <= 45.0) and (length < 2.0 * pm_length_mean) ):
            # writing data into file
            record = f"{data_id[i]} {data_ra[i]} {data_dec[i]}" \
                + f" {data_parallax[i]} {data_pmra[i]} {data_pmdec[i]}" \
                + f" {data_rv[i]} {data_b[i]} {data_g[i]} {data_r[i]}" \
                + f" {data_br[i]} {data_bg[i]} {data_gr[i]}\n"
            fh_out.write (record)
