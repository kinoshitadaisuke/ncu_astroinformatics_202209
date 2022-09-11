#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 19:44:25 (CST) daisuke>
#

# defining a function to add two numbers
def add_two_numbers (a, b):
    # adding two numbers
    c = a + b
    # returning result of calculation
    return (c)

# two numbers
n1 = 7
n2 = 8

# using the function "add_two_numbers"
n3 = add_two_numbers (n1, n2)

# printing result
print (f'n1 = {n1}')
print (f'n2 = {n2}')
print (f'n3 = n1 + n2 = {n3}')
