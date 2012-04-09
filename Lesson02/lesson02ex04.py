'''
Each String formating method will be shown twice. Once using string formating
expressions and using the newer string formatting method.
'''

RESTAURANT = "Kellan's Fine Dining"
receiptWidth = 40
prefix = 415
exchange = 944
number = 1212
entree = "Steak"
entreePrice = 16.95
beverage = "Glenlivet Scotch"
beveragePrice = 7.5
desert = "Chocolate Cake"
desertPrice = 6.0

# Using the new format method.
print '{0}'.format(RESTAURANT)

# Formating the phone number
print '{0}-{1}-{2}'.format(prefix, exchange, number)

print '-'*80
# Using the old method.
print '%s' % (RESTAURANT)
print '%s-%s-%s' % (prefix, exchange, number)


