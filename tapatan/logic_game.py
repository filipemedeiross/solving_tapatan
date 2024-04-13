from .constants import BLACK, WHITE
from .formulations import new_grid,    \
                          update_grid, \
                          move, win


class TapatanGrid:
    def __init__(self):
        self.grid = new_grid()

    def __getitem__(self, args):
        return self.grid[args]

    def __str__(self):
        return '  -  '.join(map(str, self.grid[0])) + '\n' + \
               '|  \  |  /  |'                      + '\n' + \
               '  -  '.join(map(str, self.grid[1])) + '\n' + \
               '|  /  |  \  |'                      + '\n' + \
               '  -  '.join(map(str, self.grid[2]))

    def update(self):
        self.grid = update_grid(self.grid)

    def move(self, user, start, final):
        move(self.grid, user, start, final)

    def win(self, user):
        return win(self.grid, user)


# Testing the game
if __name__ == '__main__':
    grid = TapatanGrid()

    user = WHITE
    while not grid.win(user):
        print(grid)

        user = BLACK if user == WHITE else WHITE
        start = tuple(int(c) for c in input(f'Enter the starting position [{user}]='))
        final = tuple(int(c) for c in input(f'Enter the end position      [{user}]='))

        grid.move(user, start, final)

    print(grid)
    print()
    print(f'*** User {user} won the match! ***')
