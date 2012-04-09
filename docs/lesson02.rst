================
String Formating
================

This week we are going to continue working with strings. First we need to define a what a string is. A string is simply a sequense of characters. In python we identify strings of text by enclosing them in either single or double quotes.
::
	'This is a string'
	"This is also a string"
	"$4.95"

String Catination
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
You can't concatinate numbers. Insted python will add them mathamatically. 

String Slicing
--------------
We can slice strings up easily in python by following the string with square brackets. Inside the square brackets there are three optional arguments seperated by colons. The first argument is the start of the first character of the slice. In python we start counting at zero and not one. string[1] will print the second character in the string. 

The second number after the first colon is the ending spot of the slice. It is non-inclusive. So if you want to print the first 5 characters of a slice you can use string[:5]. It will start at the beinging and go to the the end of the range leaving out the last number. In this case a string[:5] will print out the characters in posisitions 0,1,2,3,4. For a total of 5 characters from the string.

Lastly the third optional argument is the step. so if you had a string '123456789' and you only wanted to print the even numbers you could use '123456789'[1::2] You would use the 1 to start your selection at the second position and the 2 to only select every second value.
::
	"Supercalifragilisticexpialidocious"[0]
	"Supercalifragilisticexpialidocious"[0:5]
	"Supercalifragilisticexpialidocious"[::2]
	"Supercalifragilisticexpialidocious"[-5]

Strings are Immutable
---------------------
In python strings are immutable which basically means that once a string is created it can't be changed. Insted python has to make a new copy of the string if you want to modify it. 
>>>string = "MyString"
'mystring'



