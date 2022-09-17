#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/17 21:00:23 (CST) daisuke>
#

# importing os module
import os

#
# printing current working directory
#

# knowing where you are now
cwd = os.getcwd ()

# printing where you are now
print (f'current working directory = {cwd}')

#
# printing files at current working directory
#

# getting a list of files at current working directory
list_files = os.listdir ()

# printing list of files at current working directory
print (f'list of files at current working directory:')
for file in sorted (list_files):
    print (f'  {file}')

#
# the other way to print files at current working directory
#

# the other way to get a list of files at current working directory
list_files2 = os.scandir ()

# printing list of files at current working directory
print (f'list of files at current working directory:')
for file in sorted (list_files2, key=lambda x: x.name):
    print (f'  {file.name}')
    
#
# printing information about a file
#

# getting information about a file
filename = 'ai202209_s02_00.py'
statinfo = os.stat (filename)

# printing size of file
print (f'information of file "{filename}":')
print (f'  size : {statinfo.st_size} byte')
