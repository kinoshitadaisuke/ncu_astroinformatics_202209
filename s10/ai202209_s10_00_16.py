#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/20 23:17:59 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s10_00_16.png'

# units
u_deg = astropy.units.degree

# date/time
date = astropy.time.Time ('2023-01-01 00:00:00')

# number of asteroids to get position
n_asteroids = 3000

# making empty numpy arrays for storing data
data_ra_deg  = numpy.array ([])
data_dec_deg = numpy.array ([])

# processing for each asteroid
for i in range (1, n_asteroids + 1):
    # set-up a query for JPL Horizons
    query = astroquery.jplhorizons.Horizons (id=f"{i}", \
                                             id_type='smallbody', \
                                             epochs=date.jd)

    # fetching ephemeris of asteroid
    eph = query.ephemerides ()

    # priting RA and Dec of asteroid
    print (f"{eph['targetname'][0]:24s}:" \
           + f" (RA, Dec) = ({eph['RA'][0]:8.4f} deg," \
           + f" {eph['DEC'][0]:+8.4f} deg)")

    # RA in deg
    ra_deg = eph['RA'][0]
    if (ra_deg > 180.0):
        ra_deg -= 360.0

    # Dec in deg
    dec_deg = eph['DEC'][0]

    # appending data to numpy arrays
    data_ra_deg   = numpy.append (data_ra_deg, ra_deg)
    data_dec_deg = numpy.append (data_dec_deg, dec_deg)

# ecliptic plane
ecl_lon = numpy.linspace (0.001, 359.999, 1000) * u_deg
ecl_lat = numpy.zeros (1000) * u_deg
ecl_coord = astropy.coordinates.GeocentricMeanEcliptic (lon=ecl_lon, \
                                                        lat=ecl_lat, \
                                                        obstime=date)
ecl_ra  = ecl_coord.transform_to (astropy.coordinates.ICRS) \
                   .ra.wrap_at (180.0 * u_deg).radian
ecl_dec = ecl_coord.transform_to (astropy.coordinates.ICRS).dec.radian

# galactic plane
gal_lon = numpy.linspace (0.001, 359.999, 1000) * u_deg
gal_lat = numpy.zeros (1000) * u_deg
gal_coord = astropy.coordinates.Galactic (l=gal_lon, \
                                          b=gal_lat)
gal_ra  = gal_coord.transform_to (astropy.coordinates.ICRS) \
                   .ra.wrap_at (180.0 * u_deg).radian
gal_dec = gal_coord.transform_to (astropy.coordinates.ICRS).dec.radian

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111, projection='hammer')

# axes
ax.grid ()
ax.set_xlabel ('Right Ascension [deg]')
ax.set_ylabel ('Declination [deg]')

# title
text_title = f"Distribution of asteroids"
ax.set_title (text_title, loc='right')

# plotting data
density = ax.hexbin (numpy.deg2rad (data_ra_deg), numpy.deg2rad (data_dec_deg), \
                     gridsize=90, cmap=matplotlib.cm.plasma)
fig.colorbar (density, ax=ax, spacing='uniform', extend='both')

# saving file
fig.savefig (file_output, dpi=225)
