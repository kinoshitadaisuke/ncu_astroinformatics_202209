#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/11/18 11:33:12 (CST) daisuke>
#

# importing gzip module
import gzip

# catalogue file name
file_catalogue = 'mpcorb.dat.gz'

# counter
counter = 0

# opening catalogue file
with gzip.open (file_catalogue, 'rb') as fh:
    # reading catalogue line-by-line
    for line in fh:
        # number of provisional designation
        try:
            designation = line[0:7].strip ().decode ('utf-8')
        except:
            continue
        # absolute magnitude
        try:
            absmag = float (line[8:13])
        except:
            absmag = -999.99
        # mean anomaly
        try:
            M = float (line[26:35])
        except:
            M = -999.99
        # argument of perihelion
        try:
            peri = float (line[37:46])
        except:
            peri = -999.99
        # longitude of ascending node
        try:
            node = float (line[48:57])
        except:
            node = -999.99
        # inclination
        try:
            i = float (line[59:68])
        except:
            i = -999.99
        # eccentricity
        try:
            e = float (line[70:79])
        except:
            e = -999.99
        # semimajor axis
        try:
            a = float (line[92:103])
        except:
            a = -999.99
        # number of observations
        try:
            nobs = int (line[117:122])
        except:
            nobs = -999
        # residual
        try:
            residual = float (line[137:141])
        except:
            residual = -999.99
        # 4-hexdigit flags
        try:
            flag = line[161:165].strip ().decode ('utf-8')
        except:
            flag = '9999'
        # readable name
        try:
            name = line[166:194].strip ().decode ('utf-8')
        except:
            name = '__NONE__'
        # last observation date
        try:
            lastobs = int (line[194:202])
        except:
            lastobs = 99999999

        # skip when reading the header
        if ( (a < -999.0) and (e < -999.0) and (i < -999.0) \
             and (peri < -999.0) and (node < -999.0) and (M < -999.0) ):
            continue
            
        # printing orbital elements of first 5 asteroids
        if (counter < 5):
            print (f'designation = {designation}')
            print (f'  name     = {name}')
            print (f'  absmag   = {absmag}')
            print (f'  M        = {M}')
            print (f'  peri     = {peri}')
            print (f'  node     = {node}')
            print (f'  i        = {i}')
            print (f'  e        = {e}')
            print (f'  a        = {a}')
            print (f'  nobs     = {nobs}')
            print (f'  residual = {residual}')
            print (f'  flag     = {flag}')
            print (f'  lastobs  = {lastobs}')

        # increment counter
        counter += 1
        
