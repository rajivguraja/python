from sys import argv

script,filename =argv

txt =open(filename)

print "here is your file %s:" %filename  
print txt.read()

print "Enter filename"
file_again=raw_input(">")

#txt_again = open(file_again,"w")
#print txt_again.read()
#txt_again.write("this is a new line\n")
#txt_again = open(file_again)
#print txt_again.read()
#txt_again.close()


with open(file_again,"w") as f:
	f.write("Helloooooo, I'm testing this script")
with open(file_again,"r") as i:
	print i.read()
