# importing exit from the library 'sys'
from sys import exit

# creating function called 'house()'
def house():
	# printing multiple strings
	print ("You enter the house.")
	print ("Do you walk in to the kitchen or bathroom?")

	# assigning user input to variable
	next = input("> ")
	# if the variable 'next' has the string 'kitchen'
	if next == "kitchen":
		# opens the function 'kitchen()'
		kitchen()
	# if the variable 'next' has the string 'bathroom'
	elif next == "bathroom":
		# opens the function 'bathroom()'
		bathroom()
	# if the value of 'next' is anything else
	else:
		# kills the program with the function 'dead()'
		dead("You are killed by the owner when they return.")

# created function called 'kitchen()'
def kitchen():
	# printing multiple strings
	print ("You have entered the kitchen.")
	print ("You see a fresh homecooked roast dinner, and a bottle of wine.")
	print ("Do you eat the roast, drink the wine or leave them both?")

	# assigning user input to variable
	next = input("> ")
	# if the value of 'next' is the string 'dinner'
	if next == "dinner":
		# kills the program 
		dead("The roast dinner had a drug which makes it look like victims died of a heart attack")
	# if the value of 'next' is the string 'wine'
	elif next == "wine":
		# printed string
		print("Well done, you drank the safe wine")
		# starts the function of 'bathroom()'
		bathroom()
	# if the value of 'next' is anything else
	else:
		# kills the program
		dead("Sorry!")

# created function called 'bathroom()'
def bathroom():
	# printed multiple strings
	print ("You have entered the bathroom.")
	print ("You hear a scream from outside!")
	print ("The scream shouts 'HELP ME!!!'")
	print ("Do you help or stay in safety?")

	# assigning user input to variable
	next = input("> ")
	# if the value of 'next' is the string 'help'
	if next == "help":
		# the program is killed
		dead("It was all a big trap! You are killed by the tricksters.")
	# if the value of 'next' is the string 'safety'
	elif next == "safety":
		# printed string
		print("Well done! You didn't fall for the trap!")
		# starts the function of 'killer()' - trick function!
		killer()
	# if the value of 'next' is anything else
	else:
		# printed string
		print("I don't understand. Try again")
		# opens function 'bathroom()'
		bathroom()

# created function
def killer():
	# printed multiple strings
	print ("The owner finally arrives.")
	print ("They walk upstairs, and start shouting nonsense.")
	print ("Do you flee or confront the killer?")

	# assigning user input to variable
	next = input("> ")
	# if the value of 'next' is the string 'flee'
	if next == "flee":
		# program is killed
		dead("You are now dead.")
	# if the value of 'next' is the string 'confront'
	elif next == "confront":
		# printed string
		print ("Right option! The killer respects your courage!")
	# if the value of next is something else
	else:
		# program is killed
		dead("Error!")

# creating function to kill program, with variable 'why'
def dead(why):
	# printed string
	print (why, "\nThank you!")
	# kills the program with no error
	exit(0)

# creating function 
def start():
	# printed multiple strings
	print ("You approach an abandoned house.")
	print ("Do you enter or leave?")

	# assigning user input to variable
	next = input("> ")
	# if the value of next is 'enter' or 'Enter'
	if next == "enter":
		# the function 'house()' opens
		house()
	# if the value of next is 'leave'
	elif next == "leave":
		# kills the programs
		dead("A bear kills you!")
	# if the value of next is something else
	else:
		# printed string
		print ("I don't understand")
		# kills the program
		dead("You wait outside for 12,000 years and die of starvation.")

# 126 lines of code later, we finally start the program! 
start()