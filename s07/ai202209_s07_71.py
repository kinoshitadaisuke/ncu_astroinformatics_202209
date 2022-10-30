#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/31 00:26:18 (CST) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.units
import astropy.coordinates
import astropy.visualization
import astropy.wcs

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# object name
object_name = 'M57'

# FITS file name
file_fits = 'm57.fits'

# PNG file name
file_png = 'm57_norm1.png'

# colour map
cmap = 'viridis'

# opening FITS file
with astropy.io.fits.open (file_fits) as hdu_list:
    # printing HDU information
    print (hdu_list.info ())
    
    # reading FITS header, WCS information, and image data
    header = hdu_list[0].header
    wcs    = astropy.wcs.WCS (header)
    image  = hdu_list[0].data

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection=wcs)

# axes
ax.set_title (object_name)
ax.set_xlabel ('Right Ascension')
ax.set_ylabel ('Declination')

# normalisation
norm \
    = astropy.visualization.mpl_normalize.ImageNormalize \
    ( stretch=astropy.visualization.SinhStretch (0.15) )

# plotting image
im = ax.imshow (image, origin='lower', cmap=cmap, norm=norm)
fig.colorbar (im)

# saving file
print (f'{file_fits} ==> {file_png}')
fig.savefig (file_png, dpi=450)
