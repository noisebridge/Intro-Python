#!/usr/bin/env python

"""
jargon02.py

Modify your jargon module from the last lesson. The new version should take a 
string from the user and center it in a box on the screen

The box should have at least 10 characters of padding on each side of the screen
assume the users screen is 80 characters. I copied my solution from the last 
homework assignment. You should use your code over mine.

Example Run:
Please enter a string: You never forget your first doctor

          +----------------------------------------------------------+
          |            You never forget your first Doctor            |
          +----------------------------------------------------------+

"""

lenght = int(raw_input("Enter length: "))
width = int(raw_input("Enter width: "))
fillChar = raw_input("Enter fill character: ")
screenWidth = 80
padding = ' ' * ((screenWidth - lenght) / 2)
topRow = '+' + '-' * (lenght - 2) + '+' 
fillRows = '|' + fillChar * (lenght - 2) + '|' + '\n'

print topRow
print fillRows * (width - 2),
print topRow