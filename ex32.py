# created a 1-dimensional list with integer values
the_count = [1, 2, 3, 4, 5]
# created a 1-dimensional list with strings
fruits = ['apples', 'oranges', 'pears', 'apricots']
# created a 1-dimensional list with integers and string
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# this for-loop goes through a list
for number in the_count:
	# then prints the list
	print ("This is count %d" % number)

# this for-loop goes through a list
for fruit in fruits:
	# prints the list
	print ("A fruit of type: %s" % fruit)

# this for-loop goes through a list
for i in change:
	# the list is then printed 
	print ("I got %r" % i)

# here we have a 1-dimensional empty list
element = []

# here we are using a for-loop using range function to do 0 to 5 counts
for i in range(0, 6):
	# printing numbers 0 to 5.
	print ("Adding %d to the list." % i)
	# the value 'i' (which is 0 to 5) is added to the list 'elements' using the append function
	element.append(i)

# here we have a 1-dimensional empty list
elements = []
# using 'extend' function to add the range 0 to 5
elements.extend(range(0, 6))

# printing the list 'elements'
print (elements)