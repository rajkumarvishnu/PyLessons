line_width = 80
exercise_count=24
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################

def break_words(stuff):
	"""This function will break words for us"""
	words = stuff.split(' ')
	return words
	
def sort_words(words):
	"""sorts the words"""
	return sorted (words)
	
def print_first_word(words):
	"""prints the first word after popping it off"""
	word = words.pop(0)
	print word
	
def print_last_word(words):
	"""prints the last word after popping it off"""
	word= words.pop(-1)
	print word

def sort_sentence(sentence):
	"""Take a fill sentence and returns sorted words"""
	words=break_words(sentence)
	return sort_words(words)

def print_first_and_last(sentence):
	"""prints the first and last words of a sentence"""
	words=break_words(sentence)
	print_first_word(words)
	print_last_word (words)

def print_first_and_last_sorted(sentence):
	"""sorts the words then prints the first and last one"""
	words=sort_sentence(sentence)
	print_first_word(words)
	print_last_words(words)
	
	
	
	
	