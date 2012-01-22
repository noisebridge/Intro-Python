#!/usr/bin/env python

"""
tuple_example.py
Examples that will be used in showing lists in python. 
Created by Kellan Jacobs on 2011-12-28.
"""

'''
Tuples are just like lists with one major different. They are immutable. Which
is just a fancy way of saying that after you make one you can't change it.
We use tuples when we want to return a data set to our program that shouldn't
be changed. Good Examples are settings, Or when you write code to share with
someone else.
'''

#Tuples look like lists except for they are enclosed in () insted of []
tupl01 = (1, 2, 3, 4, 5, 6, 7, 8)
tupl02 = ('A', 'B', 'C')

print "Tuple 01: ", tupl01
print "Tuple 02: ", tupl02

'''
You can add tuples to create a new tuple
'''

tupl03 = tupl01 + tupl02
print "Tuple 03:", tupl03

print "Tuple Sliced: ", tupl03[::2]




