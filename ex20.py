line_width = 80
exercise_count=20
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

from sys import argv

script, input_file = argv

def print_all(f):
	print f.read()
	
def rewind(f):
	f.seek(0)
	
def print_a_line(line_count, f):
	print line_count, f.readline(line_count)
	
current_file = open(input_file)

print "First, let's print the whole file:\n"

print_all(current_file)

print "Let's now rewind"

rewind(current_file)

print "Let's print three lines:"

current_line=15
print_a_line(current_line,current_file)

current_line =current_line+1
print_a_line(current_line,current_file)

current_line =current_line+1
print_a_line(current_line,current_file)
