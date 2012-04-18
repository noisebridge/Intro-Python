=====================
File Input and Output
=====================
So far we have learned how to store information in variables in our program and we have even learned how to prompt the user for information to add to our program. In this lesson we are going to learn how to get data and store data in files on our system. The good news is that python has all the features we need built in to make this process painless. 

Python Builtin
--------------
Python gives us serveral `built-in functions`_ helpers to make doing complex things that are very common in programing easier. Open up your interactive prompt. 

>>> dir()
['__builtins__', '__doc__', '__name__', '__package__']

The dir() built-in can tell us about any python object. When we call it just like I did above it will return the current namespace. Now try typing the following

>>> dir(__builtins__)
['ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BufferError', 'BytesWarning', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'NameError', 'None', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'ReferenceError', 'RuntimeError', 'RuntimeWarning', 'StandardError', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'ZeroDivisionError', '_', '__debug__', '__doc__', '__import__', '__name__', '__package__', 'abs', 'all', 'any', 'apply', 'basestring', 'bin', 'bool', 'buffer', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'cmp', 'coerce', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'execfile', 'exit', 'file', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'intern', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'long', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'raw_input', 'reduce', 'reload', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'unichr', 'unicode', 'vars', 'xrange', 'zip']

Each one of these objects is something python gives us for free without typing a single bit of code. We are not going to cover them all in this lesson but it helps to know they are there. If you look at the long list above you will see help. Lets give that one a try.
::
	>>> help
	Type help() for interactive help, or help(object) for help about object.

	>>> help()
	Welcome to Python 2.7!  This is the online help utility.

	If this is your first time using Python, you should definitely check out
	the tutorial on the Internet at http://docs.python.org/tutorial/.

	Enter the name of any module, keyword, or topic to get help on writing
	Python programs and using Python modules.  To quit this help utility and
	return to the interpreter, just type "quit".

	To get a list of available modules, keywords, or topics, type "modules",
	"keywords", or "topics".  Each module also comes with a one-line summary
	of what it does; to list the modules whose summaries contain a given word
	such as "spam", type "modules spam".

As you can see python has a built in help system. Lets play with the help system and see if we can find the tools we need for tonight.
::
	help> open
	Help on built-in function open in module __builtin__:

	open(...)
	    open(name[, mode[, buffering]]) -> file object
	    
	    Open a file using the file() type, returns a file object.  This is the
	    preferred way to open a file.  See file.__doc__ for further information.

	help> file
	Help on class file in module __builtin__:

I cut the text but this looks like exactly what we need. What is importiant to take away from this is that we can play and try out code in the interactive prompt in python. Now that we found the function we need lets leave the help function by typing quit.

>>> import os # Import the OS Module. Lets do this all in the interactive prompt
>>> os.getcwd() # This will tell you where python has set your current directory.
'/home/kellan/Documents/Intro-Python'
>>> os.chdir('Lesson03')
>>> os.getcwd()
'/home/kellan/Documents/Intro-Python/Lesson03'

Python built in OS_ module gives you built in functionallity to interact with the under lying operating system. The huge advantage of the OS module is that you don't have to know different code for windows, mac or linux. 

Creating Files
--------------
To interact with files in python the first thing we need to do is tell python the file exists. The way we do that is by using the open method. The open method creates a file object. Which is just a fancy way of saying it creates a pointer to an object on the system. We store this pointer in a standard python variable. We need to tell python which mode to open the file in. The three that you will use most commonly is read, write and seek. 

>>> open('myfile.txt', 'w')
>>> dir(f)
['__class__', '__delattr__', '__doc__', '__enter__', '__exit__', '__format__', '__getattribute__', '__hash__', '__init__', '__iter__', '__new__', '__reduce__', '__reduce_ex__', '__repr__', '__setattr__', '__sizeof__', '__str__', '__subclasshook__', 'close', 'closed', 'encoding', 'errors', 'fileno', 'flush', 'isatty', 'mode', 'name', 'newlines', 'next', 'read', 'readinto', 'readline', 'readlines', 'seek', 'softspace', 'tell', 'truncate', 'write', 'writelines', 'xreadlines']
>>> f.write("Christopher Eccleston\n")
>>> f.write("David Tennant\n")
>>> f.write("Matt Smith\n")

Here we wrote three lines of text to out file we created with the open command. We need to add "\n" because python doesn't automatically add the newline character at the end of the line. When we are done using a file we need to tell python we are done by using the close command.

>>> f.close()

After you type close go ahead and open up a new terminal window and lets check out the file we created
::
	cat myfile.txt
	Christopher Eccleston
	David Tennant
	Matt Smith

Now that we have closed the file we can open it up again for reading.

>>> f = open('myfile.txt', 'r')
>>> f.read() # Reads file in as a string
'Christopher Eccleston\nDavid Tennant\nMatt Smith\n'
>>> f.read()
''

The first time we read the file it read it in a complete string. The second time we tried it we got an empty string. Why is that? When we open a file in python there is a pointer of the location we are reading at in the file. When we use the read command we read the whole file and it places the pointer at the end of the file. There is no more data to be read when we try to read it a second time. We can open the file up more than once though.

>>> f = open('myfile.txt', 'r')
>>> f.read() # Reads file in as a string
>>> f = open('myfile.txt', 'r')
>>> f.read() # Reads file in as a string
>>> f.close()
<built-in method close of file object at 0x7fe8b1827390>

We can use the readline method to read only one line at a time. Each time we read a line from the file we get one line up until the newline characer.

>>> f = open('myfile.txt', 'r')
>>> f.readline()
'Christopher Eccleston\n'
>>> f.readline()
'David Tennant\n'
>>> f.readline()
'Matt Smith\n'
>>> f.readline()
''

There are several more methods for dealing with file input and output. We will cover them as we learn about new datatypes in python. For the moment lets move on to our homework.

Homework
========

This weeks assignment we are going to return back to our Jargon game. Inside the files provided for class there is a folder called includes. It has the game data file we we will use for our jargon game. Your assignment for this week is to use the tools we have learned already to import the file into our python program and print out the data on screen. Our program should build on last weeks example. So you should add new code to your game and not start from scratch. 






.. _`built-in functions: http://docs.python.org/library/functions.html
.. _OS: http://docs.python.org/library/os.html