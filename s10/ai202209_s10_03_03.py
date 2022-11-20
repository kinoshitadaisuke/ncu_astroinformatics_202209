#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/20 23:04:43 (CST) daisuke>
#

# importing gzip module
import gzip

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# files
list_file_cat = ['xsc_aaa.gz', 'xsc_baa.gz']
file_output   = 'ai202209_s10_03_03.png'

# lists for storing data
list_glon_rad = []
list_glat_rad = []

# reading catalogue files
for file_cat in list_file_cat:
    # printing status
    print ("reading the file \"%s\"..." % (file_cat) )

    # opening file
    with gzip.open (file_cat, 'rb') as fh:
        # reading lines
        for line in fh:
            # decoding byte data
            line = line.decode ('utf-8')
            # splitting line
            records = line.split ('|')
            # extracting data
            glon_str = records[6].strip ()
            glat_str = records[7].strip ()
            # skip, if any of data is missing.
            if ( (glon_str == '') or (glat_str == '') ):
                continue
            # conversion from string to float
            glon_deg = float (glon_str)
            glat_deg = float (glat_str)
            # deg --> radian
            glon_rad = glon_deg / 180.0 * numpy.pi
            if (glon_rad > numpy.pi):
                glon_rad -= 2.0 * numpy.pi
            glat_rad = glat_deg / 180.0 * numpy.pi
            # appending data to lists
            list_glon_rad.append (glon_rad)
            list_glat_rad.append (glat_rad)

    # printing status
    print ("done!")

# printing status
print ("constructing numpy arrays...")

# making numpy arrays
data_glon_rad = numpy.array (list_glon_rad)
list_glon_rad.clear ()
data_glat_rad = numpy.array (list_glat_rad)
list_glat_rad.clear ()

# printing status
print ("done!")

# printing status
print ("generating a plot...")

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection="aitoff")

# axes
ax.grid ()
ax.set_title ('2MASS XSC', loc='right')
ax.set_xlabel ('Galactic longitude')
ax.set_ylabel ('Galactic latitude')

# plotting data
dist = ax.hexbin (data_glon_rad, data_glat_rad, gridsize=180, \
                  cmap=matplotlib.cm.plasma)
fig.colorbar (dist, ax=ax, spacing='uniform', extend='max')

# saving file
fig.savefig (file_output, bbox_inches="tight", dpi=225)

# printing status
print ("done!")
