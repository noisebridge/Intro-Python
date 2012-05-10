#!/usr/bin/env python
''' 
Another example of a for loop
'''

if __name__ == '__main__':

    member = {'First': 'Kellan', 'Last': 'Jacobs', 'Phone': '(415)-555-1212'}
    for key, value in member.items():
        print "{0}: {1}".format(key, value)