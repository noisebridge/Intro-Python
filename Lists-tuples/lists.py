#!/usr/bin/env python

"""
list_example.py
Examples that will be used in showing lists in python. 
Created by Kellan Jacobs on 2011-12-10.
"""

def main():
    # Create a list of numbers 1 - 10
    numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] 
    unsorted = [4, 2, 9, 6, 7, 1]
    mixed = ['Kellan', 36, ['a', 'b']]
    who = 'You never forget your first doctor'.split()


    # Slicing works for lists too
    print 'Slicing works: %s' % (numbers[3:5])

    # Print every other item in a list
    print 'Print Every other item: %s' % (numbers[::2])


    # number of items in list
    print "Items #: %s" % (len(numbers))

    # Assignment to list postition
    print 'Mixed List: ' + str(mixed)
    mixed[2] = 'Jacobs'
    print 'Mixed List after assignment: %s' % (mixed)

    # Delete item from list
    del mixed[1]
    print 'After Delete: %s' % (mixed)

    mixed.append('DOB: 11/05/1975')
    print 'Adding to list: %s' % (mixed)

    # Find first occurance of a list item
    print 'Who List: %s' % (who)
    print 'forget occurs at: %s' % (who.index('forget'))

    # Insert into a list
    mixed.insert( 1, 'Daniel')
    print 'Insert into list: %s' % (mixed)

    # Sort a list
    unsorted.sort()
    print 'Sorted List: %s' % (unsorted)



if __name__ == '__main__':
    main()