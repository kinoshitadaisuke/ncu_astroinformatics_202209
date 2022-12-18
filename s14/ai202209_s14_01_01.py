#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/18 10:45:13 (CST) daisuke>
#

# importing argparse module
import argparse

# importing astropy module
import astropy.units
import astropy.coordinates

# importing astroquery module
import astroquery.simbad

# units
u_ha  = astropy.units.hourangle
u_deg = astropy.units.deg

# command-line argument analysis
parser = argparse.ArgumentParser (description='name resolver')
parser.add_argument ('target', type=str, nargs='+', help='target name')
args = parser.parse_args ()

# list of target object names
list_target = args.target

# processing for each target
for target in list_target:
    # name resolver
    query_result = astroquery.simbad.Simbad.query_object (target)

    # coordinate from Simbad
    ra_str  = query_result['RA'][0]
    dec_str = query_result['DEC'][0]

    # using skycoord of astropy
    coord = astropy.coordinates.SkyCoord (ra_str, dec_str, frame='icrs', \
                                          unit=(u_ha, u_deg) )

    # coordinate in decimal degree
    ra_deg  = coord.ra.deg
    dec_deg = coord.dec.deg

    # coordinate in radian
    ra_rad  = coord.ra.rad
    dec_rad = coord.dec.rad

    # coordinate in hexagesimal format
    ra_str  = f"{int (coord.ra.hms.h):02d}h" \
        + f"{int (coord.ra.hms.m):02d}m" \
        + f"{coord.ra.hms.s:06.3f}s"
    if (dec_deg < 0.0):
        dec_str = f"-{int (coord.dec.dms.d * (-1)):02d}d" \
            + f"{int (coord.dec.dms.m * (-1)):02d}m" \
            + f"{coord.dec.dms.s * (-1):05.2f}s"
    else:
        dec_str = f"+{int (coord.dec.dms.d):02d}d" \
            + f"{int (coord.dec.dms.m):02d}m" \
            + f"{coord.dec.dms.s:05.2f}s"
        
    # printing result
    print (f"target: {target}")
    print (f" RA  = {ra_str:13s} = {ra_deg:10.6f} deg = {ra_rad:11.8f} rad")
    print (f" Dec = {dec_str:13s} = {dec_deg:+10.6f} deg = {dec_rad:+10.8f} rad")
