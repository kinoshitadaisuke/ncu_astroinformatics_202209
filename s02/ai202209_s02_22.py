#!/usr/pkg/bin/python3.9

#
# Time-stamp: <2022/09/19 08:21:17 (CST) daisuke>
#

# importing subprocess module
import subprocess

# executing a command "cal 9 1752" and capturing output
result = subprocess.run ('cal 9 1752', shell=True, capture_output=True)

# stdout of command execution
output = result.stdout.decode ('utf-8')

# printing result of command execution
print (output)
