#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/18 11:08:41 (CST) daisuke>
#

# importing pathlib module
import pathlib

# file names
list_filename = ['MPCORB.DAT', 'MPCORB.DAT.gz', \
                 'mpcorb.dat', 'mpcorb.data', \
                 'mpcorb.dat.gz', 'mpcorb.data.gz']

# existence check of files
for filename in list_filename:
    # making pathlib object
    path_mpcorb = pathlib.Path (filename)
    # existence check
    existence = path_mpcorb.exists ()
    # printing result of existence check
    if (existence):
        print (f"{filename:24s} : exists")
    else:
        print (f"{filename:24s} : DOES NOT exist")
