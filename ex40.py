cities ={'CA':'San Franssisco', 'MI':'Detroit', 'FL':'jacksonville'}

cities ['NY'] = 'new york'
cities ['OR'] = 'Portland'

def find_city(themap, state):
	if state in themap:
		return themap[state]
	else:
		return "Not found"
		
cities['_find'] = find_city

while True:
	print "state ?"
	state= raw_input(">")
	
	if not state: break
	
	city_found = cities ['_find'] (cities,state)
	print cities['_find']	
	print city_found