
from sys import argv
script, name = argv

ask = "#"

print "Hi %s, I'm the %s script."%(name,script)
print "I'd like to ask you few questions."
print "Do you like me %s?" %name
like=raw_input(ask)
print "where do you live %s?"%name 
lives=raw_input(ask)
print "what kind of computer do you have %s ?"%name
computer=raw_input(ask)

print "Alright you said %r about liking me. you live in %r. Not sure where it is. And you have a %r computer. nice."%(like,lives,computer)
