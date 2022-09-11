#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 21:44:36 (CST) daisuke>
#

# making a dictionary
star_mag = {
    "Sirius": -1.46,
    "Canopus": -0.74,
    "Rigil Kentaurus": -0.27,
    "Arcturus": -0.05,
    "Vega": 0.03,
    "Capella": 0.08,
    "Rigel": 0.13,
    "Procyon": 0.34,
    "Achernar": 0.46,
    "Betelgeuse": 0.50,
}

# type of "star_mag"
print ("type of star_mag:", type (star_mag) )

# printing dictionary "star_mag"
print (star_mag)

# accessing to an element
print ("magnitude of Vega =", star_mag['Vega'])

# printing all the data
for star in sorted (star_mag.keys ()):
    print (f'{star:16} : {star_mag[star]:+5.2f}')
