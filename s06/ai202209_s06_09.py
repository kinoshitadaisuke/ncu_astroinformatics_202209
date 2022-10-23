#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/23 18:52:42 (CST) daisuke>
#

# importing sqlite module
import sqlite3

# database file name
file_db = 'hip.db'

# SQL command for making a table
sql_maketable = f'create table hip (hip integer primary key, ' \
    + f'ra_hms text, ra_deg real, dec_dms text, dec_deg real, ' \
    + f'vmag real, bv real, vi real, parallax real, ' \
    + f'pmra real, pmdec real, sptype text);'

# connecting to database
conn   = sqlite3.connect (file_db)
cursor = conn.cursor ()

# making a table
cursor.execute (sql_maketable)

# committing transaction
conn.commit ()

# closing connection
conn.close ()
