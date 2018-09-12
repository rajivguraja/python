print "you entere into a dark room with two doors. Do you go through door 1 or 2 or 3?"
door = raw_input('#')

if door == "1":
	print "There is a gaint bear here eating a cheese cake. What do you do?"
	print "1. Take the cake"
	print "2. Scream at the bear"
	bear = raw_input('#')
	if bear == "1":
		print "The bear eats your face off. Good Job!"
	elif bear == "2":
		print "The bear eats your legs off. Good Job!"
	else:
		print "well, doing %s is probably better, Bear runs away" %bear

elif door == "2":
	print "You stare into the endless abyass at cthulhus retina"
	print "1. Buleberries."
	print "2. Yellow Jacket clothespins."
	print "3. Understanding revoler yelling melodies."
	insanity = raw_input(">")
	if insanity == "1" or  insanity == "2":
		print "Your body survives powered by a mind of jello. Good Job!"
#	elif insanity == "2":
#		print "your body survives powered by a mind of jello. Good Job!"
	elif insanity == "3":
		print "The insanity rot your eyes into a pool of muck. Good Job!"
	else:
		print "You are out of this game. bye!"
elif door == "3":
	print "you are with different new job opertunities select 1 or 2 or 3"
	job= raw_input('>')
	if job == "1":
		print "congrates your selected in Google!"
	elif job =="2":
		print "congrats your selected in Apple!"
		print "For you designation enter your choice"
		role = raw_input(">")
		if role == "1":
			print "congrats your a Team Lead"
		elif role == "2":
			print "congrats your a Architect"
		else:
			print "choose as you wish"
	else:
		print "You are selected in Amazon!"
else:
	print "You stumble around and fall on a knife and die. Good Job!"	
