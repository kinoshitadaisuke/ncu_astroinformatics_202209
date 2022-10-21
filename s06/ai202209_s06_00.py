#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/21 14:18:19 (CST) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_data = 'https://s3b.astro.ncu.edu.tw/ai_202209/data/dp.csv'

# output file name
file_output = 'dwarf_planet.csv'

# printing status
print (f'Now, fetching the file {url_data}...')

# opening URL
with urllib.request.urlopen (url_data) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Finished fetching the file {url_data}!')

# converting raw byte data into string
data_str = data_byte.decode ('utf-8')

# printing status
print (f'Now, writing the data into file {file_output}...')

# opening file for writing
with open (file_output, 'w') as fh_write:
    # writing data
    fh_write.write (data_str)

# printing status
print (f'Finished writing the data into file {file_output}!')
