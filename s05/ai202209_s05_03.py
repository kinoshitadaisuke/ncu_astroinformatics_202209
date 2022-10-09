#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/09 13:58:48 (CST) daisuke>
#

# importing scipy module
import scipy.constants

# finding a constant
search_result = scipy.constants.find ('Wien')

# printing search result
for constant in search_result:
    print (f'{constant}')
