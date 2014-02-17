# importing argv (special array) from module 'sys'
from sys import argv

# assigning command line arguments
script, filename = argv

# the function 'open(filename)' opens the file named in the command line argument
# this has been assigned to a variable
txt = open(filename)

# printing string with formatter
print "Here's your file %r:" % filename
# text.read() makes a 'file object'
print txt.read()

# printing string
print "Type the filename again:"
# typical raw_input()
file_again = raw_input("> ")

# telling program to open file again
txt_again = open(file_again)

# makes a 'file object'
print txt_again.read()