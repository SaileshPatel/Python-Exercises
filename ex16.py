# importing 'argv' from 'sys' library
from sys import argv

# assigning the variables 'script' (which is the name of the script), and 'filename' (which is the name of a file) to the command line argument array 'argv'
script, filename = argv
# printing string with formatter representing 'filename'
print "We're going to erase %r." % filename
# printing string
print "If you don't want that, hit CTRL-C (^C)."
print "If you do want that, hit RETURN."

raw_input("?")

print "Opening the file..."
# assigning operator to variable. using 'open' to open the file.
target = open(filename, 'w')

# printing string
print "Truncating the file. Goodbye!"
# emptying file using truncate function
target.truncate()

print "Now I'm going to ask you for three lines."

# assigning user data to variable and printing string
line1 = raw_input("line 1: ")
line2 = raw_input("line 2: ")
line3 = raw_input("line 3: ")

print "I'm going to write these to the file."

# writing string from variable to the file
target.write(line1)
# writing new line to the file
target.write('\n')
target.write(line2)
target.write('\n')
target.write(line3)
target.write('\n')

print "And finally, we close it."
# now we close the case! - '...It was Elementary, my dear Watson...'
target.close()