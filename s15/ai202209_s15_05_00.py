#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 23:02:28 (CST) daisuke>
#

# importing pathlib module
import pathlib

# list of data files
files = pathlib.Path ('.').glob ('sne-*/*.json')

# printing file names
for file in sorted (files):
    print (file)
