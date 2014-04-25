from sys import exit

def dead(reason):
	print (reason)
	exit(0)

def start():
	print("Welcome!")
	print("Do you wish to go to the past or the future?")

	next = input("> ")
	if next == "past":
		past()
	elif next == "future":
		future()
	else:
		dead("Goodbye, dear friend!")

def past():
	print("You have travelled back to your worst enemy!")
	print("You have the opportunity to change the memory. \nDo you change it or leave it?")
	next = input("> ")
	if next == "change":
		jail()
	elif next == "leave":
		billionare()
	else:
		dead("You have made a foolish error.")

def billionare():
	print("You have chosen wisely. You now have the opportunity to become a billionare.")
	print("How much money do you want in billions?")
	next = input("> ")
	money = int(next)
	if money <= 50:
		print("You are a sincere and modest person!")
		dead("You asked for £", money)
	elif money > 50:
		print("You asked for £", money)
		dead("You really are a greedy person!")

	else:
		dead("Wow, you couldn't just pick an option could you?")

def future():
	print("You have travelled to the future!")
	print("You see a piece of technology, and you are given the opportunity to bring it back to the present.")
	print("Do you bring the object back to be reverse-engineered or leave it so that time can take its natural course?")
	next = input("> ")
	if next == "back":
		jail()
	elif next == "leave":
		billionare()
	else:
		dead("Very bad decision!")

def jail():
	print("Former Agents of SHIELD arrest you and you are brought to the Fridge.")
	print("You cannot eat with a fork and are only fed meatloaf.")
	dead("You are killed by fellow inmates for siding with SHIELD!")

start()