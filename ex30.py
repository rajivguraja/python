people = 30
cars = 30
buses = 30

if cars > people:
	print "we should take cars"
elif cars < people:
	print "we should take people"
else:
	print "we can't decide."

if buses > cars:
	print "That's too many buses"
elif buses < cars:
	print "That's too many cars"
else:
	print "We cant decide"

if people > buses:
	print "Alright we will take buses"
else:
	print "Fine, let's stay at home"
