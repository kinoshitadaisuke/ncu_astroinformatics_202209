#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/10 08:16:34 (CST) daisuke>
#

# start and end numbers
n_start = 2
n_end   = 100

# output file name
file_output = "primenumbers.data"

# opening file for writing
with open (file_output, 'w') as fh:
    # checking numbers from n_start to n_end
    for i in range (n_start, n_end + 1):
        # resetting parameter "count"
        count = 0
        # examining if the number is divisible by numbers between 2 and (i-1)
        for j in range (2, i):
            # if the number is divisible, then adding 1 to "count"
            if (i % j == 0):
                count += 1
                # if count is >= 1, the number is not a prime number
                break
        if (count == 0):
            # if the number is not divisible by numbers between 2 and (i-1),
            # then it is a prime number
            result = f'{i} is a prime number.\n'
        else:
            # if the number is divisible by at least one of numbers between
            # 2 and (i-1), then it is not a prime number
            result = f'{i} is NOT a prime number.\n'
        # writing result into output file
        fh.write (result)
