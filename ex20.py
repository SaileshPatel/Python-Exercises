# importing argv from sys library
from sys import argv

# setting cmd line arguments
script, input_file = argv

# creating function with argument in function
def print_all(f):
	print f.read()

# creating function with argument in function
def rewind(f):
	f.seek(0)

# creating function with two arguments in function
def print_a_line(line_count, f):
	print line_count, f.readline()

# assigning operator to variable. 
current_file = open(input_file)

print "First let's print the whole file:\n"

# printing the contents of 'current_file'
print_all(current_file)

print "Now let's rewind, kind of like a tape."

rewind(current_file)

print "Let's print three lines:\n"

current_line = 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)

current_line = current_line + 1
print_a_line(current_line, current_file)