=================
All About Strings
=================

This week we are going to continue working with strings. First we need to define a what a string is. A string is simply a sequence of characters. In python we identify strings of text by enclosing them in either single or double quotes.
::
	'This is a string'
	"This is also a string"
	"$4.95"

String Catenation
-----------------
We can combine two strings using the + sign.
::
	first = "Matt"
	last = "Smith"
	fullName = first + last
	print fullName

	areaCode = 415
	prefix = 944
	phone = areaCode + prefix
You can't concatenate numbers. Instead python will add them mathematically. 

String Slicing
--------------
We can slice strings up easily in python by following the string with square brackets. Inside the square brackets there are three optional arguments separated by colons. The first argument is the start of the first character of the slice. In python we start counting at zero and not one. string[1] will print the second character in the string. 

The second number after the first colon is the ending spot of the slice. It is non-inclusive. So if you want to print the first 5 characters of a slice you can use string[:5]. It will start at the beginning and go to the the end of the range leaving out the last number. In this case a string[:5] will print out the characters in positions 0,1,2,3,4. For a total of 5 characters from the string.

Lastly the third optional argument is the step. so if you had a string '123456789' and you only wanted to print the even numbers you could use '123456789'[1::2] You would use the 1 to start your selection at the second position and the 2 to only select every second value.
::
	"Supercalifragilisticexpialidocious"[0]
	"Supercalifragilisticexpialidocious"[0:5]
	"Supercalifragilisticexpialidocious"[::2]
	"Supercalifragilisticexpialidocious"[-5]

Strings are Immutable
---------------------
In python strings are immutable which basically means that once a string is created it can't be changed. Instead python has to make a new copy of the string if you want to modify it.
::
	>>> string = "MyString"
	'mystring'
	string[3] = 'X'
	TypeError: 'str' object does not support item assignment
You can though save a new string to the same variable.
::
	string = "MyString"
	string = "New String"
It is a small point but one to remember as I have myself created the error above several times when I was not paying close attention. 

String Methods
--------------
Python has several built in methods that make working with strings easier. Because strings are immutable it is important to remembered that each time you use one of these string methods it creates a new string.
::
	phrase = "bow ties are cool"
	newString = phrase.upper()
	print newString
	BOW TIES ARE COOL
In the above example I used the upper() method to return a string that is all uppercase. There are several different `string methods`_ that can be used already built into python. Here is a list of some of the methods you might use. There are many more methods than I have included here. Check out the link above and read about the others yourself.

str.capitalize()
	Capitalizes the first character of a string

str.center(width)
	Centers a string in the space of the width given. ex str.center(40) will center the string in a field of 40 characters.

str.format(*args, **kwargs)
	The new method of string formatting introduced in python 2.6

str.ljust(width[, fillchar])
	Left justifies a field.

str.lower()
	Converts a string to lowercase.

str.replace(old, new[, count])
	Used to replace part of a string with another piece.

str.title()
	Converts a string to titlecase ex 'bow ties are cool' would be converted to 'Bow Ties Are Cool'

str.upper()
	Converts a string to uppercase.

String Formating
================
In python 2.6 and later there are two methods of string formating. String Formating Expressions and String Format Method. Both methods perform the same task and the jury is out on which one is better than the other. Using the format method does in some cases give you more options than formating expressions. In this lesson I will show you examples that use both methods. For the rest of the class I will favor the newer format method.

String Formatting Expressions
-----------------------------
In this method we place the string to be formated with one or more embed targets. This is followed by the % binary operator which is followed by a tuple of values to be placed in the embed targets.
::
    "%s cost $%f" % ("Ice Cream Cones", 1.5)
    Ice Cream Cones cost $1.500000
Just like in last weeks example we can set the number of values printed after the decimal. 
::
    "%s cost $%.2f" % ("Ice Cream Cones", 1.5)
    'Ice Cream Cones cost $1.50'

String Formating Method Calls
-----------------------------
This method provides all the same functions as above. The syntax is just a little different. The code above using the newer method looks like this.
::
    "{0} cost {1}".format("Ice Cream Cones", 1.5)
In this method instead of using the % Binary Operator we use curly braces with a number for the positional argument. In some versions of python the numbers can be omitted. To fix the the number of decimals places as we did earlier we write the following code.
::
    "{0} cost ${1:.2f}".format("Ice Cream Cones", 1.5)
We can align our text by adding the alignment characters < , >, =, or ^. These are left alignment, right alignment, padding after the a sign character and centered.
::
    "*{0:<30}*".format('+++')
    "*{0:^30}*".format('+++')
    "*{0:>30}*".format('+++')
    '*+++                           *'
    '*             +++              *'
    '*                           +++*'
We can add a fill character before the alignment character.
::
    "*{0:.<30}*".format('+++')
    '*+++...........................*'
We can use the +, or - sign to show positive and negative values. The - shows only if the value is negative where the + shows the sign when it is either positive or negative. 
::
    "*{0:+10.2f}*".format(1.5)

String formating can get quite complex as you can see. I have read the documentation several times and I still sometimes have a hard time getting it right. So be patient with it. It will start to become clear.

.. _string methods: http://docs.python.org/library/stdtypes.html#string-methods



