#!/usr/bin/env python

class Boards(object):
	''' Prints the game board for our jargon game'''
	def __init__(self,secretWord, wordsize=5, guesses=5):
		self.wordsize = wordsize
		self.guesses = guesses
		self.board = []
		self.secretWord = secretWord
		self.attempt = 0
		for i in range(guesses):
			self.board.append(['*'] * self.wordsize)

	def __str__(self):
		self.strboard = '+' + "---+" * self.wordsize + '\n'
		for row in range(self.guesses):
			self.strboard += '|'

			for col in range(self.wordsize):
				self.strboard += ' %s |' % (self.board[row][col]) 

			self.strboard += '\n+' + "---+" * self.wordsize + '\n'
		return self.strboard


