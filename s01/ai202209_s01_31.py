#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 21:22:30 (CST) daisuke>
#

# initialisation of a tuple
planet = ( 'Mercury', 'Venus', 'Earth', 'Mars', \
           'Jupiter', 'Saturn', 'Uranus', 'Neptune' )

# type of "planet"
print ("type of planet:", type (planet) )

# printing the tuple "tuple_a"
print ("planet:\n", planet)

# counting number of elements in the tuple "planet"
n = len (planet)

# printing number of elements in the tuple "planet"
print ("len (planet) =", n)

# accessing to an element using index
print ("planet[2]    =", planet[2])
print ("planet[7]    =", planet[7])
print ("planet[-3]   =", planet[-3])

# accessing to elements using slicing
print ("planet[2:5]  =", planet[2:5])
print ("planet[:4]   =", planet[:4])
print ("planet[6:]   =", planet[6:])
