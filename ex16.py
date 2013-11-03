line_width = 80
exercise_count=16
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

from sys import argv

script, filename =argv
print "We're going to erase %r." %filename
print "If you don't want that, hit CTRL-C"
print "If you do want that hit RETURN"

raw_input("?")

print "Opening the file..."

target= open(filename, 'w')

print "Truncating the file. Goodbye!"
target.truncate()

print "Now, I'm going to ask you for three lines"

line1 = raw_input("line1: ")
line2 = raw_input("line2: ")
line3 = raw_input("line3: ")
print "I'm going to write these to the file"

target.write(line1)
target.write (line2)
target.write(line3)


print "Finally, we are closing the file"

target.close()