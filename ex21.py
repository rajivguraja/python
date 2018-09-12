def add(a,b):
	print "Adding %d + %d"%(a,b)
	return a+b  #Does a+b and returns it to age variable 
def subtract(a,b):
	print "subtracting %d - %d" %(a,b)
	return a-b #Does a-b and returns the value to height
def multiply(a,b):
	print "Multipying %d * %d" %(a,b)
	return a*b #Does a*b and returns the value to weight
def divide(a,b):
	print "Dividing %d / %d" %(a,b)
	return a/b #Does a/b and returns the value to iq


#Defining the values for above functions.
age = add(20+1,5+3) 
height=subtract(70,2)
weight=multiply(20,4)
iq=divide(24,4)
print "age: %d" %age
print "height: %d" %height
print "weight: %d and iq: %d" %(weight,iq)


#A puzzle for the extra credit
print "Here is the puzzle"

# Doing the math using the output from above function and variables.
what=divide(age,iq)
#what= age+height+weight+iq
#what= add(age,subtract(height,divide(iq,2)))
#what=add(age, subtract(height, multiply(weight, divide(iq,4))))

print "This becoms:", what, "can you do it by hand"
