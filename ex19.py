# creating function, with arguments inside function
def cheese_and_crackers(cheese_count, boxes_of_crackers):
	# print string with formatter 
	print "You have %d cheese!" % cheese_count
	# print string with formatter
	print "You have %d boxes of crackers" % boxes_of_crackers

# print string
print "We can give the function number directly:"
# printing function with arguments taking numbers
cheese_and_crackers(20, 30)

# printing string
print "OR, we can use user input:"
# creating variable which contains user input
amount_of_cheese = raw_input("Please enter the amount of cheese you want: ")
# creating variable which contains user input
amount_of_crackers = raw_input("Please enter the amount of crackers you want: ")

# creating variable, where we convert the string in to integer
cheese = int(amount_of_cheese)
# creating variable, where we convert the string in to integer
crackers = int(amount_of_crackers)

# printing function with user inputted integers
cheese_and_crackers(cheese, crackers)

# printing string
print "We can even do math inside the function too:"
# printing function with mathematic sums inside
cheese_and_crackers(10 + 20, 5 + 6)

# printing string
print "And we can combine the two, variables and math:"
# printing function with math and variables
cheese_and_crackers(cheese + 100, crackers + 1000)

