#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/20 13:52:49 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.time

# importing astroquery module
import astroquery.jplhorizons

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# output file name
file_output = 'ai202209_s10_00_10.png'

# date/time
date = astropy.time.Time ('2023-01-01 00:00:00')

# number of asteroids to get position
n_asteroids = 100

# making empty numpy arrays for storing data
data_ra_hr   = numpy.array ([])
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

    # RA in hour
    ra_hr = eph['RA'][0] / 15.0

    # Dec in deg
    dec_deg = eph['DEC'][0]

    # appending data to numpy arrays
    data_ra_hr   = numpy.append (data_ra_hr, ra_hr)
    data_dec_deg = numpy.append (data_dec_deg, dec_deg)

# making objects "fig" and "ax"
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# axes
ax.grid ()
ax.set_xlim (24.0, 0.0)
ax.set_ylim (-90.0, +90.0)
ax.set_xticks (numpy.linspace (0, 24, 9))
ax.set_yticks (numpy.linspace (-90, 90, 7))
ax.set_xlabel ('Right Ascension [hr]')
ax.set_ylabel ('Declination [deg]')

# title
text_title = f"Distribution of asteroids on {date}"
ax.set_title (text_title)

# plotting data
ax.plot (data_ra_hr, data_dec_deg, \
         linestyle='None', marker='o', color='b', markersize=3, alpha=0.3, \
         label='Asteroids')
ax.legend ()

# saving file
fig.savefig (file_output, dpi=225)
