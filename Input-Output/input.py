#!/usr/bin/env python

"""
Examples of Getting user input in Python

To prompt the user for input we use the built in fuction raw_input(Prompt).
In some scripts you might see input insted. input expects a valid python 
expression. Because we can not expect our user to always type a valid expression
we should always use raw_input. In Python 3.0 this has changed and input should
be used. 
"""

print __doc__

#Prompt the user for input
userData = raw_input('Enter your name: ')
print "Hello " + userData + "!"