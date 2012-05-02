#!/usr/bin/env python
''' 
There are other types of tests you can do. While we have not covered lists
yet we can check to see if an item is in a list
'''

# Import argv so we can parse command arguments
from sys import argv



if __name__ == '__main__':

    friends = ['kellan', 'Sam', 'Joe']
    login = raw_input('Type your login name: ')
    if login in friends:
        print "You are logged in"
    else:
        print "You are not welcome here"
