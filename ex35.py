from sys import exit

def gold_room():   #new function gold_room
	print "This room is full of gold, How  much do you take?"

	next = raw_input(">")  #takes raw inputs
	if "0" in next or "1" in next:   # if condition (if number is have 0 or 1 do the below)
		how_much=int(next)       # stores the input value in how_much variable
	else:
		dead("Man, learn to type numbers")

	if how_much < 50:     # if input value is < 50 and how_much value is having 0 or 1 do the below
		print "Nice!, you are not greedy, you win!"
		exit(0)
	else:
		dead("you greedy bastard!")

def bear_room():     # new function bear_room
	print "There is a bear here!"
	print "The bear has bunch of honey!"
	print "The fat bear is in fornt of other door!"
	print "How you are going to move the bear?"
	bear_moved = False

	while True:  # creating infinite loop
		next = raw_input(">")
		if next == "take honey":
			dead("The bear looks at you and then slaps your face off")  # passing values for below dead() function if the above statement is true
		elif next == "taunt bear" and not bear_moved:
			print "The bear has moved from the door, you can go through it"
			bear_moved = True
		elif next == "taunt bear" and bear_moved:
			dead("The bear gets pissed off and chew you leg off.")   
		elif next == "open door" and bear_moved:
			gold_room() # if input is open door or bear_moved gold_room() function will be called.
		else:
			print "I have no idea what that means"

#gold_room()
#bear_room()

def cthulhu_room():  # new function cthulhu_room function is started.
	print "Here you see the great evil cthulhu!"
	print "He, it, what ever stares at you and you go insane!"
	print "Do you flee for your life or eat your head?"
	next = raw_input(">")
	if "flee" in next:
		start()  # if flee is selected it will call start() function
	elif "head" in next:
		dead("Well that was tasty!")
	else:
		cthulhu_room()  # same cthulhu_room() function is called if we enter other then "flee" or "head" strings


def dead(why):  # new function dead() 
	print why, "Good Job!"
	exit(0)


def start():  # new start() function is created
	print "you are in a dark room!"
	print "There is a door to your right and left!"
	print "which one do you take?"
	next = raw_input("#")

	if next == "left":
		bear_room()   # if raw_input is left bear_room() function is called
	elif next == "right":
		cthulhu_room() # if raw_input is right cthulhu_room() function is called.
	else:
		print "You stumble around the room untill you starve!"

start()  # when running the script start() function is called.
