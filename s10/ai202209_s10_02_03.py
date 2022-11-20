#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/20 22:21:14 (CST) daisuke>
#

# importing gzip module
import gzip

# importing numpy module
import numpy

# importing astropy module
import astropy.units
import astropy.coordinates

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg
u_rad = astropy.units.rad

# files
file_cat    = 'hip2.dat.gz'
file_output = 'ai202209_s10_02_03.pdf'

# list to store data
list_ra_rad  = []
list_dec_rad = []

# counting number of data
n = 0

# opening file
with gzip.open (file_cat, 'rb') as fh:
    # reading data
    for line in fh:
        n += 1

# opening file
with gzip.open (file_cat, 'rb') as fh:
    # reading data
    i = 0
    for line in fh:
        # decoding raw byte data
        line = line.decode ('utf-8')
        
        # extracting data
        ra_str  = line[15:28].strip ()
        dec_str = line[29:42].strip ()
        mag_str = line[129:136].strip ()
        BV_str  = line[152:158].strip ()

        # skipping, if any of data is missing.
        if ( (ra_str == '') or (dec_str == '') or (mag_str == '') \
             or (BV_str == '') ):
            continue
        # conversion from string to float
        ra_rad  = float (ra_str)
        dec_rad = float (dec_str)
        mag     = float (mag_str)
        BV      = float (BV_str)
    
        # coordinate
        coord = astropy.coordinates.SkyCoord (ra_rad, dec_rad, \
                                              frame=astropy.coordinates.ICRS, \
                                              unit=u_rad)

        # appending data to lists
        ra_rad_wrap = coord.ra.wrap_at (180 * u_deg).radian
        list_ra_rad.append (ra_rad_wrap)
        list_dec_rad.append (coord.dec.radian)

        # progress
        i += 1
        if (i % 5000 == 0):
            print ("progress: %6d / %6d" % (i, n) )

# making numpy arrays
data_ra_rad = numpy.array (list_ra_rad)
list_ra_rad.clear ()
data_dec_rad = numpy.array (list_dec_rad)
list_dec_rad.clear ()

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection="aitoff")

matplotlib.rcParams['agg.path.chunksize'] = 10000

# axes
ax.grid ()
ax.set_title ('Hipparcos Catalogue', loc='right')
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting data
density = ax.hexbin (data_ra_rad, data_dec_rad, gridsize=120, \
                     cmap=matplotlib.cm.inferno)
fig.colorbar (density, ax=ax, spacing='uniform', extend='max')

# saving file
fig.savefig (file_output, bbox_inches="tight", dpi=225)
