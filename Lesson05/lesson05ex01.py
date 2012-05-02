#!/usr/bin/env python
''' 
Takes username from a command line argument. Prints Welcome username
'''

# Import argv so we can parse command arguments
from sys import argv



if __name__ == '__main__':

    # Unpack command line variables
    script, username = argv
    print "Hello {0}".format(username)
