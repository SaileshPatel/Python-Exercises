# assigning user inputted data in to variable. also printing string as a part of function 'raw_input'
age = raw_input("How old are you? ")
height = raw_input("How tall are you? ")
weight = raw_input("How much do you weigh? ")

print "So, you're %r old, %r tall and %r heavy." % (
	age, height, weight)