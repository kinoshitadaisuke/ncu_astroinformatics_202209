#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/10 02:28:44 (CST) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.time
import astropy.units

# importing astroquery module
import astroquery.jplhorizons

#
# command-line argument analysis
#

# constructing parser object
desc   = "ephemerides of solar system objects"
parser = argparse.ArgumentParser (description=desc)

# choices
choices_idtype = [None, 'smallbody', 'designation', \
                  'name', 'asteroid_name', 'comet_name']

# adding arguments
parser.add_argument ('-t', '--idtype', type=str, choices=choices_idtype, \
                     default=None, help='ID type (default: None)')
parser.add_argument ('-i', '--targetid', type=str, default='1', \
                     help='ID of target body (default: 1)')
parser.add_argument ('-l', '--location', type=str, default='Sun', \
                     help='location of observer (default: Sun)')
parser.add_argument ('-s', '--start', type=str, \
                     default='2000-01-01T12:00:00', \
                     help='start date/time (default: 2001-01-01T12:00:00)')
parser.add_argument ('-e', '--end', type=str, \
                     default='2000-01-02T12:00:00', \
                     help='start date/time (default: 2001-01-01T12:00:00)')
parser.add_argument ('-d', '--timestep', type=str, \
                     default='1h', \
                     help='time step (e.g. 1h, 2d, 3y) (default: 1h)')

# parsing arguments
args = parser.parse_args ()

#
# input parameters
#

# ID type
idtype = args.idtype

# target body
target = args.targetid

# location
location = args.location

# start date/time
datetime_start = args.start

# end date/time
datetime_end = args.end

# time step
timestep = args.timestep

# date/time
t_start = astropy.time.Time (datetime_start, scale='utc', format='isot')
t_end   = astropy.time.Time (datetime_end, scale='utc', format='isot')

# making a query to NASA/JPL Horizons system
obj = astroquery.jplhorizons.Horizons (id_type=idtype, id=target, \
                                       location=location, \
                                       epochs={'start': t_start.isot, \
                                               'stop': t_end.isot, \
                                               'step': timestep})

# getting orbital elements
elements = obj.elements ()

# printing orbital elements
print (f"{elements[0]['targetname']}")
for ele in elements:
    print (f"{ele['datetime_str']:17s}", \
           f"{ele['a']:14.8f} {ele['e']:10.8f} {ele['incl']:12.8f}")
