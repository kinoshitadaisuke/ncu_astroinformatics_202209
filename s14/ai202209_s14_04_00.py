#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/18 21:18:28 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.io.votable

# VOTable file name
file_votable = "m3.vot.gz"

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

# printing header
print ("# ID, RA, Dec, parallax, pm in RA, pm in Dec, g mag, g-r colour")

# printing data
for i in range ( len (data_id) ):
    if ( numpy.isnan (data_parallax[i]) ):
        continue
    if (data_parallax[i] < 0.0):
        continue
    print (f"{data_id[i]} {data_ra[i]:8.4f} {data_dec[i]:+8.4f}", \
           f"{data_parallax[i]:6.4f}", \
           f"{data_pmra[i]:+8.4f} {data_pmdec[i]:+8.4f}", \
           f"{data_g[i]:+6.3f} {data_gr[i]:+6.3f}")
