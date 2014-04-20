# the variable 'i' has the value of zero
i = 0
# the list 'numbers' is empty
numbers = []

# this 'while-loop' only works if the variable 'i'
while i < 6:
	# the value of 'i' is printed here
	print ("At the top i is %d" % i)
	# the value is added to the empty list of 'numbers'
	numbers.append(i)

	# the value of i is now the value of 'i' plus 1
	i = i + 1
	# printing the list numbers
	print ("Numbers now: ", numbers)
	# printing 'i' after new value is added
	print ("At the bottom i is %d" % i)

# printing string
print ("The numbers: ")

# this is a for-loop which goes through the list 'numbers'
for num in numbers:
	# printing num
	print (num)