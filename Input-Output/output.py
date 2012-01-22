#!/usr/bin/env python

"""
Examples of Simple output in python

To prompt the user for input we use the built in fuction raw_input(Prompt).
In some scripts you might see input insted. input expects a valid python 
expression. Because we can not expect our user to always type a valid expression
we should always use raw_input. In Python 3.0 this has changed and input should
be used. 
"""

print __doc__

apples = 0.99
oranges = 0.59
Var1 = "Hello"
Var2 = "World"

# Print to scren
print 'Hello World!'

#print Blank Spaces
print ' '
print apples
print oranges
print 4
print 5.50
print' '

print 'Apples $' + str(apples) + 'lb'
print 'Oranges $' + str(oranges) + 'lb'
print' '

# Basic Addition
print "Basic Addition"
print "print 2 + 3"
print 2 + 3
print' '

# Basic Subtraction
print "Basic Subtraction"
print "print 5 - 2"
print 5 - 2
print' '

# Basic Multiplication
print "Basic Multiplication"
print "print 5 * 2"
print 5 * 2
print' '

# Basic Division
print "Basic Division"
print "print 9 / 3"
print 9 / 3
print' '

# Basic Exponents
print "Basic Exponents"
print "print 3 ** 3"
print 3 ** 3
print' '

