================
Making Decisions
================
This weeks lesson is going to focus on decision making in Python. In python like many other languages decisions are also known as `conditional programing <http://en.wikipedia.org/wiki/Conditional_(programming)>`_. I think this is easily explained by an example. If you go to github.com one of the first things github does is perform a test to see if you are logged in. If you are logged in it will show your personal page. If you have not logged in that it shows your the signup page. 

We can do the same thing in python.
::
    YOURNAME = 'Kellan'
    username = raw_input('Please tell me your name: ')
    if username == YOURNAME:
        print "Welcome %s" % (username)
In this example we are testing to see if the value that the user enters is the same as as the value we stored in our program. In my example above I used my name Kellan.

Indention in Python
===================
One of the reasons that python is easier to learn than other languages is because they do not mark blocks of code with curley braces {}. Python insted has chosen to obmit the curley braces in favor of using indention_ to mark blocks of code. This stops many errors that users of other languages offen experience because they forgot to add a closing }. The rules for indention can be found in PEP8_. The rules are pretty simple. In python it is perfered that we indent blocks of code with 4 spaces insted of tabs. Each level of indention is 4 spaces deeper than the one level higher. 
::
    if True:
        print "This statment always Runs"
        print "This statment also runs"
    if False:
        print "This statement never runs"
    print "This runs too"

There are several places in python where we will learn about different types of blocks of code.



.. _indention: http://www.python.org/dev/peps/pep-0008/#indentation
.. _PEP8: http://www.python.org/dev/peps/pep-0008/
