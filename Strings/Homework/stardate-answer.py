#!/usr/bin/env python

"""
stardate.py

Assignment: Create a program that will prompt the user their birthdate. Take 
their birthdate and convert it to a stardate using the rules from StarTrek TNG

Rules for computing stardate.

1. Stardate is a number composed of 4 digits followed by a . and then up to 
   3 more digits
2. The first four digits are the year on the gegorian calendar
3. The number after the period is the percentage of days that have passed in 
   that year. 

If for example I was born on June 30, 1985. The stardate would be 1985.49
As 49% of the year has passed. 
June 30 was the 181st day of the year
In 1985 there were 365 days in the year
181/365 = 0.4958904109589041 or 49.5%

I have added some code to help you compute the numbers of days in the year.

Example Run:
Please enter your birthdate in MM/DD/YYYY format: 06/30/1985
You were born on StarDate 1985.49
 
"""
# inport date from datetime module
from datetime import date

# Prompt for users birthdate
birthdate = raw_input("Please enter your birthdate in MM/DD/YYYY format: ")
birthMonth = int(birthdate[:2])
birthDay = int(birthdate[3:5])
birthYear = int(birthdate[6:])

daysInTheYear = float(date(birthYear,12,31).strftime("%j"))
daysPassed = float(date(birthYear,birthMonth,birthDay).strftime("%j"))
dayPercent = (daysPassed / daysInTheYear) * 100
print 'You were born on StarDate: {0}.{1}'.format(birthYear, int(dayPercent))