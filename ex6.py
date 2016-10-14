x = "There are %d types of people." %10
binary = "binary"
do_not ="don't"
y = "Those who know %s and those who %s" %(binary, do_not) #important

print x
print y

print "I said: %r"%x
print "I also said: '%s'." %y

hilarious = False
joke_evaluation ="Isn't that joke so funny?! %r"

print joke_evaluation % hilarious # %r  signs to %hilarious which is Falese, therefore False comes as output 

w= "This is the left side of..."
e="a string with a right side."

print w+e
