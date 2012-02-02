#!/usr/bin/env python

"""
jargon02.py

Modify your jargon module from the last lesson. The new version should take a 
string from the user and center it in a box on the screen

The box should have at least 10 characters of padding on each side of the screen
assume the users screen is 80 characters

Example Run:
Please enter a string: You never forget your first doctor

          +----------------------------------------------------------+
          |            You never forget your first Doctor            |
          +----------------------------------------------------------+
"""

userMsg = raw_input("Enter your message: ")

screenWidth = 80
padding = ' ' * 10
topRow = '+' + '-' * (58) + '+' 
fillRows = '|' + '{0:^58}'.format(userMsg) + '|'

print padding + topRow
print padding + fillRows
print padding + topRow