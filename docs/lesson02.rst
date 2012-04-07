================
Making Decisions
================
This weeks lesson is going to focus on decision making in Python. In python like many other languages decisions are also known as `conditional programing <http://en.wikipedia.org/wiki/Conditional_(programming)>`_. I think this is easily explained by an example. If you go to github.com one of the first things github does is perform a test to see if you are logged in. If you are logged in it will show your personal page. If you have not logged in that it shows your the signup page. 

We can do the same thing in python.::
	YOURNAME = 'Kellan'
	username = raw_input('Please tell me your name: ')
	if (username == YOURNAME):
		print "Welcome %s" % (username)
In this example we are testing to see if the value that the user enters is the same as as the value we stored in our program. In my example above I used my name Kellan.