#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/02 22:08:09 (CST) daisuke>
#

# importing argparse module
import argparse

# importing pathlib module
import pathlib

#
# command-line argument analysis
#

# constructing parser object
desc = f"existence check of files"
parser = argparse.ArgumentParser (description=desc)

# adding options
parser.add_argument ('files', type=str, nargs='+', \
                     help=f"files for existence check")

# analysis of command-line arguments
args = parser.parse_args ()

# values of input parameters
list_files = args.files

#
# existence check of files
#

# processing each file
for filename in list_files:
    # making pathlib object
    path_file = pathlib.Path (filename)
    # existence check
    existence = path_file.exists ()
    # printing result
    if (existence):
        print (f"the file '{filename}' exists!")
    else:
        print (f"the file '{filename}' does not exist!")
