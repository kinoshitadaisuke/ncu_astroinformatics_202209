#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 21:22:09 (CST) daisuke>
#

# initialisation of a list
list_a = [ 0.1, 2.3, 4.5, 5.6, 6.7, 8.9, 10.1 ]

# type of "list_a"
print ("type of list_a:", type (list_a) )

# printing the list "list_a"
print ("list_a       =", list_a)

# counting number of elements in the list "list_a"
n = len (list_a)

# appending a new element to the list
list_a.append (11.3)

# printing the list "list_a"
print ("list_a       =", list_a)

# counting number of elements in the list "list_a"
n = len (list_a)

# printing number of elements in the list "list_a"
print ("len (list_a) =", n)

# printing an element of the list "list_a"
print ("list_a[0]    =", list_a[0])
print ("list_a[3]    =", list_a[3])
print ("list_a[-2]   =", list_a[-2])

# printing elements of the list "list_a" using slicing
print ("list_a[2:5]  =", list_a[2:5])

# printing elements of the list "list_a" using slicing
print ("list_a[4:]   =", list_a[4:])

# printing elements of the list "list_a" using slicing
print ("list_a[:3]   =", list_a[:3])

# adding 1.23 to each element of "list_a"
for i in range ( len (list_a) ):
    list_a[i] += 1.23

# printing the list "list_a"
print ("list_a       =", list_a)
