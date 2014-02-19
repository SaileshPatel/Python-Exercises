# printing string
print "How old are you?",
# collecting user input and assigning the input ot 'age' as a string
age = raw_input()
print "How tall are you?",
height = raw_input()
print "How much do you weigh?",
weight = raw_input()

# using formatters, we're now printing this information, as a part of a string.
print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)