#!/usr/bin/env python

"""
Create an module that asks the user for a lenght and width and chacter. 
Use these values to print out a box in these dementions. Use the character
the user gives you to fill the box. Extra credit if you print the box border 
and only use the fill character in to fill the box. Extra Extra credit if you
center the box.

+----------+
|**********|  Extra Credit Example for 12 x 4 box
|**********|
+----------+

Example Run of the program...

Please enter a Length: 50
Please enter a Width: 15
Enter your fill character: *

**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
**************************************************
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