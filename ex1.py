

line_width=80
exercise_count =0
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################


print "Exercise ", exercise_count, "got Notepad++ installed"

##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################
print "Hello World!"
print "Hello again"
print "I like typing this."
print "This is fun"
print "Yay! printing"
print "I'd much rather you 'not'."
print 'I "said" do not touch this.'

##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

print "I could code like this" # and the comment after this is ignored

# print "this wont run"

print "This will run"
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################
print "I'll now count my chickens:"

print "Hens", 25+30/6
print "Roosters", 100-25*3%4
print "Now, I'll count the eggs:"
print 3+2+1-5+4%2-1/4+6
print "Is it true that 3+2 < 5-7?"
print "What is 3+2?", 3+2
print "What is 5-7?", 5-7
print "Oh, that's why it's false"
print "How about some more"
print "Is it greater?", 5 > -2
print "Is it greater or equal?", 5 >= -2
print "Is it less or equal?", 5 <= -2

##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################


cars= 400
space_in_a_car = 4.0
drivers = 30
passengers = 90
cars_not_driven = cars-drivers
cars_driven = drivers
carpool_capacity = cars_driven * space_in_a_car
average_passengers_per_car = passengers / cars_driven

print "There are ", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven , "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have ", passengers, "to carpool today."
print "We have to put about", average_passengers_per_car, "in each car"


##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

name = 'Vishnu Rajkumar'
age = 28
height = "5'7"
weight = 68
eyes = 'Black'
teeth = 'White'
hair = 'Black'

print "let's talk about %s" % name
print "He is %s tall" %height
print "He's %d kgs heavy" %weight
print "Actually that's not very heavy"
print "He's got %s eyes and %s hair" %(eyes, hair)

print "His teeth is usually %s depending on the coffee" %teeth
print "If I add %d & %d I get %d" %(age,weight, age+weight)


##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################
integer = 20
x= "There are %d types of people" %integer
binary="binary"
do_not = "don't"
y = "Those who know %s and those who %s" % (binary,do_not)
print x
print y
integer = 21
x= "There are %d types of people" %integer
print "I said: %r." %x
print "I also said: '%s'" %y
hilarious = False
joke_evaluation = "Isn't that joke so funny? %r"

print joke_evaluation %hilarious
w= "That is the left side of..."
e= "A string with aright side."

print w+e

##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

print "Mary had a little lamb"
print "Its fleece was white as %s" % 'snow'
print "And everywhere that Mary went"
print '.' *10 #what'd that do?

end1= "C"
end2= "h"
end3= "e"
end4= "e"
end5= "s"
end6= "e"
end7= "B"
end8= "u"
end9= "r"
end10= "g"
end11= "e"
end12= "r"

print end1+end2+end3+end4+end5+end6,
print end7+end8+end9+end10+end11+end12
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

formatter = "%r %r %r %r"
print formatter % (1,2,3,4)
print formatter % ("one","two","three", "four")
print formatter % (True, False, False, True)

print formatter % (formatter, formatter,formatter,formatter)

print formatter % (
	"I had this thing",
	"That you could type up right",
	"But it didn't sing",
	"So I said goodnight"
)

##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################


#Some strange stuff
days = "Mon Tue Wed Thu Fri Sat Sun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

print "Here are the days: ", days
print "Here are the months: ", months

print """
There's something going on here.
With the three quotes.
We'll be able to type as much we like. 
"""

