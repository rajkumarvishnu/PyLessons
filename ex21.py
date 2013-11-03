line_width = 80
exercise_count=21
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

def add(a,b):
	print "ADDING %d + %d" %(a,b)
	return a+b
	
def subtract (a,b):
	print "SUBTRACTING %d - %d" %(a,b)
	return a-b

def multiply (a,b):
	print "MULTIPLYING %d * %d " %(a,b)
	return a*b

def divide (a,b):
	print "DIVIDING %d / %d " %(a,b)
	return a/b

print "Let's do some math with just functions"

age = add(30,5)
height = subtract (78,4)
weight = multiply (90,2)
iq= divide(100,2)

print "Age: %d, height: %d, weight: %d, iq: %d" % (age,height,weight,iq)

print "here's a puzzle"

what= add(age, subtract (height, multiply(weight,divide(iq,2))))

print "That is ", what, "\b. can you do it by hand?"