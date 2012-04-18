''' 
Starting off with the answer to last weeks assignment. We are going to import the file words.txt 
and print it out on the screen. We want to place our import statements at the top of our file. 
While not syntatically required it is a good coding practice and follows PEP8. 

PEP8 is a really short document that outlines the formatting of good python code. 
http://www.python.org/dev/peps/pep-0008/
'''

import os # we need the os module to control directories. 
from os import path


welcomeMsg = "Welcome to Jargon"
msgSize = len(welcomeMsg)
screenWidth = 80



BoxTop = '+{0}+'.format('-' * (msgSize +2))
msgRow = '|{0:^{1}}|'.format(welcomeMsg, msgSize+2)

print '{0:^{1}}'.format(BoxTop, screenWidth)
print '{0:^{1}}'.format(msgRow, screenWidth)
print '{0:^{1}}'.format(BoxTop, screenWidth)

# Get full path to the jargon file
gameLocation = path.abspath(__file__)

# Lets get the game directory
gameDirectory = path.dirname(gameLocation)


# change directory to current directory
os.chdir(gameDirectory)

# Now that we know we are are we can open the file from here.
gameFile = open("../includes/words.txt") # Leaving out r because it is the default.

# Read in the data from the file
gameData = gameFile.read()
# print game data
print gameData