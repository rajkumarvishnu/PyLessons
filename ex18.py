line_width = 80
exercise_count=18
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

#this one is like your scripts with argv

def print_two (*args):
	arg1,arg2= args
	print "arg1: %r,arg2: %r" %(arg1, arg2)
	
#ok, that * args is pointless, we can just do this
	
def print_two_again (arg1,arg2):
	print "arg1: %r,arg2: %r" %(arg1,arg2)
	
def print_one(arg1):
	print "arg1: %r" %arg1
	
def print_none():
	print"I've got nothing"
	
print_two ("Vishnu","Rajkumar")
print_two_again("Anita","Singha")
print_one("First")
print_none()

