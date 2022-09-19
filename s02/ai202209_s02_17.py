#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 07:46:22 (CST) daisuke>
#

# importing pathlib module
import pathlib

# file name
file_00 = 'ai202209_s02_00.py'

# making pathlib object
path_00 = pathlib.Path (file_00)

# existence check
exists_00 = path_00.exists ()
print (f'existence check:')
if (exists_00):
    print (f'  file "{file_00}" does exist.')
else:
    print (f'  file "{file_00}" does not exist.')

# printing parent, name, suffix, stem
print (f'parent, name, suffix, and stem:')
print (f'  parent of "{path_00}" = {path_00.parent}')
print (f'  name of "{path_00}"   = {path_00.name}')
print (f'  suffix of "{path_00}" = {path_00.suffix}')
print (f'  stem of "{path_00}"   = {path_00.stem}')

# finding directory contents of current working directory using .iterdir ()
path_cwd   = pathlib.Path ('.')
list_files = path_cwd.iterdir ()

# printing files in current working directory
print (f'files in current working directory:')
for file in sorted (list_files):
    print (f'  {file}')
    
# finding file information
file_pi = 'pi_1000.txt'
path_pi = pathlib.Path (file_pi)
info_pi = path_pi.stat ()

# printing information of file
print (f'file information of "pi_1000.txt":')
print (f'  file mode         : {oct (info_pi.st_mode)}')
print (f'  file size         : {info_pi.st_size} bytes')
print (f'  last modification : {info_pi.st_mtime} sec from 01/Jan/1970')

# opening file 'pi_1000.txt'
with path_pi.open () as fh:
    # reading file
    data = fh.read ()

# printing content of file 'pi_1000.txt'
print (f'---------- {file_pi} ----------')
print (data)
print (f'---------- {file_pi} ----------')
