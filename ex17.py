# importing argv array from sys library
from sys import argv
# importing exists from os.path library
from os.path import exists

# command line arguments needed
script, from_file, to_file = argv

# printing string with formatters
print "Copying from %s to %s" % (from_file, to_file)

# this is essentially two lines of code in one
# in_file variable opens the file in 'from_file'
# indata variable reads the file in 'in_file'
in_file = open(from_file); indata = in_file.read()

# printing string with formatters
# 'len' function gets the length of the string, then prints the length as a numerical value
print "The input file is %d bytes long" % len(indata)

# printing string with formatter
print "Does the output file exist? %r" % exists(to_file)
# printing string
print "Ready, hit the RETURN button to continue, CTRL-C to abort."
raw_input()

# opening file
out_file = open(to_file, 'w')
# writing new material to out_file
out_file.write(indata)

# printing string
print "Alright, done"

# closing the two files
out_file.close()
in_file.close()