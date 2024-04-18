import numpy as np
from ..constants import N, \
                        EMPTY, BLACK, WHITE,  \
                        MOVES, WINNING_POS


def new_grid():
    return update_grid(np.zeros(shape=(N, N),
                                dtype='int8'))

def update_grid(grid):
    grid[0, :] = BLACK, EMPTY, WHITE
    grid[1, :] = WHITE, EMPTY, BLACK
    grid[2, :] = BLACK, EMPTY, WHITE

    return grid

def user_pos(grid, user):
    return list(zip(*np.where(grid == user)))

def get_pos(grid, x, y):
    return [pos
            for pos in MOVES[x][y]
            if not grid[pos]]

def get_moves(grid, user):
    return [(pos, move)
            for pos in user_pos(grid, user)
            for move in get_pos(grid, *pos)]

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

def win(grid, user):
    for pos in WINNING_POS:
        if all(grid[p] == user for p in pos):
            return True

    return False
