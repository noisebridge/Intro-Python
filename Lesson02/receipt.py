'''
There is no homework assignment this week for the Eliza program. Because of that
I would like to you practice formating a receipt. This is straight up string 
formating practice.
When complete restaurant name and phone number should be centered.
The items ordered should be left aligned with the prices right aligned.
Continue on from last week with adding total, 15% tip and a 9% sales tax.
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
dessert = "Chocolate Cake"
dessertPrice = 6.0

# Lets center the text on the receipt.
topRow = "+{0}+".format('-' * receiptWidth)
name = "|{0:^40}|".format(RESTAURANT)
phoneNumber = "({0}) {1}-{2}".format(prefix,exchange,number)
firstItem = "|{0:20}{1:20.2f}|".format(entree,entreePrice)
secondItem = "|{0:20}{1:20.2f}|".format(beverage,beveragePrice)
thirdItem = "|{0:20}{1:20.2f}|".format(dessert,dessertPrice)

print topRow
print name
print "|{0:^40}|".format(phoneNumber)
print firstItem
print secondItem
print thirdItem
print topRow