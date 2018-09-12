def cheese_and_crackers(cheese_count, box_of_crackers):
	print "you have %d cheeses!" %cheese_count
	print "you have %d boxes of crackers" %box_of_crackers
	print "Man that enough for party"
	print "Get a blancket.\n"

print "We can just give the function numbers directly: "
cheese_and_crackers(20, 30) #here we are passing the values directly to the above function


print "OR, we can use varibles from our script:"
amount_of_cheese= 10
amount_of_crackers= 50

cheese_and_crackers(amount_of_cheese,amount_of_crackers) # here it directly takes input from vaiables and pass them to above function

print "We can even do math inside too:"

cheese_and_crackers(10+20,5+10) # here it adds two valuse and pass them to above function


print "And we can combine the two variables and math:"
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers+100) #here it adds variables and values and then pass them to above function.
