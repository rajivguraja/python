from sys import argv

script,filename = argv

print "We're going to erase %r" %filename
print "If you don't want hit CTRL-C (^c)."
print "If you do want then, hit RETURN"

raw_input(">")
print "Opening file.."
target = open(filename,"w")
print "Truncating the file..Goodbye!"
target.truncate()
print "Now I'm gonna ask you for 3 lines"
line1 = raw_input("Line1: ")
line2 = raw_input("Line2: ")
line3 = raw_input("Line3: ")

print "I'm gonna write this to a file"
target.write(line1)
target.write("\n")
target.write(line2)
target.write("\n")
target.write(line3)
target.write("\n")

print "And finally, will close it"
target.close()

filename1=raw_input("filename1: ")
new=open(filename1,"r")
print new.read()
#print "And finally, will close it"
#target.close()
