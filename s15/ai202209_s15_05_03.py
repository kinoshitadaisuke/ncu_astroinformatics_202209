#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 23:43:42 (CST) daisuke>
#

# importing pathlib module
import pathlib

# importing json module
import json

# importing scipy module
import scipy.constants

# constants
c = scipy.constants.c

# list of data files
files = pathlib.Path ('.').glob ('sne-*/*.json')

# key names
key_type       = 'claimedtype'
key_distance   = 'lumdist'
key_velocity   = 'velocity'
key_redshift   = 'redshift'
key_spectra    = 'spectra'
key_photometry = 'photometry'
key_maxabsmag  = 'maxvisualabsmag'
key_maxappmag  = 'maxvisualappmag'
key_maxband    = 'maxvisualband'

# processing each file
for file in sorted (files):
    # opening file
    with open (file, 'r') as fh:
        # reading JSON data from file
        data = json.load (fh)

    # checking all the objects in JSON file
    for obj in data:
        # skip if type is not known
        if not (key_type in data[obj]):
            continue
        # skip if supernova is not type-Ia
        if not (data[obj][key_type][0]['value'] == 'Ia'):
            continue
        # skip if distance is not known
        if not (key_distance in data[obj]):
            continue
        # skip if velocity is not known
        if not (key_velocity in data[obj]):
            continue
        # skip if redshift is not known
        if not (key_redshift in data[obj]):
            continue
        # skip if spectrum is missing
        if not (key_spectra in data[obj]):
            continue
        # skip if photometry is missing
        if not (key_photometry in data[obj]):
            continue
        # skip if max abs mag is missing
        if not (key_maxabsmag in data[obj]):
            continue
        # skip if max app mag is missing
        if not (key_maxappmag in data[obj]):
            continue
        # skip if max visual band is missing
        if not (key_maxband in data[obj]):
            continue
        # skip if max visual band is not B-band
        if not (data[obj][key_maxband][0]['value'] == 'B'):
            continue
        
        # distance, velocity, and redshift, ...
        distance_str  = data[obj][key_distance][0]['value']
        velocity_str  = data[obj][key_velocity][0]['value']
        redshift_str  = data[obj][key_redshift][0]['value']
        maxabsmag_str = data[obj][key_maxabsmag][0]['value']
        maxappmag_str = data[obj][key_maxappmag][0]['value']

        # conversion from string to float
        distance  = float (distance_str)
        velocity  = float (velocity_str)
        redshift  = float (redshift_str)
        maxabsmag = float (maxabsmag_str)
        maxappmag = float (maxappmag_str)

        # distance modulus
        distmod = maxappmag - maxabsmag
        dist_from_distmod = 10**(distmod / 5.0 + 1.0) * 10**-6

        # velocity
        v_from_z = ( (redshift + 1.0)**2 - 1.0 ) \
            / ( (redshift + 1.0)**2 + 1.0 ) * c * 10**-3
        
        # printing data
        print (f"{distance:15.8f} {dist_from_distmod:15.8f}", \
               f" {redshift:15.8f} {v_from_z:15.8f} # {obj}")
