from array2d import Array2D
# from datastructures.array import Array
import Cell
rows = 8
cols = 8

class Grid:
    def __init__(self) -> None:
        self.empty_grid = Array2D.empty(rows, cols, data_type= Cell)
        self.populate_grid()
        self.num_neighbors = int

    def num_alive(self):
        pass

    def next_gen(self):
        pass

    def populate_grid(self):
        for i in (self.empty_grid):
            x = Cell()
