#!/usr/bin/env python

"""
Strings Examples

This week continues where we left off working with strings. This week we will 
cover string slicing, and a little bit of string formatting.

"""

firstName = "Rose"
lastName = "Tyler"

areaCode = 212
exchange = 664
numSuffix = 7665

print "We can cancatinate strings with the + sign"
print "fullName = firstName + lastName"
fullName = firstName + lastName
print 'Full Name: ' + fullName
print ' '

print "You can't cancatinate numbers like string"
print "wrongNumber = areaCode + exchange + numSuffix"
wrongNumber = areaCode + exchange + numSuffix
print 'Wrong Number: %s' % wrongNumber
print ' '

print 'String can be sliced using slice notation'
print 'Slice Notation is [start:exclusive end]'
print 'firstName[0]'
print firstName[0]
print 'firstName[0:3] excludes last character'
print firstName[0:3]
print ' '

print 'We can print the last char of a string using negative numbers'
print 'firstName[-1]'
print firstName[-1]
print ' '

print "Skip first three characters"
print "fullName[3:]"
print fullName[3:]
print ' '

print "Print First 4 Characters"
print "fullName[:4]"
print fullName[:4]

# Format a phone number
print '({0}) {1}-{2}'.format(areaCode,exchange,numSuffix)

# First Initial Last name
print '{0}. {1}'.format(firstName[0],lastName)

# Left Aligned
print '*' + '{0:<30}'.format("Doctor Who") + '*'

# Centered
print '*' + '{0:^30}'.format("Doctor Who") + '*'

# Right Aligned
print '*' + '{0:>30}'.format("Doctor Who") + '*'
