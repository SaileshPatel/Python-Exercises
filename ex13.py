# importing 'argv' from 'sys'
# 'sys' is a Python module
# 'argv' is a feature from 'sys'
from sys import argv

# the variables assigned to 'argv'
script, first, second, third = argv

# printing string and first variable (which holds the name of the script)
print "The script is called:", script
print "Your first variable is:", first
print "Your second variable is:", second
print "Your third variable is:", third