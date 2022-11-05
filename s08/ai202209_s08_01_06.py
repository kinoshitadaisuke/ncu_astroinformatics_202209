#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/05 19:43:20 (CST) daisuke>
#

# importing numpy module
import numpy

# importing astropy module
import astropy.coordinates
import astropy.time
import astropy.units

# importing astroplan module
import astroplan

# importing matplotlib module
import matplotlib.figure
import matplotlib.backends.backend_agg
import matplotlib.dates

# units
u_m   = astropy.units.m
u_day = astropy.units.day

# using "DE440" for solar system ephemeris
astropy.coordinates.solar_system_ephemeris.set ('de440')

# output file name
file_output = 'sun_maxalt_world.png'

# locations
observatories = {
    'uppsala': {
        'longitude': '+17d38m13.1s',
        'latitude' : '+59d51m35.5s',
        'height'   : 37.9 * u_m,
        'name'     : 'Uppsala',
    },
    'greenwich': {
        'longitude': '-0d00m05s',
        'latitude' : '+51d28m40s',
        'height'   : 45.0 * u_m,
        'name'     : 'Greenwich',
    },
    'vatican': {
        'longitude': '+12d39m02s',
        'latitude' : '+41d44m50s',
        'height'   : 430.0 * u_m,
        'name'     : 'Vatican',
    },
    'palomar': {
        'longitude': '-116d51m54s',
        'latitude' : '+33d21m23s',
        'height'   : 1712.0 * u_m,
        'name'     : 'Palomar',
    },
    'chiangmai': {
        'longitude': '+98d29m12s',
        'latitude' : '+18d35m26s',
        'height'   : 2457.0 * u_m,
        'name'     : 'Chiang-Mai',
    },
    'paranal': {
        'longitude': '-70d24m15s',
        'latitude' : '-24d37m38s',
        'height'   : 2635.0 * u_m,
        'name'     : 'Paranal',
    },
    'sidingspring': {
        'longitude': '+149d03m52s',
        'latitude' : '-31d16m24s',
        'height'   : 1165.0 * u_m,
        'name'     : 'Siding Spring',
    },
}

# making fig, canvas, and ax objects
fig    = matplotlib.figure.Figure ()
canvas = matplotlib.backends.backend_agg.FigureCanvasAgg (fig)
ax     = fig.add_subplot (111)

# labels
ax.set_xlabel ('Date')
ax.set_ylabel ('Altitude Angle [deg]')
ax.set_title ('Change of Maximum Altitude of the Sun')

# calculations for each observatory site
for site in observatories.keys ():
    # printing status
    print (f'Now, calculating for {observatories[site]["name"]}...')
    
    # empty numpy arrays for plotting
    dates = numpy.array ([])
    alts  = numpy.array ([])

    # making a location object using Astropy
    location \
        = astropy.coordinates.EarthLocation.from_geodetic \
        (lon=observatories[site]['longitude'], \
         lat=observatories[site]['latitude'], \
         height=observatories[site]['height'])

    # making an observer object
    observer = astroplan.Observer (location=location, name=site)

    # initial guess of local noon (501 days from 01/Nov/2022)
    time_guess = astropy.time.Time ('2022-11-01 05:00:00', \
                                    format='iso', scale='utc') \
                                    + numpy.linspace (0.0, 500.0, 501) \
                                    * u_day

    # calculation of altitude angle at local noon
    for i in range (len (time_guess)):
        # local apparent solar noon
        noon = observer.noon (time_guess[i], which='nearest', \
                              n_grid_points=200)

        # getting position of the Sun
        sun = astropy.coordinates.get_body ('sun', noon, location=location)

        # conversion from equatorial into horizontal
        altaz = astropy.coordinates.AltAz (obstime=noon, location=location)
        sun_altaz = sun.transform_to (altaz)

        # appending data to numpy arrays
        dates = numpy.append (dates, noon.plot_date)
        alts  = numpy.append (alts, sun_altaz.alt.value)


    # plotting data
    ax.plot (dates, alts, linestyle='-', linewidth=3.0, \
             label=observatories[site]['name'])

# legend
ax.legend (loc='upper right')

# grid
ax.grid ()

# ticks
months     = matplotlib.dates.MonthLocator ()
days       = matplotlib.dates.DayLocator ()
months_fmt = matplotlib.dates.DateFormatter ('%Y-%m-%d')
ax.xaxis.set_major_locator (months)
ax.xaxis.set_major_formatter (months_fmt)
ax.xaxis.set_minor_locator (days)

# formatting labels
fig.autofmt_xdate()

# saving file
fig.savefig (file_output, dpi=225)
