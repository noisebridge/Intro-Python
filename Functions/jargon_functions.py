#!/usr/bin/python
import os
from random import choice

def printHeader():
	# Clear the screen
	os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
	#Print Board Header
	print '\n' * 3
	print ' ' * 10 + '+' + '-' * 48 + '+'
	print ' ' * 10 + '|' + "Welcome to Jargon".center(48) + '|'
	print ' ' * 10 + '+' + '-' * 48 + '+'

def printBoard(a, board):
	if board != []:
		for g in board:	
			print " " * 20 + '+---+---+---+---+---+'
			print " " * 20 + '| %s | %s | %s | %s | %s |' % \
					(g[0],g[1],g[2],g[3],g[4])
	# Print the answer
	print " " * 20 + '+---+---+---+---+---+'
	print " " * 20 + '| %s | %s | %s | %s | %s |' % \
					(a[0],a[1],a[2],a[3],a[4])
	print " " * 20 + '+---+---+---+---+---+'

def primeWords(wordfile):
	f = open(wordfile)
	text = f.read()
	words = text.split()
	f.close()
	return words

def main():
	words = primeWords('words.txt')
	mysteryWord = choice(words)
	#Prime Empty Board
	board = list()
	# Prime the answers
	answer = [mysteryWord[0],'*','*','*','*']
	result = ['-','-','-','-','-']
	while True:
		# Clear the screen
		os.system( [ 'clear', 'cls' ][ os.name == 'nt' ] )
		printBoard(answer,board)
		guess = raw_input('Enter your guess: ')
		if not guess: break

		#Check for Valid Word
		if guess not in words:
			print "You entered an invalid word"
			continue

		if guess == mysteryWord:
			print "You guessed the right word"
			break
		
		for i in range(len(guess)):
			if mysteryWord[i] == guess[i]:
				answer[i] = guess[i]
				result[i] = guess[i]
			elif guess[i] in mysteryWord[i:]:
				result[i] = '+'
			else:
				result[i] = '-'
		board.append(result)





if __name__ == '__main__':
	main()


