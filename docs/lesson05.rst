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
One of the reasons that python is easier to learn than other languages is because they do not mark blocks of code with curly braces {}. Python instead has chosen to omit the curly braces in favor of using indention_ to mark blocks of code. This stops many errors that users of other languages often experience because they forgot to add a closing }. The rules for indention can be found in PEP8_. The rules are pretty simple. In python it is preferred that we indent blocks of code with 4 spaces instead of tabs. Each level of indention is 4 spaces deeper than the one level higher. 
::
    if True:
        print "This statment always Runs"
        print "This statment also runs"
    if False:
        print "This statement never runs"
    print "This runs too"

There are several places in python where we will learn about different types of blocks of code.

Command Line Arguments
======================
Before we get into the main topic of making decisions I want to go over another python built in method. The builtin sys module gives you a builtin list named argv that stores the command line arguments passed when your script is run.
::
    #!/usr/bin/env python
    ''' 
    Takes username from a command line argument. Prints Welcome username
    '''
    # Import argv so we can parse command arguments
    from sys import argv
    if __name__ == '__main__':

        # Unpack command line variables
        script, username = argv
        print "Hello {0}".format(username)

This takes one command line argument and passes it to the value username. Try this example without passing a value or passing more than one value and see what happens. 

While there are better ways to fix this error in the future lets use this weeks new skill.

Making Decisions
================
In computer programing one way we control our system is by making simple decisions. The method for making decisions is based on writing a simple test. Each test is evaluated for truthfulness. If the test results in a true value we take one path, If not we go in another. 

::
    if SOMETEST:
        Do something

In our example from above we know that argv needs to have two values in it. So we can test the len of argv and see if it equals 2

::
    #!/usr/bin/env python

    # Import argv so we can parse command arguments
    from sys import argv

    if __name__ == '__main__':
        if len(argv) == 2:
            # Unpack command line variables
            script, username = argv
            print "Hello {0}".format(username)

While this gets rid of our error it is not very helpful. When the user types the wrong number of arguments. It would be better to give the user some feedback.





.. _indention: http://www.python.org/dev/peps/pep-0008/#indentation
.. _PEP8: http://www.python.org/dev/peps/pep-0008/
