#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 21:39:59 (CST) daisuke>
#

# making a set
fruits = { 'apple', 'banana', 'cherry', 'durian', 'grape', \
           'mango', 'orange', 'apple', 'banana', 'cherry' }

# type of "fruits"
print ("type of fruits:", type (fruits) )

# printing "fruits"
print ("fruits:\n", fruits)

# adding an element to "fruits"
fruits.add ('lemon')

# printing "fruits"
print ("fruits:\n", fruits)

# existence check
exist_banana = 'banana' in fruits
print ("banana exists?", exist_banana)

# one more existence check
exist_tomato = 'tomato' in fruits
print ("tomato exists?", exist_tomato)

# making a list
list_cities1 = [ 'Taipei', 'Taoyuan', 'Hsinchu', 'Taichung', 'Tainan', \
                 'Taipei', 'Taoyuan' ]

# printing type of "list_cities1"
print ("type of list_cities1:", type (list_cities1) )

# printing list "list_cities1"
print ("list_cities1:\n", list_cities1)

# generating a set from a list
set_cities1 = set (list_cities1)

# printing type of "set_cities1"
print ("type of set_cities1:", type (set_cities1) )

# printing set "set_cities1"
print ("set_cities1:\n", set_cities1)

# making a set "set_cities2"
set_cities2 = { 'Taipei', 'Taoyuan', 'Kaohsiung', 'Pingtung', 'Taitung', \
                'Hualien', 'Yilan', 'Taipei', 'Taoyuan' }

# printing type of "set_cities2"
print ("type of set_cities2:", type (set_cities2) )

# printing set "set_cities2"
print ("set_cities2:\n", set_cities2)

# finding elements in both set_cities1 and set_cities2
set_cities_both = set_cities1 & set_cities2

# printing elements in both set_cities1 and set_cities2
print ("cities in both set_cities1 and set_cities2:\n", set_cities_both)
