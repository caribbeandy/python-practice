from typing import List

def matrix_in_spiral_order(square_matrix: List[List[int]]) -> List[int]:
    shift = ((0,1), (1,0), (0,-1), (-1,0))
    direction = x = y = 0
    spiral_ordering = []

    for _ in range(len(square_matrix)**2):
        spiral_ordering.append((square_matrix[x][y]))
        square_matrix[x][y] = 0
        next_x, next_y = x + shift[direction][0], y + shift[direction][1]
    pass

shift = ((0,1), (1,0), (0,-1), (-1,0))
print(shift[2])
