#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 08:06:52 (CST) daisuke>
#

# importing shutil module
import shutil

# importing pathlib module
import pathlib

# source file
file_source      = 'pi_1000.txt'

# destination file
file_destination = 'pi_1000_2.txt'

# making pathlib objects
path_source      = pathlib.Path (file_source)
path_destination = pathlib.Path (file_destination)

# existence check of file "pi_1000.txt"
if (path_source.exists ()):
    print (f'file "{file_source}" exists.')
else:
    print (f'file "{file_source}" DOES NOT exist.')

# existence check of file "pi_1000_2.txt"
if (path_destination.exists ()):
    print (f'file "{file_destination}" exists.')
else:
    print (f'file "{file_destination}" DOES NOT exist.')
    
# printing status
print (f'now, copying file from {file_source} to {file_destination}...')

# copying file
shutil.copy2 (file_source, file_destination)

# printing status
print (f'finished copying file from {file_source} to {file_destination}!')

# existence check of file "pi_1000.txt"
if (path_source.exists ()):
    print (f'file "{file_source}" exists.')
else:
    print (f'file "{file_source}" DOES NOT exist.')

# existence check of file "pi_1000_2.txt"
if (path_destination.exists ()):
    print (f'file "{file_destination}" exists.')
else:
    print (f'file "{file_destination}" DOES NOT exist.')

# printing status
print (f'now, removing file {file_destination}...')

# removing file "pi_1000_2.txt"
path_destination.unlink ()

# printing status
print (f'finished removing file {file_destination}!')

# existence check of file "pi_1000.txt"
if (path_source.exists ()):
    print (f'file "{file_source}" exists.')
else:
    print (f'file "{file_source}" DOES NOT exist.')

# existence check of file "pi_1000_2.txt"
if (path_destination.exists ()):
    print (f'file "{file_destination}" exists.')
else:
    print (f'file "{file_destination}" DOES NOT exist.')

# printing status
print (f'now, copying file from {file_source} to {file_destination}...')

# copying file again using pathlib objects
shutil.copy2 (path_source, path_destination)

# printing status
print (f'finished copying file from {file_source} to {file_destination}!')

# existence check of file "pi_1000.txt"
if (path_source.exists ()):
    print (f'file "{file_source}" exists.')
else:
    print (f'file "{file_source}" DOES NOT exist.')

# existence check of file "pi_1000_2.txt"
if (path_destination.exists ()):
    print (f'file "{file_destination}" exists.')
else:
    print (f'file "{file_destination}" DOES NOT exist.')
