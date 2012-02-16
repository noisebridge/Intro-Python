# User only to make a set number of guesses
# Game Board into a class
# allow for words of Any size

class Board(object):

	def __init__(self, wordsize = 5, guesses = 5):
		self.wordsize = wordsize
		self.guesses = guesses
		self.board = []
		for i in range(self.guesses):
			self.board.append(['*'] * self.wordsize)


	def printBoard(self):
		print '+' + "---+" * self.wordsize 
		for row in range(self.guesses):
			strRow  = '|'
			for col in range(self.wordsize):
				strRow += ' %s |' % (self.board[row][col])

			print strRow
		print '+' + "---+" * self.wordsize 


if __name__ == "__main__":
	b = Board()
	b.printBoard()
 


