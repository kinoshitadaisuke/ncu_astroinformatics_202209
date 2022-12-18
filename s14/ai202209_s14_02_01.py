#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/18 12:44:27 (CST) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# input file name
file_input = 'm1.fits'

# output file name
file_output = 'm1.png'

# reading FITS file
with astropy.io.fits.open (file_input) as hdu:
    # reading header
    header = hdu[0].header
    # WCS information
    wcs = astropy.wcs.WCS (header)
    # reading image
    image  = hdu[0].data

# making objects "fig", "canvas", and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (file_input)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting image
norm = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.AsinhStretch () )
im = ax.imshow (image, origin='lower', cmap='bone', norm=norm)
fig.colorbar (im)

# saving file
fig.savefig (file_output, dpi=225)
