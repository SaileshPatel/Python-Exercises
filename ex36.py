# importing exit from the library 'sys'
from sys import exit

def house():
	print ("You enter the house.")
	print ("Do you walk in to the kitchen or bathroom?")

	next = input("> ")
	if next == "kitchen":
		kitchen()
	elif next == "bathroom":
		bathroom()
	else:
		dead("You are killed by the owner when they return.")

def kitchen():
	print ("You have entered the kitchen.")
	print ("You see a fresh homecooked roast dinner, and a bottle of wine.")
	print ("Do you eat the roast, drink the wine or leave them both?")

	next = input("> ")
	if next == "dinner":
		dead("The roast dinner had a drug which makes it look like victims died of a heart attack")
	elif next == "wine":
		print("Well done, you drank the safe wine")
		bathroom()
	else:
		dead("Sorry!")

def bathroom():
	print ("You have entered the bathroom.")
	print ("You hear a scream from outside!")
	print ("The scream shouts 'HELP ME!!!'")
	print ("Do you help or stay in safety?")

	next = input("> ")
	if next == "help":
		dead("It was all a big trap! You are killed by the tricksters.")
	elif next == "safety":
		print("Well done! You didn't fall for the trap!")
		killer()
	else:
		print("I don't understand. Try again")
		bathroom()

def killer():
	print ("The owner finally arrives.")
	print ("They walk upstairs, and start shouting nonsense.")
	print ("Do you flee or confront the killer?")

	next = input("> ")
	if next == "flee":
		dead("You are now dead.")
	elif next == "confront":
		print ("Right option! The killer respects your courage!")
	else:
		dead("Error!")

def dead(why):
	print (why, "\nThank you!")
	exit(0)

def start():
	print ("You approach an abandoned house.")
	print ("Do you enter or leave?")

	next = input("> ")
	if next == "enter" or "Enter":
		house()
	elif next == "leave":
		dead("A bear kills you!")
	else:
		print ("I don't understand")
		dead("You wait outside for 12,000 years and die of starvation.")

start()
