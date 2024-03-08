import numpy

grid = numpy.array([[0, 0, 6, 5, 3, 0, 0, 1, 0],
					[0, 0, 0, 0, 2, 0, 5, 0, 4],
					[2, 0, 0, 0, 0, 0, 0, 0, 0],
					[0, 0, 0, 0, 8, 0, 3, 4, 2],
					[0, 0, 0, 9, 0, 3, 0, 0, 0],
					[6, 3, 1, 0, 4, 0, 0, 0, 0],
					[0, 0, 0, 0, 0, 0, 0, 0, 7],
					[8, 0, 4, 0, 6, 0, 0, 0, 0],
					[0, 6, 0, 0, 7, 1, 8, 0, 0]])


# Etapes 1 : Création de la classe SudokuSolver

# Etape 2 : Création d'une méthode d'instance : is_number_valid(row, col, number) -> True or False

# Etape 3 : Création d'une méthode d'instance Solve() : 


class SudokuSolver:
	def __init__(self, grid):
		self.grid = grid
		self.solution = None

	def is_number_valid(self, row, col, number):

		in_row = number in self.grid[row, : ]
		in_col = number in self.grid[:, col]
		

		square_row = row - row % 3
		square_col = col - col % 3	
		# square_row = (row//3) * 3
		# square_col = (col//3) * 3 

		in_square = number in self.grid[square_row: square_row+3, square_col : square_col+3]

		number_is_valid = not (in_row or in_col or in_square)
		# number_is_valid = not in_row and not in_col and not in_square
		
		return number_is_valid