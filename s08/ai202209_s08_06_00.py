#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/07 00:55:47 (CST) daisuke>
#

# importing astropy module
import astropy.units

# importing astroplan module
import astroplan
import astroplan.plots

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# output file name
file_output = 'findingchart_00.png'

# units
unit_arcmin = astropy.units.arcmin

# field-of-view
fov = 20.0 * unit_arcmin

# target object
m101 = astroplan.FixedTarget.from_name ('M101')

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# image
ax, hdu = astroplan.plots.plot_finder_image (m101, fov_radius=fov, ax=ax)

# saving the image to file
fig.savefig (file_output, dpi=225)
