#!/usr/bin/env python
''' 
Takes username from a command line argument. Prints Welcome username
Program will deliver an error is the user does not pass in one value.
'''

# Import argv so we can parse command arguments
from sys import argv



if __name__ == '__main__':

    if len(argv) == 2:
        # Unpack command line variables
        script, username = argv
        print "Hello {0}".format(username)
    else:
        print "One argument required you provided {0}".format(len(argv))
