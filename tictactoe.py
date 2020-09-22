###############################
#    TIC-TAC-TOE for Tuq      #
#        Python 3.6+          #
#    Author:  Harris Luo      #
#  Date Created: 2020-09-21   #
###############################

def main():
	t = TicTacToe()
	while True:
		t.run_game()

class TicTacToe:

	def __init__(self):
		pass

	def clean_board(self):
		self.board = [[' ', ' ', ' '], [' ', ' ', ' '], [' ', ' ', ' ']]

	def print_board(self):
		s = '\n'.join((
				"",
				" {} | {} | {}".format(*self.board[0]),
				"-----------",
				" {} | {} | {}".format(*self.board[1]),
				"-----------",
				" {} | {} | {}".format(*self.board[2]),
				"",
			))
		print(s)

	@staticmethod
	def letter_to_square(square):
		if square == 'q':
			return (0, 0)
		if square == 'w':
			return (0, 1)
		if square == 'e':
			return (0, 2)
		if square == 'a':
			return (1, 0)
		if square == 's':
			return (1, 1)
		if square == 'd':
			return (1, 2)
		if square == 'z':
			return (2, 0)
		if square == 'x':
			return (2, 1)
		if square == 'c':
			return (2, 2)
		return None

	def turn(self, player):
		'''
			Execute one turn of the game.
			One empty square will be updated with 'X' or 'O' depending on player arg.
		'''

		print('=' * 80)
		self.print_board()
		print(f"Player {player}'s turn")
		print('\n'.join((
				"",
				" q | w | e",
				"-----------",
				" a | s | d",
				"-----------",
				" z | x | c",
				"",
			)))
		while True:
			square = input("Enter the letter of the square you want to play: ").lower()
			square = self.letter_to_square(square)
			if not square:
				print("Invalid input!")
				continue
			if self.board[square[0]][square[1]] != ' ':
				print("Square already occupied!")
				continue
			self.board[square[0]][square[1]] = player
			break

	def game_over(self):
		'''
			Determine if a game end state has been reached.
			If yes, print an appropriate message.
		'''

		# check for winner
		patterns = [('q', 'w', 'e'), ('a', 's', 'd'), ('z', 'x', 'c'), ('q', 's', 'c'),
					('q', 'a', 'z'), ('w', 's', 'x'), ('e', 'd', 'c'), ('e', 's', 'z')]
		for p in patterns:
			p = map(self.letter_to_square, p)
			s = set(self.board[x[0]][x[1]] for x in p)
			if len(s) == 1 and ' ' not in s:
				# all values in this pattern are identical and != ' ' => there is a winner
				print('=' * 80)
				self.print_board()
				print(f"Player {s.pop()} has won!")
				return True

		# check for draw
		if all(map(lambda x: x != ' ', (x for row in self.board for x in row))):
			# no more spaces
			print('=' * 80)
			self.print_board()
			print("The game is a draw.")
			return True

		# still in play
		return False

	def turn_order(self):
		'''
			Poor man's itertools.cycle
			Generator that yields 'X', 'O', 'X', 'O', etc.
		'''
		while True:
			yield 'X'
			yield 'O'

	def run_game(self):
		print('=' * 80)
		print("Play Tic-Tac-Toe!")
		self.clean_board()
		for p in self.turn_order():
			self.turn(p)
			if self.game_over():
				input("Press any key to continue...\n")
				return

if __name__ == "__main__":
	main()