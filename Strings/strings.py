#!/usr/bin/env python

"""
str_example.py
Examples that will be used in showing strings in python. 
Created by Kellan Jacobs on 2011-12-10.
"""

def main():
    strArea = '415'
    strPrefix = '555'
    strSuffix = '1212'

    numArea = 415
    numPrefix = 555
    numSuffix = 1212

    # Concatinating three strings into one.
    phoneNumber = strArea + strPrefix + strSuffix
    print 'Phone Number: ' + phoneNumber

    # You can not concatinate numbers in the same way.
    wrongNumber = numArea + numPrefix + numSuffix
    print 'Wrong Number: ' + str(wrongNumber)

    # Lets get fancy and add - in the number
    print 'Phone with Dash: ' + strArea + '-' + strPrefix + '-' + strSuffix 

    # We can use the %s to add strings into another string.
    print 'Getting Tricky: (%s) %s-%s' % (strArea, strPrefix, strSuffix)

    # Print First Character in a string
    print 'First Char: ' + phoneNumber[0]

    # Print Last Character:
    print 'Last Character: ' + phoneNumber[-1]

    # Using Slice Notation Last number is non inclusive
    print 'Print #\'s 4-6: ' + phoneNumber[3:6]

    # Skip the first three characters by using open ended notation
    print 'Skip first three: ' + phoneNumber[3:]

    # Print only the first 6 numbers
    print 'First 6: ' + phoneNumber[:6]

    #repeat a string. Print 60 - characters
    print '-' * 60

    # Print a box
    screenWidth = 80
    boxWidth = 40
    padding = (screenWidth - boxWidth) / 2
    print 'Printing a box. This will help with your homework'
    print ' ' * padding + '+' + '-' * (boxWidth - 2) + '+'
    print ' ' * padding + '|' + ' ' * (boxWidth - 2) + '|'
    print ' ' * padding + '|' + ' ' * (boxWidth - 2) + '|'
    print ' ' * padding + '+' + '-' * (boxWidth - 2) + '+'



    


if __name__ == '__main__':
    main()