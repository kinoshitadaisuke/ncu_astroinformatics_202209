#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 19:23:36 (CST) daisuke>
#

# importing json module
import json

# JSON file name
file_json = 'exoplanet.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON file
    data = json.load (fh)

# printing the information of exoplanet hosted by Kepler-90
for i in range (len (data)):
    if (data[i]['star_name'] == 'Kepler-90'):
        print (f"Host star: {data[i]['star_name']}")
        print (f"  {data[i]['# name']:12s}:", \
               f" M={data[i]['mass']},", \
               f" P={data[i]['orbital_period']:8.4f},", \
               f" a={data[i]['semi_major_axis']:8.4f},", \
               f" detect={data[i]['detection_type']}")
