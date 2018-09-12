i = 0
number = []

while i < 6:
	print "at the top i is %d" %i
	number.append(i)
	i = i+1
	print "Numbers now: ", number
	print "at the bottem i is %d" % i

print "the numbers:"

for num in number:
	print num
