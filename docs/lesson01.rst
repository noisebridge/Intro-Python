==========================
Lesson 01 Input and Output
==========================

Welcome to your first lesson on Begining Python. Our first lesson we will focus on simple input and output. 

input
	getting information into your program.
output
	getting data out of your program.

Lets get started writing our first python program

Hello World
===========
It is tradition to make your first program in any new language simply have the computer print the text Hello World on the screen. In python this is really simple. 

Type the following
::
	print "Hello World!"

This reserved word print tells python to print out whatever is on the rest of the line. When we want to print text we need to enclose it in either single or double quotes. 

Commenting Code
===============
As good programers we should comment our code. There are two ways to comment code in python. The first option is to start a comment with a # sign. Whenever python encounters a # it will treat all the text to the end of the line as a comment. 
::
	# This is a comment
	print "Not a comment" # This text is a comment

Documentation Strings
---------------------
The second type of python comment is called a documentation string or docstring for short. Docstrings are multiline comments and always start and end with tripple single/double quotes. 

Python also reads the first docstring in a file and assigns it to a varable. `__doc__`