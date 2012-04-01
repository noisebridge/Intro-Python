"""
More examples of printing output to the screen in python. In this file we will
use simple math in our output. We will also see how to surpress the new line
character. Lastly we will make our life easier with some variables.
"""

# Shows printing the docstring
print __doc__

print "My dinner check comes to $24.50"
print "A 10 percent tip: ", 24.5 * .1
print "A 15 percent tip: ", 24.5 * .15
print "A 20 percent tip: ", 24.5 * .2

print '-' * 40
dinnerTotal = 24.5
salesTax = dinnerTotal * .09
tipAmount = dinnerTotal * .15
grandTotal = dinnerTotal + salesTax + tipAmount
print "Dinner Total: $", dinnerTotal
print "Sales Tax $", salesTax
print "15 percent tip: $", tipAmount
print "Grand Total $", grandTotal