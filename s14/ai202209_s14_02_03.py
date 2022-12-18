#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/18 18:51:18 (CST) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.io.fits
import astropy.wcs

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# cmap
list_cmap = [
    'viridis', 'plasma', 'inferno', 'magma', 'cividis', 'gray', \
    'bone', 'pink', 'spring', 'summer', 'autumn', 'winter', \
    'cool', 'hot', 'copper', 'hsv', 'ocean', 'terrain', 'gnuplot', \
    'rainbow', 'turbo'
]

# command-line argument analysis
parser = argparse.ArgumentParser (description='conversion from FITS to PNG')
parser.add_argument ('-i', '--input', help='name of input file')
parser.add_argument ('-o', '--output', help='name of output file')
parser.add_argument ('-n', '--name', help='name of the object')
parser.add_argument ('-c', '--cmap', choices=list_cmap, default='gray', \
                     help='choice of cmap (default: gray)')
args = parser.parse_args ()

# target object name, file names
name        = args.name
cmap        = args.cmap
file_input  = args.input
file_output = args.output

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
ax.set_title (name)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# plotting image
norm = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.AsinhStretch () )
im = ax.imshow (image, origin='lower', cmap=cmap, norm=norm)
fig.colorbar (im)

# saving file
fig.savefig (file_output, dpi=225)
