line_width = 80
exercise_count=19
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

def cheese_and_crackers (cheese_count,boxes_of_crackers):
	print "You've %d cheeses" %cheese_count
	print "You've %d boxes of crackers" % boxes_of_crackers
	print "Man that's enough for a party"
	print "get a blanket\n"
	
print "We can give func the numbers directly:"
cheese_and_crackers(20,30)


print "Or, we could use variables"
amount_of_cheese =10
amount_of_crackers =50

cheese_and_crackers(amount_of_cheese,amount_of_crackers)


print "We can even do math inside"

cheese_and_crackers (10+2,5+6)

print "And, we can combine the two"
cheese_and_crackers(amount_of_cheese + 10,amount_of_crackers+20)