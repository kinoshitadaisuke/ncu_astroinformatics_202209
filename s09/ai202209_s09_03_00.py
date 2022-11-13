#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/13 23:47:14 (CST) daisuke>
#

# importing urllib module
import urllib.request

# importing ssl module
import ssl

# allow insecure downloading
ssl._create_default_https_context = ssl._create_unverified_context

# URL of data file
url_data = 'https://iopscience.iop.org/0004-637X/774/1/80/suppdata/' \
    + 'apj480431t2_ascii.txt?doi=10.1088/0004-637X/774/1/80'

# output file name
file_output = 'hd61005_spec.data'

# printing status
print (f'Fetching {url_data}...')

# opening URL
with urllib.request.urlopen (url_data) as fh_read:
    # reading data
    data_byte = fh_read.read ()

# printing status
print (f'Fetched {url_data}!')

# converting raw byte data into string
data_str = data_byte.decode ('utf-8')

# printing status
print (f'Now, writing data into file "{file_output}"...')

# opening file for writing
with open (file_output, 'w') as fh_write:
    # writing data
    fh_write.write (data_str)

# printing status
print (f'Finished writing data into file "{file_output}"!')
