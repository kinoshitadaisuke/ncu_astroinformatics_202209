#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 21:09:55 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_data = 'simple0.data'

# figure file name prefix
prefix_fig = 'simple0'

# counter
i = 0

# opening data file for reading
with open (file_data, 'r') as fh:
    # reading data file
    for line in fh:
        # skipping line if the line starts with '#'
        if (line[0] == '#'):
            continue
        # splitting line
        (time, star_x, star_y, star_z, planet_x, planet_y, planet_z) \
            = line.split ()
        # figure file name
        file_fig = f"{prefix_fig}_{i:08d}.png"

        # making objects "fig", "canvas", and "ax"
        fig    = matplotlib.figure.Figure ()
        canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
        ax     = fig.add_subplot (111)

        # labels
        ax.set_xlabel ('X [au]')
        ax.set_ylabel ('Y [au]')

        # axes
        ax.set_xlim (-2.0, +2.0)
        ax.set_ylim (-2.0, +2.0)
        ax.set_aspect ('equal')
        ax.grid ()

        # plotting location of star
        ax.plot (float (star_x), float (star_y), linestyle='None', \
                 marker='o', markersize=10, color='red', label='Star')

        # plotting location of planet
        ax.plot (float (planet_x), float (planet_y), linestyle='None', \
                 marker='o', markersize=3, color='blue', label='Planet')

        # title
        ax.set_title (f"Star and planet at {float (time):6.2f} day")

        # legend
        ax.legend (loc='upper right')
        
        # saving the plot into a file
        fig.savefig (file_fig, dpi=225)

        # incrementing counter
        i += 1
