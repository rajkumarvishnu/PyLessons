line_width = 80
exercise_count=17
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

from sys import argv
from os.path import exists

script, from_file, to_file = argv

print "copying from %s to %s" % (from_file, to_file)

input= open(from_file)
indata = input.read()

print "The input file is %d long" %len(indata)

print "Does the output file exist? %r" % exists(to_file)

print "Ready, hit RETURN to continue, CTRL C to abort"

raw_input()

output = open(to_file,'w')

output.write(indata)

print "Alright, all done"

output.close()
input.close()

