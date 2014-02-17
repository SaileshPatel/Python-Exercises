# creating function
# the '*' in args tells Python to put all the arguments in the function in a list in 'args'
# this is similar to 'argv', but for functions only
def print_two(*args):
	arg1, arg2 = args
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# creating function
# placing arguments directly in function to skip unpacking
def print_two_again(arg1, arg2):
	# printing statement with formatters
	print "arg1: %r, arg2: %r" % (arg1, arg2)

# creating function
# placing argument directly in function to skip unpacking
def print_one(arg1):
	# printing statement with formatters
	print "arg1: %r" % arg1

# creating statement
def print_none():
	# printing statement
	print "I got nothing"

print_two("Zed", "Shaw")
print_two_again("Zed", "Shaw")
print_one("First!")
print_none()