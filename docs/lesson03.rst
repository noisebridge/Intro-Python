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

>>> help
Type help() for interactive help, or help(object) for help about object.
::
	>>> help()
	``Welcome to Python 2.7!  This is the online help utility.

	If this is your first time using Python, you should definitely check out
	the tutorial on the Internet at http://docs.python.org/tutorial/.

	Enter the name of any module, keyword, or topic to get help on writing
	Python programs and using Python modules.  To quit this help utility and
	return to the interpreter, just type "quit".

	To get a list of available modules, keywords, or topics, type "modules",
	"keywords", or "topics".  Each module also comes with a one-line summary
	of what it does; to list the modules whose summaries contain a given word
	such as "spam", type "modules spam".``

.. _`built-in functions: http://docs.python.org/library/functions.html