number = []


def testing(value1,value2):
	print "value1: %d , Value2: %d" %(value1,value2)
	number.append(value1)
	value1 = value1 + 1
	print value1
	return value1 < value2

value1 = 2
value2 = 10
testing(value1,value2)
