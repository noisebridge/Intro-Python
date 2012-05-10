#!/usr/bin/env python
''' 
Prompt the user until they enter just hit enter without typing anything.
'''

if __name__ == '__main__':

    # Prime the loop with a dummy value
    word = 'dummy'
    while word:
        word = raw_input('Enter a Word: ')
        print 'You entered: %s' % (word)