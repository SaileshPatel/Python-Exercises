# creating function with 'a' and 'b' as parameters
def add(a, b):
	# the function prints the following string with formatters
	print "ADDING %d + %d" % (a, b)
	# the function then returns the answer to a mathematic sum
	return a + b

def subtract(a, b):
	print "SUBTRACTING %d - %d" % (a, b)
	return a - b

def multiply(a, b):
	print "MULTIPLYING %d * %d" % (a, b)
	return a * b

def divide(a, b):
	print "DIVIDING %d / %d" % (a, b)
	return a / b

# printing string!
print "Let's do some maths with just functions!"

# assigning value to variable. the value is add, with the parameters, '30' and '5'
age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print "Age: %d, Height: %d, Weight: %d, IQ: %d" % (age, height, weight, iq)

print "Here's a puzzle."

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))

print "That becomes: ", what, "Can you do it by hand?"