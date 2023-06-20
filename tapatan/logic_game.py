import numpy as np
from .constants import REDS, BLUES, MOVES, WINNING_POSITIONS


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
        grid = np.zeros((3, 3), dtype='int8')

        grid[0, 0] = grid[1, 2] = grid[2, 0] = REDS
        grid[0, 2] = grid[1, 0] = grid[2, 2] = BLUES

        return grid
    
    def move(self, user, start, final):
        x_start, y_start = start
        x_final, y_final = final

        assert 0 <= x_start <= 2, 'Invalid value for x in start'
        assert 0 <= y_start <= 2, 'Invalid value for y in start'

        assert 0 <= x_final <= 2, 'Invalid value for x in final'
        assert 0 <= y_final <= 2, 'Invalid value for y in final'

        assert user in [REDS, BLUES], 'Invalid value for user'
        assert self.grid[start] == user, 'User is not in start position'

        if (start, final) in self.available_moves(user):
            self.grid[start] = 0
            self.grid[final] = user

            return start, final

    def available_moves(self, user):
        pos_user = list(zip(*np.where(self.grid == user)))

        moves = []
        for pos in pos_user:
            for move in self.moves[pos[0]][pos[1]]:
                if not self.grid[move]:
                    moves.append((pos, move))

        return moves
    
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


if __name__ == '__main__':
    grid = TapatanGrid()

    user = REDS
    while True:
        print(grid)

        pos_start = tuple(int(c) for c in input(f'Insira a posição inicial [{user}]='))
        pos_final = tuple(int(c) for c in input(f'Insira a posição final   [{user}]='))

        if grid.move(user, pos_start, pos_final):
            if grid.win(user):
                print(f'\n*** Usuário {user} venceu a partida! ***\n')
                break
            else:
                user = BLUES if user == REDS else REDS
