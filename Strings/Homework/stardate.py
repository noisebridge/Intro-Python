#!/usr/bin/env python

"""
hw_strings_01.py

Assignment: Create a program that will prompt the user for a date and convert that date into stardate

Rules for computing stardate.

1. Stardate is a number composed of 4 digits followed by a . and then three more digits.
2. The first four digits are the year the user gave.
3. The number after the period is the percentage of days that have passed in the year. 

Example Dec 01, 2011 would be converted to stardate 2011.91
That is computed by using Dec 1, 2011 is the 335th day of the year and this year has 365 days
So 365/335 = .91 or 91% 

I have added some code to help you compute dates. 

Secondly to do math with decimals you will have to cast your numbers as floats.

I have included an example.

"""

import datetime

def main():
    #compute the number of days in a year. In your final product
    # you will need to use the actual year the user inputs.
    daysInTheYear = datetime.date(2011,12,31).strftime("%j")

    ''' 
    Example only This doesnt need to be in your answer.
    Test with 30 questions and you got 23 correct. You will need to
    type cast the values as floats so you can get the percentage correct.
    Then to get the percentage number you should cast it back as a
    integer. 
    '''
    questionsTotal = "30"
    questionsCorrect = 23
    testScore = float(questionsCorrect) / float(questionsTotal)
    testScore = int(testScore * 100)
    




if __name__ == '__main__':
    main()