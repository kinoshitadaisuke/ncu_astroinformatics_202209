#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/30 22:43:46 (CST) daisuke>
#

# importing astropy module
import astropy.io.fits
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad
import astroquery.skyview

# object name
object_name = 'M3'

# survey name
survey = 'DSS2 Red'

# field-of-view
fov_arcmin = 30.0
fov_arcsec = fov_arcmin * 60.0
npixel     = int (fov_arcsec)

# output file name
file_output = 'm3.fits'

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
print (f'Writing a FITS file "{file_output}"...')
hdu = astropy.io.fits.PrimaryHDU (data=data, header=header)
hdu.writeto (file_output)
print (f'Done!')
