#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 08:13:02 (CST) daisuke>
#

# importing shutil module
import shutil

# location of an executable named 'python'
location_python = shutil.which ('python')

# printing location of 'python'
print (f'location of "python"    = {location_python}')

# location of an executable named 'python2'
location_python2 = shutil.which ('python2')

# printing location of 'python2'
print (f'location of "python2"   = {location_python2}')

# location of an executable named 'python2.7'
location_python27 = shutil.which ('python2.7')

# printing location of 'python2.7'
print (f'location of "python2.7" = {location_python27}')

# location of an executable named 'python3'
location_python3 = shutil.which ('python3')

# printing location of 'python3'
print (f'location of "python3"   = {location_python3}')

# location of an executable named 'python3.9'
location_python39 = shutil.which ('python3.9')

# printing location of 'python3.9'
print (f'location of "python3.9" = {location_python39}')

# location of an executable named 'python4'
location_python4 = shutil.which ('python4')

# printing location of 'python4'
print (f'location of "python4"   = {location_python4}')
