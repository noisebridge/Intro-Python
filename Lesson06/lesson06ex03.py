#!/usr/bin/env python
''' 
This loop is the same as before but by using the while True syntax we don't 
need to prime the loop with a dummy value. Also by using a break statement we
avoid the extra print statement when the user exits the program. 
'''

if __name__ == '__main__':

    while True:
        better = raw_input('Enter a Word: ')
        if not better: break
        print 'You entered: %s' % (better)