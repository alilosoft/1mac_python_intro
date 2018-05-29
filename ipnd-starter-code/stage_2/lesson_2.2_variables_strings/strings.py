# Lesson 2.2: Strings

# Strings are sequences of characters that are enclosed in quotes.
# We can enclose them with single or double quotes and assign them
# to variables. We can even combine strings by adding them (we call
# this concatenation).

# https://classroom.udacity.com/nanodegrees/nd000/parts/0001345403/modules/356813882475460/lessons/4192698630/concepts/49819819440923

print 'Hello'
print "Hello"

hello = "Howdy"
print hello

# Add your own code and notes here
s1 = "ab"  # s = 'ab'
s2 = 'cd'
print s1 + s2 # concatenation
print s1 * 3

# String Indexing
# Syntax: <string>[<expr>]
print "string"[0]  # first char 's'
print "string"[-1] # last char 'g'

# Quiz
s = '<any string>'
print s[3] + " " + s[1 + 1 + 1]
print s[0] + " " + (s + s)[0]
print s[0] + s[1] + " " + s[0 + 1]
print s[1] + " " + (s+'ity')[1]
print s[-1] + " " + (s + s)[-1]

# String Sub Sequences
# Syntax: <string>[<start_expr>:<stop_epxr>]
# Note: char at <stop_expr> index is not included
print "string"[0:2] # from 0 to 1 -> 'st'
print "string"[2:] # from 2 to the end -> 'ring'
print "string"[:3] # from the start to 2 -> 'str'
print "string"[3:3] # from 3 to 2 -> ''
print "string"[:] # from the start to the end (useless) -> 'string'
# Quiz
s = "udacity"
print s[3:3]
s = "hi"
print s[3:]
print s[:3]
print s[:-1]
