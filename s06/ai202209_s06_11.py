#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/23 19:28:12 (CST) daisuke>
#

# importing sqlite module
import sqlite3

# database file name
file_db = 'hip.db'

# connecting to database
conn   = sqlite3.connect (file_db)
cursor = conn.cursor ()

# SQL command for a query
sql_query = 'select hip, ra_hms, dec_dms, vmag, bv, parallax, sptype ' \
    + f'from hip where parallax > 200 order by parallax desc;'

# executing a SQL query
cursor.execute (sql_query)

# fetching results of query
results = cursor.fetchall ()

# printing results of query
print (f'# HIP   RA           Dec          Vmag   B-V      p      sptype')
for result in results:
    print (f'{result[0]:06d}  {result[1]}  {result[2]}  {result[3]:5.2f}', \
           f' {result[4]:7.2f}  {result[5]:5.1f}  {result[6]}')

# committing transaction
conn.commit ()

# closing connection
conn.close ()
