from sys import argv
from os.path import exists

script,from_file,to_file = argv

print "this script is for copying data from %s to %s ." %(from_file,to_file)

in_file=open(from_file)
indata=in_file.read()

print "This input file id %d bytes long " %len(indata)

print "Does this output file exists? %r" %exists(to_file)
print "Ready, hit RETURN to continue, CTRL+C to abort"
raw_input(">")


out_file=open(to_file,"w")
out_file.write(indata)

print "Alright its done!"

out_file.close()
in_file.close()


