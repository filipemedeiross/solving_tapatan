import numpy as np
from .constants import N, EMPTY, BLACK, WHITE, MOVES, WINNING_POSITIONS


# Class that implements the tapatan logic
class TapatanGrid:
    def __init__(self):
        self.__grid   = self.new_grid()
        self.__moves  = MOVES
        self.__winpos = WINNING_POSITIONS

    def __str__(self):
        return '  -  '.join(map(str, self.grid[0])) + '\n' + \
               '|  \  |  /  |'                      + '\n' + \
               '  -  '.join(map(str, self.grid[1])) + '\n' + \
               '|  /  |  \  |'                      + '\n' + \
               '  -  '.join(map(str, self.grid[2]))
    
    def __getitem__(self, args):
        return self.grid[args]
    
    def new_grid(self):
        grid = np.zeros((N, N), dtype='int8')

        grid[0, 0] = grid[1, 2] = grid[2, 0] = BLACK
        grid[0, 2] = grid[1, 0] = grid[2, 2] = WHITE

        return grid
    
    def move(self, user, start, final):
        x0, y0 = start
        x1, y1 = final

        assert 0 <= x0 <= 2, 'Invalid value for x in start'
        assert 0 <= y0 <= 2, 'Invalid value for y in start'

        assert 0 <= x1 <= 2, 'Invalid value for x in final'
        assert 0 <= y1 <= 2, 'Invalid value for y in final'

        assert user in [BLACK, WHITE]     , 'Invalid value for user'
        assert self.grid[start] == user   , 'User is not in start position'
        assert self.grid[final] == EMPTY  , 'The final position is occupied'
        assert final in self.moves[x0][y0], 'Invalid movement'

        self.grid[start] = 0
        self.grid[final] = user

        return start, final
    
    def win(self, user):
        for positions in self.winning_positions:
            if all(self.grid[pos] == user for pos in positions):
                return True

        return False
    
    @property
    def grid(self):
        return self.__grid
    
    @property
    def moves(self):
        return self.__moves
    
    @property
    def winning_positions(self):
        return self.__winpos
    
    def user_pos(self, user):
        return list(zip(*np.where(self.grid == user)))


# Game prototype
if __name__ == '__main__':
    grid = TapatanGrid()

    user = BLACK
    while True:
        print(grid)

        pos_start = tuple(int(c) for c in input(f'Enter the starting position [{user}]='))
        pos_final = tuple(int(c) for c in input(f'Enter the end position      [{user}]='))

        if grid.move(user, pos_start, pos_final):   
            if grid.win(user):
                break
            else:
                user = BLACK if user == WHITE else WHITE

    print(f'\n*** User {user} won the match! ***\n')
