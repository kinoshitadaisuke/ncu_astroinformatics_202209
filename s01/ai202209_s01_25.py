#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/09 18:19:01 (CST) daisuke>
#

# initialisation of a variable "total"
total = 0

# calculating 1 + 2 + 3 + ... + 10 using "for" statement
for i in range (1, 11, 1):
    # adding "i" to "total"
    total += i

# printing result of calculation
print (f'1 + 2 + 3 + ... + 10 = {total}')
