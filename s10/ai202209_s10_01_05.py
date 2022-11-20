#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/20 20:28:20 (CST) daisuke>
#

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

# data file
file_data = 'bsc5.txt'

# output files
file_output = 'ai202209_s10_01_05.png'

# numpy arrays to storing data
data_hr   = numpy.array ([])
data_ra   = numpy.array ([])
data_dec  = numpy.array ([])
data_l    = numpy.array ([])
data_b    = numpy.array ([])
data_Vmag = numpy.array ([])

# opening file
with open (file_data, 'r') as fh:
    # counting number of objects
    n = 0
    for line in fh:
        n += 1

# opening file
with open (file_data, 'r') as fh:
    # initialising counter
    i = 0
    # reading file
    for line in fh:
        # counting and showing progress
        i += 1
        if (i % 500 == 0):
            print ("progress: %4d / %4d" % (i, n) )
        # splitting line
        (hr_str, ra_str, dec_str, glon_str, glat_str, Vmag_str) = line.split ()
        # conversion from string to int or float
        hr = int (hr_str)
        glon_deg = float (glon_str)
        glat_deg = float (glat_str)
        Vmag = float (Vmag_str)

        # skip if Vmag > 6.0
        if (Vmag > 6.0):
            continue
    
        # coordinate
        coord = astropy.coordinates.SkyCoord (ra_str, dec_str, \
                                              frame=astropy.coordinates.FK5, \
                                              equinox="J2000", \
                                              unit=(u_ha, u_deg) )

        # (RA, Dec) in radian
        ra_rad = coord.ra.radian
        dec_rad = coord.dec.radian
        # conversion from (RA, Dec) to (l, b) using astropy
        l_rad = coord.galactic.l.radian
        b_rad = coord.galactic.b.radian

        # changing from [0:2pi] to [-pi:pi]
        if (ra_rad > numpy.pi):
            ra_rad -= 2.0 * numpy.pi
        if (l_rad > numpy.pi):
            l_rad -= 2.0 * numpy.pi

        # appending data to numpy arrays
        data_hr   = numpy.append (data_hr, hr)
        data_ra   = numpy.append (data_ra, ra_rad)
        data_dec  = numpy.append (data_dec, dec_rad)
        data_l    = numpy.append (data_l, l_rad)
        data_b    = numpy.append (data_b, b_rad)
        data_Vmag = numpy.append (data_Vmag, Vmag)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection="hammer")

# axes
ax.grid ()
ax.set_title ('Bright Star Catalogue', loc='right')
ax.set_xlabel ('Galactic longitude')
ax.set_ylabel ('Galactic latitude')

# plotting data
size = (6.5 - data_Vmag) * 5.0
ax.scatter (data_l, data_b, marker='o', s=size, c='b', alpha=0.3)

# saving figure to files
fig.savefig (file_output, dpi=225, bbox_inches="tight")
