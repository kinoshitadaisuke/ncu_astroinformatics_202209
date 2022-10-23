#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/10/23 14:00:13 (CST) daisuke>
#

# importing gzip module
import gzip

# importing sys module
import sys

# catalogue file name
file_catalogue = 'bsc.catalog.gz'

# opening catalogue file
with gzip.open (file_catalogue, 'rb') as fh:
    # reading catalogue line-by-line
    for line in fh:
        # Harvard Revised Number of star
        try:
            HR = int (line[0:4])
        except:
            # printing message
            print (f'Something is wrong with following line...')
            print (f'  {line[:75]}')
            print (f'Cannot extract HR number!')
            # exit
            sys.exit (1)
        # name of star
        name = line[4:14].strip ().decode ('utf-8')
        if (name == ''):
            name = '__NONE__'
        # RA
        try:
            RA_h = int (line[75:77])
            RA_m = int (line[77:79])
            RA_s = float (line[79:83])
        except:
            RA_h = 99
            RA_m = 99
            RA_s = 99.9
        RA_str = f'{RA_h:02d}:{RA_m:02d}:{RA_s:04.1f}'
        RA_deg = (RA_h + RA_m / 60.0 + RA_s / 3600.0) * 15.0
        # Dec
        try:
            Dec_sign = line[83:84].decode ('utf-8')
            Dec_d    = int (line[84:86])
            Dec_m    = int (line[86:88])
            Dec_s    = int (line[88:90])
        except:
            Dec_sign = '-'
            Dec_d    = 99
            Dec_m    = 99
            Dec_s    = 99
        Dec_str = f'{Dec_sign}{Dec_d:02d}:{Dec_m:02d}:{Dec_s:02d}'
        if (Dec_sign == '+'):
            Dec_deg = Dec_d + Dec_m / 60.0 + Dec_s / 3600.0
        else:
            Dec_deg = (Dec_d + Dec_m / 60.0 + Dec_s / 3600.0) * (-1.0)
        # galactic longitude
        try:
            glon = float (line[90:96])
        except:
            glon = -999.99
        # galactic latitude
        try:
            glat = float (line[96:102])
        except:
            glat = -999.99
        # Vmag
        try:
            mag_V = float (line[102:107])
        except:
            mag_V = -999.9
        # B-V colour
        try:
            colour_BV = float (line[109:114])
        except:
            colour_BV = -999.9
        # spectral type
        sptype = line[127:147].strip ().decode ('utf-8')
        # proper motion RA
        try:
            pm_RA = float (line[148:154])
        except:
            pm_RA = -999.9
        # proper motion Dec
        try:
            pm_Dec = float (line[154:160])
        except:
            pm_Dec = -999.9
        # parallax
        try:
            parallax = float (line[161:166])
        except:
            parallax = -999.9


        # printing extracted data
        print (f'HR = {HR}')
        print (f'  name     = "{name}"')
        print (f'  RA_str   = {RA_str}')
        print (f'  RA_deg   = {RA_deg}')
        print (f'  Dec_str  = {Dec_str}')
        print (f'  Dec_deg  = {Dec_deg}')
        print (f'  glon     = {glon}')
        print (f'  glat     = {glat}')
        print (f'  Vmag     = {mag_V}')
        print (f'  B-V      = {colour_BV}')
        print (f'  sptype   = "{sptype}"')
        print (f'  pmRA     = {pm_RA}')
        print (f'  pmDec    = {pm_Dec}')
        print (f'  parallax = {parallax}')
        
