print "Let's practice everything we learnt"
print "You'd need to know \'bout escapes with \\ that do \n newlines and \t tabs"


poem= """
\t The lovely words
with logic of firmly planted
cannot discern \n the need of love
nor comprehenced passion from intituion
and requires an explanation
\n\twhere there is non.
"""

print "=================================="
print poem
print "=================================="

five= 10-2+3-6

print "This should give five: %d"%five

def secret_formula(started): #here we are starting a function secret_formula
	jelly_beans = started * 500
	jars = jelly_beans/1000
	crates=jars/100
	return jelly_beans,jars,crates # here we are using return for using the output for later purpose

start_point = 10000 #assiging value to variable
beans,jars,crates = secret_formula(start_point) # passing the variable to function and assigning the output to beans,jars,crates variables 

print "with a starting point of : %d" %start_point
print"we'd have %d beans, %d jars, %dcrates"%(beans,jars,crates)

start_point = start_point/10

print "We can also do that in this way:"
print "We'd have %d beans,%d jars, %d rates" %secret_formula(start_point)
