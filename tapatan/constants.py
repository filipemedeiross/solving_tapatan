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
COLOR_GRID = 184, 134, 11

# Dimensions

size = width, height = 240, 360
font_size = 20 

spacing = 10
spacing_lateral = 15
spacing_grid_lateral = 25
spacing_grid_top = 60
spacing_button_bottom = height * 3 / 4

grid = width - 2 * spacing_grid_lateral

size_piece = grid / (2 * N)
spacing_piece_center = size_piece / 2
radius_piece_empty   = size_piece / 4

w_button = h_button = 35
w_button_play, h_button_play = width - 2 * spacing_lateral, h_button
w_grid_line = 5
