from sys import exit
def gold_room():
	print "Thsi room is full of gold, how much do you take"
	next = raw_input("> ")
	if "0" in next or "1" in next:
		how_much= int(next)
	else:
		dead("Man, learn to typre a number")
		
		if how_much<50:
			print "Nice"
		else:
			dead("You greedy")
def bear_room():
	print "There is a bear here"
	print "The bear has a bunch of honey"
	print "The fat h=bear is in front of another door"
	print "How are you going tomove the bear"
	
	bear_moved = False
	
	while True:
		next= raw_input("> ")
	
		if next=="take honey":
			dead("The bear looks at you then slaps your face")
		elif next=="taunt bear" and not bear_moved:
			print "The bear has moved from teh door YOU CAN GO THROUGH TEH DOOR"
			bear_moved = True
		elif next=="taunt bear" and bear_moved:
			dead("the bear gets pissed off and chews you")
		elif next=="open door" and bear_moved:
			gold_room()
		else:
			print "I got no idea what that means"
		
		
def cthulu_room():
	print "here you see the great evil Cthulu"
	print "He, it, whatebver stares at you and you go insane"
	print "Do you flee for your life or eat your head"
	next= raw_input("> ")
	
	if "flee" in next:
		start()
	elif "head" in next:
		dead("well that was tasty")
	else:
		cthulu_room()
	
def dead(why):
	print why, "wgood job"
	exit(0)
def start():
	print "You are in a dark room"
	print "There is a door to your right na dleft"
	print "Whgich one do you take"
	next= raw_input("> ")
	if next=="left":
		bear_room()
	elif next=="right":
		cthulu_room()
	else:
		dead("Yiyu stumble around, startve and die")
	
	
start()
	