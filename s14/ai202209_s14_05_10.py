#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/18 23:54:28 (CST) daisuke>
#

# importing argparse module
import argparse

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# command-line argument analysis
parser = argparse.ArgumentParser (description='selecting stars by distance')
parser.add_argument ('-i', '--input', help='input VOTable file name')
parser.add_argument ('-o', '--output', help='output file name')
parser.add_argument ('-a', '--min', type=float, help='minimum data value')
parser.add_argument ('-b', '--max', type=float, help='maximum data value')
args = parser.parse_args ()

# VOTable file name
file_votable = args.input
file_output  = args.output

# information of bins
x_min  = args.min
x_max  = args.max

# reading VOTable
table = astropy.io.votable.parse_single_table (file_votable).to_table ()

# data
data_id        = numpy.array (table['source_id'])
data_ra        = numpy.array (table['ra'])
data_dec       = numpy.array (table['dec'])
data_parallax  = numpy.array (table['parallax'])
data_pmra      = numpy.array (table['pmra'])
data_pmdec     = numpy.array (table['pmdec'])
data_rv        = numpy.array (table['radial_velocity'])
data_b         = numpy.array (table['phot_bp_mean_mag'])
data_g         = numpy.array (table['phot_g_mean_mag'])
data_r         = numpy.array (table['phot_rp_mean_mag'])
data_br        = numpy.array (table['bp_rp'])
data_bg        = numpy.array (table['bp_g'])
data_gr        = numpy.array (table['g_rp'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_ra_err    = numpy.array (table['ra_error'])
data_dec_err   = numpy.array (table['dec_error'])
data_pmra_err  = numpy.array (table['pmra_error'])
data_pmdec_err = numpy.array (table['pmdec_error'])
data_p_snr     = numpy.array (table['parallax_over_error'])
data_b_snr     = numpy.array (table['phot_bp_mean_flux_over_error'])
data_g_snr     = numpy.array (table['phot_g_mean_flux_over_error'])
data_r_snr     = numpy.array (table['phot_rp_mean_flux_over_error'])

# distance
data_distance = numpy.array ([])
for i in range ( len (data_parallax) ):
    # rejecting stars of negative parallax, no measurement of parallax,
    # and parallax SNR less than 10.0
    if ( (data_parallax[i] <= 0.0) or (numpy.isnan (data_parallax[i]) ) \
         or (data_p_snr[i] < 10.0) ):
        data_distance = numpy.append (data_distance, -1.0)
    else:
        data_distance = numpy.append (data_distance, 1000.0 / data_parallax[i])

# opening file for writing
with open (file_output, 'w') as fh:
    # examining each star
    for i in range ( len (data_distance) ):
        # rejecting stars of low signal-to-noise ratio
        if (data_b_snr[i] < 10.0):
            continue
        if (data_g_snr[i] < 10.0):
            continue
        if (data_r_snr[i] < 10.0):
            continue
        # selecting stars between distances x_min and x_max
        if ( (data_distance[i] >= x_min) and (data_distance[i] <= x_max) ):
            # writing data into file
            record = f"{data_id[i]} {data_ra[i]} {data_dec[i]}" \
                + f" {data_parallax[i]} {data_pmra[i]} {data_pmdec[i]}" \
                + f" {data_rv[i]} {data_b[i]} {data_g[i]} {data_r[i]}" \
                + f" {data_br[i]} {data_bg[i]} {data_gr[i]}\n"
            fh.write (record)
