from .constants import BLACK, WHITE
from .formulations import new_grid, update_grid, move, win


# Class that implements the tapatan logic
class TapatanGrid:
    def __init__(self):
        self.__grid  = self.new_grid()

    def __str__(self):
        return '  -  '.join(map(str, self.grid[0])) + '\n' + \
               '|  \  |  /  |'                      + '\n' + \
               '  -  '.join(map(str, self.grid[1])) + '\n' + \
               '|  /  |  \  |'                      + '\n' + \
               '  -  '.join(map(str, self.grid[2]))
    
    def __getitem__(self, args):
        return self.grid[args]
    
    @staticmethod
    def new_grid():
        return new_grid()
    
    def update(self):
        update_grid(self.grid)
    
    def move(self, user, start, final):
        return move(self.grid, user, start, final)
    
    def win(self, user):
        return win(self.grid, user)
    
    @property
    def grid(self):
        return self.__grid
    
    @grid.setter
    def grid(self, grid):
        self.__grid = grid


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
