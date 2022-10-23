#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/23 19:42:18 (CST) daisuke>
#

# importing sqlite module
import sqlite3

# database file name
file_db = 'hip.db'

# catalogue file name
file_catalogue = 'hip_main.dat'

# connecting to database
conn   = sqlite3.connect (file_db)
cursor = conn.cursor ()

# opening catalogue file
with open (file_catalogue, 'r') as fh_hip:
    # reading catalogue line-by-line
    for line in fh_hip:
        # Hipparcos Number of star
        try:
            hip = int (line[8:14])
        except:
            # printing message
            print (f'Something is wrong with following line...')
            print (f'  {line[:75]}')
            print (f'Cannot extract Hipparcos number!')
            # exit
            sys.exit (1)
        # RA in hhmmss format
        try:
            RA_hms = line[17:28].strip ()
        except:
            RA_hms = '99 99 99.99'
        # Dec in ddmmss format
        try:
            Dec_dms = line[29:40].strip ()
        except:
            Dec_dms = '-99 99 99.9'
        # V-band magnitude
        try:
            mag_V = float (line[41:46])
        except:
            mag_V = -99.99
        # RA in deg
        try:
            RA_deg = float (line[51:63])
        except:
            RA_deg = -999.99
        # Dec in deg
        try:
            Dec_deg = float (line[64:76])
        except:
            Dec_deg = -999.99
        # parallax in mas
        try:
            parallax = float (line[79:86])
        except:
            parallax = -999999.99
        # proper motion in RA
        try:
            pm_RA = float (line[87:95])
        except:
            pm_RA = -999999.99
        # proper motion in Dec
        try:
            pm_Dec = float (line[96:104])
        except:
            pm_Dec = -999999.99
        # (B-V) colour index
        try:
            colour_BV = float (line[245:251])
        except:
            colour_BV = -999.99
        # (V-I) colour index
        try:
            colour_VI = float (line[260:264])
        except:
            colour_VI = -999.99
        # spectral type
        try:
            sptype = line[435:447].strip ()
        except:
            sptype = '___NONE___'

        # SQL command to add data to table
        sql_adddata = f'insert into hip values ({hip}, ' \
            + f'"{RA_hms}", {RA_deg}, "{Dec_dms}", {Dec_deg}, ' \
            + f'{mag_V}, {colour_BV}, {colour_VI}, {parallax}, ' \
            + f'{pm_RA}, {pm_Dec}, "{sptype}");'

        # executing SQL command to add data to table
        cursor.execute (sql_adddata)

# committing transaction
conn.commit ()

# closing connection
conn.close ()
