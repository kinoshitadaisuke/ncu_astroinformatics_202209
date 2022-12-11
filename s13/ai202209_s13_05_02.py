#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/11 22:44:58 (CST) daisuke>
#

# importing datetime module
import datetime

# importing pathlib module
import pathlib

# importing numpy module
import numpy

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg

# data file
file_data = 'comets.data'

# directory to store PNG files
dir_png = 'comets'

# making directory if it does not exist
p_png = pathlib.Path (dir_png)
p_png.mkdir (mode=0o755, exist_ok=True)

# counter
i = 0

# number of major bodies
n_major = 10
# number of minor bodies
n_minor = 7

# opening data file
with open (file_data, 'r') as fh:
    # reading data line-by-line
    for line in fh:
        # if the line starts with '#', then skip
        if (line[0] == '#'):
            continue
        # splitting data
        records = line.split ('|')
        # JD
        jd = float (records[0])
        # date/time
        t          = records[1]
        t_datetime = datetime.datetime.fromisoformat (t)
        YYYY       = t_datetime.year

        # PNG file name
        file_png = "%s/%04d.png" % (dir_png, i)
        
        # making objects "fig" and "canvas"
        fig    = matplotlib.figure.Figure ()
        canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)

        # making object "ax"
        ax = fig.add_subplot (121)

        # labels
        ax.set_xlabel ('X [au]')
        ax.set_ylabel ('Y [au]')

        # axes
        ax.set_xlim (-35.0, 35.0)
        ax.set_ylim (-35.0, 35.0)
        ax.set_aspect('equal')
        ax.grid ()
        ax.set_xticks (numpy.linspace (-30, 30, 7))
        ax.set_yticks (numpy.linspace (-30, 30, 7))

        for j in ( range (2, n_major + n_minor + 2) ):
            xyz = records[j].split (',')
            x = float (xyz[0])
            y = float (xyz[1])
            z = float (xyz[2])
            if (j == 2):
                sun, = ax.plot (x, y, color='yellow', linestyle='None', \
                                marker='o', markersize=10, label='Sun')
            elif (j == 3):
                mercury, = ax.plot (x, y, color='blue', linestyle='None', \
                                   marker='o', markersize=2, label='Mercury')
            elif (j == 4):
                venus, = ax.plot (x, y, color='gold', linestyle='None', \
                                  marker='o', markersize=3, label='Venus')
            elif (j == 5):
                earth, = ax.plot (x, y, color='green', linestyle='None', \
                                  marker='o', markersize=3, label='Earth')
            elif (j == 6):
                mars, = ax.plot (x, y, color='red', linestyle='None', \
                                 marker='o', markersize=2, label='Mars')
            elif (j == 7):
                jupiter, = ax.plot (x, y, color='orange', linestyle='None', \
                                    marker='o', markersize=8, label='Jupiter')
            elif (j == 8):
                saturn, = ax.plot (x, y, color='brown', linestyle='None', \
                                   marker='o', markersize=7, label='Saturn')
            elif (j == 9):
                uranus, = ax.plot (x, y, color='lime', linestyle='None', \
                                   marker='o', markersize=6, label='Uranus')
            elif (j == 10):
                neptune, = ax.plot (x, y, color='indigo', linestyle='None', \
                                    marker='o', markersize=6, label='Neptune')
            elif (j == 11):
                pluto, = ax.plot (x, y, color='slategrey', linestyle='None',
                                  marker='o', markersize=2, label='Pluto')
            else:
                comets, = ax.plot (x, y, color='aqua', linestyle='None',
                                   marker='^', markersize=2,
                                   label='comets')

        # showing legend and title
        ax.legend (bbox_to_anchor=(0.0, -0.3), loc='upper left', \
                   frameon=False, ncol=2, \
                   handles=[sun, mercury, venus, earth, mars, jupiter])
        title_name = "Comets (Year %04d)" % (YYYY)
        ax.set_title (title_name)

        # making object "ax"
        ax = fig.add_subplot (222)

        # labels
        ax.set_xlabel ('X [au]')
        ax.set_ylabel ('Z [au]')

        # axes
        ax.set_xlim (-35.0, 35.0)
        ax.set_ylim (-15, 15)
        ax.set_aspect('equal')
        ax.grid ()
        ax.set_xticks (numpy.linspace (-30, 30, 7))
        ax.set_yticks (numpy.linspace (-15, 15, 7))

        for j in ( range (2, n_major + n_minor + 2) ):
            xyz = records[j].split (',')
            x = float (xyz[0])
            y = float (xyz[1])
            z = float (xyz[2])
            if (j == 2):
                sun, = ax.plot (x, z, color='yellow', linestyle='None', \
                                marker='o', markersize=10, label='Sun')
            elif (j == 3):
                mercury, = ax.plot (x, z, color='blue', linestyle='None', \
                                   marker='o', markersize=2, label='Mercury')
            elif (j == 4):
                venus, = ax.plot (x, z, color='gold', linestyle='None', \
                                  marker='o', markersize=3, label='Venus')
            elif (j == 5):
                earth, = ax.plot (x, z, color='green', linestyle='None', \
                                  marker='o', markersize=3, label='Earth')
            elif (j == 6):
                mars, = ax.plot (x, z, color='red', linestyle='None', \
                                 marker='o', markersize=2, label='Mars')
            elif (j == 7):
                jupiter, = ax.plot (x, z, color='orange', linestyle='None', \
                                    marker='o', markersize=8, label='Jupiter')
            elif (j == 8):
                saturn, = ax.plot (x, z, color='brown', linestyle='None', \
                                   marker='o', markersize=7, label='Saturn')
            elif (j == 9):
                uranus, = ax.plot (x, z, color='lime', linestyle='None', \
                                   marker='o', markersize=6, label='Uranus')
            elif (j == 10):
                neptune, = ax.plot (x, z, color='indigo', linestyle='None', \
                                    marker='o', markersize=6, label='Neptune')
            elif (j == 11):
                pluto, = ax.plot (x, z, color='slategrey', linestyle='None',
                                  marker='o', markersize=2, label='Pluto')
            else:
                comets, = ax.plot (x, z, color='aqua', linestyle='None',
                                   marker='^', markersize=2,
                                   label='comets')

        # making object "ax"
        ax = fig.add_subplot (224)

        # labels
        ax.set_xlabel ('Y [au]')
        ax.set_ylabel ('Z [au]')

        # axes
        ax.set_xlim (-35.0, 35.0)
        ax.set_ylim (-15, 15)
        ax.set_aspect('equal')
        ax.grid ()
        ax.set_xticks (numpy.linspace (-30, 30, 7))
        ax.set_yticks (numpy.linspace (-15, 15, 7))

        for j in ( range (2, n_major + n_minor + 2) ):
            xyz = records[j].split (',')
            x = float (xyz[0])
            y = float (xyz[1])
            z = float (xyz[2])
            if (j == 2):
                sun, = ax.plot (y, z, color='yellow', linestyle='None', \
                                marker='o', markersize=10, label='Sun')
            elif (j == 3):
                mercury, = ax.plot (y, z, color='blue', linestyle='None', \
                                   marker='o', markersize=2, label='Mercury')
            elif (j == 4):
                venus, = ax.plot (y, z, color='gold', linestyle='None', \
                                  marker='o', markersize=3, label='Venus')
            elif (j == 5):
                earth, = ax.plot (y, z, color='green', linestyle='None', \
                                  marker='o', markersize=3, label='Earth')
            elif (j == 6):
                mars, = ax.plot (y, z, color='red', linestyle='None', \
                                 marker='o', markersize=2, label='Mars')
            elif (j == 7):
                jupiter, = ax.plot (y, z, color='orange', linestyle='None', \
                                    marker='o', markersize=8, label='Jupiter')
            elif (j == 8):
                saturn, = ax.plot (y, z, color='brown', linestyle='None', \
                                   marker='o', markersize=7, label='Saturn')
            elif (j == 9):
                uranus, = ax.plot (y, z, color='lime', linestyle='None', \
                                   marker='o', markersize=6, label='Uranus')
            elif (j == 10):
                neptune, = ax.plot (y, z, color='indigo', linestyle='None', \
                                    marker='o', markersize=6, label='Neptune')
            elif (j == 11):
                pluto, = ax.plot (y, z, color='slategrey', linestyle='None',
                                  marker='o', markersize=2, label='Pluto')
            else:
                comets, = ax.plot (y, z, color='aqua', linestyle='None',
                                   marker='^', markersize=2,
                                   label='comets')

        ax.legend (bbox_to_anchor=(0.0, -0.4), loc='upper left', \
                   frameon=False, ncol=2, \
                   handles=[saturn, uranus, neptune, pluto, comets])
        # saving the plot into a file
        fig.tight_layout ()
        fig.savefig (file_png, dpi=225)

        # increment
        i += 1
        if (i % 100 == 0):
            print (f"progress: {i}")
