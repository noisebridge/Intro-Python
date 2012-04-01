""" This example explands on the code from our last example. This time we will 
use a little bit of string formatting to get rid of the spaces between the $ 
the ammount. We will also make sure the ammount shows with the proper number of 
decimal places showing. 
"""

dinnerTotal = 24.5
taxPercent = .09

# Print the check header
print "Please pay your server"
# Print a 30 character line seperator
print "-" * 30
print "Your Dinner Total is $%.2f" % (dinnerTotal)
print "Sales Tax $%.2f" % (dinnerTotal * taxPercent)
print "Suggested Gratuity 10%% $%.2f, 15%% $%.2f, 20%% $%.2f"\
	% (dinnerTotal * .1, dinnerTotal * .15, dinnerTotal * .2)

print "You chose a 15% tip"
print "Grand Total %.2f" % (dinnerTotal + dinnerTotal * taxPercent + dinnerTotal * .15)