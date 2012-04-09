'''
Continue working on printing our receipt
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

# Lets center the text on the receipt.
print "+{0}+".format('-' * receiptWidth)
print "|{0:^40}|".format(RESTAURANT)
print "+{0}+".format('-' * receiptWidth)

print '-'*80

# With the old method
print "+%s+" % ('-' * receiptWidth)
print "|%s|" %(RESTAURANT.center(40))
print "+%s+" % ('-' * receiptWidth)