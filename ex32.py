count = ['1','2','3','4','5']
fruits = ['apples','oranges','graps','mangos']
change = [1,'pennies','2','dimes','3','quarters']

#this first kind of for goes through a list

for no in count:
	print "this is count %s" % no

for fruit in fruits:
	print "A fruit of type %s" %fruit

for g in change:
	print "I got %r" %g


#we can also build lists 

element = []

for f in range(0,7):
	print "adding %d to the list" %f
	element.append(f)

#now will print them 
for n in element:
	print "elements was %d" %n
	print n+1
