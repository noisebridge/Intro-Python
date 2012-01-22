#!/usr/bin/python

from random import choice

f = open("words.txt")
text = f.read()
words = text.split()
f.close()

mysteryWord = choice(words)

board = list()
board.append(mysteryWord[0])
answer = ['-', '-', '-', '-', '-']

for i in range(4):
	board.append('*')

print ' ' * 10 + '+' + '-' * 48 + '+'
print ' ' * 10 + '|' + "Welcome to Jargon".center(48) + '|'
print ' ' * 10 + '+' + '-' * 48 + '+'

while True:
	print board
	guess = raw_input('Enter your guess: ')
	if not guess: break

	# Check for Valid Word
	if guess not in words:
		print "You entered an invalid word"
		continue

	if guess == mysteryWord:
		print "You guessed the right word"
		break
	
	for i in range(len(guess)):
		if mysteryWord[i] == guess[i]:
			board[i] = guess[i]
			answer[i] = guess[i]
		elif guess[i] in mysteryWord:
			answer[i] = '+'
		else:
			answer[i] = '-'
	print "Your Results".center(20)
	print '-'*20 
	print answer
	print "Try Again".center(20)
	print '-'*20 


