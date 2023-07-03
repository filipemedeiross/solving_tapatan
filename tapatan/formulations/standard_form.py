import numpy as np
from ..constants import N, EMPTY, BLACK, WHITE, \
                        MOVES, WINNING_POSITIONS


def new_grid():
    grid = np.zeros((N, N), dtype='int8')

    grid[0, 0] = grid[1, 2] = grid[2, 0] = BLACK
    grid[0, 2] = grid[1, 0] = grid[2, 2] = WHITE

    return grid
    
def update_grid(grid):
    grid[0, 0] = grid[1, 2] = grid[2, 0] = BLACK
    grid[0, 1] = grid[1, 1] = grid[2, 1] = EMPTY
    grid[0, 2] = grid[1, 0] = grid[2, 2] = WHITE

def user_pos(grid, user):
    return list(zip(*np.where(grid == user)))

def available_pos(grid, x, y):
    return [pos
            for pos in MOVES[x][y]
            if not grid[pos]]

def available_moves_user(grid, user):
    return [(pos, move)
            for pos in user_pos(grid, user)
            for move in available_pos(grid, *pos)]

def move(grid, user, start, final):
    x0, y0 = start
    x1, y1 = final

    assert 0 <= x0 <= 2, 'Invalid value for x in start'
    assert 0 <= y0 <= 2, 'Invalid value for y in start'

    assert 0 <= x1 <= 2, 'Invalid value for x in final'
    assert 0 <= y1 <= 2, 'Invalid value for y in final'

    assert user in [BLACK, WHITE], 'Invalid value for user'
    assert grid[start] == user   , 'User is not in start position'
    assert grid[final] == EMPTY  , 'The final position is occupied'
    assert final in MOVES[x0][y0], 'Invalid movement'

    grid[start] = 0
    grid[final] = user

    return start, final
    
def win(grid, user):
    for positions in WINNING_POSITIONS:
        if all(grid[pos] == user for pos in positions):
            return True

    return False
