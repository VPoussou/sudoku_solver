
import numpy as np
import math

# class Special_square:
#     def __init__(self, row, col, value):
#         self.row = row
#         self.col = col
#         self.value = value

class Special_matrix:
    def __init__(self, matrix:np.array) -> None:
        self.matrix = matrix
        self.dim = matrix.shape[0]
        self.columns = np.array(tuple(self.matrix[col_index,:]) for col_index in range(self.dim))
        self.rows = np.array(tuple(self.matrix[:, row_index]) for row_index in range(self.dim))
        self.squares = np.array(tuple(self.matrix[square_index // math.sqrt(self.dim), ]) for square_index in range(self.dim))