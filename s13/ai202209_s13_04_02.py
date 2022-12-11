#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 21:42:41 (CST) daisuke>
#

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file name
file_data = 'simple1.data'

# figure file name prefix
prefix_fig = 'simple1'

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
        (time, star1_x, star1_y, star1_z, star2_x, star2_y, star2_z) \
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
        ax.set_xlim (-25.0, +25.0)
        ax.set_ylim (-25.0, +25.0)
        ax.set_aspect ('equal')
        ax.grid ()

        # plotting location of star
        ax.plot (float (star1_x), float (star1_y), linestyle='None', \
                 marker='o', markersize=10, color='red', label='Star 1')

        # plotting location of planet
        ax.plot (float (star2_x), float (star2_y), linestyle='None', \
                 marker='o', markersize=5, color='blue', label='Star 2')

        # title
        ax.set_title (f"A binary system at {float (time):6.2f} yr")

        # legend
        ax.legend (loc='upper right')
        
        # saving the plot into a file
        fig.savefig (file_fig, dpi=225)

        # incrementing counter
        i += 1
