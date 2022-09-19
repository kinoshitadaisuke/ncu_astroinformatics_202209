#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 07:54:44 (CST) daisuke>
#

# importing pathlib module
import pathlib

# making pathlib object
path_cwd = pathlib.Path ('.')

# finding files recursively using .glob () method
list_files = path_cwd.glob ('**/*')

# printing files in current working directory and its sub-directories
print (f'files in current working directory and its sub-directories:')
for file in sorted (list_files):
    print (f'  {file}')
