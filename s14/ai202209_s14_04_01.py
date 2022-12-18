#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/18 21:31:27 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# command-line argument analysis
parser = argparse.ArgumentParser (description='reading VOTable file')
parser.add_argument ('-i', '--input', help='input VOTable file name')
parser.add_argument ('-o', '--output', help='output file name')
args = parser.parse_args ()

# VOTable file name
file_votable = args.input

# output file name
file_output  = args.output

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['source_id'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_gr        = numpy.array (table['g_rp'])

# opening file for writing
with open (file_output, 'w') as fh:
    # writing header
    header = "# ID, RA, Dec, parallax, pm in RA, pm in Dec, g mag, g-r colour\n"
    fh.write (header)
    
    # writing data
    for i in range ( len (data_id) ):
        if ( numpy.isnan (data_parallax[i]) ):
            continue
        if (data_parallax[i] < 0.0):
            continue
        record = f"{data_id[i]} {data_ra[i]:8.4f} {data_dec[i]:+8.4f}" \
            + f" {data_parallax[i]:6.4f}" \
            + f" {data_pmra[i]:+8.4f} {data_pmdec[i]:+8.4f}" \
            + f" {data_g[i]:+6.3f} {data_gr[i]:+6.3f}\n"
        fh.write (record)
