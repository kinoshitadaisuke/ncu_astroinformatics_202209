#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/31 00:27:19 (CST) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.units
import astropy.coordinates
import astropy.wcs

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# object name
object_name = 'M66'

# survey name
survey = 'DSS2 Red'

# field-of-view
fov_arcmin = 15.0
fov_arcsec = fov_arcmin * 60.0
npixel     = int (fov_arcsec)

# FITS file name
file_fits = 'm66.fits'

# PNG file name
file_png = 'm66.png'

# colour map
cmap = 'bone'

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# name resolver
query_result = astroquery.simbad.Simbad.query_object (object_name)

# coordinate from Simbad
ra_str  = query_result['RA'][0]
dec_str = query_result['DEC'][0]

# making SkyCoord object of astropy
coord = astropy.coordinates.SkyCoord (ra_str, dec_str, frame='icrs', \
                                      unit=(u_ha, u_deg) )
(ra, dec) = coord.to_string (style='hmsdms').split ()

# printing result
print (f'Target name: "{object_name}"')
print (f'  RA  = {ra}')
print (f'  Dec = {dec}')

# getting a list of images
list_image = astroquery.skyview.SkyView.get_image_list (position=coord, \
                                                        survey=survey)

print ("images =", list_image)

# getting images
images = astroquery.skyview.SkyView.get_images (position=coord, \
                                                survey=survey, \
                                                pixels=npixel)

# image
image  = images[0]
header = image[0].header
data   = image[0].data
print (image.info ())

# writing FITS file
print (f'Writing a FITS file "{file_fits}"...')
hdu = astropy.io.fits.PrimaryHDU (data=data, header=header)
hdu.writeto (file_fits)
print (f'Done!')

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

# plotting image
im = ax.imshow (image, origin='lower', cmap=cmap)
fig.colorbar (im)

# saving file
print (f'{file_fits} ==> {file_png}')
fig.savefig (file_png, dpi=450)
