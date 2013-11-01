line_width = 80
exercise_count=14
##########################################################################
print "="*line_width
print "Start of exercise", exercise_count
exercise_count+=1
print "="*line_width
##########################################################################


from sys import argv

script, user_name = argv

prompt = '>'

print "Hi %s, I'm the %s script." % (user_name, script)

print "I'd like to ask you a few questions"

print "Do you like me %s" %user_name
likes=raw_input(prompt)

print "Where do you live %s?" %user_name
lives= raw_input(prompt)
print "What kinda computer you've gotten"
computer=raw_input(prompt)

print '''
Alright, so you said %r about liking me.
you live in %r. Not sure where that is.
And you have a %r computer. Nice
'''%(likes, lives, computer)

