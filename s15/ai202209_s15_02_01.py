#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 19:02:52 (CST) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing keys of the data
for key in data[0].keys ():
    print (f"{key}")
