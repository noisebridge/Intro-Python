================
String Formating
================

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
	Useds to replace part of a string with another piece.

str.title()
	Converts a string to titlecase ex 'bow ties are cool' would be converted to 'Bow Ties Are Cool'

str.upper()
	Converts a string to uppercase.


.. _string methods: http://docs.python.org/library/stdtypes.html#string-methods



