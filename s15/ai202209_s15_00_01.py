#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/25 11:42:59 (CST) daisuke>
#

# importing argparse module
import argparse

#
# command-line argument analysis
#

# constructing parser object
desc = f"availability check of Python modules"
parser = argparse.ArgumentParser (description=desc)

# adding options
parser.add_argument ('module', type=str, nargs='+', \
                     help=f"module name (e.g. numpy)")

# analysis of command-line arguments
args = parser.parse_args ()

#
# input parameters
#

# list of module names for availability check
list_modules = args.module

#
# availability check of modules
#

for module in list_modules:
    # check of availability of rebound module
    try:
        # importing module
        imported = __import__ (module)
    except:
        # if rebound module is not installed, print an error message
        print (f"The module '{module}' is NOT installed on your computer.")
    else:
        # if rebound module is found, print following message
        print (f"The module '{module}' is found on your computer.")
        print (f"{imported}")
    finally:
        # print that the check of availability of rebound module is finished
        print (f"An availability check of '{module}' module is now finished.")
        print (f"")
