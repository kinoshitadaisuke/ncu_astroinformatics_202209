#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/18 16:43:46 (CST) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of a resource
url_pi3 = 'https://newton.ex.ac.uk/research/qsystems/collabs/pi/pi3.txt'

# output file name
file_output = 'pi_1000.txt'

# printing status
print (f'Now, opening {url_pi3}...')

# opening URL
with urllib.request.urlopen (url_pi3) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Retrieved data from {url_pi3}!')
    
# printing type of "data_byte"
print (f'type of "data_byte" = {type (data_byte)}')
    
# converting raw byte data into string
data_str = data_byte.decode ('utf-8')

# printing type of "data_str"
print (f'type of "data_str"  = {type (data_str)}')

# printing status
print (f'Now, writing data to file "{file_output}"...')

# opening file for writing
with open (file_output, 'w') as fh_write:
    # writing data
    fh_write.write (data_str)

# printing status
print (f'Finished writing data to file "{file_output}"!')
