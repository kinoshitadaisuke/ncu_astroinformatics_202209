#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/23 21:03:35 (CST) daisuke>
#

# importing gzip module
import gzip

# importing sqlite module
import sqlite3

# catalogue file name
file_catalogue = 'mpcorb.dat.gz'

# database file name
file_db = 'mpcorb.db'

# connecting to database
conn   = sqlite3.connect (file_db)
cursor = conn.cursor ()

# SQL command for making a table
sql_maketable = f'create table mpcorb (designation text primary key, ' \
    + f'name text, a real, e real, i real, node real, peri real, M real, ' \
    + f'nobs integer, residual real, flag text, lastobs integer, ' \
    + f'absmag real);'

# making a table
cursor.execute (sql_maketable)

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
            
        # SQL command to add data to table
        sql_adddata = f'insert into mpcorb values ("{designation}", ' \
            + f'"{name}", {a}, {e}, {i}, {node}, {peri}, {M}, ' \
            + f'{nobs}, {residual}, "{flag}", {lastobs}, {absmag});'

        # adding data to table
        cursor.execute (sql_adddata)

# committing transaction
conn.commit ()

# closing connection
conn.close ()
