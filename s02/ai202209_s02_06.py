#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 08:17:26 (CST) daisuke>
#

# importing sys module
import sys

#
# command-line arguments
#

# receiving command-line arguments
args = sys.argv

# printing command-line arguments
print (f'Command-line arguments:')
for i in range (len (args)):
    print (f'  sys.argv[{i}] = "{sys.argv[i]}"')

#
# platform information
#

# getting platform information
platform = sys.platform

# printing platform information
print (f'Platform information:')
print (f'  platform = {platform}')

#
# byte order of the system (big-endian? or little-endian?)
#

# finding byte order of the system
byteorder = sys.byteorder

# printing byte order of the system
print (f'Byte order:')
print (f'  byte order = {byteorder}')

#
# implementation of Python interpreter
#

# finding implementation of Python interpreter
implementation = sys.implementation

# printing implementation of Python interpreter
print (f'Implementation of Python interperter:')
print (f'  name : {implementation.name}')

#
# version of Python interpreter
#

# getting the version of Python interpreter
version = sys.version_info

# printing the version of Python interpreter
print (f'Version of Python interpreter:')
print (f'  version = {version[0]}.{version[1]}.{version[2]}')

#
# location of Python interpreter
#

# finding the absolute path of Python interpreter
location_python = sys.executable

# printing location of Python interpreter
print (f'Location of Python interpreter:')
print (f'  Python interpreter = {location_python}')

#
# list of already loaded modules
#

# getting a list of already loaded modules
list_modules = sys.modules

# printing a list of already loaded modules
print (f'List of already loaded modules:')
for module in sorted (list_modules):
    print (f'  {module}')

#
# exiting Python interpreter
#

# exit
sys.exit (1)
