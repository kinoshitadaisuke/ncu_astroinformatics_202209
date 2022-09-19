#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 13:11:09 (CST) daisuke>
#

# importing re module
import re

# making a pattern for regular expression
pattern_vega = re.compile ('Alp Lyr')

# catalogue file of BSC
file_bsc = 'bsc.data'

# opening file for reading
with open (file_bsc, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # pattern matching using regular expression
        match_vega = re.search (pattern_vega, line)
        # if matched, print the line
        if (match_vega):
            # HR number
            HR    = line[0:4].strip ()
            # name
            name  = line[4:14].strip ()
            # RAh
            RAh   = line[75:77].strip ()
            # RAm
            RAm   = line[77:79].strip ()
            # RAs
            RAs   = line[79:83].strip ()
            # Decpm
            Decpm = line[83].strip ()
            # Decd
            Decd  = line[84:86].strip ()
            # Decm
            Decm  = line[86:88].strip ()
            # Decs
            Decs  = line[88:90].strip ()
            # Vmag
            Vmag  = line[102:107].strip ()
            # SpType
            SpType = line[127:147].strip ()
            # RA
            RA = f'{RAh}:{RAm}:{RAs}'
            # Dec
            Dec = f'{Decpm}{Decd}:{Decm}:{Decs}'
            # printing information about star
            print (f'{HR:4}  {name:10}  {RA}  {Dec}  {Vmag}  {SpType}')
