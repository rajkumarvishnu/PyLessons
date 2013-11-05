from sys import exit
from random import randint

def death():
	quips = [ "You die. you kinda suck at this",
			"Your mom would be proud. If she were smarter"
			"such a luser"
			"If I have  asamll puppy, thats better than this"]
	print quips[randint(0,len(quips)-1)]
	exit(1)
	
def princess_lives_here(self):
	print "you see a beatiful princess with a shiny crown"
	print "She offers you some cake"
	
	eat_it = raw_input("> ")
	
	if eat_it == "eat it":
		print "You explode like a pinata full of frogs"
		return 'death'
	elif eat_it == "do not eat it":
		print "she throws the cake at you amd cuts off your head"
		return 'death'
	elif eat_it == "make her eat it":
		print "The princess screams as you cram the cake in her mouth"
		return 'gold_koi_pond'
	
	else:
		print "The princess looks at you confused and just point sat teh cake"
		return 'princess_lives_here'
		

		