#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/12/08 14:15:20 (CST) daisuke>
#

# check of availability of rebound module
try:
    # importing rebound module
    import rebound
except:
    # if rebound module is not installed, print an error message
    print (f"The module 'rebound' is not installed on your computer.")
    print (f"The module 'rebound' is required for this session.")
    print (f"Visit following web page and install the package 'rebound'.")
    print (f"  https://rebound.readthedocs.io/")
    print (f"After the installation, try to run this script again.")
else:
    # if rebound module is found, print following message
    print (f"The module 'rebound' is found on your computer.")
finally:
    # print that the check of availability of rebound module is finished
    print (f"A test of availability check of 'rebound' module is now finished.")
