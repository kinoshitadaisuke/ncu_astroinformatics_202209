#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 21:53:51 (CST) daisuke>
#

# making a multi-dimensional dictionary
asteroid = {
    'Ceres': {
        'a': 2.769,
        'e': 0.076,
        'i': 10.594,
        'H': 3.4,
        'diameter': 939.4,
    },
    'Pallas': {
        'a': 2.774,
        'e': 0.230,
        'i': 34.833,
        'H': 4.2,
        'diameter': 545,
    },
    'Juno': {
        'a': 2.668,
        'e': 0.257,
        'i': 12.991,
        'H': 5.33,
        'diameter': 246.596,
    },
    'Vesta': {
        'a': 2.361,
        'e': 0.089,
        'i': 7.142,
        'H': 3.0,
        'diameter': 525.4,
    },
}

# printing dictionary information
print ("Ceres:\n", asteroid['Ceres'])
print ("Vesta:\n", asteroid['Vesta'])
print ("a of Pallas =", asteroid['Pallas']['a'], "au")
print ("e of Juno   =", asteroid['Juno']['e'])
print ("i of Vesta  =", asteroid['Vesta']['i'], "deg")
print ("H of Ceres  =", asteroid['Ceres']['H'], "mag")

# printing rotation period of 4 asteroids
print ('Diameters of asteroids:')
for key in (asteroid.keys ()):
    print (f'  {key:6} : {asteroid[key]["diameter"]:4.1f} km')
