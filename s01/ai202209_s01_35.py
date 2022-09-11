#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/10 07:58:54 (CST) daisuke>
#

# name of data file
file_data = 'fruits.data'

# a variable for total price
total = 0

# opening file with read mode
with open (file_data, 'r') as fh:
    # reading file line-by-line
    for line in fh:
        # if line starts with '#', then it is a header line and skip
        if (line[0] == '#'):
            continue
        # splitting line
        (name, unit_price_str, quantity_str) = line.split ()
        # converting from string into integer
        unit_price = int (unit_price_str)
        quantity   = int (quantity_str)
        # calculation of sub-total
        subtotal = unit_price * quantity
        # adding "subtotal" to "total"
        total += subtotal
        # printing information
        print (f'{name:10} {unit_price:3d} {quantity:2d} {subtotal:3d}')

# printing total price
print (f'\ntotal price: {total:4d}')
