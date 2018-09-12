#this one line is like your script with argv
def print_two(*args):
	arg1,arg2 = args
	print "arg1: %s, arg2: %s" %(arg1,arg2)

#ok that *args is pointless we can actually do this
def print_two_again(arg1,arg2):
	print "arg1: %s, arg2: %s" %(arg1,arg2)

#this is for just one argv
def print_one(arg1):
	print "arg1: %s" %arg1

#this will not take arguments
def print_noarg():
	print "no arguments"


print_noarg()
print_one("owner")
print_two("Rajiv","Sindhu")
print_two_again("Sindhu","Rajiv")

