line_width = 80
exercise_count=15
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

from sys import argv
script, filename = argv
txt=open(filename)
print "Here's your file %r: \n\n" %filename 
print txt.read()

print "\n\nI'll also ask you to type it again:"
file_again=raw_input(">")
txt_again = open (file_again)
print txt_again.read()