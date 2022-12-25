#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 23:21:30 (CST) daisuke>
#

# importing json module
import json

# file name
file_json = 'sne-2005-2009/2MASSJ02051081-0447150.json'

# opening file
with open (file_json, 'r') as fh:
    # reading JSON data from file
    data = json.load (fh)

# printing data
for obj in data:
    print ("obj =", obj)
    for key in data[obj]:
        print ("  %-12s ==> %s" % (key, data[obj][key]) )
