# importing a something from a library
from sys import exit

# creating a function called 'gold_room()'
def gold_room():
	# printing a string
	print ("This room is full of gold. How much gold do you take?")

	# creating a variable which collects user input
	next = input("> ")
	# creating an if-loop to determine next move.
	if "0" in next or "1" in next:
		# the variable created 'how_much' is the user inputted value as a integer (number)
		how_much = int(next)
	# if the condition of the if-loop doesn't meet the former		
	else:
		# using 'dead' function
		dead("Man, learn to type a number.")

	# creating an if-loop to determine next move. 
	# this will happen if the variable 'how_much' has a value less than 50
	if how_much < 50:
		# printing string
		print ("Nice, you're not greedy, you win!")
		# exits program without an error
		exit(0)
	# if the variable 'how_much' has a higher value than 50
	else:
		# using dead function to kill the game
		dead("You greedy bastard!")

# creating function called 'bear_room'
def bear_room():
	# printing various string
	print ("There is a bear here.")
	print ("The bear has a bunch of honey.")
	print ("The fat bear is in front of another door.")
	print ("How are you going to move the bear?")
	# the variable 'bear_moved' has a boolean value of 'False'
	bear_moved = False

	# created an infinite while loop
	while True:
		# the variable 'next' takes user input
		next = input("> ")

		# if the variable 'next' has the the string 'take honey' 
		# the following happens
		if next == "take honey":
			# the 'dead' function is used to kill the game
			dead("The bear looks at you then slaps your face off.")
		# if the variable 'next' has the string 'taunt bear' and 'bear_moved' = 'False'
		# the following happens
		elif next == "taunt bear" and not bear_moved:
			# printed string 
			print ("The bear has moved from the door. You can go through it now.")
			# changed boolean value of 'bear_moved' to True meaning function re started
			bear_moved = True
		# if the variable 'next' has the string 'taunt bear' and the variable 'bear_moved' has the boolean value 'True'
		# the following happens			
		elif next == "taunt bear" and bear_moved:
			# printed string
			print ("The bear gets pissed off and chews you leg off.")
		# if the variable 'next' has the string 'open door' and the variable 'bear_moved' has the boolean variable 'True'
		# then the following happens
		elif next == "open door" and bear_moved:
			# starts function 'gold_room()'
			gold_room()
		# other value
		else:
			# printed string
			print ("I got no idea what that means.")

# created new function
def cthulhu_room():
	# printed multiple strings
	print ("Here you see the great evil Cthulhu.")
	print ("He, it, whatever stares at you and you go insane.")
	print ("Do you flee for your life or eat your head?")

	# the variable 'next' collects user input as string
	next = input("> ")
	# if the string 'flee' is in the variable 'next' 
	# the following happens
	if "flee" in next:
		# the 'start()' function happens
		start()
	# if the string 'head' is in the variable 'next'
	# the following happens
	elif "head" in next:
		# the 'dead' function happens
		dead("Well that was tasty!")
	# anything else
	else:
		# the function 'cthulhu_room()' starts again
		cthulhu_room()

# creating the function 'dead' to kill the program without an error
def dead(why):
	# prints the variable why and string
	print (why, "Good job!")
	# kills the program without an error
	exit(0)

# creating the function 'start()' to kick off the program
def start():
	# printing multiple strings
	print ("You are in a dark room.")
	print ("There is a door to your right and left.")
	print ("Which one do you take?")

	# the variable next collects user input as a string
	next = input("> ")

	# if the variable 'next' contains the string 'left'
	if next == "left":
		# the function 'bear_room()' starts
		bear_room()
	# if the variable 'next' contains the string 'right'
	elif next == "right":
		# the function 'cthulhu_room()' starts
		cthulhu_room()
	else:
		# the program is killed by the function 'dead()'
		dead("You stumble around the room until you starve.")

# after all that, the program finally starts
start()