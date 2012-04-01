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
It is tradition to make your first program in any new language simply have the computer print the text Hello World on the screen. In python this is really simple. *Sample code in Lesson01/exp01.py*

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

Math in Python
==============
In python you can use simple math like this
::
	print 2 + 3
	5
notice that numbers do not have quote marks around them. 

+----------+-----------+---------+--------+
| Operator | Operation | Example | Result |
+==========+===========+=========+========+
|     +    |  Addition |  3 + 2  |    5   |
+----------+-----------+---------+--------+
|     -    |  Subtract |  3 - 2  |    1   |
+----------+-----------+---------+--------+
|     *    | Multiply  |  3 * 2  |    6   |
+----------+-----------+---------+--------+
|     /    | Division  |  6 / 2  |    3   |
+----------+-----------+---------+--------+
|     %    |  Modulus  |  5 % 3  |    2   |
+----------+-----------+---------+--------+
|    **    |  Exponent |  3 ** 2 |    9   |
+----------+-----------+---------+--------+

Variables in Python
===================
Variables are holding places for values. Just like in high school math class you can assign a value to a variable **x = 3** In python variable names must start with a letter. They can contain any letter or number and the _ character. No other characters can be in the variable name. Pythons variables are case sensitive. Which means MyVar myvar and MYVAR are all different variables. 

In python you do not need to declare what type of variable it is like you do in other languages. You assign a value to a variable with the assignment operator which is the equal sign
::
	price = 4.95
	myName = "Kellan"
	someVar = myName

String Formating
================
While we will cover string formating in a later lesson I have included a little bit of string formating in our examples. I will fill in this section of the docs later.

Getting User Input
==================
Prompting the user for input is quite easy in python. You can use `raw_input()` to prompt the user for to input data. 
::
	print "Please enter a value:"
	myVar = raw_input()
This can be combined into one statement making your code easier to type.
::
	myVar = raw_input("Please enter a value: ")


Homework
========
Each week we will have homework assignments that invlove using the skills we learned this week. Each assignment will be a building block of one of the two games we will be building over the course. 

Homework Assignment #1 Eliza
----------------------------
We are going to create an Eliza_ chatbot. Eliza is a simple interactive script that acts as a thearipist. She takes a response from the user and turns the words around to simulate a real conversation. 

1. Create a file eliza.py
2. Prompt your user for their name.
3. Welcome the user by name to your office and ask them what their problem is. 

**Example Run**
::
	Hello can I have your name: Kellan
	Hi Kellan I am Eliza your thearipist. Please come into my office and have a seat on the couch. Great now that you are comfortable please tell me what is troubling you:

.. _Eliza: http://en.wikipedia.org/wiki/ELIZA

Homework Assignment #2 Jargon
-----------------------------
The second game we are going to create is called Jargon. It is a word guessing game mixed with mastermind. One importiant part of this game will be drawing the gameboard on screen. For your first assignment will be to draw a box on screen. 
1. Create a file named jargon.py
2. Prompt the user for the box width
3. Prompt the user for the box height
4. Use these values to draw a box centered on the screen
5. For the purpose of centering the box assume the screen width is 80 characters wide.

**Example Run**
::
	Please give me a width: 40
	Please give me a height: 3
	               +--------------------------------------+
	               |                                      |
	               +--------------------------------------+
