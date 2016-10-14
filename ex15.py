from sys import argv

script, filename = argv

txt = open(filename) #opens the desired file

print "Here's your file %r:" % filename
print txt.read() #read and prints the file that is being opened

print  "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()
