#!/usr/bin/env python
import os
from os import path
from random import choice

"""
This week we are going to work on on our python game. 
1. Start up the game and read in the game file.
2. Select a random word from the file.
3. Show the user the first letter of the word.
4. Prompt the user for a guess
5. Compare the users guess with the mystery word. 
6. If the user word matches they win, if not show them which letters are correct.
7. User gets 5 guesses
8. Keep playing until the user quits the game.
"""

SCREENWIDTH = 80

def loadwords():
	''' Loads the word data file comes from Lesson03'''
	# Get full path to the jargon file
	gameLocation = path.abspath(__file__)

	# Lets get the game directory
	gameDirectory = path.dirname(gameLocation)

	# change directory to current directory
	os.chdir(gameDirectory)

	# Now that we know we are are we can open the file from here.
	gameFile = open("../includes/words.txt", 'r') 

	# Read in the data from the file
	gameData = gameFile.read()

	# Close the datafile
	gameFile.close()

	# Split the data into a python list
	wordList = gameData.split()

	# Return the wordlist
	return wordList

def draw_welcome(welcome, screensize=80):
	''' Draws the welcome message on the screen for the user. Lesson03 '''
	msgSize = len(welcome)
	BoxTop = '+{0}+'.format('-' * (msgSize +2))
	msgRow = '|{0:^{1}}|'.format(welcome, msgSize+2)

	print '{0:^{1}}'.format(BoxTop, screensize)
	print '{0:^{1}}'.format(msgRow, screensize)
	print '{0:^{1}}'.format(BoxTop, screensize)

def draw_board(guesses, )

if __name__ == '__main__':

	# Load the data file 
	words = loadwords()

	# Draw the game name
	draw_welcome("Let's Play Jargon")

	# Select the mystery word

	
