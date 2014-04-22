from sys import exit

def dead(reason):
	print (reason)
	print ("Thank you for playing the game!")
	exit(0)

def past():
	print ("You are transported back to your worst memory.")
	print ("Do you change the memory or watch as the events unfold?")
	next = input("> ")

	if next == "change":
		dead("You create holes in the wibbly-wobbly timey-wimey! And die as a result of this interference.")		
	elif next == "watch":
		print ("Well done! You haven't given in to breaking the time continum!")
		print ("You now have two options!")
		print ("You can either have enough money to make your way in life or become a billionare.")

		next = input("> ")
		
		if next == "enough":
			dead("Ha! You lose sucker!")
		elif next == "billionare":
			billionare()
		else:
			dead("Took too long! LOL!")

	else:
		dead("Took too long! LOL!")

def future():
	print ("You are in the future, where we have flying cars and technologies beyond our imaginations.")
	print ("Do you take the device back so that it can be reverse engineered or do you feign ignorance about being from the past?")

	next = input("> ")
	if next == "technology":
		print ("")
	elif next == "ignorance":
		print ("")
	else:
		dead("Took too long! LOL!!")

def billionare():
	print ("How many billions do you want?:")
	money = input("> ")
	amount = int(money)

	if amount <= 25:
		print ("You are very modest!")
	elif amount > 25:
		dead("You're a greedy bastard! You die immediately.")
	else:
		dead("Took too long!")

def start():
	print ("Welcome!")
	print ("Do you wish to go to the past or the future?")

	next = input("> ")
	if next == "past":
		past()
	elif next == "future":
		future()
	else:
		dead("Goodbye, dear friend!")

start()