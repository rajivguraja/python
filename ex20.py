from sys import argv

script, input_file = argv

def print_all(f):
	print f.read() # read function for reading and printing file data.

def rewind(f):
	f.seek(0) # seek function for reading the file from beginning.

def print_a_line(line_count,f):
	print line_count, f.readline() # for printing the line count for every line.

current_file = open(input_file) # here we are storing input file date in current_file.

print "First let us print the whole file:\n"
print_all(current_file)  #here we are current file data to print_all function.

print "now let us rewind kind of like a tape:\n"
rewind(current_file)  # here we are again passing current file data to rewind function.


print "Let us print three lines:"
current_line = 1
print_a_line (current_line,current_file) #for printing the first line counts of input file.
current_line = current_line+1
print_a_line (current_line,current_file)
current_line = current_line+1
print_a_line (current_line, current_file)
current_line = current_line+1
print_a_line (current_line, current_file)
