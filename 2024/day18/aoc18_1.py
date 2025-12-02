import heapq
from math import sqrt


class Loc:
    def __init__(self, row: int, col: int) -> None:
        self.row = row
        self.col = col


class Memory:
    def __init__(self, grid_size_x, grid_size_y, corruptions):
        self.grid = self.make_grid(grid_size_x, grid_size_y)
        self.corruptions = corruptions
        self.goal = (grid_size_x - 1, grid_size_y - 1)

    def make_grid(self, x, y):
        return [["." for _ in range(y)] for _ in range(x)]

    def corrupt(self, n):
        for i in range(n):
            self.grid[self.corruptions[i].row][self.corruptions[i].col] = "#"

    def h(self, curr_pos):
        out = sqrt(
            (self.goal[0] - curr_pos[0]) ** 2 + (self.goal[1] - curr_pos[1]) ** 2
        )
        return out

    def shortest_path(self):
        frontier = []
        visited = set()
        path = []
        heapq.heappush(frontier, (self.h((0, 0)), (0, 0)))
        while frontier:
            pass
