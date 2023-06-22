# Logic settings

N = 3

EMPTY = 0
BLACK = 1
WHITE = 2

MOVES =  [[[(0, 1), (1, 0), (1, 1)],
           [(0, 0), (0, 2), (1, 1)],
           [(0, 1), (1, 1), (1, 2)]],
          [[(0, 0), (1, 1), (2, 0)],
           [(0, 0), (0, 1), (0, 2),
            (1, 0), (1, 2), (2, 0),
            (2, 1), (2, 2)],
           [(0, 2), (1, 1), (2, 2)]],
          [[(1, 0), (1, 1), (2, 1)],
           [(1, 1), (2, 0), (2, 2)],
           [(1, 1), (1, 2), (2, 1)]]]

WINNING_POSITIONS = [[(0, 0), (0, 1), (0, 2)],
                     [(1, 0), (1, 1), (1, 2)],
                     [(2, 0), (2, 1), (2, 2)],
                     [(0, 0), (1, 0), (2, 0)],
                     [(0, 1), (1, 1), (2, 1)],
                     [(0, 2), (1, 2), (2, 2)],
                     [(0, 0), (1, 1), (2, 2)],
                     [(0, 2), (1, 1), (2, 0)]]

# Colors

COLOR_FONT = 0, 0, 0
LINE_COLOR = 255, 255, 255

# Dimensions

size = width, height = 240, 360
font_size = 20

spacing = 10
spacing_grid = 25
side_spacing = 15
top_spacing = 60
bottom_spacing = height * 3 / 4

w_button = h_button = 35

grid = width - 2 * spacing_grid

side = grid / (2 * N)
spacing_piece_center = side / 2
spacing_piece_empty = side / 4
